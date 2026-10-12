# Model entry implementation report — 2242 ten / tēon

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2242-ten-tēon.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2242-ten-tēon.md`
- `Germanic/docs/lexeme_reports/research_memos/2242-ten-tēon.md`
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
- local reference files for Fulk, Campbell, Sievers-Brunner, and Hirt

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2242-ten-tēon.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2242-ten-tēon.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2242-ten-tēon.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2242-ten-tēon.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `attested_variant` case centered on the un-umlauted
  bare-cardinal branch.
- Treated exact `tēon` as a normalized comparison form rather than as the most
  common directly cited simplex headword.
- Used a manual `Variant comparison`; no extra paradigm-probe artifact was added
  in this pass.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `Fulk2018`
- `SieversBrunner1965`

## Unresolved points

- Exact simplex `tēon` remains less directly attested than the wider variant set
  `tien/tīen`, `tēn`, `tēo`, `tēa`.
- The live row label `attested_variant` may deserve later review if the project
  prefers to describe `tēon` more explicitly as a normalized regular outcome.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
