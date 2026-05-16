# Model entry implementation report — 2268 wake / wacan

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2268-wake-wacan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2268-wake-wacan.md`
- `Germanic/docs/lexeme_reports/research_memos/2268-wake-wacan.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_33_summary.md`
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
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_revision_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Kroonen, Ringe & Taylor, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2268-wake-wacan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2268-wake-wacan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2268-wake-wacan.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2268-wake-wacan.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` class-split case rather than as a
  sound-law repair.
- Kept strong **`wacan`** and weak **`wacian`** separate throughout.
- Explicitly marked **`wacan`** as a normalized strong headword in light of the
  Bosworth-Toller note on simplex infinitive attestation.
- Used a manual `Class comparison`; no paradigm probe was needed.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`

## OCR / source-transcription checks

- Consulted Google Vision versions of Kroonen, Clark Hall, and Bosworth-Toller.
- No suspicious OCR form had to be quoted in the final prose; the final entry
  relies on clear dictionary wording and the stable trace output.

## Unresolved points

- The main caveat is philological, not derivational: **`wacan`** is the right
  strong comparator, but it is a normalized headword rather than a directly
  quoted simplex infinitive.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 226`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

## Citation-locator claim-isolation 05

Citation locator tightened after claim-isolation pass; verified against ClarkHall1960 at 338.

## Citation-locator claim-isolation 07

- Citation locator tightened or status reclassified after claim-isolation 07;
  verified against `Kroonen2013, 568`.
