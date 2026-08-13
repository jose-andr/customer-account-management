#!/usr/bin/env python3

"""
Publish Customer Account Management Markdown documentation to Confluence.

Publishing model
----------------
Configured Confluence parent
├── Open issues
├── CAM initiative register
├── 00 Project control
├── 01 Discover
├── 02 Define
├── 03 Design
├── 04 Deliver
├── 05 Evaluation and learning
├── 06 Decisions
└── References

Repository source files remain the source for published CAM documentation.

Key behaviours
--------------
- Publishes selected root-level control pages first.
- Publishes numbered top-level folder pages in controlled order.
- Preserves the numeric taxonomy in Confluence titles.
- Publishes Markdown files beneath their corresponding folder page.
- Uses the first Markdown H1 as the Confluence page title.
- Removes the first H1 from the published body.
- Injects Git review notes in memory.
- Does not modify source Markdown.
- Creates missing Confluence pages.
- Updates existing pages only when title + expected parent match.
- Protects unrelated pages elsewhere in the Confluence space.
- Resolves space-wide title collisions using "CAM — <title>".
- Supports dry-run preview.
- Supports optional publication of one configured folder.

Required environment variables
------------------------------
CONFLUENCE_BASE_URL
CONFLUENCE_SPACE_ID
CONFLUENCE_PARENT_PAGE_ID
CONFLUENCE_USER_EMAIL
CONFLUENCE_API_TOKEN
"""

from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import markdown
import requests


# ---------------------------------------------------------------------------
# Repository configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

PUBLISHABLE_DIRECTORIES: Tuple[str, ...] = (
    "00-project-control",
    "01-discover",
    "02-define",
    "03-design",
    "04-deliver",
    "05-evaluation-and-learning",
    "06-decisions",
    "references",
)

ROOT_PAGES: Tuple[Path, ...] = (
    Path("open-issues.md"),
    Path("cam-initiative-register.md"),
)

FOLDER_TITLES: Dict[str, str] = {
    "00-project-control": "00 Project control",
    "01-discover": "01 Discover",
    "02-define": "02 Define",
    "03-design": "03 Design",
    "04-deliver": "04 Deliver",
    "05-evaluation-and-learning": "05 Evaluation and learning",
    "06-decisions": "06 Decisions",
    "references": "References",
}

TITLE_COLLISION_PREFIX = "CAM — "

REVIEW_NOTES_START = "<!-- AUTO-REVIEW-NOTES:START -->"
REVIEW_NOTES_END = "<!-- AUTO-REVIEW-NOTES:END -->"

MARKDOWN_EXTENSIONS = (
    "tables",
    "fenced_code",
    "sane_lists",
)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ConfluencePage:
    page_id: str
    title: str
    parent_id: Optional[str]


@dataclass(frozen=True)
class PublishResult:
    action: str
    title: str
    page_id: Optional[str] = None


# ---------------------------------------------------------------------------
# General helpers
# ---------------------------------------------------------------------------

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        fail(f"Required environment variable is missing: {name}")
    return value


def relative_path(path: Path) -> Path:
    return path.resolve().relative_to(REPO_ROOT.resolve())


def normalise_parent_id(value: Optional[object]) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


# ---------------------------------------------------------------------------
# Markdown discovery
# ---------------------------------------------------------------------------

def discover_root_pages() -> List[Path]:
    pages: List[Path] = []

    for relative in ROOT_PAGES:
        full_path = REPO_ROOT / relative
        if full_path.exists() and full_path.is_file():
            pages.append(full_path)
        else:
            print(f"WARNING: configured root page not found: {relative}")

    return pages


def discover_folder_files(folder_name: str) -> List[Path]:
    folder = REPO_ROOT / folder_name

    if not folder.exists():
        print(f"WARNING: configured folder not found: {folder_name}")
        return []

    return sorted(
        (
            path
            for path in folder.rglob("*.md")
            if path.is_file()
        ),
        key=lambda path: str(relative_path(path)).lower(),
    )


def discover_markdown_files(
    selected_folder: Optional[str] = None,
) -> Dict[str, List[Path]]:
    result: Dict[str, List[Path]] = {}

    folders: Sequence[str]
    if selected_folder:
        if selected_folder not in PUBLISHABLE_DIRECTORIES:
            fail(
                f"Unknown folder '{selected_folder}'. "
                f"Allowed values: {', '.join(PUBLISHABLE_DIRECTORIES)}"
            )
        folders = (selected_folder,)
    else:
        folders = PUBLISHABLE_DIRECTORIES

    for folder_name in folders:
        result[folder_name] = discover_folder_files(folder_name)

    return result


