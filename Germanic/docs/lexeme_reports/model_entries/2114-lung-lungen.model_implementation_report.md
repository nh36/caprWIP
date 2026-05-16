# Model entry implementation report — 2114 lung / lungen

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2114-lung-lungen.md`
- `Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md`
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
- local reference files for Kroonen, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2114-lung-lungen.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2114-lung-lungen.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2114-lung-lungen.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2114-lung-lungen.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `early_analogy` derivational-selection case centered
  on the attested OE feminine noun.
- Kept the source-level tension between the normalized input used here and
  Kroonen's cited derivative visible in the final package.
- Used a manual `Formation comparison`; no automatic paradigm probe was run in
  this pass.

## Post-review polish

- Recast the `*lungunjō-` / `*lúnganjō` difference as a source-notation and
  normalization issue rather than repository state.
- Reduced the emphasis on the notation difference in the model entry while
  keeping the substantive caveat in this report and the checklist.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`

## Unresolved points

- The main review point is the relation between normalized `*lúnganjō` and
  Kroonen's cited `*lungunjō-`; the entry keeps that tension visible rather than
  flattening it.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  pilot report was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 634`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

## Citation-locator headword audit 01

- Citation locator tightened or reclassified after headword audit; verified against `Kroonen2013, 384`.
