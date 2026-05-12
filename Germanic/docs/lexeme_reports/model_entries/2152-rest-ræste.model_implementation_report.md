# Model entry implementation report — 2152 rest / ræste

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2152-rest-ræste.md`
- `Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_09_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_01_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_revision_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Kroonen, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as a `late_analogy` paradigm-cell case centered on the
  attested oblique `ræste` form.
- Kept citation-form `ræst` visible throughout so the entry does not confuse the
  selected oblique target with the dictionary headword.
- Used a manual `Paradigm comparison`; no saved automatic probe was added in
  this pass.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`

## Unresolved points

- A later promotion pass should decide whether the selected genitive-singular
  framing is best left narrow or broadened to a more explicit oblique-singular
  comparison.
- The row remains review-sensitive because the source stack still cites an older
  shorter explanation of the ending chronology outside the final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 121`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.
