# Model entry implementation report — 2030 fowl / fugol

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2030-fowl-fugol.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2030-fowl-fugol.md`
- `Germanic/docs/lexeme_reports/research_memos/2030-fowl-fugol.md`
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
- local reference files for Campbell, Luick, Ringe-Taylor, Kroonen, Orel, Bosworth-Toller, and Clark Hall

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2030-fowl-fugol.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2030-fowl-fugol.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2030-fowl-fugol.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2030-fowl-fugol.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `unexplained_unmodelled` lexical exception.
- Kept the regular computed output `fogol` distinct from attested `fugol`.
- Did not introduce any paradigm-cell or analogical rescue argument unsupported
  by the source material.

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the model entry without changing the analysis, citations, selected input,
  target form, classification, or comparison tables.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `Kroonen2013`
- `Luick1914`
- `Orel2003`
- `RingeTaylor2014`

## Unresolved points

- The core unresolved point is the unexplained retention of root `u`.
- This entry should remain a cautionary model for how to document an exception,
  not for how to regularize one.

## Citation-locator pilot 01

- Added page-specific Pandoc locators to the paired model entry for
  `[@Kroonen2013, 197]`, `[@Orel2003, 155]`, and `[@ClarkHall1960, 138]`.
- Left `RingeTaylor2014`, `Campbell1959`, `BosworthToller1898`, and `Luick1914`
  broad in this pilot because the exact page-to-claim mapping was not recovered
  with enough confidence from the local files.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.
