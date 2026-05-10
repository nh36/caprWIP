# Model entry implementation report — 2274 water / wæter

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2274-water-wæter.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2274-water-wæter.md`
- `Germanic/docs/lexeme_reports/research_memos/2274-water-wæter.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_01_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_revision_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_03_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_revision_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Kroonen, Ringe & Taylor, Bright, and the current water-fix note

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2274-water-wæter.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2274-water-wæter.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2274-water-wæter.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2274-water-wæter.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` singular-selection case for a
  heteroclitic r/n-stem noun.
- Kept generalized **`*wátną`** separate from singular **`*wátōr`** throughout.
- Used a manual `Stage comparison`; no new paradigm-probe file was added.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `Kroonen2013`
- `RingeTaylor2014`

## OCR / source-transcription checks

- Consulted Google Vision versions of Kroonen and Bright where available.
- No corrupt source form needed to be quoted in the final entry.

## Unresolved points

- The main caveat is representational: the generalized comparative label is less
  precise than the heteroclitic stem notation and the selected singular input.
- Dialectal `weter/weeter` remains useful background but not the selected target.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
