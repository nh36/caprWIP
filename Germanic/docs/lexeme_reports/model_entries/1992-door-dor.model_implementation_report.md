# Model entry implementation report — 1992 door / dor

## Files inspected

- `Germanic/docs/lexeme_reports/packets/1992-door-dor.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/1992-door-dor.md`
- `Germanic/docs/lexeme_reports/research_memos/1992-door-dor.md`
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
- local reference files for Kroonen, Ringe & Taylor, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/1992-door-dor.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1992-door-dor.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model_implementation_report.md`

## Notes on this pass

- Kept the entry compact and centered on the attested neuter `dor`.
- Treated `duru` as parallel Old English evidence rather than as the selected modeling target.
- Omitted a paradigm comparison because the live row is a straightforward regular derivation once the stem split is made explicit.

## Citation-key check

Checked against `docs/refs.bib`:

- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`

## Unresolved points

- Later editorial review should keep the selected `dor` line distinct from the more familiar feminine `duru` tradition.

## OCR and source-transcription checks

- No suspicious OCR form required corrective rewriting in the final prose.
- Kroonen's Greek comparator line is noisy in the local OCR, so the model entry paraphrases only the relevant Germanic evidence.
- No Google Vision fallback beyond the ordinary local vision-backed reference files was needed.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
