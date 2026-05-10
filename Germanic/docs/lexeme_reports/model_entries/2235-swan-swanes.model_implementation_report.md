# Model entry implementation report — 2235 swan / swanes

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2235-swan-swanes.md`
- `Germanic/docs/lexeme_reports/research_memos/2235-swan-swanes.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_30_summary.md`
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
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Orel, Clark Hall, and Bright

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` paradigm-cell case centered on the
  attested genitive singular `swanes`.
- Kept the citation form `swan` explicit so the inflected target does not read
  like the default headword.
- Used a manual `Paradigm-cell comparison`; no saved probe spec was added in
  this pass.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `ClarkHall1960`
- `Orel2003`

## Unresolved points

- The row is review-sensitive because `swanes` is a real OE form but still only
  a paradigm cell, whereas `swan` remains the ordinary headword.
- No row-specific automatic probe artifact exists beyond the current manual
  citation-form/genitive contrast.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
