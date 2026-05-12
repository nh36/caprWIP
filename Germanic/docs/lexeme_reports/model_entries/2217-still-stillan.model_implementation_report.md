# Model entry implementation report — 2217 still / stillan

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2217-still-stillan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2217-still-stillan.md`
- `Germanic/docs/lexeme_reports/research_memos/2217-still-stillan.md`
- `Germanic/data/germanic-aligned-final.tsv`
- local reference files for Clark Hall, Bosworth-Toller, and Kluge-Seebold
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2217-still-stillan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2217-still-stillan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2217-still-stillan.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2217-still-stillan.model_implementation_report.md`

## Notes on this pass

- Kept the entry on the verb row and treated adjective `stille` as related background only.
- Avoided importing the older shared notation debate into the final prose.
- Used Clark Hall and Bosworth-Toller as the main OE-side control sources.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `KlugeSeebold2011`

## Unresolved points

- Later review should preserve the verb-versus-adjective distinction explicitly.

## OCR and source-transcription checks

- Existing local reference files were sufficient; no extra Google Vision fallback beyond those files was needed.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 724`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.
