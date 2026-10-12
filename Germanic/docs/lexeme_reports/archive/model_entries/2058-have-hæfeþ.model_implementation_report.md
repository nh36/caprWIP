# Model entry implementation report — 2058 have / hæfeþ

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2058-have-hæfeþ.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2058-have-hæfeþ.md`
- `Germanic/docs/lexeme_reports/research_memos/2058-have-hæfeþ.md`
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
- local reference files for Ringe-Taylor, Fulk, Campbell, Bosworth-Toller, Clark Hall, and Kroonen

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2058-have-hæfeþ.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2058-have-hæfeþ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2058-have-hæfeþ.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2058-have-hæfeþ.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as a `late_analogy` paradigm-cell case centered on the 3sg
  present.
- Kept the normalized target `hæfeþ` distinct from the ordinary citation form
  `habban` and the syncopated finite forms.
- Used a manual `Paradigm comparison`; no automatic paradigm probe was run in
  this pass.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `Fulk2018`
- `Kroonen2013`
- `RingeTaylor2014`

## Unresolved points

- The main review point is how strongly to foreground the normalized `hæfeþ`
  against the more familiar attested forms `habban` and `hæfþ`.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `ClarkHall1960, 157`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.

Citation locator claim-isolation 01 split the class-III stem and finite-form sentences and added verified locators for `RingeTaylor2014, 93` and `Campbell1959, §762`.

## Citation-locator claim-isolation 03

- Citation locator tightened after claim-isolation pass; verified against `RingeTaylor2014, 364`.
- Citation locator tightened after claim-isolation pass; verified against `Campbell1959, §762`.

## Citation locator source-preparation triage 01

- Citation locator tightened or source status reclassified after source-preparation triage; verified against `ClarkHall1960, 157`.

## Post-exhaustion audit 03

- Post-exhaustion audit 03: localized reopened broad citation / removed redundant support / retained broad with source-specific reason / revised under-cited prose.

## Post-exhaustion audit 04

- Post-exhaustion audit 04: localized reopened broad citation / removed redundant support / retained broad with source-specific reason / revised under-cited prose.
