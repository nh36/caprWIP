# Model entry implementation report — 1975 calf / ċealf

## Files inspected

- `Germanic/docs/lexeme_reports/dev_notes_slices/1975-calf-ċealf.md`
- `Germanic/docs/lexeme_reports/packets/1975-calf-ċealf.md`
- `Germanic/docs/lexeme_reports/research_memos/1975-calf-ċealf.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_06_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Kroonen, Orel, Ringe & Taylor, Campbell, Fulk, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model_implementation_report.md`

## Notes on this pass

- Kept the entry compact because the row is regular and the note chiefly concerns normalized `ċ-` spelling.
- Centered the prose on the singular citation form while briefly preserving the inherited `-r-` plural background.
- Omitted a paradigm comparison because the row does not hinge on a disputed paradigm cell.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `Fulk2018`
- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The only standing review-sensitive point is representational: dictionary sources usually print `cealf`, whereas the entry makes the palatalized onset explicit as `ċealf`.

## OCR and source-transcription checks

- The local dictionary and grammar passages used here were legible in the available files.
- The bad `old_english_wiktionary.tsv` value for calf was treated as unusable metadata and excluded from final prose.
- No Google Vision fallback beyond the existing local vision-backed transcriptions was needed.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Fulk2018, 193`; `Orel2003, 248`; `RingeTaylor2014, 220`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.

## Citation-locator conditional-source pass

- Added page-specific locators for `BosworthToller1898, 131`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.
