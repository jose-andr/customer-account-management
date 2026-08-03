#!/usr/bin/env python3
"""Generate Git-derived review notes for publishable Markdown files.

The script:

- scans the configured project documentation folders;
- reads file-specific Git history;
- creates newest-first review-note rows;
- replaces the managed review-note block when it already exists;
- appends the section when it is missing; and
- leaves content outside the managed block unchanged.

Run from the repository root:

    python3 scripts/generate-review-notes.py

Check whether files need updating without writing changes:

    python3 scripts/generate-review-notes.py --check

Process one file:

    python3 scripts/generate-review-notes.py \
        --file 00-project-control/purpose-and-scope.md
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


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

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

EXCLUDED_PATHS = {
    Path("README.md"),
}

REVIEW_HEADING = "## Review notes"
START_MARKER = "<!-- AUTO-REVIEW-NOTES:START -->"
END_MARKER = "<!-- AUTO-REVIEW-NOTES:END -->"

DEFAULT_HISTORY_LIMIT = 25

MANAGED_BLOCK_PATTERN = re.compile(
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


@dataclass(frozen=True)
class CommitRecord:
    """One Git commit affecting a Markdown file."""

    date: str
    subject: str
    author: str
    short_hash: str


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate Git-derived Review notes sections for repository "
            "Markdown pages."
        )
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files requiring updates without modifying them.",
    )

    parser.add_argument(
        "--file",
        type=Path,
        help="Process one repository-relative Markdown file.",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=int(
            os.getenv("REVIEW_NOTES_LIMIT", str(DEFAULT_HISTORY_LIMIT))
        ),
        help=(
            "Maximum Git-history rows per file. "
            f"Default: {DEFAULT_HISTORY_LIMIT}."
        ),
    )

    return parser.parse_args()


def run_git_command(arguments: list[str]) -> str:
    """Run a Git command from the repository root."""
    command = ["git", *arguments]

    completed = subprocess.run(
        command,
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    if completed.returncode != 0:
        error_message = completed.stderr.strip() or completed.stdout.strip()

        raise RuntimeError(
            f"Git command failed: {' '.join(command)}\n{error_message}"
        )

    return completed.stdout


def confirm_git_repository() -> None:
    """Confirm the script is running within a Git working tree."""
    result = run_git_command(["rev-parse", "--is-inside-work-tree"]).strip()

    if result != "true":
        raise RuntimeError(
            f"Not a Git working tree: {REPOSITORY_ROOT}"
        )


def repository_relative_path(path: Path) -> Path:
    """Return and validate a repository-relative file path."""
    candidate = path

    if candidate.is_absolute():
        try:
            candidate = candidate.resolve().relative_to(
                REPOSITORY_ROOT.resolve()
            )
        except ValueError as error:
            raise ValueError(
                f"File is outside the repository: {path}"
            ) from error

    candidate = Path(candidate.as_posix())

    if ".." in candidate.parts:
        raise ValueError(
            f"Parent-directory references are not allowed: {path}"
        )

    return candidate


def is_publishable_markdown(path: Path) -> bool:
    """Return whether a path belongs to the current publishing scope."""
    if path.suffix.lower() != ".md":
        return False

    if path in EXCLUDED_PATHS:
        return False

    if not path.parts:
        return False

    return path.parts[0] in PUBLISHABLE_DIRECTORIES


def discover_markdown_files() -> list[Path]:
    """Discover all publishable Markdown files."""
    discovered: list[Path] = []

    for directory_name in PUBLISHABLE_DIRECTORIES:
        directory = REPOSITORY_ROOT / directory_name

        if not directory.exists():
            continue

        for file_path in directory.rglob("*.md"):
            relative_path = file_path.relative_to(REPOSITORY_ROOT)

            if is_publishable_markdown(relative_path):
                discovered.append(relative_path)

    return sorted(discovered, key=lambda item: item.as_posix().lower())


def resolve_target_files(single_file: Path | None) -> list[Path]:
    """Resolve either one requested file or the standard publishing scope."""
    if single_file is None:
        return discover_markdown_files()

    relative_path = repository_relative_path(single_file)
    absolute_path = REPOSITORY_ROOT / relative_path

    if not absolute_path.exists():
        raise FileNotFoundError(
            f"Markdown file does not exist: {relative_path}"
        )

    if not absolute_path.is_file():
        raise ValueError(
            f"Path is not a file: {relative_path}"
        )

    if relative_path.suffix.lower() != ".md":
        raise ValueError(
            f"Only Markdown files are supported: {relative_path}"
        )

    return [relative_path]


def parse_git_history(path: Path, limit: int) -> list[CommitRecord]:
    """Read file-specific Git history, following renames where possible."""
    if limit < 1:
        raise ValueError("--limit must be at least 1.")

    separator = "\x1f"

    output = run_git_command(
        [
            "log",
            "--follow",
            f"--max-count={limit}",
            f"--format=%cs{separator}%s{separator}%an{separator}%h",
            "--",
            path.as_posix(),
        ]
    )

    commits: list[CommitRecord] = []

    for line in output.splitlines():
        if not line.strip():
            continue

        parts = line.split(separator)

        if len(parts) != 4:
            raise RuntimeError(
                f"Unexpected Git-history output for {path}: {line}"
            )

        date, subject, author, short_hash = parts

        commits.append(
            CommitRecord(
                date=date.strip(),
                subject=subject.strip(),
                author=author.strip(),
                short_hash=short_hash.strip(),
            )
        )

    return commits


def escape_markdown_table_value(value: str) -> str:
    """Escape content that could break a Markdown table."""
    cleaned = " ".join(value.split())
    return cleaned.replace("|", r"\|")


def build_review_section(commits: Iterable[CommitRecord]) -> str:
    """Build the managed Review notes section."""
    lines = [
        REVIEW_HEADING,
        "",
        START_MARKER,
        "",
        "| Date | Update | Updated by | Commit |",
        "|---|---|---|---|",
    ]

    commit_rows = list(commits)

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

    return "\n".join(lines)


def remove_existing_managed_section(content: str) -> str:
    """Remove the existing managed block and its heading."""
    updated = MANAGED_BLOCK_PATTERN.sub("", content)

    return updated.rstrip()


def apply_review_section(
    content: str,
    review_section: str,
) -> str:
    """Place the refreshed Review notes section at the file bottom."""
    base_content = remove_existing_managed_section(content)

    if base_content:
        return f"{base_content}\n\n{review_section}\n"

    return f"{review_section}\n"


def process_file(
    path: Path,
    *,
    check_only: bool,
    history_limit: int,
) -> bool:
    """Refresh one file and return whether a change was required."""
    absolute_path = REPOSITORY_ROOT / path
    original_content = absolute_path.read_text(encoding="utf-8")

    commits = parse_git_history(path, history_limit)
    review_section = build_review_section(commits)

    updated_content = apply_review_section(
        original_content,
        review_section,
    )

    if updated_content == original_content:
        print(f"Unchanged: {path}")
        return False

    if check_only:
        print(f"Needs update: {path}")
        return True

    absolute_path.write_text(
        updated_content,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Updated: {path}")
    return True


def main() -> int:
    """Generate review notes for the selected Markdown files."""
    arguments = parse_arguments()

    try:
        confirm_git_repository()

        target_files = resolve_target_files(arguments.file)

        if not target_files:
            print("No publishable Markdown files were found.")
            return 0

        changed_files = 0

        for path in target_files:
            if process_file(
                path,
                check_only=arguments.check,
                history_limit=arguments.limit,
            ):
                changed_files += 1

        if arguments.check:
            if changed_files:
                print(
                    f"{changed_files} file(s) require refreshed review notes."
                )
                return 1

            print("All review-note sections are current.")
            return 0

        print(
            f"Review notes complete. "
            f"{changed_files} file(s) updated."
        )

        return 0

    except (
        FileNotFoundError,
        OSError,
        RuntimeError,
        ValueError,
    ) as error:
        print(
            f"Review-note generation failed: {error}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())