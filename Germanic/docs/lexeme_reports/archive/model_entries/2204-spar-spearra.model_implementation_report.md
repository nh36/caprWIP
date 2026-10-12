# Model entry implementation report — 2204 spar / spearra

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2204-spar-spearra.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2204-spar-spearra.md`
- `Germanic/docs/lexeme_reports/research_memos/2204-spar-spearra.md`
- `Germanic/data/germanic-aligned-final.tsv`
- local reference files for Kroonen, Orel, and Luick
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2204-spar-spearra.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2204-spar-spearra.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2204-spar-spearra.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2204-spar-spearra.model_implementation_report.md`

## Notes on this pass

- Kept the entry on the noun and explicitly fenced off unrelated verb `sperran`.
- Used Kroonen and Orel for the comparative noun set and Luick for the breaking environment.
- Avoided inflating the row just because neighboring `spar-` materials in the repo are verbal.

## Citation-key check

Checked against `docs/refs.bib`:

- `Kroonen2013`
- `Luick1914`
- `Orel2003`

## Unresolved points

- Later review should preserve the explicit noun-versus-verb distinction, since direct OE lexicographic support for `spearra` is thinner in the local files than for some other rows.

## OCR and source-transcription checks

- Existing local reference files were sufficient; no extra Google Vision fallback beyond those files was needed.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