# ---------------------------------------------------------------------------
# Markdown title/body handling
# ---------------------------------------------------------------------------

H1_PATTERN = re.compile(r"^\s*#\s+(.+?)\s*$")


def extract_title_and_body(path: Path) -> Tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()

    title: Optional[str] = None
    title_index: Optional[int] = None

    for index, line in enumerate(lines):
        match = H1_PATTERN.match(line)
        if match:
            title = match.group(1).strip()
            title_index = index
            break

    if not title:
        title = path.stem.replace("-", " ").strip()
        title = title[:1].upper() + title[1:]

    if title_index is not None:
        del lines[title_index]

        while lines and not lines[0].strip():
            lines.pop(0)

    body = "\n".join(lines).strip()

    return title, body


# ---------------------------------------------------------------------------
# Git review notes
# ---------------------------------------------------------------------------

def run_git(args: Sequence[str]) -> str:
    command = ["git", "-C", str(REPO_ROOT), *args]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: {' '.join(command)}\n"
            f"{result.stderr.strip()}"
        )

    return result.stdout


def git_history(path: Path) -> List[Tuple[str, str, str, str]]:
    rel = str(relative_path(path)).replace("\\", "/")

    try:
        output = run_git(
            [
                "log",
                "--follow",
                "--date=short",
                "--pretty=format:%ad%x1f%s%x1f%an%x1f%h",
                "--",
                rel,
            ]
        )
    except RuntimeError as exc:
        print(f"WARNING: unable to read Git history for {rel}: {exc}")
        return []

    rows: List[Tuple[str, str, str, str]] = []

    for line in output.splitlines():
        parts = line.split("\x1f")

        if len(parts) != 4:
            continue

        date, subject, author, commit = [part.strip() for part in parts]
        rows.append((date, subject, author, commit))

    return rows


def escape_markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def generate_review_notes(path: Path) -> str:
    history = git_history(path)

    lines = [
        "## Review notes",
        "",
        REVIEW_NOTES_START,
        "",
        "| Date | Update | Updated by | Commit |",
        "|---|---|---|---|",
    ]

    for date, subject, author, commit in history:
        lines.append(
            "| "
            + " | ".join(
                (
                    escape_markdown_cell(date),
                    escape_markdown_cell(subject),
                    escape_markdown_cell(author),
                    f"`{escape_markdown_cell(commit)}`",
                )
            )
            + " |"
        )

    lines.extend(
        [
            "",
            REVIEW_NOTES_END,
        ]
    )

    return "\n".join(lines)


def inject_review_notes(body: str, path: Path) -> str:
    review_notes = generate_review_notes(path)

    managed_pattern = re.compile(
        r"(?ms)"
        r"^##\s+Review notes\s*$"
        r".*?"
        + re.escape(REVIEW_NOTES_START)
        + r".*?"
        + re.escape(REVIEW_NOTES_END)
        + r"\s*"
    )

    if managed_pattern.search(body):
        return managed_pattern.sub(review_notes + "\n", body).strip()

    marker_only_pattern = re.compile(
        re.escape(REVIEW_NOTES_START)
        + r".*?"
        + re.escape(REVIEW_NOTES_END),
        flags=re.DOTALL,
    )

    if marker_only_pattern.search(body):
        replacement = "\n".join(review_notes.splitlines()[2:])
        return marker_only_pattern.sub(replacement, body).strip()

    if not body:
        return review_notes

    return f"{body.rstrip()}\n\n{review_notes}"


# ---------------------------------------------------------------------------
# Markdown conversion
# ---------------------------------------------------------------------------

def markdown_to_storage(markdown_text: str) -> str:
    return markdown.markdown(
        markdown_text,
        extensions=list(MARKDOWN_EXTENSIONS),
        output_format="html5",
    )


def folder_page_body(folder_name: str) -> str:
    title = FOLDER_TITLES[folder_name]

    return (
        f"<p><strong>{html.escape(title)}</strong> groups the "
        "Customer Account Management repository documentation for this phase.</p>"
        "<p>Content on this page and its child pages is published from the "
        "repository.</p>"
    )


