# Germanic control plane — SOURCE / GENERATED / ARCHIVE map

Classification of every file that encodes machine-relevant sound-change
state. Rule: for each fact there is exactly one editable SOURCE; everything
else is GENERATED from it or ARCHIVE. Never hand-edit a GENERATED file;
never treat an ARCHIVE file as current authority.

## SOURCE (hand-edited, authoritative)

| File | Owns |
|---|---|
| `registry/sc_registry.tsv` | SC identity, lifecycle status, executable identifier, cascade position, display names, historical stage/scope, confidence, reader-facing placement, adjudication status/verdict, memo path |
| `registry/chronology_edges.tsv` | Chronology relations: relation type, evidence basis (stage-entailed vs independently demonstrated), witnesses, witness roles |
| `registry/sc_inventory_annotations.tsv` | Inventory-only annotation columns (evidence pointers, notes) not otherwise owned by the registry |
| `Germanic/fsts/germanic.txt` | Executable rule semantics and cascade composition |
| `audits/*.md` adjudication memos | Per-SC scientific reasoning; each carries a machine-readable `Registry-verdict:` line that must agree with the registry |
| `cascade_baseline/cascade_baseline_summary.json` | Frozen fingerprints (change only via the explicit adjudication/refreeze procedure) |
| `Germanic/docs/CURRENT_STATE.md` | Current phase, next SC, standard commands |
| `Germanic/docs/README.md`, `sound_changes/README.md` | Navigation |
| `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md`, `audits/ADJUDICATION_TEMPLATE.md` | Method |

## GENERATED (never hand-edit; rebuild with `python3 Germanic/tools/generate_registry_views.py`)

| File | Source |
|---|---|
| `sound_change_historical_staging_map.tsv` | sc_registry |
| `sound_change_inventory.tsv` | sc_registry + annotations |
| `order_tests/chronology_graph/first_break_edges.{tsv,json,dot}` | chronology_edges (+ registry for node metadata) |
| `order_tests/chronology_graph/first_break_nodes.tsv` | sc_registry |
| `order_tests/chronology_graph/first_break_graph_summary.md` | both registries |
| `registry/settled_verdicts.md` | sc_registry |

Chained generators (run after registry views if staging/inventory changed):

| File | Generator |
|---|---|
| `cascade_baseline/historical_audit_table.tsv` | `tools/build_historical_audit_table.py` |
| `cascade_baseline/rename_migration_manifest.tsv` | `tools/build_rename_migration_manifest.py` |

## ARCHIVE / RECORD (historical; never current authority)

- `Germanic/docs/archive/` — DEV_NOTES.md, WORKFLOW.md, CANONICAL_STATE.md, HISTORICAL_CHRONOLOGY_AUDIT_PLAN.md, canonical_state_freeze_report.md (tombstones remain at old paths)
- `sound_changes/archive/next_batch_candidates.tsv` — retired candidate board; the registry owns lifecycle/candidate status
- `order_tests/chronology_cards/*.md` and `chronology_cards/chronology_graph_nodes.tsv` — per-SC evidence records from past audits; cite but do not treat their metadata as current
- `chronology_card_index.tsv` — record of the card set (read by the book pipeline; id set only)

## Standard workflow for one SC adjudication

1. `python3 Germanic/tools/adjudicate.py SCNNN --prepare`
2. Investigate per `RESEARCH_ADJUDICATION_PROTOCOL.md`; write the memo from `audits/ADJUDICATION_TEMPLATE.md` including a `Registry-verdict:` line.
3. Edit the SOURCE files only: `sc_registry.tsv`, `chronology_edges.tsv`, memo, and `germanic.txt` if the verdict requires.
4. `python3 Germanic/tools/generate_registry_views.py` then the chained builders if staging/inventory changed.
5. `python3 Germanic/tools/adjudicate.py SCNNN --check`
6. `cd Germanic/tests && python3 -m pytest -q`

## Known remaining duplications (accepted, machine-checked where possible)

- `tools/build_historical_audit_table.py` internally hard-codes the SC021 archival prose block; consistency with the registry is covered by tests rather than eliminated.
- `book_dossiers/sound_change_book_dossier_inventory.tsv` and book-entry planning files repeat display names/stages for the publication pipeline; the registry is authoritative and divergence would be a bug.
- Archived audit layers preserve legacy stage-label vocabulary (e.g. wgmc/ingvaeonic vs eaf/pwgmc) as historical record; do not normalize.
