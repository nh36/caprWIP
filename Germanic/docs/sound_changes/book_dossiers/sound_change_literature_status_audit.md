# Sound-change literature status audit

## Summary

This audit reconciles the per-change book-dossier inventory against the current
sound-change register and the actual files present in `literature_dossiers/` and
`book_dossiers/`.

The scaffold-free state of the sound-change half remains intact throughout this
audit:

1. 70 ordinary sound changes represented.
2. 70 covered by pilot/full production reports.
3. 0 scaffold placeholders.

## What changed

Before this audit, the inventory counted **64** changes with
`literature_status = not_found`.

This pass updated **62** inventory rows where a real existing
`literature_dossiers/` file already covered the change either directly or through
an exact unit/range dossier.

After the audit, the inventory now breaks down as:

| Status | Count | Meaning |
| --- | ---: | --- |
| `substantial` | 30 | Dedicated single-rule or exact-unit literature dossier coverage, plus the already-established substantial rows. |
| `partial` | 38 | Coverage through broader corridor, bridge, review, or cluster dossiers. |
| `not_found` | 2 | No actual literature-dossier file currently covers the change. |

## Coverage categories

Using actual file coverage rather than the raw inventory values, the 70 ordinary
changes currently fall into three practical categories:

1. **30 changes with dedicated literature-dossier coverage** — either a
   single-rule dossier or an exact unit dossier already exists.
2. **38 changes with broader range/review/cluster literature-dossier coverage** —
   these are supported by existing corridor, bridge, regional, or cluster
   dossiers rather than by a narrowly named single-change dossier.
3. **2 genuinely uncovered changes** — `SC057` and `SC058` still have no actual
   `literature_dossiers/` file covering them.

No `book_dossier_only` cases needed to be introduced in this pass: every safe
inventory correction was justified by an actual `literature_dossiers/` file, not
merely by a production report or a book dossier.

## Rows left untouched

The following cases remain intentionally `not_found`:

1. **`SC057`** — the current full note cites source literature, but there is no
   actual literature-dossier file covering the rule yet.
2. **`SC058`** — likewise represented in final prose, but still lacks a real
   literature-dossier file.

These are the only genuinely uncovered ordinary changes in the current
inventory.

This pass does **not** globally normalize every auxiliary inventory field. In
particular, `has_direct_quotations` and `quotation_source_files` were left alone
unless already correct, because validating quotation-level metadata would require
row-by-row dossier inspection beyond the scope of this safe audit.

## Recommended next dossier work

If further dossier work is wanted, the most useful next steps are:

1. **Create explicit literature-dossier coverage for `SC057` and `SC058`** so
   the inventory can reach zero `not_found` rows.
2. **Optionally backfill narrower single-change dossiers** for rows currently
   covered only by broader range/review dossiers, especially where later QC wants
   more granular source traceability. This is an enhancement task, not a blocker
   for the current scaffold-free assembled half.

## Result

The `needs_literature` count in generated coverage should now reflect actual
missing dossier coverage much more honestly. If it does not drop to **2**, the
remaining discrepancy should be treated as a bug in the reporting pipeline
rather than as a real absence of dossier files.

## Follow-up: SC057 and SC058 dossier completion

Explicit literature-dossier coverage has now been added for the two remaining
ordinary-change gaps:

1. `SC057` — `Germanic/docs/sound_changes/literature_dossiers/057-oe-j-cluster-coalescence.dossier.md`
2. `SC058` — `Germanic/docs/sound_changes/literature_dossiers/058-oe-nasal-dissimilation-residual.dossier.md`

The inventory therefore now has **zero** `not_found` rows for ordinary
sound-change literature coverage.

This does **not** make SC058 a strong source-backed chapter. Its new dossier is
deliberately residual and documents thin, scattered source support plus the
current chronology-negative card state. Any future work here is optional
refinement rather than required coverage repair.

## Follow-up: readiness and quotation metadata normalization

After the SC057/SC058 dossier files closed the last `not_found` gaps, this pass
normalized the inventory's downstream readiness and quotation metadata so it no
longer says that a literature dossier is still missing where a real dossier file
 already exists.

In particular:

1. `SC057` and `SC058` now record verified quotation-source witness files in the
   inventory.
2. Rows with actual literature coverage no longer keep the stale
   `book_section_readiness = needs_literature_dossier` state.
3. Rows with `partial` dossier coverage may still carry future-work items such as
   direct quotations, representative examples, or human chronology framing, but
   those are now refinement needs rather than missing-dossier coverage.
4. Boundary-limited residual rules such as `SC058` remain deliberately modest in
   readiness and drafting priority.

## Final reproducibility audit

Final verification reran:

1. `python3 Germanic/docs/assembly/build_sound_change_volume.py`
2. `bash Germanic/docs/assembly/build_sound_change_volume.sh`

The assembled half remains scaffold-free and literature-complete:

1. no scaffold placeholders remain in the active assembled outputs;
2. no ordinary-change literature gaps remain;
3. inventory consistency checks passed;
4. listed literature-dossier and quotation-witness paths all exist.

This pass made one narrow reproducibility fix: it regenerated the tracked
`sound_change_volume_alpha_01.tex` file so the LaTeX artifact now matches the
current scaffold-free Markdown build instead of an older scaffold-era state.
