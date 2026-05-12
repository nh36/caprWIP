# Model entry implementation report — 2088 lade / hladan

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2088-lade-hladan.md`
- `Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1962-bow-bēag.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1968-breast-brēost.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2030-fowl-fugol.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_01_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Ringe-Taylor, Kroonen, Campbell, Orel, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2088-lade-hladan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2088-lade-hladan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2088-lade-hladan.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2088-lade-hladan.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` class-selection case.
- Kept the OE-facing strong verb separate from the wider weak comparative
  family label.
- Used a manual `Class comparison`; no automatic paradigm probe was run in this
  pass.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The main review point is presentational: the entry should continue to show
  clearly that the comparative weak headword and the OE strong input are
  different branches of one family.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 559`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.
