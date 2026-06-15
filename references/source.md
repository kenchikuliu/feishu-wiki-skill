# Source Feishu Wiki

Source URL:

```text
https://t02xmt66jgr.feishu.cn/wiki/Ei91wxkxSistBkkBHDrc29bMnah
```

## Initial Access Result

Checked on 2026-06-15 from this workstation.

- Browser navigation redirected toward Feishu login and showed `login.feishu.cn` failing with HTTP 504.
- `curl -L` reached an `accounts.feishu.cn/accounts/page/login` page rather than wiki content.
- Direct `HEAD` requests to the wiki URL returned HTTP 404.
- Search for the exact wiki token and full URL found no public indexed copy.

Conclusion: the wiki body was not publicly accessible from this environment. Do not treat the Feishu login HTML as source content.

## Update Path

Export the wiki page or space from Feishu as Markdown or HTML, then run:

```powershell
python scripts/import_markdown_export.py path\to\export.md --skill-dir . --source-url "https://t02xmt66jgr.feishu.cn/wiki/Ei91wxkxSistBkkBHDrc29bMnah" --force
```

That command writes the exported body to `references/wiki-export.md` and regenerates `SKILL.md` so future Codex sessions can use the imported wiki content directly.
