#!/usr/bin/env python3
"""Publish the controlled Customer Account Management demo subset.

This wrapper reads:

    scripts/confluence-demo-manifest.yml

It then reuses the tested functions in:

    scripts/publish-confluence.py

Supported commands:

    python3 scripts/publish-confluence-demo.py --dry-run
    python3 scripts/publish-confluence-demo.py
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import requests
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

PUBLISHER_PATH = (
    REPOSITORY_ROOT
    / "scripts"
    / "publish-confluence.py"
)

MANIFEST_PATH = (
    REPOSITORY_ROOT
    / "scripts"
    / "confluence-demo-manifest.yml"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Publish the controlled Customer Account Management "
            "demonstration subset to Confluence."
        )
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the demo publishing plan without changing Confluence.",
    )

    return parser.parse_args()


def load_publisher_module() -> ModuleType:
    """Load the existing publisher without renaming its file."""
    if not PUBLISHER_PATH.exists():
        raise FileNotFoundError(
            f"Publisher file not found: {PUBLISHER_PATH}"
        )

    specification = importlib.util.spec_from_file_location(
        "customer_account_management_confluence_publisher",
        PUBLISHER_PATH,
    )

    if specification is None or specification.loader is None:
        raise RuntimeError(
            f"Unable to load publisher module: {PUBLISHER_PATH}"
        )

    module = importlib.util.module_from_spec(specification)

    sys.modules[specification.name] = module
    specification.loader.exec_module(module)

    return module


def load_manifest() -> dict[str, Any]:
    """Load and validate the demonstration publishing manifest."""
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"Manifest file not found: {MANIFEST_PATH}"
        )

    with MANIFEST_PATH.open(
        "r",
        encoding="utf-8",
    ) as manifest_file:
        manifest = yaml.safe_load(manifest_file)

    if not isinstance(manifest, dict):
        raise ValueError(
            "The demonstration manifest must contain a YAML object."
        )

    pages = manifest.get("pages")

    if not isinstance(pages, list) or not pages:
        raise ValueError(
            "The demonstration manifest must contain at least one page."
        )

    return manifest


def manifest_page_paths(
    manifest: dict[str, Any],
) -> list[Path]:
    """Return validated repository-relative Markdown paths."""
    page_entries = manifest["pages"]

    ordered_entries = sorted(
        page_entries,
        key=lambda item: (
            item.get("order", 9999)
            if isinstance(item, dict)
            else 9999
        ),
    )

    selected_paths: list[Path] = []
    seen_paths: set[Path] = set()

    for entry in ordered_entries:
        if not isinstance(entry, dict):
            raise ValueError(
                "Each manifest page entry must be a YAML object."
            )

        raw_path = entry.get("path")

        if not isinstance(raw_path, str) or not raw_path.strip():
            raise ValueError(
                "Each manifest page entry must contain a path."
            )

        relative_path = Path(raw_path.strip())

        if relative_path.is_absolute():
            raise ValueError(
                f"Manifest paths must be repository-relative: {relative_path}"
            )

        if ".." in relative_path.parts:
            raise ValueError(
                f"Parent-directory references are not allowed: {relative_path}"
            )

        if relative_path.suffix.lower() != ".md":
            raise ValueError(
                f"Only Markdown files can be published: {relative_path}"
            )

        absolute_path = REPOSITORY_ROOT / relative_path

        if not absolute_path.exists():
            raise FileNotFoundError(
                f"Manifest page does not exist: {relative_path}"
            )

        if not absolute_path.is_file():
            raise ValueError(
                f"Manifest page is not a file: {relative_path}"
            )

        if relative_path in seen_paths:
            raise ValueError(
                f"Duplicate manifest page: {relative_path}"
            )

        selected_paths.append(relative_path)
        seen_paths.add(relative_path)

    return selected_paths


def print_manifest_summary(
    manifest: dict[str, Any],
    selected_paths: list[Path],
) -> None:
    """Print the controlled publishing scope."""
    manifest_name = manifest.get(
        "name",
        "Customer Account Management Confluence demonstration",
    )

    print(f"Manifest: {manifest_name}")
    print(
        f"Selected {len(selected_paths)} demonstration page(s):"
    )

    for index, path in enumerate(
        selected_paths,
        start=1,
    ):
        print(f"  {index}. {path.as_posix()}")


def main() -> int:
    """Run the controlled demonstration publisher."""
    arguments = parse_arguments()

    try:
        publisher = load_publisher_module()
        manifest = load_manifest()

        selected_paths = manifest_page_paths(
            manifest
        )

        print_manifest_summary(
            manifest,
            selected_paths,
        )

        publisher.confirm_git_repository()

        configuration = publisher.load_configuration()

        client = publisher.ConfluenceClient(
            configuration
        )

        client.load_pages()

        publisher.publish_repository(
            client=client,
            configuration=configuration,
            markdown_files=selected_paths,
            dry_run=arguments.dry_run,
        )

        action = (
            "previewed"
            if arguments.dry_run
            else "published"
        )

        print(
            "Confluence demonstration complete: "
            f"{len(selected_paths)} page(s) {action}."
        )

        return 0

    except requests.RequestException as error:
        print(
            f"Network error while contacting Confluence: {error}",
            file=sys.stderr,
        )
        return 1

    except (
        FileNotFoundError,
        KeyError,
        OSError,
        RuntimeError,
        TypeError,
        ValueError,
        yaml.YAMLError,
    ) as error:
        print(
            f"Confluence demonstration failed: {error}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())