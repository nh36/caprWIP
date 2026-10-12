# Model entry implementation report — 2095 learn / liornian

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2095-learn-liornian.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md`
- `Germanic/docs/lexeme_reports/research_memos/2095-learn-liornian.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `docs/refs.bib`
- local reference files for Campbell, Ringe & Taylor, Kroonen, Clark Hall, and Bright

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.model_implementation_report.md`

## Notes on this pass

- Kept the entry short because the row is `regular` with a note, not a complex
  analogical rescue case.
- Treated the issue as dialectal selection between Northumbrian `liornian` and
  the better-known West Saxon `leornian`.
- Used a manual `Form comparison`; no automatic paradigm probe was run.

## Revision-pass corrections

- Expanded the development section slightly so the `liornian` / `leornian`
  distinction is tied more explicitly to Campbell's statement that Northumbrian
  preserves `io` where original `eo` and `io` remain distinct.
- Reworded the comparison table so `*líznōjaną -> liornian` is labeled as a
  computed regular output and attested Northumbrian comparison form, rather than
  as an over-broadly “documented” derivation.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`

## Unresolved points

- The dictionary tradition still strongly favors `leornian`; the entry therefore
  needs to keep the Northumbrian selection explicit.
- Some older local analysis files preserve superseded WS-oriented discussion;
  these were treated as background rather than as final authority.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.
