# Model entry implementation report — 2308 youth / ġeoguþ

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2308-youth-ġeoguþ.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2308-youth-ġeoguþ.md`
- `Germanic/docs/lexeme_reports/research_memos/2308-youth-ġeoguþ.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_37_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Kroonen, Ringe & Taylor, Campbell, Fulk, Sievers-Brunner, and Luick

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model_implementation_report.md`

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `Fulk2018`
- `Kroonen2013`
- `Luick1914`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The entry still depends on keeping the earlier `*ju(w)unþi-` headword distinct
  from the later g-bearing comparative label used in the row header.
- Later promotion should preserve the Brunner/Luick stem-`u` harmony account and
  not collapse it into the older provisional heuristic.

## OCR and source-transcription checks

- The relevant passages in the local OCR files were stable enough for use.
- No source-transcription corruption needed correction in the final prose.
- Google Vision was not required for a corrective rewrite, though Vision-backed
  files are available for Brunner and Fulk.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `Luick1914, 397`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.

Citation locator claim-isolation 01 split the staging sentence and added a verified locator for `RingeTaylor2014, 141`.

Citation locator claim-isolation 02 tightened the remaining broad claims and added verified locators for `RingeTaylor2014, 141`, `Campbell1959, §374`, and `SieversBrunner1965, §150.3`.