# ---------------------------------------------------------------------------
# Confluence client
# ---------------------------------------------------------------------------

class ConfluenceClient:
    def __init__(
        self,
        base_url: str,
        space_id: str,
        parent_page_id: str,
        user_email: str,
        api_token: str,
        dry_run: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.space_id = space_id
        self.parent_page_id = parent_page_id
        self.dry_run = dry_run

        self.session = requests.Session()
        self.session.auth = (user_email, api_token)
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        self.pages_by_id: Dict[str, ConfluencePage] = {}
        self.pages_by_title: Dict[str, List[ConfluencePage]] = {}
        self.pages_by_parent_title: Dict[
            Tuple[Optional[str], str],
            ConfluencePage,
        ] = {}

def api_url(self, path: str) -> str:
    base = self.base_url.rstrip("/")

    if base.endswith("/wiki"):
        return f"{base}/api/v2/{path.lstrip('/')}"

    return f"{base}/wiki/api/v2/{path.lstrip('/')}"

    def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> requests.Response:
        response = self.session.request(
            method,
            url,
            timeout=60,
            **kwargs,
        )

        if not response.ok:
            detail = response.text[:2000]
            raise RuntimeError(
                f"Confluence API request failed "
                f"({response.status_code} {response.reason}): {detail}"
            )

        return response

    def load_space_pages(self) -> None:
        self.pages_by_id.clear()
        self.pages_by_title.clear()
        self.pages_by_parent_title.clear()

        url: Optional[str] = self.api_url(
            f"pages?space-id={self.space_id}&limit=250"
        )

        while url:
            response = self.request("GET", url)
            payload = response.json()

            for item in payload.get("results", []):
                page_id = str(item["id"])
                title = str(item.get("title", "")).strip()
                parent_id = normalise_parent_id(item.get("parentId"))

                page = ConfluencePage(
                    page_id=page_id,
                    title=title,
                    parent_id=parent_id,
                )

                self._index_page(page)

            next_link = (
                payload.get("_links", {}).get("next")
                or payload.get("links", {}).get("next")
            )

            if not next_link:
                url = None
            elif next_link.startswith("http"):
                url = next_link
            else:
                url = f"{self.base_url}{next_link}"

        print(
            f"Loaded {len(self.pages_by_id)} existing page(s) "
            f"from Confluence space {self.space_id}."
        )

    def _index_page(self, page: ConfluencePage) -> None:
        self.pages_by_id[page.page_id] = page
        self.pages_by_title.setdefault(page.title, []).append(page)
        self.pages_by_parent_title[(page.parent_id, page.title)] = page

    def _replace_indexed_page(
        self,
        page_id: str,
        title: str,
        parent_id: Optional[str],
    ) -> None:
        old = self.pages_by_id.get(page_id)

        if old:
            title_pages = self.pages_by_title.get(old.title, [])
            self.pages_by_title[old.title] = [
                page for page in title_pages
                if page.page_id != page_id
            ]

            if not self.pages_by_title[old.title]:
                del self.pages_by_title[old.title]

            self.pages_by_parent_title.pop(
                (old.parent_id, old.title),
                None,
            )

        self._index_page(
            ConfluencePage(
                page_id=page_id,
                title=title,
                parent_id=parent_id,
            )
        )

    def find_expected_page(
        self,
        parent_id: str,
        title: str,
    ) -> Optional[ConfluencePage]:
        return self.pages_by_parent_title.get((str(parent_id), title))

    def title_exists_elsewhere(
        self,
        title: str,
        expected_parent_id: str,
    ) -> bool:
        pages = self.pages_by_title.get(title, [])

        return any(
            page.parent_id != str(expected_parent_id)
            for page in pages
        )

    def resolve_title(
        self,
        requested_title: str,
        parent_id: str,
    ) -> str:
        expected = self.find_expected_page(parent_id, requested_title)

        if expected:
            return requested_title

        if requested_title not in self.pages_by_title:
            return requested_title

        candidate = f"{TITLE_COLLISION_PREFIX}{requested_title}"

        expected_qualified = self.find_expected_page(parent_id, candidate)
        if expected_qualified:
            print(
                f"Title collision resolved: '{requested_title}' "
                f"→ '{candidate}'"
            )
            return candidate

        if candidate not in self.pages_by_title:
            print(
                f"Title collision resolved: '{requested_title}' "
                f"→ '{candidate}'"
            )
            return candidate

        suffix = 2

        while True:
            numbered = f"{candidate} ({suffix})"

            expected_numbered = self.find_expected_page(
                parent_id,
                numbered,
            )
            if expected_numbered:
                print(
                    f"Title collision resolved: '{requested_title}' "
                    f"→ '{numbered}'"
                )
                return numbered

            if numbered not in self.pages_by_title:
                print(
                    f"Title collision resolved: '{requested_title}' "
                    f"→ '{numbered}'"
                )
                return numbered

            suffix += 1

    def get_page_version(self, page_id: str) -> int:
        response = self.request(
            "GET",
            self.api_url(f"pages/{page_id}"),
        )

        payload = response.json()
        version = payload.get("version", {}).get("number")

        if version is None:
            raise RuntimeError(
                f"Unable to determine current version for page {page_id}"
            )

        return int(version)

    def create_page(
        self,
        title: str,
        parent_id: str,
        body_html: str,
    ) -> PublishResult:
        if self.dry_run:
            print(f"Would create: {title}")
            return PublishResult(
                action="would-create",
                title=title,
            )

        payload = {
            "spaceId": self.space_id,
            "status": "current",
            "title": title,
            "parentId": str(parent_id),
            "body": {
                "representation": "storage",
                "value": body_html,
            },
        }

        response = self.request(
            "POST",
            self.api_url("pages"),
            json=payload,
        )

        data = response.json()
        page_id = str(data["id"])

        self._replace_indexed_page(
            page_id=page_id,
            title=title,
            parent_id=str(parent_id),
        )

        print(f"Created: {title}")

        return PublishResult(
            action="created",
            title=title,
            page_id=page_id,
        )

    def update_page(
        self,
        page: ConfluencePage,
        body_html: str,
    ) -> PublishResult:
        if self.dry_run:
            print(f"Would update: {page.title}")
            return PublishResult(
                action="would-update",
                title=page.title,
                page_id=page.page_id,
            )

        current_version = self.get_page_version(page.page_id)

        payload = {
            "id": page.page_id,
            "status": "current",
            "title": page.title,
            "spaceId": self.space_id,
            "parentId": page.parent_id,
            "body": {
                "representation": "storage",
                "value": body_html,
            },
            "version": {
                "number": current_version + 1,
                "message": "Published from Customer Account Management repository",
            },
        }

        self.request(
            "PUT",
            self.api_url(f"pages/{page.page_id}"),
            json=payload,
        )

        print(f"Updated: {page.title}")

        return PublishResult(
            action="updated",
            title=page.title,
            page_id=page.page_id,
        )

    def publish_page(
        self,
        requested_title: str,
        parent_id: str,
        body_html: str,
    ) -> PublishResult:
        resolved_title = self.resolve_title(
            requested_title=requested_title,
            parent_id=parent_id,
        )

        existing = self.find_expected_page(
            parent_id=parent_id,
            title=resolved_title,
        )

        if existing:
            return self.update_page(existing, body_html)

        return self.create_page(
            title=resolved_title,
            parent_id=parent_id,
            body_html=body_html,
        )


# ---------------------------------------------------------------------------
# Publishing
# ---------------------------------------------------------------------------

def publish_markdown_file(
    client: ConfluenceClient,
    path: Path,
    parent_id: str,
) -> PublishResult:
    rel = relative_path(path)

    title, body = extract_title_and_body(path)
    body = inject_review_notes(body, path)
    body_html = markdown_to_storage(body)

    print(f"\nSource: {rel}")
    print(f"Requested title: {title}")

    return client.publish_page(
        requested_title=title,
        parent_id=parent_id,
        body_html=body_html,
    )


def ensure_folder_page(
    client: ConfluenceClient,
    folder_name: str,
) -> PublishResult:
    title = FOLDER_TITLES[folder_name]
    body_html = folder_page_body(folder_name)

    print(f"\nFolder: {folder_name}")
    print(f"Folder title: {title}")

    return client.publish_page(
        requested_title=title,
        parent_id=client.parent_page_id,
        body_html=body_html,
    )


def resolve_result_page_id(
    client: ConfluenceClient,
    result: PublishResult,
    requested_title: str,
    parent_id: str,
) -> Optional[str]:
    if result.page_id:
        return result.page_id

    # Dry-run does not create page IDs.
    if client.dry_run:
        return None

    resolved_title = client.resolve_title(
        requested_title=requested_title,
        parent_id=parent_id,
    )

    page = client.find_expected_page(
        parent_id=parent_id,
        title=resolved_title,
    )

    return page.page_id if page else None


def publish_root_pages(
    client: ConfluenceClient,
) -> int:
    published = 0

    root_pages = discover_root_pages()

    if not root_pages:
        print("\nNo configured root pages found.")
        return published

    print("\n=== Root pages ===")

    for path in root_pages:
        publish_markdown_file(
            client=client,
            path=path,
            parent_id=client.parent_page_id,
        )
        published += 1

    return published


def publish_folder(
    client: ConfluenceClient,
    folder_name: str,
    files: Iterable[Path],
) -> int:
    files = list(files)

    folder_title = FOLDER_TITLES[folder_name]

    folder_result = ensure_folder_page(
        client=client,
        folder_name=folder_name,
    )

    if client.dry_run:
        # We cannot know the ID of a folder that would be created.
        # Existing folders can still be resolved for informative output.
        existing_folder = client.find_expected_page(
            client.parent_page_id,
            folder_title,
        )

        if existing_folder:
            folder_parent_id = existing_folder.page_id
        else:
            folder_parent_id = f"DRY-RUN:{folder_name}"
    else:
        folder_parent_id = resolve_result_page_id(
            client=client,
            result=folder_result,
            requested_title=folder_title,
            parent_id=client.parent_page_id,
        )

        if not folder_parent_id:
            raise RuntimeError(
                f"Unable to determine page ID for folder '{folder_title}'."
            )

    published = 0

    for path in files:
        publish_markdown_file(
            client=client,
            path=path,
            parent_id=folder_parent_id,
        )
        published += 1

    return published


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Publish Customer Account Management Markdown "
            "documentation to Confluence."
        )
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview publication without changing Confluence.",
    )

    parser.add_argument(
        "--folder",
        choices=PUBLISHABLE_DIRECTORIES,
        help=(
            "Publish only one configured repository folder. "
            "Root pages are skipped when this option is used."
        ),
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    base_url = required_env("CONFLUENCE_BASE_URL")
    space_id = required_env("CONFLUENCE_SPACE_ID")
    parent_page_id = required_env("CONFLUENCE_PARENT_PAGE_ID")
    user_email = required_env("CONFLUENCE_USER_EMAIL")
    api_token = required_env("CONFLUENCE_API_TOKEN")

    client = ConfluenceClient(
        base_url=base_url,
        space_id=space_id,
        parent_page_id=parent_page_id,
        user_email=user_email,
        api_token=api_token,
        dry_run=args.dry_run,
    )

    mode = "DRY RUN" if args.dry_run else "LIVE"

    print("=" * 72)
    print("Customer Account Management → Confluence publisher")
    print(f"Mode: {mode}")
    print(f"Space ID: {space_id}")
    print(f"Parent page ID: {parent_page_id}")

    if args.folder:
        print(f"Selected folder: {args.folder}")
    else:
        print("Scope: full controlled publication")

    print("=" * 72)

    client.load_space_pages()

    file_count = 0
    folder_count = 0
    root_count = 0

    if not args.folder:
        root_count = publish_root_pages(client)

    folder_files = discover_markdown_files(
        selected_folder=args.folder,
    )

    print("\n=== Numbered repository sections ===")

    for folder_name in PUBLISHABLE_DIRECTORIES:
        if folder_name not in folder_files:
            continue

        files = folder_files[folder_name]

        publish_folder(
            client=client,
            folder_name=folder_name,
            files=files,
        )

        folder_count += 1
        file_count += len(files)

    print("\n" + "=" * 72)

    if args.dry_run:
        print("Confluence publication preview complete.")
    else:
        print("Confluence publication complete.")

    print(f"Root page(s): {root_count}")
    print(f"Folder page(s): {folder_count}")
    print(f"Folder Markdown page(s): {file_count}")
    print(
        "Total Markdown page(s): "
        f"{root_count + file_count}"
    )

    if args.dry_run:
        print("\nNo Confluence content was changed.")

    print("=" * 72)


if __name__ == "__main__":
    main()