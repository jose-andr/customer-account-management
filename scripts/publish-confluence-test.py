#!/usr/bin/env python3
"""Create or update a controlled Confluence publishing test page."""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from typing import Any

import markdown
import requests
from requests.auth import HTTPBasicAuth


TEST_PAGE_TITLE = "Customer Account Management — Publishing Test"
REQUEST_TIMEOUT_SECONDS = 30


def required_environment_variable(name: str) -> str:
    """Return a required environment variable or stop with a clear error."""
    value = os.getenv(name, "").strip()

    if not value:
        raise RuntimeError(f"Required environment variable is missing: {name}")

    return value


def confluence_api_url(base_url: str, path: str) -> str:
    """Build a Confluence Cloud REST API v2 URL."""
    normalised_base = base_url.rstrip("/")

    if normalised_base.endswith("/wiki"):
        normalised_base = normalised_base[:-5]

    return f"{normalised_base}/wiki/api/v2/{path.lstrip('/')}"


def request_headers() -> dict[str, str]:
    """Return standard Confluence API request headers."""
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def raise_for_confluence_error(response: requests.Response, action: str) -> None:
    """Raise a useful error without exposing credentials."""
    if response.ok:
        return

    response_excerpt = response.text[:1000].replace("\n", " ")

    raise RuntimeError(
        f"{action} failed with HTTP {response.status_code}: {response_excerpt}"
    )


def find_existing_test_page(
    *,
    base_url: str,
    space_id: str,
    parent_page_id: str,
    auth: HTTPBasicAuth,
) -> dict[str, Any] | None:
    """Find the existing controlled test page under the configured parent."""
    url = confluence_api_url(base_url, f"spaces/{space_id}/pages")
    params: dict[str, str | int] = {
        "limit": 250,
        "status": "current",
    }

    while url:
        response = requests.get(
            url,
            params=params,
            headers=request_headers(),
            auth=auth,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        raise_for_confluence_error(response, "Searching for the test page")

        payload = response.json()

        for page in payload.get("results", []):
            if (
                page.get("title") == TEST_PAGE_TITLE
                and str(page.get("parentId", "")) == parent_page_id
            ):
                return page

        next_path = payload.get("_links", {}).get("next")

        if next_path:
            if next_path.startswith("http"):
                url = next_path
            else:
                url = f"{base_url.rstrip('/')}{next_path}"
            params = {}
        else:
            url = ""

    return None


def build_test_body() -> str:
    """Create the Markdown test content and convert it to storage-compatible HTML."""
    published_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    source_markdown = f"""
# Customer Account Management publishing test

**Status:** Successful pipeline test

This page confirms that the Bitbucket pipeline can:

- authenticate with Confluence;
- access the configured space;
- publish beneath the configured parent page; and
- update the same controlled test page without creating duplicates.

**Last pipeline run:** {published_at}

This is a technical validation page. It is not part of the approved Customer Account Management documentation set.
""".strip()

    return markdown.markdown(
        source_markdown,
        extensions=["tables", "fenced_code"],
    )


def create_test_page(
    *,
    base_url: str,
    space_id: str,
    parent_page_id: str,
    body_html: str,
    auth: HTTPBasicAuth,
) -> dict[str, Any]:
    """Create the controlled Confluence test page."""
    url = confluence_api_url(base_url, "pages")

    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": TEST_PAGE_TITLE,
        "parentId": parent_page_id,
        "body": {
            "representation": "storage",
            "value": body_html,
        },
    }

    response = requests.post(
        url,
        json=payload,
        headers=request_headers(),
        auth=auth,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    raise_for_confluence_error(response, "Creating the test page")

    return response.json()


def get_page(
    *,
    base_url: str,
    page_id: str,
    auth: HTTPBasicAuth,
) -> dict[str, Any]:
    """Retrieve the current page version before an update."""
    url = confluence_api_url(base_url, f"pages/{page_id}")

    response = requests.get(
        url,
        headers=request_headers(),
        auth=auth,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    raise_for_confluence_error(response, "Retrieving the existing test page")

    return response.json()


def update_test_page(
    *,
    base_url: str,
    page_id: str,
    body_html: str,
    auth: HTTPBasicAuth,
) -> dict[str, Any]:
    """Update the controlled test page using its next version number."""
    current_page = get_page(
        base_url=base_url,
        page_id=page_id,
        auth=auth,
    )

    current_version = current_page.get("version", {}).get("number")

    if not isinstance(current_version, int):
        raise RuntimeError(
            "The existing page did not return a valid version number."
        )

    url = confluence_api_url(base_url, f"pages/{page_id}")

    payload = {
        "id": page_id,
        "status": "current",
        "title": TEST_PAGE_TITLE,
        "body": {
            "representation": "storage",
            "value": body_html,
        },
        "version": {
            "number": current_version + 1,
            "message": "Updated by the Customer Account Management Bitbucket pipeline",
        },
    }

    response = requests.put(
        url,
        json=payload,
        headers=request_headers(),
        auth=auth,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    raise_for_confluence_error(response, "Updating the test page")

    return response.json()


def main() -> int:
    """Run the controlled Confluence publishing test."""
    try:
        base_url = required_environment_variable("CONFLUENCE_BASE_URL")
        space_id = required_environment_variable("CONFLUENCE_SPACE_ID")
        parent_page_id = required_environment_variable(
            "CONFLUENCE_PARENT_PAGE_ID"
        )
        user_email = required_environment_variable("CONFLUENCE_USER_EMAIL")
        api_token = required_environment_variable("CONFLUENCE_API_TOKEN")

        auth = HTTPBasicAuth(user_email, api_token)
        body_html = build_test_body()

        existing_page = find_existing_test_page(
            base_url=base_url,
            space_id=space_id,
            parent_page_id=parent_page_id,
            auth=auth,
        )

        if existing_page:
            page_id = str(existing_page["id"])

            result = update_test_page(
                base_url=base_url,
                page_id=page_id,
                body_html=body_html,
                auth=auth,
            )

            action = "updated"
        else:
            result = create_test_page(
                base_url=base_url,
                space_id=space_id,
                parent_page_id=parent_page_id,
                body_html=body_html,
                auth=auth,
            )

            page_id = str(result["id"])
            action = "created"

        web_ui_path = result.get("_links", {}).get("webui", "")
        page_url = (
            f"{base_url.rstrip('/')}{web_ui_path}"
            if web_ui_path
            else f"{base_url.rstrip('/')}/wiki/pages/viewpage.action?pageId={page_id}"
        )

        print(f"Confluence test page {action} successfully.")
        print(f"Page ID: {page_id}")
        print(f"Page URL: {page_url}")

        return 0

    except requests.RequestException as error:
        print(f"Network error while contacting Confluence: {error}", file=sys.stderr)
        return 1

    except (KeyError, ValueError, RuntimeError) as error:
        print(f"Confluence publishing test failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())