#!/usr/bin/env python3
"""Publish Customer Account Management Markdown documentation to Confluence.

The publisher:

- preserves stakeholder-owned Confluence pages that are not explicitly
  configured for automated publication;
- publishes selected repository root pages directly beneath the configured
  Customer Account Management parent page;
- discovers approved repository documentation folders;
- creates matching Confluence folder pages;
- preserves the numbered taxonomy for top-level repository folders;
- publishes Markdown files beneath their matching folder pages;
- uses the first Markdown H1 as the Confluence page title;
- removes that H1 from the rendered page body;
- generates file-specific Git review notes in memory;
- creates or updates pages without modifying source Markdown;
- avoids duplicate managed pages on repeated runs; and
- resolves Confluence space-wide title collisions using a CAM prefix.

Expected managed Confluence structure:

    Open issues                    [stakeholder-owned; not automated]
    CAM initiative register       [repository-managed]
    00 Project control
    01 Discover
    02 Define
    03 Design
    04 Deliver
    05 Evaluation and learning
    06 Decisions
    07 References

The repository may contain:

    open-issues.md

as a preserved reference copy.

That file is deliberately excluded from automated Confluence publishing so
the existing stakeholder-owned Confluence page retains its ownership,
history and manual control.

Required environment variables:

    CONFLUENCE_BASE_URL
    CONFLUENCE_SPACE_ID
    CONFLUENCE_PARENT_PAGE_ID
    CONFLUENCE_USER_EMAIL
    CONFLUENCE_API_TOKEN

Run:

    python3 scripts/publish-confluence.py

Preview without changing Confluence:

    python3 scripts/publish-confluence.py --dry-run

Publish one repository folder:

    python3 scripts/publish-confluence.py --folder 00-project-control
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin

import markdown
import requests
from requests.auth import HTTPBasicAuth


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

# Root-level repository pages managed by the publisher.
#
# IMPORTANT:
# open-issues.md is intentionally NOT included here.
# The corresponding Confluence page is stakeholder-owned and must remain
# untouched by repository automation.
ROOT_PAGES = (
    Path("cam-initiative-register.md"),
)

PUBLISHABLE_DIRECTORIES = (
    "00-project-control",
    "01-discover",
    "02-define",
    "03-design",
    "04-deliver",
    "05-evaluation-and-learning",
    "06-decisions",
    "references",
)

TOP_LEVEL_FOLDER_TITLES = {
    "00-project-control": "00 Project control",
    "01-discover": "01 Discover",
    "02-define": "02 Define",
    "03-design": "03 Design",
    "04-deliver": "04 Deliver",
    "05-evaluation-and-learning": "05 Evaluation and learning",
    "06-decisions": "06 Decisions",
    "references": "07 References",
}

REQUEST_TIMEOUT_SECONDS = 30
REVIEW_NOTES_LIMIT = int(
    os.getenv("REVIEW_NOTES_LIMIT", "25")
)

REVIEW_HEADING = "## Review notes"
START_MARKER = "<!-- AUTO-REVIEW-NOTES:START -->"
END_MARKER = "<!-- AUTO-REVIEW-NOTES:END -->"

MANAGED_REVIEW_PATTERN = re.compile(
    rf"""
    (?:
        ^{re.escape(REVIEW_HEADING)}[ \t]*\n
        [ \t]*\n?
    )?
    ^{re.escape(START_MARKER)}[ \t]*\n
    .*?
    ^{re.escape(END_MARKER)}[ \t]*$
    """,
    flags=re.MULTILINE | re.DOTALL | re.VERBOSE,
)

FIRST_H1_PATTERN = re.compile(
    r"^\s*#\s+(.+?)\s*$",
    flags=re.MULTILINE,
)


@dataclass(frozen=True)
class Configuration:
    """Runtime configuration."""

    base_url: str
    space_id: str
    parent_page_id: str
    user_email: str
    api_token: str


@dataclass(frozen=True)
class CommitRecord:
    """One Git commit affecting a Markdown file."""

    date: str
    subject: str
    author: str
    short_hash: str


@dataclass
class ConfluencePage:
    """Minimal Confluence page information used by the publisher."""

    page_id: str
    title: str
    parent_id: str
    version_number: int


class ConfluenceClient:
    """Small client for the Confluence Cloud REST API v2."""

    TITLE_PREFIX = "CAM —"

    def __init__(
        self,
        configuration: Configuration,
    ) -> None:
        self.configuration = configuration

        self.auth = HTTPBasicAuth(
            configuration.user_email,
            configuration.api_token,
        )

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self.pages_by_identity: dict[
            tuple[str, str],
            ConfluencePage,
        ] = {}

        self.pages_by_title: dict[
            str,
            list[ConfluencePage],
        ] = {}

    def api_url(
        self,
        path: str,
    ) -> str:
        """Build a Confluence REST API v2 URL."""
        base_url = self.configuration.base_url.rstrip("/")

        if base_url.endswith("/wiki"):
            base_url = base_url[:-5]

        return (
            f"{base_url}/wiki/api/v2/"
            f"{path.lstrip('/')}"
        )

    def raise_for_error(
        self,
        response: requests.Response,
        action: str,
    ) -> None:
        """Raise a useful API error without exposing credentials."""
        if response.ok:
            return

        excerpt = response.text[:1500].replace(
            "\n",
            " ",
        )

        raise RuntimeError(
            f"{action} failed with HTTP "
            f"{response.status_code}: {excerpt}"
        )

    def register_page(
        self,
        page: ConfluencePage,
    ) -> None:
        """Add or refresh a page in the local lookup indexes."""
        identity = (
            page.parent_id,
            page.title,
        )

        previous_page = self.pages_by_identity.get(
            identity
        )

        self.pages_by_identity[
            identity
        ] = page

        title_pages = self.pages_by_title.setdefault(
            page.title,
            [],
        )

        if previous_page is not None:
            title_pages[:] = [
                existing
                for existing in title_pages
                if existing.page_id != previous_page.page_id
            ]

        title_pages[:] = [
            existing
            for existing in title_pages
            if existing.page_id != page.page_id
        ]

        title_pages.append(page)

    def load_pages(self) -> None:
        """Load current pages in the configured Confluence space."""
        url = self.api_url(
            f"spaces/"
            f"{self.configuration.space_id}/pages"
        )

        params: dict[str, str | int] = {
            "limit": 250,
            "status": "current",
        }

        loaded_count = 0

        while url:
            response = requests.get(
                url,
                params=params,
                headers=self.headers,
                auth=self.auth,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )

            self.raise_for_error(
                response,
                "Loading Confluence pages",
            )

            payload = response.json()

            for item in payload.get(
                "results",
                [],
            ):
                page_id = str(
                    item.get("id", "")
                ).strip()

                title = str(
                    item.get("title", "")
                ).strip()

                parent_id = str(
                    item.get("parentId", "")
                ).strip()

                version_number = item.get(
                    "version",
                    {},
                ).get(
                    "number",
                    1,
                )

                if not page_id or not title:
                    continue

                if not isinstance(
                    version_number,
                    int,
                ):
                    version_number = 1

                page = ConfluencePage(
                    page_id=page_id,
                    title=title,
                    parent_id=parent_id,
                    version_number=version_number,
                )

                self.register_page(page)
                loaded_count += 1

            next_link = payload.get(
                "_links",
                {},
            ).get("next")

            if next_link:
                if next_link.startswith("http"):
                    url = next_link
                else:
                    url = urljoin(
                        (
                            self.configuration
                            .base_url.rstrip("/")
                            + "/"
                        ),
                        next_link.lstrip("/"),
                    )

                params = {}
            else:
                url = ""

        print(
            f"Loaded {loaded_count} existing "
            "Confluence page(s)."
        )

    def page_exists_under_parent(
        self,
        *,
        parent_id: str,
        title: str,
    ) -> bool:
        """Return whether the exact page identity already exists."""
        return (
            parent_id,
            title,
        ) in self.pages_by_identity

    def title_exists_in_space(
        self,
        title: str,
    ) -> bool:
        """Return whether a title already exists anywhere in the space."""
        return bool(
            self.pages_by_title.get(title)
        )

    def resolve_page_title(
        self,
        *,
        desired_title: str,
        parent_id: str,
    ) -> str:
        """Resolve a stable title that avoids space-wide collisions."""
        if self.page_exists_under_parent(
            parent_id=parent_id,
            title=desired_title,
        ):
            return desired_title

        if not self.title_exists_in_space(
            desired_title
        ):
            return desired_title

        qualified_title = (
            f"{self.TITLE_PREFIX} "
            f"{desired_title}"
        )

        if self.page_exists_under_parent(
            parent_id=parent_id,
            title=qualified_title,
        ):
            return qualified_title

        if not self.title_exists_in_space(
            qualified_title
        ):
            print(
                "Title collision resolved: "
                f"'{desired_title}' "
                f"→ '{qualified_title}'"
            )

            return qualified_title

        suffix = 2

        while True:
            candidate_title = (
                f"{qualified_title} "
                f"({suffix})"
            )

            if self.page_exists_under_parent(
                parent_id=parent_id,
                title=candidate_title,
            ):
                return candidate_title

            if not self.title_exists_in_space(
                candidate_title
            ):
                print(
                    "Title collision resolved: "
                    f"'{desired_title}' "
                    f"→ '{candidate_title}'"
                )

                return candidate_title

            suffix += 1

    def create_page(
        self,
        *,
        title: str,
        parent_id: str,
        body_html: str,
    ) -> ConfluencePage:
        """Create a Confluence page."""
        payload = {
            "spaceId": self.configuration.space_id,
            "status": "current",
            "title": title,
            "parentId": parent_id,
            "body": {
                "representation": "storage",
                "value": body_html,
            },
        }

        response = requests.post(
            self.api_url("pages"),
            json=payload,
            headers=self.headers,
            auth=self.auth,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        self.raise_for_error(
            response,
            f"Creating page '{title}'",
        )

        result = response.json()

        page = ConfluencePage(
            page_id=str(result["id"]),
            title=title,
            parent_id=parent_id,
            version_number=int(
                result.get(
                    "version",
                    {},
                ).get(
                    "number",
                    1,
                )
            ),
        )

        self.register_page(page)

        print(
            f"Created: {title}"
        )

        return page

    def get_current_page_version(
        self,
        page_id: str,
    ) -> int:
        """Retrieve the current Confluence page version."""
        response = requests.get(
            self.api_url(
                f"pages/{page_id}"
            ),
            headers=self.headers,
            auth=self.auth,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        self.raise_for_error(
            response,
            (
                "Retrieving page version for "
                f"'{page_id}'"
            ),
        )

        payload = response.json()

        version_number = payload.get(
            "version",
            {},
        ).get("number")

        if not isinstance(
            version_number,
            int,
        ):
            raise RuntimeError(
                f"Page '{page_id}' did not return "
                "a valid version number."
            )

        return version_number

    def update_page(
        self,
        *,
        page: ConfluencePage,
        body_html: str,
    ) -> ConfluencePage:
        """Update an existing Confluence page."""
        current_version = (
            self.get_current_page_version(
                page.page_id
            )
        )

        next_version = current_version + 1

        payload = {
            "id": page.page_id,
            "status": "current",
            "title": page.title,
            "spaceId": self.configuration.space_id,
            "parentId": page.parent_id,
            "body": {
                "representation": "storage",
                "value": body_html,
            },
            "version": {
                "number": next_version,
                "message": (
                    "Published from the "
                    "Customer Account Management "
                    "repository"
                ),
                "minorEdit": True,
            },
        }

        response = requests.put(
            self.api_url(
                f"pages/{page.page_id}"
            ),
            json=payload,
            headers=self.headers,
            auth=self.auth,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        self.raise_for_error(
            response,
            f"Updating page '{page.title}'",
        )

        updated_page = ConfluencePage(
            page_id=page.page_id,
            title=page.title,
            parent_id=page.parent_id,
            version_number=next_version,
        )

        self.register_page(
            updated_page
        )

        print(
            f"Updated: {page.title}"
        )

        return updated_page

    def create_or_update_page(
        self,
        *,
        title: str,
        parent_id: str,
        body_html: str,
        dry_run: bool,
    ) -> ConfluencePage:
        """Create or update a collision-safe Confluence page."""
        resolved_title = (
            self.resolve_page_title(
                desired_title=title,
                parent_id=parent_id,
            )
        )

        existing_page = (
            self.pages_by_identity.get(
                (
                    parent_id,
                    resolved_title,
                )
            )
        )

        if dry_run:
            action = (
                "Would update"
                if existing_page
                else "Would create"
            )

            print(
                f"{action}: {resolved_title}"
            )

            if existing_page:
                return existing_page

            dry_run_page = ConfluencePage(
                page_id=(
                    f"dry-run:"
                    f"{parent_id}:"
                    f"{resolved_title}"
                ),
                title=resolved_title,
                parent_id=parent_id,
                version_number=1,
            )

            self.register_page(
                dry_run_page
            )

            return dry_run_page

        if existing_page:
            return self.update_page(
                page=existing_page,
                body_html=body_html,
            )

        return self.create_page(
            title=resolved_title,
            parent_id=parent_id,
            body_html=body_html,
        )


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Publish Customer Account Management "
            "Markdown pages to Confluence."
        )
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Show the publishing plan without "
            "changing Confluence."
        ),
    )

    parser.add_argument(
        "--folder",
        choices=PUBLISHABLE_DIRECTORIES,
        help=(
            "Publish only one approved "
            "repository folder."
        ),
    )

    return parser.parse_args()


def required_environment_variable(
    name: str,
) -> str:
    """Return a required environment variable."""
    value = os.getenv(
        name,
        "",
    ).strip()

    if not value:
        raise RuntimeError(
            "Required environment variable "
            f"is missing: {name}"
        )

    return value


def load_configuration() -> Configuration:
    """Load publishing configuration from environment variables."""
    return Configuration(
        base_url=required_environment_variable(
            "CONFLUENCE_BASE_URL"
        ),
        space_id=required_environment_variable(
            "CONFLUENCE_SPACE_ID"
        ),
        parent_page_id=required_environment_variable(
            "CONFLUENCE_PARENT_PAGE_ID"
        ),
        user_email=required_environment_variable(
            "CONFLUENCE_USER_EMAIL"
        ),
        api_token=required_environment_variable(
            "CONFLUENCE_API_TOKEN"
        ),
    )


def run_git_command(
    arguments: list[str],
) -> str:
    """Run a Git command from the repository root."""
    completed = subprocess.run(
        [
            "git",
            *arguments,
        ],
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    if completed.returncode != 0:
        message = (
            completed.stderr.strip()
            or completed.stdout.strip()
        )

        raise RuntimeError(
            "Git command failed: "
            f"git {' '.join(arguments)}\n"
            f"{message}"
        )

    return completed.stdout


def confirm_git_repository() -> None:
    """Confirm the script is running in a Git working tree."""
    result = run_git_command(
        [
            "rev-parse",
            "--is-inside-work-tree",
        ]
    ).strip()

    if result != "true":
        raise RuntimeError(
            "Not a Git working tree: "
            f"{REPOSITORY_ROOT}"
        )


def discover_root_pages() -> list[Path]:
    """Return configured repository-managed root pages."""
    discovered: list[Path] = []

    for file_path in ROOT_PAGES:
        absolute_path = (
            REPOSITORY_ROOT
            / file_path
        )

        if not absolute_path.exists():
            print(
                "Skipped missing root page: "
                f"{file_path.as_posix()}"
            )

            continue

        if not absolute_path.is_file():
            print(
                "Skipped non-file root page: "
                f"{file_path.as_posix()}"
            )

            continue

        discovered.append(
            file_path
        )

    return discovered


def discover_markdown_files(
    selected_folder: str | None,
) -> list[Path]:
    """Discover folder-based Markdown files in publishing order."""
    directories = (
        (selected_folder,)
        if selected_folder
        else PUBLISHABLE_DIRECTORIES
    )

    discovered: list[Path] = []

    for directory_name in directories:
        directory = (
            REPOSITORY_ROOT
            / directory_name
        )

        if not directory.exists():
            print(
                f"Skipped missing folder: "
                f"{directory_name}"
            )

            continue

        directory_files: list[Path] = []

        for absolute_path in directory.rglob(
            "*.md"
        ):
            relative_path = (
                absolute_path.relative_to(
                    REPOSITORY_ROOT
                )
            )

            directory_files.append(
                relative_path
            )

        directory_files.sort(
            key=lambda path: (
                len(path.parts),
                path.as_posix().lower(),
            )
        )

        discovered.extend(
            directory_files
        )

    return discovered


def humanise_name(
    value: str,
) -> str:
    """Convert a repository file or child-folder name into a page title."""
    cleaned = re.sub(
        r"^\d{2}-",
        "",
        value,
    )

    cleaned = cleaned.replace(
        "_",
        " ",
    ).replace(
        "-",
        " ",
    )

    cleaned = re.sub(
        r"\s+",
        " ",
        cleaned,
    ).strip()

    special_terms = {
        "abn": "ABN",
        "acn": "ACN",
        "crm": "CRM",
        "cx": "CX",
        "dq": "DQ",
        "id": "ID",
    }

    words: list[str] = []

    for word in cleaned.split():
        replacement = special_terms.get(
            word.lower()
        )

        words.append(
            replacement
            or word.capitalize()
        )

    return " ".join(
        words
    )


def top_level_folder_title(
    folder_name: str,
) -> str:
    """Return the controlled title for a top-level folder."""
    configured_title = (
        TOP_LEVEL_FOLDER_TITLES.get(
            folder_name
        )
    )

    if configured_title:
        return configured_title

    return humanise_name(
        folder_name
    )


def repository_folder_title(
    folder_path: Path,
) -> str:
    """Return the Confluence title for a repository folder."""
    if len(
        folder_path.parts
    ) == 1:
        return top_level_folder_title(
            folder_path.name
        )

    return humanise_name(
        folder_path.name
    )


def extract_page_title(
    markdown_content: str,
    file_path: Path,
) -> str:
    """Use the first Markdown H1 or fall back to the file name."""
    match = FIRST_H1_PATTERN.search(
        markdown_content
    )

    if match:
        title = re.sub(
            r"\s+#+\s*$",
            "",
            match.group(1),
        ).strip()

        if title:
            return title

    return humanise_name(
        file_path.stem
    )


def remove_first_h1(
    markdown_content: str,
) -> str:
    """Remove the first H1 because Confluence provides the page title."""
    return FIRST_H1_PATTERN.sub(
        "",
        markdown_content,
        count=1,
    ).lstrip()


def parse_git_history(
    path: Path,
) -> list[CommitRecord]:
    """Read newest-first Git history for one Markdown file."""
    separator = "\x1f"

    output = run_git_command(
        [
            "log",
            "--follow",
            (
                f"--max-count="
                f"{REVIEW_NOTES_LIMIT}"
            ),
            (
                f"--format=%cs"
                f"{separator}%s"
                f"{separator}%an"
                f"{separator}%h"
            ),
            "--",
            path.as_posix(),
        ]
    )

    records: list[CommitRecord] = []

    for line in output.splitlines():
        if not line.strip():
            continue

        parts = line.split(
            separator
        )

        if len(parts) != 4:
            raise RuntimeError(
                "Unexpected Git-history "
                f"output for {path}: {line}"
            )

        records.append(
            CommitRecord(
                date=parts[0].strip(),
                subject=parts[1].strip(),
                author=parts[2].strip(),
                short_hash=parts[3].strip(),
            )
        )

    return records


def escape_markdown_table_value(
    value: str,
) -> str:
    """Escape a value for a Markdown table."""
    cleaned = " ".join(
        value.split()
    )

    return cleaned.replace(
        "|",
        r"\|",
    )


def build_review_notes(
    commits: Iterable[CommitRecord],
) -> str:
    """Build the managed Review notes Markdown section."""
    lines = [
        REVIEW_HEADING,
        "",
        START_MARKER,
        "",
        "| Date | Update | Updated by | Commit |",
        "|---|---|---|---|",
    ]

    commit_rows = list(
        commits
    )

    if commit_rows:
        for commit in commit_rows:
            lines.append(
                "| "
                f"{escape_markdown_table_value(commit.date)} | "
                f"{escape_markdown_table_value(commit.subject)} | "
                f"{escape_markdown_table_value(commit.author)} | "
                f"`{escape_markdown_table_value(commit.short_hash)}` |"
            )
    else:
        lines.append(
            "| — | No committed file history found | — | — |"
        )

    lines.extend(
        [
            "",
            END_MARKER,
        ]
    )

    return "\n".join(
        lines
    )


def inject_review_notes(
    markdown_content: str,
    commits: Iterable[CommitRecord],
) -> str:
    """Replace or append the managed Review notes section in memory."""
    base_content = (
        MANAGED_REVIEW_PATTERN.sub(
            "",
            markdown_content,
        ).rstrip()
    )

    review_notes = build_review_notes(
        commits
    )

    if base_content:
        return (
            f"{base_content}\n\n"
            f"{review_notes}\n"
        )

    return (
        f"{review_notes}\n"
    )


def convert_markdown_to_storage(
    markdown_content: str,
) -> str:
    """Convert Markdown into Confluence storage-compatible HTML."""
    return markdown.markdown(
        markdown_content,
        extensions=[
            "tables",
            "fenced_code",
            "sane_lists",
            "nl2br",
        ],
        output_format="html5",
    )


def build_folder_body(
    folder_path: Path,
    child_items: list[str],
) -> str:
    """Build a lightweight folder landing page."""
    folder_title = repository_folder_title(
        folder_path
    )

    child_list = "\n".join(
        f"- {item}"
        for item in child_items
    )

    markdown_content = f"""
