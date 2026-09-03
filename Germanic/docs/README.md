# Germanic pipeline — navigation

Read this first. Every file relevant to current work is SOURCE (hand-edited),
GENERATED (never hand-edited), or ARCHIVE (historical; never authoritative).

## What you may edit (SOURCE)

- `sound_changes/registry/sc_registry.tsv` — **the canonical SC registry.**
  One row per SC ever used (including retired). Owns identity, lifecycle,
  executable identifier/position, display names, historical stage/scope,
  confidence, adjudication status/verdict/memo path, chronology-node facts.
- `sound_changes/registry/chronology_edges.tsv` — **the canonical
  chronology-edge registry.** Owns all chronology relations, witnesses,
  witness roles, and evidence basis.
- `sound_changes/registry/sc_inventory_annotations.tsv` — inventory-view
  annotations (trace/rule-source/literature fields) not owned by the registry.
- `sound_changes/audits/scNNN-adjudication.md` — per-SC adjudication memos
  (copy `sound_changes/audits/ADJUDICATION_TEMPLATE.md`).
- `../fsts/germanic.txt` — the FST cascade (only as an adjudication verdict
  requires).
- Reader-facing chapters, dossiers, and `CURRENT_STATE.md`.

## What is GENERATED (do not edit; regenerate)

Run `python3 Germanic/tools/generate_registry_views.py` after editing any
registry file. It writes: `sound_changes/sound_change_historical_staging_map.tsv`,
`sound_changes/sound_change_inventory.tsv`, the chronology graph files under
`sound_changes/order_tests/chronology_graph/` (edges TSV/JSON/DOT, nodes,
summary), and `sound_changes/registry/settled_verdicts.md`.
Then run `python3 Germanic/tools/build_historical_audit_table.py` and
`python3 Germanic/tools/build_rename_migration_manifest.py` if the staging
view changed. `--check` on the generator verifies everything is clean.

## What is ARCHIVE (never authoritative)

`archive/` (old project states, DEV_NOTES research log, old workflow/plans),
`sound_changes/archive/`, batch reports, frozen baselines' historical
snapshots, and the chronology-card programme records. See `archive/README.md`.

## One SC adjudication, start to finish

1. `python3 Germanic/tools/adjudicate.py SCNNN --prepare` — assembles the
   packet (registry row, rule text, edges, memo path, fingerprints, census
   command).
2. Follow `RESEARCH_ADJUDICATION_PROTOCOL.md`; record everything in the memo.
3. Propagate the verdict by editing the registry files (and FST/corpus only
   if the verdict requires), then regenerate views (command above).
4. `python3 Germanic/tools/adjudicate.py SCNNN --check` — validates
   propagation consistency.
5. `cd Germanic/tests && python3 -m pytest -q` — full suite must pass.
6. Commit and push; STOP after one SC.

Current phase and frozen baselines: `CURRENT_STATE.md`.
