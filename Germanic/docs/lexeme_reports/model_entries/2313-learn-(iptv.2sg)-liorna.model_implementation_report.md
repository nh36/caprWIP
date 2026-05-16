# Model entry implementation report — 2313 learn (iptv.2sg) / liorna

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2313-learn-iptv-2sg-liorna.md`
- `Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_12_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2258-timber-timber.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2309-make-(iptv.2sg)-maca.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Kroonen, Ringe & Taylor, Fulk, Campbell, Clark Hall, Brunner, Kilday, and Bright

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.model_implementation_report.md`

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `Fulk2018`
- `Kroonen2013`
- `RingeTaylor2014`
- `SieversBrunner1965`

## Unresolved points

- The ordinary dictionary headword remains `leornian`, so the Northumbrian imperative `liorna` must stay clearly distinguished from the headword tradition.
- The learn-family row cluster still lacks a saved built-in probe, even though the current manual comparison is stable.

## OCR and source-transcription checks

- Brunner's plain-text OCR is noisy around some finite learn-family forms, so the relevant passages were cross-checked in `brunner_1965_altenglische_grammatik.vision.txt`.
- No corrupt Brunner form was reproduced in the final prose.
- The Campbell, Ringe-Taylor, Kroonen, Fulk, and Clark Hall passages used here were legible in local text or vision files.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Kroonen2013, 380`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.

Citation locator claim-isolation 02 tightened the remaining broad claims and added verified locators for `RingeTaylor2014, 38, 247` and `SieversBrunner1965, §417 Anm. 10`.
