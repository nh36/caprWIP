# Model entry implementation report — 2119 man / mannes

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2119-man-mannes.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2119-man-mannes.md`
- `Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_08_summary.md`
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
- local reference files for Campbell, Sievers-Brunner, Clark Hall, Ringe-Taylor, Orel, and Kroonen

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2119-man-mannes.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2119-man-mannes.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2119-man-mannes.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2119-man-mannes.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as a `late_analogy` paradigm-cell case centered on the
  attested genitive singular.
- Kept the citation headword `mann` separate from the selected target `mannes`.
- Used a manual `Paradigm comparison`; no automatic paradigm probe was run in
  this pass.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The row-local TSV note still cites `Kurath 1956`, but that key is absent from
  `docs/refs.bib`; the model entry therefore relies on Brunner and Campbell
  instead.
- The comparison remains manual because no saved probe spec yet exists for the
  `mannes` cell selection.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Orel2003, 299`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.

## Citation-locator master manifest 03

- Tightened `Kroonen2013` from a broad citation to verified page locator `354` after direct inspection of the local Kroonen text.

## Citation-locator master manifest 04

- Tightened `SieversBrunner1965` from broad citations to verified section locators `§226` and `§231` after direct inspection of the local Brunner text.

## Citation-locator claim-isolation 04

- Citation locator tightened after claim-isolation pass; verified against `ClarkHall1960, 197`.

## Citation-locator claim-isolation 05

Citation locator tightened after claim-isolation pass; verified against Campbell1959 at §621.

## Citation locator full-exhaustion 04

- Citation locator full-exhaustion 04: citation localized / removed / retained broad after primary-source review.
