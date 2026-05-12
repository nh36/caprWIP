# Model entry implementation report — 2293 will / willa

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2293-will-willa.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2293-will-willa.md`
- `Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- nearby shared `DEV_NOTES` passages for row 2292 only as contrastive background
- local reference files for `ClarkHall1960`, `Kluge2002`, `Kroonen2013`, `Orel2003`
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.model_implementation_report.md`

## Notes on this pass

- Treated the row as a lexical-disambiguation case, not a paradigm-cell case.
- Kept the final prose on the noun and moved the verb warning into a short lexical note.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `ClarkHall1960`
- `Kluge2002`
- `Kroonen2013`
- `Orel2003`

## Unresolved points

- Later review should keep the row note aligned with Kroonen's noun/verb split and avoid reviving the older `*walj-` wording.

## OCR and source-transcription checks

- Existing local vision-backed reference files were sufficient; no extra Google Vision rescue beyond those files was needed.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `ClarkHall1960, 368`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.
