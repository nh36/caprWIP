# Germanic pipeline — navigation

Read this first. Every file relevant to current work is SOURCE (hand-edited),
GENERATED (never hand-edited), or ARCHIVE (historical; never authoritative).

## What you may edit (SOURCE)

SOURCE files come in three kinds; all are hand-edited, everything else is
generated or archived.

**Machine-state SOURCE** (structured facts; one owner per fact):

- `sound_changes/registry/sc_registry.tsv` — **the canonical SC registry.**
  One row per SC ever used (including retired). Owns identity, lifecycle,
  executable identifier/position, display names, historical stage/scope,
  confidence, adjudication status/verdict/memo path, chronology-node facts,
  and document pointers (evidence dossiers, chronology card, reader-facing
  chapter).
- `sound_changes/registry/chronology_edges.tsv` — **the canonical
  chronology-edge registry.** Owns all chronology relations, witnesses,
  witness roles, and evidence basis.
- `sound_changes/registry/sc_inventory_annotations.tsv` — inventory-view
  annotations (trace/rule-source/literature fields) not owned by the registry.
- `../fsts/germanic.txt` — the FST cascade (only as an adjudication verdict
  requires).

**Scientific-reasoning SOURCE** (prose arguments and evidence):

- `sound_changes/audits/scNNN-adjudication.md` — per-SC adjudication memos
  (copy `sound_changes/audits/ADJUDICATION_TEMPLATE.md`; must carry a
  `Registry-verdict:` line agreeing with the registry).

**Publication-prose SOURCE** (reader-facing text; inspect after a verdict):

- `sound_changes/reader_facing/*.md` chapters and
  `sound_changes/book_dossiers/*.md` — `adjudicate.py SCNNN --prepare`
  lists exactly which of these are relevant to a given SC.
- `CURRENT_STATE.md` (phase/commands only; no per-SC facts).

## What is GENERATED (do not edit; regenerate)

`python3 Germanic/tools/adjudicate.py SCNNN --finalize` regenerates all of
these deterministically and then runs propagation checks — you never decide
which generator to run. Generated files:
`sound_changes/sound_change_historical_staging_map.tsv`,
`sound_changes/sound_change_inventory.tsv`, the chronology graph files under
`sound_changes/order_tests/chronology_graph/` (edges TSV/JSON/DOT, nodes,
summary), `sound_changes/registry/settled_verdicts.md`,
`sound_changes/cascade_baseline/historical_audit_table.tsv`, and
`sound_changes/cascade_baseline/rename_migration_manifest.tsv`.
(Debugging only: `python3 Germanic/tools/generate_registry_views.py [--check]`.)

## What is ARCHIVE (never authoritative)

`archive/` (old project states, DEV_NOTES research log, old workflow/plans),
`sound_changes/archive/`, batch reports, frozen baselines' historical
snapshots, and the chronology-card programme records. See `archive/README.md`.

## One SC adjudication, start to finish

1. `python3 Germanic/tools/adjudicate.py --next` — the next SC (derived
   from the registry; never hand-maintained).
2. `python3 Germanic/tools/adjudicate.py SCNNN --prepare` — assembles the
   packet: registry row, rule text, edges, fingerprints, and a
   registry-driven reading list (required sources, existing
   adjudication, chronology evidence, publication prose, historical
   support). Do not search the repository for evidence; the packet is the
   reading list.
3. `python3 Germanic/tools/adjudicate.py SCNNN --evidence` — rebuilds the
   full cascade and stage bins in the backend container, verifies their
   freshness, and prints the complete live firing census plus witness
   pre/post forms. Never run `foma`/`flookup` or trace scripts by hand.
4. Follow `RESEARCH_ADJUDICATION_PROTOCOL.md`; record everything in the memo.
5. Propagate the verdict by editing SOURCE files only (registries, memo,
   FST/corpus only if the verdict requires, relevant publication prose).
6. `python3 Germanic/tools/adjudicate.py SCNNN --finalize` — regenerates
   all derived artifacts and validates propagation consistency.
7. `cd Germanic/tests && python3 -m pytest -q` — full suite must pass.
8. Commit and push; STOP after one SC.

Current phase and frozen baselines: `CURRENT_STATE.md`.