**Repository path:** `{folder_path.as_posix()}`

This page groups the Customer Account Management documentation for **{folder_title}**.

The source Markdown files remain authoritative. This Confluence hierarchy is an automatically published working view.

## Included pages

{child_list or "- No publishable child pages found."}
""".strip()

    return convert_markdown_to_storage(
        markdown_content
    )


def folder_paths_for_files(
    markdown_files: Iterable[Path],
) -> list[Path]:
    """Return required repository folders in parent-first order."""
    folders: set[Path] = set()

    top_level_order = {
        name: index
        for index, name in enumerate(
            PUBLISHABLE_DIRECTORIES
        )
    }

    for file_path in markdown_files:
        current = file_path.parent

        while current != Path("."):
            folders.add(
                current
            )

            current = current.parent

    def folder_sort_key(
        path: Path,
    ) -> tuple[int, int, str]:
        top_level_name = (
            path.parts[0]
        )

        return (
            top_level_order.get(
                top_level_name,
                len(
                    top_level_order
                ),
            ),
            len(
                path.parts
            ),
            path.as_posix().lower(),
        )

    return sorted(
        folders,
        key=folder_sort_key,
    )


def direct_children_for_folder(
    folder_path: Path,
    markdown_files: Iterable[Path],
    folder_paths: Iterable[Path],
) -> list[str]:
    """Return human-readable direct children for a folder page."""
    children: set[str] = set()

    for child_folder in folder_paths:
        if child_folder.parent == folder_path:
            children.add(
                repository_folder_title(
                    child_folder
                )
            )

    for file_path in markdown_files:
        if file_path.parent != folder_path:
            continue

        content = (
            REPOSITORY_ROOT
            / file_path
        ).read_text(
            encoding="utf-8"
        )

        children.add(
            extract_page_title(
                content,
                file_path,
            )
        )

    return sorted(
        children,
        key=str.lower,
    )


def publish_markdown_file(
    *,
    client: ConfluenceClient,
    file_path: Path,
    parent_page_id: str,
    dry_run: bool,
) -> ConfluencePage:
    """Publish one repository-managed Markdown file."""
    absolute_path = (
        REPOSITORY_ROOT
        / file_path
    )

    source_markdown = absolute_path.read_text(
        encoding="utf-8"
    )

    page_title = extract_page_title(
        source_markdown,
        file_path,
    )

    body_markdown = remove_first_h1(
        source_markdown
    )

    git_history = parse_git_history(
        file_path
    )

    body_markdown = inject_review_notes(
        body_markdown,
        git_history,
    )

    body_html = convert_markdown_to_storage(
        body_markdown
    )

    return client.create_or_update_page(
        title=page_title,
        parent_id=parent_page_id,
        body_html=body_html,
        dry_run=dry_run,
    )


def publish_root_pages(
    *,
    client: ConfluenceClient,
    configuration: Configuration,
    root_pages: list[Path],
    dry_run: bool,
) -> None:
    """Publish repository-managed root pages beneath the CAM parent."""
    for file_path in root_pages:
        publish_markdown_file(
            client=client,
            file_path=file_path,
            parent_page_id=(
                configuration.parent_page_id
            ),
            dry_run=dry_run,
        )


def publish_repository(
    *,
    client: ConfluenceClient,
    configuration: Configuration,
    markdown_files: list[Path],
    dry_run: bool,
) -> None:
    """Publish folder pages followed by their Markdown document pages."""
    required_folders = folder_paths_for_files(
        markdown_files
    )

    confluence_folder_ids: dict[
        Path,
        str,
    ] = {}

    for folder_path in required_folders:
        repository_parent = (
            folder_path.parent
        )

        if repository_parent == Path("."):
            parent_page_id = (
                configuration.parent_page_id
            )
        else:
            parent_page_id = (
                confluence_folder_ids[
                    repository_parent
                ]
            )

        child_items = (
            direct_children_for_folder(
                folder_path,
                markdown_files,
                required_folders,
            )
        )

        folder_page = (
            client.create_or_update_page(
                title=repository_folder_title(
                    folder_path
                ),
                parent_id=parent_page_id,
                body_html=build_folder_body(
                    folder_path,
                    child_items,
                ),
                dry_run=dry_run,
            )
        )

        confluence_folder_ids[
            folder_path
        ] = folder_page.page_id

    for file_path in markdown_files:
        parent_page_id = (
            confluence_folder_ids[
                file_path.parent
            ]
        )

        publish_markdown_file(
            client=client,
            file_path=file_path,
            parent_page_id=parent_page_id,
            dry_run=dry_run,
        )


def main() -> int:
    """Run the repository-to-Confluence publisher."""
    arguments = parse_arguments()

    try:
        confirm_git_repository()

        configuration = (
            load_configuration()
        )

        if arguments.folder:
            root_pages: list[Path] = []
        else:
            root_pages = (
                discover_root_pages()
            )

        markdown_files = (
            discover_markdown_files(
                arguments.folder
            )
        )

        if (
            not root_pages
            and not markdown_files
        ):
            print(
                "No publishable Markdown files "
                "were found."
            )

            return 0

        total_file_count = (
            len(root_pages)
            + len(markdown_files)
        )

        print(
            f"Discovered {total_file_count} "
            "publishable Markdown file(s)."
        )

        print(
            "Stakeholder-owned page excluded from "
            "automation: open-issues.md"
        )

        if root_pages:
            print(
                "Repository-managed root pages: "
                + ", ".join(
                    path.as_posix()
                    for path in root_pages
                )
            )

        client = ConfluenceClient(
            configuration
        )

        client.load_pages()

        if root_pages:
            publish_root_pages(
                client=client,
                configuration=configuration,
                root_pages=root_pages,
                dry_run=arguments.dry_run,
            )

        if markdown_files:
            publish_repository(
                client=client,
                configuration=configuration,
                markdown_files=markdown_files,
                dry_run=arguments.dry_run,
            )

        action = (
            "previewed"
            if arguments.dry_run
            else "published"
        )

        print(
            "Confluence migration complete: "
            f"{total_file_count} "
            f"file(s) {action}."
        )

        return 0

    except requests.RequestException as error:
        print(
            "Network error while contacting "
            f"Confluence: {error}",
            file=sys.stderr,
        )

        return 1

    except (
        KeyError,
        OSError,
        RuntimeError,
        TypeError,
        ValueError,
    ) as error:
        print(
            "Confluence publishing failed: "
            f"{error}",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(
        main()
    )