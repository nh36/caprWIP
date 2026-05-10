# Model entry implementation report — 2252 thousand / þūsend

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2252-thousand-þūsend.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2252-thousand-þūsend.md`
- `Germanic/docs/lexeme_reports/research_memos/2252-thousand-þūsend.md`
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
- local reference files for Kroonen, Campbell, Luick, and Viredaz

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2252-thousand-þūsend.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2252-thousand-þūsend.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2252-thousand-þūsend.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2252-thousand-þūsend.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` stage-comparison case centered on the
  OE-oriented transponent `*θūs-èndi`.
- Kept the etymological PGmc reconstruction `*þūsundī-` separate from the
  selected OE-facing modelling input.
- Used a manual `Stage comparison`; no noun-paradigm probe was needed for this
  pass.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `GermanicSlavicBaltic2025`
- `Kroonen2013`
- `Luick1914`

## Unresolved points

- The chronology excluding regular double umlaut is stronger than any single
  positive explanation for medial `e`.
- The entry therefore keeps Luick's analogical account and Viredaz's schwa
  caution side by side instead of treating one as uniquely proved.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
