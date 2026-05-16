# Model entry implementation report — 2090 lap / lappa

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2090-lap-lappa.md`
- `Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md`
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
- local reference files for Orel, Kroonen, Kluge-Seebold, Campbell, Sievers-Brunner, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` stem-selection case centered on the
  weak masculine noun.
- Kept the attested OE variant line (`læppa`, `leappan`) visible without making
  it carry the derivational argument.
- Used a manual `Stem comparison`; no automatic paradigm probe was run in this
  pass.

## Post-review polish

- Removed metadata-facing phrasing from the body prose and comparison table.
- Reframed `*lábbaz` as a competing comparative label rather than as repository
  bookkeeping.
- Preserved the substantive caveat that the weak-noun analysis is stronger than
  the preserved citation label.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `KlugeSeebold2011`
- `Kroonen2013`
- `Orel2003`
- `SieversBrunner1965`

## Unresolved points

- The main review point is row policy: the selected weak masculine input is
  well-supported, but the preserved citation label still follows the older
  `*lábbaz` line.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 613`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

## Citation-locator page-anchor repair 01

- Citation locator tightened after page-anchor repair pass; verified against `ClarkHall1960, 180`.

## Citation-locator claim-isolation 05

Citation locator tightened after claim-isolation pass; verified against Campbell1959 at §158 and SieversBrunner1965 at §10.

## Citation locator full-exhaustion 01

- Citation locator full-exhaustion 01: citation localized / removed / retained broad after primary-source review.

## Citation locator full-exhaustion 02

- Citation locator full-exhaustion 02: citation localized / removed / retained broad after primary-source review.
