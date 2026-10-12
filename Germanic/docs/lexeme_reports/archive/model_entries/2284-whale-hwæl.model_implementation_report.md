# Model entry implementation report — 2284 whale / hwæl

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2284-whale-hwæl.md`
- `Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md`
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
- local reference files for Orel, Kroonen, Clark Hall, Bosworth-Toller, and Bright

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2284-whale-hwæl.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2284-whale-hwæl.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2284-whale-hwæl.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2284-whale-hwæl.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` comparative-notation case centered on
  normalized singular **`hwæl`**.
- Kept Orel's **`*xwalaz`** and Kroonen's **`*hwali-`** distinct throughout.
- Marked **`hwæl`** explicitly as a normalization from dictionary spelling
  **`hwal`**.
- Used a manual `Formation comparison`; no paradigm probe was needed.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`
- `Orel2003`

## OCR / source-transcription checks

- Consulted Google Vision versions of Orel, Kroonen, Clark Hall, and
  Bosworth-Toller.
- The plain local Bright text shows odd OCR (`hwsel`, punctuation noise), so it
  was treated as background only and not quoted in the final entry.
- The final prose does not repeat the inaccurate exact note-form `Kroonen
  *hwalaz`; it keeps Kroonen's checked `*hwali-` separate from Orel's
  `*xwalaz`.

## Unresolved points

- Comparative notation remains divided between Orel's a-stem-like citation and
  Kroonen's `*hwali-`.
- The normalized singular `hwæl` depends on keeping dictionary spelling `hwal`
  and plural `hwalas` in view together.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 326`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

## Citation-locator page-anchor repair 01

- Citation locator tightened after page-anchor repair pass; verified against `Orel2003, 197`.
- Citation locator tightened after page-anchor repair pass; verified against `ClarkHall1960, 170`.

## Citation locator source-preparation triage 01

- Citation locator tightened or source status reclassified after source-preparation triage; verified against `Kroonen2013, 262`.
