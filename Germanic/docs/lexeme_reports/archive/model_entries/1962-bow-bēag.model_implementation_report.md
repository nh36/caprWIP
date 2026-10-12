# Model entry implementation report — 1962 bow / bēag

## Files inspected

- `Germanic/docs/lexeme_reports/packets/1962-bow-bēag.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/1962-bow-bēag.md`
- `Germanic/docs/lexeme_reports/research_memos/1962-bow-bēag.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `docs/refs.bib`
- local reference files for Campbell, Ringe-Taylor, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/1962-bow-bēag.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/1962-bow-bēag.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1962-bow-bēag.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/1962-bow-bēag.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as a `late_analogy` paradigm-cell case centered on the
  singular preterite rather than the infinitive.
- Kept the main analytical distinction between regular `bēag` and the later
  leveling visible in the wider `būgan` paradigm.
- Used a manual `Paradigm comparison`; no automatic paradigm probe was run in
  this pass.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `RingeTaylor2014`

## Unresolved points

- The verbal `bēag` must remain clearly distinguished from the noun `bēag` in
  any later editorial pass.

## Citation-locator pilot 01

- Added page-specific Pandoc locators to the paired model entry for
  `[@RingeTaylor2014, 55]` and `[@ClarkHall1960, 45]`.
- Left `Campbell1959` and `BosworthToller1898` broad in this pilot because the
  exact page-to-claim mapping for the cited statements was not confirmed from
  the available local files.

## Citation-locator rescue pilot 02

- Recovered `[@Campbell1959, 53]` for the class-II singular-preterite
  discussion and `[@BosworthToller1898, 122]` for `bēag` under `bugan`.
- Updated the paired model entry and source ledger accordingly.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.
