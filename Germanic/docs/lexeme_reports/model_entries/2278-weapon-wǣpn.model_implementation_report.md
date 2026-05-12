# Model entry implementation report — 2278 weapon / wǣpn

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2278-weapon-wǣpn.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2278-weapon-wǣpn.md`
- `Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- relevant shared `DEV_NOTES` passages on `wǣpn`, `wǣpen`, and `wǣpnes`
- local reference files for `BrightCassidyRingler1971`, `Campbell1959`, `ClarkHall1960`, `Kroonen2013`
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2278-weapon-wǣpn.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2278-weapon-wǣpn.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2278-weapon-wǣpn.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2278-weapon-wǣpn.model_implementation_report.md`

## Notes on this pass

- Kept the entry on the selected unbroken noun and let the note explain the later broken simplex.
- Used Campbell and Bright for the `wǣpen ~ wǣpnes` contrast and Clark Hall for headword practice.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`

## Unresolved points

- Later review should keep the entry compact and resist turning the register issue into a full paradigm report.

## OCR and source-transcription checks

- Existing local vision-backed reference files were sufficient; no extra Google Vision rescue beyond those files was needed.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Citation-locator pilot 01

- Added page-specific Pandoc locators to the paired model entry for
  `[@Kroonen2013, 617]`, `[@BrightCassidyRingler1971, 29]`, and
  `[@ClarkHall1960, 355]`.
- Left `Campbell1959` broad in this pilot because the local file supports the
  relevant cluster-noun behavior more confidently than the exact
  nominative/oblique wording cited in the model entry.

## Citation-locator rescue pilot 02

- Recovered `[@Campbell1959, 150]` and `[@Campbell1959, 226–227]` for the
  cluster-noun behavior that the local file actually supports.
- Narrowed the paired model-entry wording accordingly and updated the source
  ledger.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
