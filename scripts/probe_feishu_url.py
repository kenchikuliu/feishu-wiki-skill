#!/usr/bin/env python3
"""Probe a Feishu/Lark wiki URL and report whether document content is readable."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener


LOGIN_MARKERS = (
    "accounts.feishu.cn",
    "login.feishu.cn",
    "passport",
    "suite-passport",
    "accounts/page/login",
)

SENSITIVE_HEADER_PARTS = (
    "authorization",
    "cookie",
    "request-ip",
    "secret",
    "token",
    "x-lgw",
)


class NoRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


def fetch(url: str, method: str, max_bytes: int, timeout: float) -> dict[str, Any]:
    request = Request(
        url,
        method=method,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )

    try:
        opener = build_opener(NoRedirectHandler)
        with opener.open(request, timeout=timeout) as response:
            body = response.read(max_bytes) if method != "HEAD" else b""
            preview = decode_preview(body)
            return {
                "ok": True,
                "status": response.status,
                "final_url": response.geturl(),
                "headers": sanitize_headers(dict(response.headers.items())),
                "bytes_read": len(body),
                "body_preview": sanitize_preview(preview),
            }
    except HTTPError as exc:
        body = exc.read(max_bytes) if method != "HEAD" else b""
        preview = decode_preview(body)
        return {
            "ok": False,
            "status": exc.code,
            "final_url": exc.geturl(),
            "headers": sanitize_headers(dict(exc.headers.items())) if exc.headers else {},
            "bytes_read": len(body),
            "body_preview": sanitize_preview(preview),
            "error": str(exc),
        }
    except URLError as exc:
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "headers": {},
            "bytes_read": 0,
            "body_preview": "",
            "error": str(exc.reason),
        }


def decode_preview(body: bytes) -> str:
    if not body:
        return ""
    text = body.decode("utf-8", errors="replace")
    return text[:4000]


def sanitize_headers(headers: dict[str, str]) -> dict[str, str]:
    redacted: dict[str, str] = {}
    for key, value in headers.items():
        lowered = key.lower()
        if any(part in lowered for part in SENSITIVE_HEADER_PARTS):
            redacted[key] = "[redacted]"
        else:
            redacted[key] = value
    return redacted


def sanitize_preview(text: str) -> str:
    lowered = text.lower()
    if any(marker in lowered for marker in LOGIN_MARKERS):
        return "[redacted Feishu login/passport page preview]"
    return text


def classify(head_result: dict[str, Any], get_result: dict[str, Any]) -> tuple[bool, str]:
    final_url = str(get_result.get("final_url") or "").lower()
    body = str(get_result.get("body_preview") or "").lower()
    status = get_result.get("status")
    head_status = head_result.get("status")

    if any(marker in final_url or marker in body for marker in LOGIN_MARKERS):
        return False, "redirected_to_feishu_login"
    if status in (401, 403):
        return False, "authentication_required"
    if status == 404 or head_status == 404:
        return False, "not_found_or_private"
    if status and 200 <= int(status) < 300 and body:
        return True, "readable_http_body"
    if not get_result.get("ok"):
        return False, "request_failed"
    return False, "no_readable_body"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Feishu/Lark wiki URL to probe")
    parser.add_argument("--output", help="Write JSON diagnostic to this path")
    parser.add_argument("--max-bytes", type=int, default=200_000)
    parser.add_argument("--timeout", type=float, default=10.0, help="Per-request timeout in seconds")
    args = parser.parse_args()

    head_result = fetch(args.url, "HEAD", args.max_bytes, args.timeout)
    get_result = fetch(args.url, "GET", args.max_bytes, args.timeout)
    accessible, reason = classify(head_result, get_result)

    report = {
        "source_url": args.url,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "accessible": accessible,
        "reason": reason,
        "head": head_result,
        "get": get_result,
    }

    payload = json.dumps(report, indent=2, ensure_ascii=True)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if accessible else 2


if __name__ == "__main__":
    sys.exit(main())
