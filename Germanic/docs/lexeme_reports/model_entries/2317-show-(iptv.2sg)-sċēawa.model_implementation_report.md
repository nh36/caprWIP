# Model entry implementation report — 2317 show (iptv.2sg) / sċēawa

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2317-show-(iptv.2sg)-sċēawa.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2317-show-(iptv.2sg)-sċēawa.md`
- `Germanic/docs/lexeme_reports/research_memos/2317-show-(iptv.2sg)-sċēawa.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_13_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2309-make-(iptv.2sg)-maca.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Bright, Campbell, Orel, and Ringe & Taylor

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model_implementation_report.md`

## Notes on this pass

- Kept the distinction explicit among row-level `PROTO *skawōną`, lexeme-level `*skáwōjaną`, and selected cell input `*skáwô`.
- Treated `sċēawa` as a selected imperative paradigm form beside headword `scēawian`, while preserving source spelling `scēawa` in the prose.
- Verified the paradigm comparison with a manual `oe_paradigm_probe.py` run: `*skáwōjaną -> sċēawian`, `*skáwô -> sċēawa`, `*skáwōθi -> sċēawaþ`.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `Campbell1959`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The live row metadata still pairs `PROTO *skawōną` with lexeme-level comparative evidence for `*skáwōjaną`.
- The entry depends on keeping attested source spelling `scēawa` distinct from normalized `sċēawa`.
- A reusable built-in paradigm probe for the show-family finite cells is still absent.

## OCR and source-transcription checks

- Bright's local Vision text was used directly for `scēawian ... imp. 2 sg. scēawa` and showed no suspicious corruption.
- No additional OCR repair or alternative transcription was needed in the final prose.
- The comparative and grammatical reference passages used here were legible in the local files.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator master manifest 04

- Tightened `Orel2003` from a broad citation to verified page locator `337` after direct inspection of the local Orel text.

Citation locator claim-isolation 02 tightened the remaining broad claims and added verified locators for `RingeTaylor2014, 314` and `Campbell1959, §120`.

## Citation-locator claim-isolation 04

- Citation locator tightened after claim-isolation pass; verified against `BrightCassidyRingler1971, 346`.
