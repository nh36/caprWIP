# Model entry implementation report — 2227 strew / strīeġan

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2227-strew-strīeġan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2227-strew-strīeġan.md`
- `Germanic/docs/lexeme_reports/research_memos/2227-strew-strīeġan.md`
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
- local reference files for Kroonen, Ringe-Taylor, Campbell, Fulk, and Luick

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2227-strew-strīeġan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2227-strew-strīeġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2227-strew-strīeġan.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2227-strew-strīeġan.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as a `reconstructed_oe` case contrasting inherited Anglian
  `strēgan`, reconstructed WS `strīeġan`, and remodeled WS class-II forms.
- Kept the target explicitly marked as reconstructed throughout the OE evidence
  and comparison sections.
- Used a manual `Reconstruction status` table rather than a paradigm-probe run.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `Fulk2018`
- `Kroonen2013`
- `Luick1914`
- `RingeTaylor2014`

## Unresolved points

- The strongest directly attested Old English evidence belongs either to Anglian
  `strēgan` or to remodeled West Saxon class-II forms, not to exact `strīeġan`.
- The entry therefore remains a review-sensitive reconstructed-OE comparator
  case.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
