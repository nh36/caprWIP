# Old English lexeme-entry writing skill

This writing skill is for producing **book-style lexical entries** for the
Germanic -> Old English write-up. It is meant to keep future drafting in the
genre established by the accepted model entry
`Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`.

The local repository files are **evidence-gathering tools**, not the subject of
the prose. Packets, DEV_NOTES, dossiers, traces, backlog files, and
implementation reports may be used to recover forms, claims, citations, and
uncertainties, but the final entry should be about the word, its
reconstruction, its Old English evidence, and its development.

## Workflow

Future entries should proceed in this order:

1. extract a **source ledger**;
2. draft a **book-style lexical entry**;
3. use the shared **reviewer checklist** and automated publication checks;
4. only then consider **manifest promotion**.

Do not create a completed checklist and implementation report for each word.
Record unique evidence, review qualifications and unresolved questions in the
source ledger or existing research memo; Git and test logs record mechanics.
Historical paired reports remain in `../archive/model_entries/`.

This order matters. The source ledger is the place where local file paths,
working uncertainties, and source-discovery notes belong. The final entry should
not narrate those local tools.

## Scope and length

Entries are not all the same length.

- A difficult analogical case may need every section in the template.
- A simple `regular`-with-`NOTE` case may be much shorter.
- `Paradigm comparison` is useful when the argument depends on choosing among
  competing paradigm cells; it should not be inflated for straightforward rows.

## Files in this skill

- `source_ledger_template.md` — reusable extraction table for source claims
- `book_entry_template.md` — reusable book-style entry template
- `reviewer_checklist.md` — acceptance checklist for draft review
- `anti_patterns.md` — banned or discouraged prose habits with replacements
- `../production_backlog.md` — current production routing
- `../archive/writing_skill/` — superseded rollout plan and skill creation record

## Core principles

- The source ledger may discuss local project files; the final entry should not.
- Give **actual forms**, not vague claims about disagreement.
- Establish **Old English evidence before paradigm comparison**.
- Keep short entries short.
- Do not include a conclusion section by default.
- Do not invent unattested forms, bibliography keys, or automatic probe results.
- Label manual comparisons honestly.
