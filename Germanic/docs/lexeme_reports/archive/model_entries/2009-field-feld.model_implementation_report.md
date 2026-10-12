# Model entry implementation report — 2009 field / feld

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2009-field-feld.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2009-field-feld.md`
- `Germanic/docs/lexeme_reports/research_memos/2009-field-feld.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1942-beech-bōc.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1943-begin-beġinnan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1954-bone-bān.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1987-deed-dǣd.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_07_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Ringe & Taylor, Campbell, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2009-field-feld.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2009-field-feld.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2009-field-feld.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2009-field-feld.model_implementation_report.md`

## Notes on this pass

- Kept the entry compact because the row is already a stable regular derivation.
- Preserved the `*felþu- ~ *feldu-` issue only as explanatory background for medial `-ld-`.
- Omitted a paradigm comparison because the row does not depend on any contested OE cell choice.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `RingeTaylor2014`

## Unresolved points

- Later editorial review should keep the historical `*felþu- ~ *feldu-` ambiguity explanatory rather than treating it as a live metadata problem.

## OCR and source-transcription checks

- The relevant Ringe-Taylor OCR line is noisy in its exact preforms, so the model entry paraphrases the ambiguity instead of reproducing the garbled text.
- Campbell and Clark Hall were legible in the local files.
- No Google Vision fallback beyond the ordinary local reference files was needed.

## Citation-locator pilot 01

- Added page-specific Pandoc locators to the paired model entry for
  `[@RingeTaylor2014, 170]`, `[@Campbell1959, 169]`, and
  `[@ClarkHall1960, 114]`.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
