# Model entry implementation report — 1949 bier / bǣr

## Files inspected

- `Germanic/docs/lexeme_reports/packets/1949-bier-bǣr.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/1949-bier-bǣr.md`
- `Germanic/docs/lexeme_reports/research_memos/1949-bier-bǣr.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Kroonen, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/1949-bier-bǣr.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/1949-bier-bǣr.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1949-bier-bǣr.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/1949-bier-bǣr.model_implementation_report.md`

## Notes on this pass

- Kept the corrected `*bērō-` lexeme central and left the stale `*barwōn` detour out of the model entry.
- Used a short source note so dictionary `bær` / `bar` and normalized `bǣr` stay clearly separated.
- Omitted a paradigm comparison because the row is a straightforward citation-form noun.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2013`

## Unresolved points

- Later editorial review may decide whether dictionary-style `bær` should ever replace normalized `bǣr` in a different presentation layer, but no change is needed for this model entry.

## OCR and source-transcription checks

- No suspicious OCR or transcription issue required corrective rewriting in the final prose.
- The only source issue was lexicographic normalization (`bær` / `bar` beside normalized `bǣr`), not OCR corruption.
- No Google Vision fallback beyond the ordinary local vision/reference files was needed.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.
