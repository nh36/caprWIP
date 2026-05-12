# Model entry implementation report — 2298 wolf / wulf

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2298-wolf-wulf.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2298-wolf-wulf.md`
- `Germanic/docs/lexeme_reports/research_memos/2298-wolf-wulf.md`
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
- local reference files for Campbell, Bülbring, Luick, Ringe & Taylor, Sievers-Brunner, Kroonen, and Stiles

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.model_implementation_report.md`

## Citation-key check

Checked against `docs/refs.bib`:

- `Bulbring1902`
- `Campbell1959`
- `Kroonen2013`
- `Luick1914`
- `RingeTaylor2014`
- `SieversBrunner1965`
- `Stiles2012`

## Unresolved points

- The central result remains that the citation-form development to attested
  `wulf` is unexplained.
- The negative control `wulfi / wúlfis -> wylf / wylfe` is important for the
  argument, but it does not supply a regular source for the noun.

## OCR and source-transcription checks

- No suspicious OCR form required correction in the final prose.
- The Brunner wording on `wulfe aus wulfi` was checked in the local OCR and
  retained only as a source-backed negative control.
- No Google Vision spot-check was required beyond the local reference files used
  in the packet and memo.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.

## Citation-locator conditional-source pass

- Added page-specific locators for `Luick1914, 148`.
- This pass was limited to claim-by-claim localization for `Campbell1959`, `BosworthToller1898`, and `Luick1914`.
- `KlugeSeebold2011` remained unchanged because the local text still does not preserve a reliable page marker.
