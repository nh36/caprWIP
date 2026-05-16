# Model entry implementation report — 2258 timber / timber

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2258-timber-timber.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2258-timber-timber.md`
- `Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_32_summary.md`
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
- local reference files for Kroonen, Ringe & Taylor, Clark Hall, and the shared epenthesis note

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` case centered on the consonantal frame
  **`timbr-`**.
- Kept Kroonen's **`*timbra-`** separate from Ringe and Taylor's citation line
  **`*timra > *timbr`**.
- Used a manual `Formation comparison`; no paradigm probe was needed.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`

## OCR / source-transcription checks

- Consulted Google Vision versions of Kroonen and Clark Hall directly.
- No suspicious OCR form was carried into the final prose; the entry uses only
  forms that were clear in the checked local sources.

## Unresolved points

- Comparative notation still differs between Kroonen's **`*timbra-`** and Ringe
  and Taylor's **`*timra > *timbr`** description.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.

## Citation-locator claim-isolation 03

- Citation locator tightened after claim-isolation pass; verified against `RingeTaylor2014, 327`.

## Citation-locator claim-isolation 07

- Citation locator tightened or status reclassified after claim-isolation 07;
  verified against `Kroonen2013, 517` and `ClarkHall1960, 294`.
