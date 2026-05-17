# Model entry implementation report — 2134 neck / hnecca

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2134-neck-hnecca.md`
- `Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_01_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_revision_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Kroonen 2011, Kluge-Seebold, Orel, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2134-neck-hnecca.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2134-neck-hnecca.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2134-neck-hnecca.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2134-neck-hnecca.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` stem-selection case centered on the
  e-grade weak masculine noun.
- Kept the wider a-grade family visible without letting it control the OE-facing
  derivation.
- Used a manual `Stem comparison`; no paradigm probe was needed in this pass.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `KlugeSeebold2011`
- `Kroonen2011`
- `Orel2003`

## Unresolved points

- The strongest philological tension is still the difference between the retained
  comparative label `*xnákkaz` and the e-grade weak-noun input used for Old
  English.
- The live TSV note is blank, so this distinction is not yet summarized there.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 567`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

## Citation-locator claim-isolation 04

- Citation locator tightened after claim-isolation pass; verified against `ClarkHall1960, 162`.

## Citation locator source-preparation triage 01

- Citation locator tightened or source status reclassified after source-preparation triage; verified against `Kroonen2011, 167`.

## Citation locator source-preparation audit 06

- Source-preparation audit 06: recovered page-safe locator / retained broad pending paginated witness / updated source-witness blocker.
