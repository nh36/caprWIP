# Model entry implementation report — 1958 both / bū

## Files inspected

- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `Germanic/docs/lexeme_reports/packets/1958-both-bū.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/1958-both-bū.md`
- `Germanic/docs/lexeme_reports/research_memos/1958-both-bū.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/DEV_NOTES.md`
- `docs/refs.bib`
- local reference files under `docs/references/` for Brunner, Campbell, Fulk,
  Kroonen, and Orel

## Files created

- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model_implementation_report.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.reviewer_checklist.md`

## What this pass did

- created a source ledger before drafting the prose entry;
- created one compact book-style model entry for `1958 both / bū`;
- created a reviewer-checklist result for the new draft;
- kept the accepted shoulder, cow, and follow models unchanged;
- kept the writing-skill files unchanged.

## Citation-key check

Citation keys used in the both model entry were checked against `docs/refs.bib`:

- `Campbell1959`
- `Fulk2018`
- `Kroonen2013`
- `Orel2003`
- `SieversBrunner1965`

## Form-comparison status

- No automatic paradigm or form probe was run in this pass.
- The `Form comparison` section in the model entry is **manual**.
- The manual comparison relies on the dual-paradigm evidence in Brunner,
  Campbell, and Fulk; Kroonen's inherited bare paradigm; Orel's older
  `*bō-jenō` route for `bēġen`; and the compact trace `*bō -> bū`.

## Unresolved uncertainties

- The historical analysis of `bēġen` remains disputed: older `*bō-jen-`
  explanations survive in Brunner, Orel, and Fulk, while Kroonen treats `bēġen`
  as analogical and Fulk reports Seebold's `*bō-þ-` objection.
- Campbell's OCR line for the final accented `ō` examples prints `bā`, while the
  local notes, Brunner, and Fulk support `bū` as the intended neuter example.
- The live TSV note still contains stale pre-fix mismatch wording, but this pass
  did not edit the TSV.

## Scope confirmation

- No TSV files were changed.
- No FST files were changed.
- `report_manifest.tsv` was not changed.
- No packets, dev-note slices, research memos, bibliography files, derivation
  traces, existing pilot reports, the shoulder model, the cow model, the follow
  model, or writing-skill files were changed.
