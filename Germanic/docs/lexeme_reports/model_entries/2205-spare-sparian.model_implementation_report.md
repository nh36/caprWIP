# Model entry implementation report — 2205 spare / sparian

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2205-spare-sparian.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2205-spare-sparian.md`
- `Germanic/docs/lexeme_reports/research_memos/2205-spare-sparian.md`
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
- local reference files for Brunner, Campbell, Kroonen, Orel, and Ringe-Taylor

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2205-spare-sparian.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2205-spare-sparian.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2205-spare-sparian.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2205-spare-sparian.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` class-remodelling case centered on the
  attested citation verb `sparian`.
- Kept inherited class-III `*sparēną` distinct from the selected class-II
  formation `*spárōjaną`.
- Used a manual `Formation comparison`; no checked-in dedicated probe spec was
  available for this lexeme.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The main review point is whether the current balance between West-Saxon
  citation form `sparian` and the Anglian relic forms is the right one for
  promotion.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.

## Citation-locator claim-isolation 06

- Citation locator tightened after claim-isolation pass; verified against `Kroonen2013, 465`.
