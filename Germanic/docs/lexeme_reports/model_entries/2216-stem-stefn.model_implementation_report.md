# Model entry implementation report — 2216 stem / stefn

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2216-stem-stefn.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2216-stem-stefn.md`
- `Germanic/docs/lexeme_reports/research_memos/2216-stem-stefn.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_29_summary.md`
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
- local reference files for Ringe-Taylor, Clark Hall, Bülbring, Luick, Orel, Kroonen, and Fulk

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` case centered on the OE-facing
  transponent `*stébnō -> stefn`.
- Kept the broader comparative label `*stámnaz` separate from the source-backed
  `stefn/stemn` material.
- Used a manual `Source comparison`; no automatic paradigm probe was needed for
  this pass.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Bulbring1902`
- `ClarkHall1960`
- `Fulk2018`
- `Kroonen2013`
- `Luick1914`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The strongest source support still concerns the noun `stefn` 'voice, sound',
  whereas the comparative label `*stámnaz` belongs to a broader stem/trunk
  family.
- The entry therefore remains review-sensitive as a production item, even
  though the OE-side derivation itself is clear.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
