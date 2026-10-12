# Model entry implementation report — 2234 swallow / swealwe

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2234-swallow-swealwe.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2234-swallow-swealwe.md`
- `Germanic/docs/lexeme_reports/research_memos/2234-swallow-swealwe.md`
- `Germanic/data/germanic-aligned-final.tsv`
- local reference files for Kroonen, Ringe & Taylor, Clark Hall, Campbell, and Brunner
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2234-swallow-swealwe.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2234-swallow-swealwe.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2234-swallow-swealwe.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2234-swallow-swealwe.model_implementation_report.md`

## Notes on this pass

- Kept the entry on the bird noun and treated the old confusion with `swelgan` as background only.
- Used Ringe & Taylor for the WS versus Mercian framing and Campbell or Brunner for later variant forms.
- Kept the citation form separate from oblique or variant `swaluwe`-type material.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- Later review should preserve the distinction between citation-form `swealwe` and later variant or oblique forms such as `swaluwe` and `swalewan`.

## OCR and source-transcription checks

- Existing local reference files were sufficient; no extra Google Vision fallback beyond those files was needed.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Kroonen2013, 535`; `RingeTaylor2014, 200`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.
