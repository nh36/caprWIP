# Model entry implementation report — 2086 knight / cniht

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2086-knight-cniht.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2086-knight-cniht.md`
- `Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md`
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
- local reference files for Ringe-Taylor, Orel, Kluge-Seebold, Campbell, Sievers-Brunner, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2086-knight-cniht.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2086-knight-cniht.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2086-knight-cniht.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2086-knight-cniht.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` stem-choice case because that is the
  live row classification, while explicitly reflecting the corrected
  `*knéxtaz`-based derivation.
- Kept the stale row label visible in the metadata table but did not use it as
  linguistic authority in the prose.
- Used a manual `Stem comparison`; no automatic paradigm probe was run in this
  pass.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `KlugeSeebold2011`
- `Orel2003`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The main review point is row policy: the corrected derivational input is clear,
  but the row's `PROTO` and `DERIVATION_CLASS` metadata lag behind it.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.
