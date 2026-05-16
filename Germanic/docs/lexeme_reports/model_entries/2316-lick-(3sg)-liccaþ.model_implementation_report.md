# Model entry implementation report — 2316 lick (3sg) / liccaþ

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2316-lick-(3sg)-liccaþ.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2316-lick-(3sg)-liccaþ.md`
- `Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md`
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
- local reference files for Bosworth-Toller, Campbell, Brunner, Orel, and Ringe & Taylor

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.model_implementation_report.md`

## Notes on this pass

- Kept the distinction explicit among row-level `PROTO *likkōną`, lexeme-level `*líkkōjaną`, and selected cell input `*líkkōθi`.
- Treated `liccaþ` as a selected 3sg paradigm form beside lemma `liccian`, not as a separate headword.
- Verified the paradigm comparison with a manual `oe_paradigm_probe.py` run: `*líkkōjaną -> liccian`, `*líkkô -> licca`, `*líkkōθi -> liccaþ`, `*líkkōsi -> +?`.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `Orel2003`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The live row metadata still pairs `PROTO *likkōną` with lexeme-level comparative evidence for `*líkkōjaną`.
- No stronger local dossier for bare 3sg `liccaþ` turned up beyond the lemma evidence and finite-cell comparison.
- A reusable built-in paradigm probe for the lick-family finite cells is still absent.

## OCR and source-transcription checks

- No suspicious OCR form required correction in the final prose.
- The Bosworth-Toller, Campbell, Brunner, Orel, and Ringe-Taylor passages used here were legible in the local files.
- No Google Vision fallback was needed beyond the ordinary local reference texts.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator master manifest 04

- Tightened `Orel2003` from a broad citation to verified page locator `285` after direct inspection of the local Orel text.

Citation locator claim-isolation 01 split the finite-cell sentence and added verified locators for `Campbell1959, §356.4` and `RingeTaylor2014, 80`.

Citation locator claim-isolation 02 tightened the remaining broad claims and added verified locators for `Campbell1959, §398.1, §356.4`, `SieversBrunner1965, §45 Anm. 3`, and `RingeTaylor2014, 80`.
