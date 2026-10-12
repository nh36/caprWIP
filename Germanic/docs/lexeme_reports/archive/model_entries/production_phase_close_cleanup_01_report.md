# Production phase-close cleanup pass 01 report

## Files inspected

- `Germanic/docs/lexeme_reports/model_entries/production_phase_close_audit.md`
- The 25 audit-listed `.model.md` files:
  - `1962-bow-bēag.model.md`
  - `1968-breast-brēost.model.md`
  - `1980-cow-cȳ.model.md`
  - `1990-dill-dile.model.md`
  - `2004-fast-festan.model.md`
  - `2009-field-feld.model.md`
  - `2011-find-fundene.model.md`
  - `2016-flask-flasce.model.md`
  - `2027-follow-fylġan.model.md`
  - `2030-fowl-fugol.model.md`
  - `2034-fright-fyrhte.model.md`
  - `2037-gall-ġealla.model.md`
  - `2152-rest-ræste.model.md`
  - `2181-shilling-sċilling.model.md`
  - `2202-span-spannan.model.md`
  - `2217-still-stillan.model.md`
  - `2230-summer-sumer.model.md`
  - `2232-sunder-sundrian.model.md`
  - `2234-swallow-swealwe.model.md`
  - `2278-weapon-wǣpn.model.md`
  - `2293-will-willa.model.md`
  - `2294-wind-windan.model.md`
  - `2296-withy-wīþiġ.model.md`
  - `2297-wold-weald.model.md`
  - `2305-yarn-ġearn.model.md`
- The matching `.reviewer_checklist.md` and `.model_implementation_report.md`
  files for those 25 entries
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model_implementation_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_10_report.md`
- `Germanic/docs/lexeme_reports/packets/2120-march-mearc.md`
- `Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2120-marrow-mearg.md`

## Files changed

- 25 model entries: the audit-listed `.model.md` files named above
- 25 paired reviewer checklists for those changed model entries
- 25 paired implementation reports for those changed model entries
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2120-march-mearc.production_exception.md`
- `Germanic/docs/lexeme_reports/model_entries/production_phase_close_audit.md`
- `Germanic/docs/lexeme_reports/model_entries/production_phase_close_cleanup_01_report.md`

## Phrase hits removed or recast

The cleanup pass removed or recast the flagged formulaic phrasing in the final
prose of all 25 audit-listed model entries.

Main recast types:

- `the decisive point` -> `the relevant point`
- `the decisive comparison` -> `the relevant comparison form`
- `the row` / `the row therefore` / `the row's` -> source-facing wording such as
  `the selected input`, `the selected target`, `this entry`, or
  `the source tradition used here`

Representative examples:

- `1962 bow / bēag` — recast the singular-preterite sentence as a
  source-facing comparison form.
- `2009 field / feld` — recast the sentence about `*félθuz` as comparative
  background rather than row-facing explanation.
- `2030 fowl / fugol` — removed the project-facing `row` wording from the
  stem-class statement.
- `2234 swallow / swealwe` — recast both bird-versus-verb separation sentences
  away from `the row` phrasing.
- `2297 wold / weald` — recast the target sentence so it now names the selected
  form directly.

## Entries left unchanged and why

- **None of the 25 audit-listed model entries were left unchanged.**
- Every listed hit was recast in place.

## QA-file updates

For each changed model entry:

- the paired `.reviewer_checklist.md` now records that post-audit cleanup pass
  01 recast the flagged formulaic final-prose wording without changing the
  analysis;
- the paired `.model_implementation_report.md` now records the same phrase-level
  cleanup in its process notes.

## Legacy package issue: 2183 shoulder / sċuldrum

- `2183-shoulder-sċuldrum.reviewer_checklist.md` was created.
- It is explicitly a **retrospective checklist** for a pre-existing current
  model entry.
- The shoulder entry itself was **not** rewritten in this cleanup pass.
- This closes the package-completeness issue noted in
  `production_phase_close_audit.md`.

## 2120 march / mearc exception

- `2120-march-mearc.production_exception.md` was created.
- The note records the batch-10 skip reason: the backlog source path pointed to
  `dev_notes_slices/2120-marrow-mearg.md` rather than a clean row-local march
  file.
- The note also records that the packet and research memo for
  `2120-march-mearc` are identifiable now, while the dev-note slice remains
  filename-misleading and should be reviewed before any drafting task.
- No model entry was created for `2120` in this pass.

## Optional model-entry index

- `production_model_entry_index.tsv` was **intentionally skipped** in this pass.
- Reason: this cleanup pass was kept tightly scoped to prose hygiene and the two
  carried-forward exceptions, and a reliable corpus-wide index would require a
  broader inventory task than this pass needed.

## Remaining phrase hits needing human review

- After the cleanup pass, a direct rescan of the 25 audit-listed `.model.md`
  files found **no remaining hits** for the flagged phrases
  `the decisive point`, `the decisive comparison`, or `the row` / `row's`.
- Broader corpus-level phrase scanning outside this 25-file scope was not part
  of this pass.

## Analysis preservation

- No substantive analysis was changed.
- No citations, selected inputs, target forms, derivation-class labels, or
  comparison tables were changed beyond tiny wording adjustments needed to keep
  the recast sentences grammatical.

## Scope confirmation

- No source data, FST files, `report_manifest.tsv`, pilot reports, packets,
  dev-note slices, research memos, bibliography files, derivation traces,
  writing-skill files, or model entries outside the 25 listed cleanup set were
  changed.
