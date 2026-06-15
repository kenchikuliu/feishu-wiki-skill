---
name: feishu-wiki-skill
description: "Convert Feishu or Lark wiki pages, access diagnostics, and exported Markdown or HTML into reusable Codex skill content. Use when Codex needs to scrape or diagnose a Feishu wiki link, import a Feishu wiki export, update this skill from a fresh export, or answer from an imported Feishu wiki reference."
---

# Feishu Wiki Skill

## Workflow

1. Probe the Feishu wiki URL before assuming the content is public:

   ```powershell
   python scripts/probe_feishu_url.py "https://example.feishu.cn/wiki/token" --output references/access-diagnostic.json
   ```

2. If the probe reaches a readable document page, extract the visible article text with a browser or Feishu export and preserve the original headings.

3. If the probe redirects to `accounts.feishu.cn`, `login.feishu.cn`, or a passport page, treat the page as private. Do not infer hidden wiki content from the login page. Ask for one of these inputs:

   - A Feishu Markdown export.
   - A Feishu HTML export.
   - A copied full-page Markdown/text dump.
   - Explicit authenticated browser/API access for that workspace.

4. Import the exported content into this skill:

   ```powershell
   python scripts/import_markdown_export.py path\to\feishu-export.md --skill-dir . --source-url "https://example.feishu.cn/wiki/token" --force
   ```

5. After import, answer user requests from `references/wiki-export.md` first. Load `references/source.md` only when provenance, access status, or update steps matter.

## Content Rules

- Preserve product names, commands, URLs, tables, and numbered workflows exactly when importing.
- Keep `SKILL.md` procedural and concise. Put the full wiki content in `references/wiki-export.md`.
- If the wiki content describes a fragile workflow, turn the core steps into imperative instructions in `SKILL.md` and keep details in the reference file.
- If the wiki content is broad or long, keep only a navigation guide in `SKILL.md` and tell Codex when to read the relevant sections in `references/wiki-export.md`.
- Never commit cookies, session state, exported auth JSON, or captured login pages.

## Current Source

This repository was initialized from the Feishu wiki URL recorded in `references/source.md`. The URL was not publicly readable during the initial capture attempt, so this skill currently contains the acquisition and import workflow rather than the private wiki body.

Run the import script with a real Feishu export to convert this repository from an acquisition skill into the final content skill.
