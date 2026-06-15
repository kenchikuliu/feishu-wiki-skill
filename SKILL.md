---
name: feishu-wiki-skill
description: "Guide Foreign-owned U.S. Delaware single-member LLC IRS information reporting DIY workflows. Use when Codex needs to explain, prepare checklists for, or draft field-by-field Form 5472 + pro forma Form 1120 packages for a foreign-owned U.S. disregarded entity, including owner capital contributions/distributions, Part V attachments, fax/mail filing order, and evidence retention."
---

# Foreign-Owned U.S. DE LLC IRS Filing

## Scope

Use this skill for a foreign person who wholly owns a U.S. domestic disregarded entity, especially a Delaware single-member LLC, and needs to prepare the IRS information filing package described in the imported Feishu wiki:

- Form 5472 as the substantive information return.
- Pro forma Form 1120 as the filing cover/attachment vehicle.
- Part V attachment for reportable transactions between the LLC and foreign owner or related party.
- Fax/mail submission order and proof-retention workflow.

This is a workflow aid, not tax or legal advice. For current-year work, verify the latest IRS Form 5472, Form 1120, and instructions before finalizing.

## Primary Reference

Load `references/wiki-export.md` before doing field-level work. It contains the full imported guide, sample facts, field-by-field examples, and copyable text templates.

Load `references/irs-official.md` when checking official IRS authority, filing methods, or current instructions.

## Core Logic

- Treat Form 5472 as the core disclosure form for reportable transactions involving the foreign owner or related party.
- Treat pro forma Form 1120 as the required wrapper for a foreign-owned U.S. DE that otherwise has no ordinary corporate income tax return filing requirement.
- Do not turn the DE into a full C corporation income tax workflow unless the user gives facts that require a different analysis.
- For the simple imported example, report owner funding in Form 5472 Part V and attach a short transaction statement.
- Use the special foreign-owned U.S. DE filing route from the Form 5472 instructions, not the ordinary Form 1120 filing address.

## Collect Inputs

Before drafting a package, collect:

- LLC legal name, EIN, address, formation date, state, and tax year.
- Whether this is the first filing, a final filing, or a name/address change year.
- Foreign owner name, country, tax residence, citizenship, address, U.S. identifying number if any, and foreign taxpayer ID if any.
- LLC total assets at year end.
- Principal business activity and code when available.
- Owner-to-LLC transfers during the tax year, including verification deposits and Stripe/payment-platform setup transfers.
- LLC-to-owner transfers, owner draws, distributions, reimbursements, or payment-platform payouts to the owner.
- Any non-cash, below-market, loan, service, royalty, rent, sale, purchase, or other related-party transactions that make the simple template insufficient.

## Drafting Workflow

1. Decide whether the imported simple path applies:
   - 100% foreign-owned U.S. DE.
   - Reportable transaction exists with the foreign owner or related party.
   - No facts suggesting a full Form 1120, Form 1120-F, partnership return, payroll, withholding, sales tax, or state filing issue.

2. Prepare pro forma Form 1120:
   - Write `Foreign-owned U.S. DE` across the top.
   - Fill entity name and address.
   - Fill item B with EIN.
   - Fill item C or other first-page items only when the current official form/instructions require them for this use case.
   - Check item E for initial/final/name/address changes when applicable.
   - Leave ordinary income, deduction, and tax computation lines blank unless facts require escalation.

3. Prepare Form 5472:
   - Part I: reporting LLC details, total assets, activity, transaction totals, number of Forms 5472, country and date fields, and foreign-owned U.S. DE checkboxes.
   - Part II: foreign owner as the 25% foreign shareholder.
   - Part III: same foreign owner as related party when applicable.
   - Part IV: use zero/blank only if transactions are being reported in Part V under the foreign-owned U.S. DE rules and no Part IV facts exist.
   - Part V: attach a statement summarizing owner contributions/distributions or other reportable transactions.
   - Parts VI and VII: answer from facts; do not blindly copy the sample if facts differ.

4. Build the filing packet in this order:
   - Fax cover sheet if faxing.
   - Pro forma Form 1120.
   - Form 5472.
   - Part V attachment.

5. File by the due date for the relevant Form 1120 year, including extensions if properly requested. Preserve proof:
   - Fax confirmation receipt, or
   - Mailing receipt/tracking and copy of the mailed packet.

## Escalate

Pause and tell the user to consult a qualified tax professional when:

- The LLC has U.S. trade or business income, employees, contractors, withholding, payroll, inventory, U.S. real estate, loans, services, royalties, rent, sale/purchase transactions, crypto, or multiple owners.
- The owner is not an individual, or ownership changed during the year.
- The user asks for penalty defense, reasonable cause letters, delinquent filings, state filings, treaty positions, or entity classification elections.
- Current IRS instructions conflict with the imported wiki.

## Updating The Skill

If the Feishu wiki is exported again, import it with:

```powershell
python scripts/import_markdown_export.py path\to\export.md --skill-dir . --source-url "https://t02xmt66jgr.feishu.cn/wiki/Ei91wxkxSistBkkBHDrc29bMnah" --force
```

After import, review and restore this domain-specific `SKILL.md` if the script regenerated a generic one.
