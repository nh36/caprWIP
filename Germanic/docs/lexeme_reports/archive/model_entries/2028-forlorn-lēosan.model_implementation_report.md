# Model entry implementation report — 2028 forlorn / lēosan

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2028-forlorn-lēosan.md`
- `Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_17_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1943-begin-beġinnan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1987-deed-dǣd.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Kroonen, Orel, Ringe & Taylor, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2028-forlorn-lēosan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2028-forlorn-lēosan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2028-forlorn-lēosan.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2028-forlorn-lēosan.model_implementation_report.md`

## Notes on this pass

- Kept the entry compact and treated the row as a regular simplex derivation.
- Added a short form note explaining that the English adjective is directly continued by the prefixed Old English family `forlēosan / forloren`.
- Omitted a paradigm comparison because the live issue is lexical targeting rather than a paradigm-cell rescue.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The strongest direct Old English evidence behind English `forlorn` remains prefixed, so later editorial review may still decide whether `forlēosan` should replace `lēosan` as the citation form.

## OCR and source-transcription checks

- No suspicious OCR or transcription issue required corrective rewriting in the final prose.
- The consulted local Kroonen, Orel, Ringe & Taylor, and dictionary files were legible enough for direct use.
- No Google Vision fallback beyond the ordinary local vision/reference files was needed.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
