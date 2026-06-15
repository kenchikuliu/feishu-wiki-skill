#!/usr/bin/env python3
"""Import a Feishu Markdown or HTML export into this Codex skill."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_REFERENCE = "wiki-export.md"


class BasicHTMLToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.heading_level: int | None = None
        self.in_li = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.parts.append("\n\n" + ("#" * self.heading_level) + " ")
        elif tag in {"p", "div", "section", "article", "tr"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.in_li = True
            self.parts.append("\n- ")
        elif tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.parts.append("[")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = None
            self.parts.append("\n")
        elif tag == "li":
            self.in_li = False
            self.parts.append("\n")
        elif tag == "a":
            self.parts.append("]")

    def handle_data(self, data: str) -> None:
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self.parts.append(text)

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def read_export(path: Path) -> str:
    raw = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = BasicHTMLToMarkdown()
        parser.feed(raw)
        return parser.markdown()
    return raw.strip() + "\n"


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return clean_inline(match.group(1))
    for line in markdown.splitlines():
        stripped = clean_inline(line)
        if stripped:
            return stripped[:80]
    return fallback


def clean_inline(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_skill_md(skill_name: str, title: str, source_url: str | None) -> str:
    source_phrase = f" imported from {source_url}" if source_url else ""
    description = (
        f"Use when Codex needs to answer questions, follow workflows, or update "
        f"references from the imported Feishu wiki export titled '{title}'{source_phrase}."
    )

    return f"""---
name: {skill_name}
description: {yaml_quote(description)}
---

# {title}

## How To Use

Load `references/{DEFAULT_REFERENCE}` before answering questions or performing workflows from this Feishu wiki export. Treat the reference as the source of truth for terminology, commands, URLs, examples, and step order.

## Answering Rules

- Preserve names, commands, URLs, and configuration values exactly as written in the reference.
- If a user asks for an action described by the wiki, follow the relevant section step by step.
- If the reference is ambiguous or incomplete, state the gap and use local context to make the smallest safe assumption.
- If the user asks to refresh the skill from Feishu, request a fresh Markdown or HTML export and run `scripts/import_markdown_export.py`.

## Source

- Imported title: `{title}`
- Source URL: `{source_url or "not provided"}`
- Full imported content: `references/{DEFAULT_REFERENCE}`
"""


def write_reference(path: Path, title: str, source_url: str | None, body: str) -> None:
    stamped = datetime.now(timezone.utc).isoformat()
    header = f"""# {title}

Imported from: {source_url or "not provided"}
Imported at UTC: {stamped}

---

"""
    path.write_text(header + body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export_path", help="Feishu Markdown or HTML export")
    parser.add_argument("--skill-dir", default=".", help="Skill directory to update")
    parser.add_argument("--source-url", help="Original Feishu wiki URL")
    parser.add_argument("--force", action="store_true", help="Overwrite existing imported reference")
    parser.add_argument("--dry-run", action="store_true", help="Print generated SKILL.md without writing files")
    args = parser.parse_args()

    export_path = Path(args.export_path)
    skill_dir = Path(args.skill_dir)
    skill_md_path = skill_dir / "SKILL.md"
    reference_path = skill_dir / "references" / DEFAULT_REFERENCE

    if not export_path.exists():
        print(f"Export file not found: {export_path}", file=sys.stderr)
        return 1
    if reference_path.exists() and not args.force and not args.dry_run:
        print(f"Refusing to overwrite {reference_path}; pass --force", file=sys.stderr)
        return 1

    body = read_export(export_path)
    title = extract_title(body, export_path.stem)
    skill_name = skill_dir.resolve().name
    generated_skill = build_skill_md(skill_name, title, args.source_url)

    if args.dry_run:
        print(generated_skill)
        print(f"\nWould write reference: {reference_path}", file=sys.stderr)
        return 0

    (skill_dir / "references").mkdir(parents=True, exist_ok=True)
    write_reference(reference_path, title, args.source_url, body)
    skill_md_path.write_text(generated_skill, encoding="utf-8")
    print(f"Updated {skill_md_path}")
    print(f"Updated {reference_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
