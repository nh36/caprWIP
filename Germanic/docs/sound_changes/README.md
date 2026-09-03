# sound_changes — layout

Classification: SOURCE (edit), GENERATED (regenerate, never edit), ARCHIVE
(historical record). See `../README.md` for the full workflow.

## SOURCE

- `registry/sc_registry.tsv` — canonical SC registry (single owner of SC
  identity, lifecycle, executable identifier/position, names, stage, scope,
  confidence, adjudication status/verdict/memo, chronology-node facts).
- `registry/chronology_edges.tsv` — canonical chronology-edge registry.
- `registry/sc_inventory_annotations.tsv` — inventory-view annotations.
- `audits/` — adjudication memos (`ADJUDICATION_TEMPLATE.md` is the template).
- `reader_facing/`, `book_dossiers/`, `literature_dossiers/`, `change_entries/`
  — prose layers.
- `sound_change_aliases.tsv`, `sound_change_literature_matrix.tsv`,
  `sound_change_book_entry_plan.tsv` — auxiliary hand-edited tables (own only
  their unique fields; never restate registry facts as authority).

## GENERATED (by `Germanic/tools/generate_registry_views.py` unless noted)

- `sound_change_historical_staging_map.tsv` — staging view of the registry.
- `sound_change_inventory.tsv` — inventory view (registry + annotations).
- `order_tests/chronology_graph/` — first-break edge/node views (TSV, JSON,
  DOT, summary).
- `registry/settled_verdicts.md` — settled-verdict summary.
- `cascade_baseline/historical_audit_table.tsv`,
  `cascade_baseline/rename_migration_manifest.tsv` — via
  `Germanic/tools/build_historical_audit_table.py` /
  `build_rename_migration_manifest.py` (read the staging view).

## ARCHIVE / RECORD

- `archive/` — retired current-authority files (e.g. the old
  next-batch candidates board).
- `order_sensitivity_*`, `order_tests/` batch reports, chronology cards and
  their index, `sound_change_order_sensitivity.tsv`, `cascade_baseline`
  frozen snapshots and audit reports — records of completed experiments and
  audits. Consult freely; never treat as current metadata authority and never
  update them during an adjudication.
