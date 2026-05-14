# Model entry implementation report — 2027 follow / fylġan

## Files inspected

- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `Germanic/docs/lexeme_reports/packets/2027-follow-fylġan.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2027-follow-fylġan.md`
- `Germanic/docs/lexeme_reports/research_memos/2027-follow-fylġan.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/DEV_NOTES.md`
- `docs/refs.bib`
- local reference files under `docs/references/` for Kroonen, Ringe & Taylor,
  Bright, Clark Hall, and Bosworth-Toller

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model_implementation_report.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.reviewer_checklist.md`

## What this pass did

- created a source ledger before drafting the prose entry;
- created one book-style model entry for `2027 follow / fylġan`;
- created a reviewer-checklist result for the new draft;
- kept the accepted shoulder and cow models unchanged;
- kept the writing-skill files unchanged.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Citation keys used in the follow model entry were checked against `docs/refs.bib`:

- `BosworthToller1898`
- `BrightCassidyRingler1971`
- `ClarkHall1960`
- `Kroonen2013`
- `RingeTaylor2014`

## Class-comparison status

- No automatic paradigm or class probe was run in this pass.
- The `Class comparison` section in the model entry is **manual**.
- The manual comparison relies on Kroonen's `*fulgen-` / `*fulgjan-` distinction,
  Ringe and Taylor's `*fulgija- ~ *fulgai- > OE fylgan ~ folgian`, the local
  trace `*fúlgijaną -> fylġan`, and the dictionary evidence summarized in the
  source ledger.

## Unresolved uncertainties

- The strongest sources confirm the class split and the coexistence of `fylgan`
  and `folgian`, but they do not all label the class-I form with the same
  dialect terminology. The drafted entry therefore avoids making a narrow dialect
  claim stronger than the sources require.
- The normalized spelling `fylġan` is a project normalization of the class-I
  `fylgan / fylgean` forms preserved in the sources.
- The compact trace documents the selected class-I path directly; the class-II
  mismatch `*fulgēną -> folgon` comes from the checked local analysis rather than
  from the compact trace itself.

Citation locator tightened for BrightCassidyRingler1971 from broad citation to verified page locator.

## Scope confirmation

- No TSV files were changed.
- No FST files were changed.
- `report_manifest.tsv` was not changed.
- No packets, dev-note slices, research memos, bibliography files, derivation
  traces, existing pilot reports, the shoulder model, the cow model, or
  writing-skill files were changed.
