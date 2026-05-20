# Sound-change inventory post-removal audit 03 report

## Summary

- Active sandbox stage count after removal: **94**.
- Late `OEPrefixAReduction` is absent from active FST/sandbox/tooling: **yes**.
- The former late prefix-a-reduction row is removed from the active inventory rather than retained as a deprecated active row.
- Active order is continuous: **yes** (`current_order` now runs from 1 to 94).
- Stable change IDs were preserved: **yes** (`SC078` and later IDs remain stable while `current_order` was recomputed).
- Historical sound changes: **84**.
- Support stages: **2**.
- Orthography/surface stages: **5**.
- Duplicate applications: **0**.
- Technical markers: **3**.
- Uncertain rows: **0**.
- Main book entries: **84**.
- Appendix entries: **8**.

## Relationship to earlier reports

- `sound_change_inventory_audit_02_report.md` described the pre-removal **95-stage** scaffold state and the original duplicate classification of the former late prefix-a-reduction row.
- `prefix_a_reduction_duplicate_audit_01_report.md` supplied the computational evidence that the late `OEPrefixAReduction` application was redundant and could be removed safely.
- This report supersedes the inventory counts and duplicate-stage status from audit 02 while preserving both earlier reports as historical decision records.

## Order policy

- **Policy A adopted.** `change_id` remains a stable identifier and may therefore have gaps in its numeric suffixes.
- `current_order` now records the live active stack order continuously from `1` to `94`.
- Consequence: stable IDs after the removed stage keep their names (for example `SC078`), but their `current_order` shifts to the live position (`77`).

## Inventory updates

- `sound_change_inventory.tsv`: recomputed `current_order` continuously, kept only one active prefix-a-reduction row (`SC035`), and updated the SC035 note to reflect duplicate audit 01.
- `sound_change_book_entry_plan.tsv`: recomputed `current_order_or_orders` from the active inventory so downstream order references are no longer misleading after the removed stage.
- `sound_change_aliases.tsv`: confirmed that active `SC077` aliases are gone and annotated the canonical SC035 sandbox alias as the active early checkpoint only.
- `sound_change_order_sensitivity.tsv`: confirmed no deleted late-stage row remains and synchronized `current_order` to the same live-order policy.

## Prefix-a-reduction state

- One canonical reader-facing prefix-a-reduction entry remains: **SC035**.
- No active late duplicate remains in the FST, sandbox, stage list, or active inventory.
- Remaining references to the removed late prefix-a-reduction stage are documentation only in the earlier historical reports.

## Remaining human-review items

| change_id | display_name | historical_stage | pipeline_stage | review_note |
| --- | --- | --- | --- | --- |
| SC005 | NWGmc A To U Before M | Northwest Germanic | Proto-West Germanic developments | NWGmc-labeled rule remains inside the PWGmcChanges pipeline bundle; preserve bundle order but flag the historical label split. |
| SC016 | OE Ws Palatal Glide | Old English | Northwest Germanic developments | The rule is labeled OE/West Saxon but is checkpointed before the main Old English section break in the sandbox. |
| SC020 | PGmc Final Z Deletion | Proto-Germanic | Northwest Germanic developments | The cascade applies this PGmc-labeled rule in the NWGmc section; keep pipeline order but flag the earlier historical label. |
| SC041 | PWGmc Final Bare A Loss | Proto-West Germanic | Old English | PWGmc-labeled loss is implemented late in the OE pipeline; dossier work should explain the historical vs computational placement. |
| SC042 | PWGmc Surviving Bimoric O Unrounding | Proto-West Germanic | Old English | PWGmc-labeled unrounding is implemented late in the OE pipeline; keep the sandbox order but flag the chronology mismatch. |
| SC043 | Anglo Frisian Brightening | Old English | Old English | The current taxonomy has no separate Anglo-Frisian bucket, so this rule is provisionally filed under Old English for book planning. |
| SC049 | PGmc B Allophony | Proto-Germanic | Old English | PGmc B Allophony is intentionally delayed in the live cascade, so the historical label and pipeline placement diverge. |
| SC050 | Sievers Law Syncope | Proto-West Germanic | Old English | Sievers Law Syncope is provisionally grouped with Proto-West Germanic developments even though the sandbox checkpoints it in the Old English section. |
| SC064 | NWGmc In Stem N Loss | Northwest Germanic | Old English | NWGmc In Stem N Loss is applied after OEHighVowelApocope in the current cascade, so the historical label needs an explanatory note. |

## Recommended next task

**A. Build first literature dossier pilot.**

The scaffold is now synchronized to the active 94-stage stack, so the next step should be one pilot literature dossier (preferably `SC043` or `SC063`) rather than more inventory bookkeeping.
