# Model entry implementation report — 2087 knob / cnobba

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2087-knob-cnobba.md`
- `Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md`
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
- local reference files for Kroonen, Bosworth-Toller, Clark Hall, and the local knob note

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model_implementation_report.md`

## Notes on this pass

- Drafted the row as a `reconstructed_oe` case and stated the reconstructed
  status explicitly in the final prose.
- Kept attested `cnopp / cnoppa` in view as the principal control form, but did
  not rewrite row policy in this pass.
- Used a manual `Reconstruction status` section; no automatic paradigm or class
  probe was run.

## Revision-pass corrections

- Corrected the Old English development statement so that Proto-Germanic `kn-`
  is described as corresponding to OE `cn-`, rather than as losing the initial
  velar.
- Sharpened the prose to state that `cnobba` is reconstructed, not directly
  attested, and that the choice of `cnobba` over attested `cnoppa` is a
  modeling/comparative decision rather than settled OE philology.
- Updated the checklist wording so the entry no longer passes without caveat:
  the comparator decision remains the main human-review issue in the batch.

## Citation-key check

Checked against `docs/refs.bib`:

- `BosworthToller1898`
- `ClarkHall1960`
- `Kroonen2011`

## Unresolved points

- The main unresolved issue is row policy rather than prose quality: whether the
  better attested OE comparator `cnoppa` should outweigh the currently selected
  reconstructed form `cnobba` in a later review.
- The local expert note supports the voiced-branch analysis but was not relied
  on in the final prose except as background.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, writing-skill file, or existing model entry was
  changed.

## Citation-locator claim-isolation 07

- Citation locator tightened or status reclassified after claim-isolation 07;
  verified against `ClarkHall1960, 79`.

## PDF review 01

- PDF review 01: corrected rendered prose/formatting issue.
