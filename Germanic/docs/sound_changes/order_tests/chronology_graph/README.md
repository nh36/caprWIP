# First-break chronology graph export

This directory contains a lightweight graph/data export of the completed searchable explicit-chain first-break chronology corpus. It is derived from the existing chronology cards and summary tables only; no new first-break computations are run here.

## Files

1. `build_first_break_graph.py` — standard-library exporter that regenerates the graph files in this directory.
2. `first_break_nodes.tsv` — one row per chronology-card node in the current searchable corpus.
3. `first_break_edges.tsv` — ordinary sound-change chronology relations and diagnostically useful boundary relations extracted from the card/index layer.
4. `first_break_edges.dot` — Graphviz DOT export for dependency-free downstream rendering.
5. `first_break_edges.json` — JSON export of the node/edge payload.
6. `first_break_graph_summary.md` — corpus-level summary of node/edge counts and major relation classes.
7. `first_break_graph_terminology_note.md` — terminology rationale and old-to-new label mapping for this export layer.

## Terminology note

In this documentation, **ordinary chronology** means a first-break relation between modeled sound-change rules. Technical markers, bundled runner stages such as `PWGmcChanges`, and no-break search boundaries are still useful computational evidence, but they are not ordinary sound-change chronology constraints.

## Node schema

`first_break_nodes.tsv` exports the searchable chronology-card corpus itself. The current file contains the 70 audited chronology-card nodes and uses these main fields:

1. `change_id`
2. `display_name`
3. `current_order`
4. `rule_name`
5. `card_path`
6. `card_type`
7. `has_reciprocal_boundary`
8. `short_summary`

`card_type` uses a controlled vocabulary:

1. `reciprocal_or_near_reciprocal`
2. `one_sided_chronology`
3. `broad_far`
4. `negative_boundary`
5. `runner_limited_or_technical`
6. `mixed`

## Edge schema

`first_break_edges.tsv` exports both ordinary sound-change chronology constraints and diagnostically useful boundary observations. Main fields:

1. `source_change_id`
2. `target_change_id`
3. `relation_type`
4. `direction_basis`
5. `representative_lexemes`
6. `representative_forms`
7. `strength`
8. `interpretation_category`
9. `reciprocal_group_id`
10. `notes`

`relation_type` uses a controlled vocabulary:

1. `reciprocal_chronology`
2. `near_reciprocal_chronology`
3. `one_sided_chronology`
4. `broad_far_chronology`
5. `technical_computational`
6. `no_break_search_boundary`
7. `runner_limited_boundary`

## Diagnostic target ids

Some diagnostic edges point to boundary targets that are not exported as ordinary chronology-card nodes:

1. `PWGmcChanges` — bundled earlier runner boundary
2. `SC038` — technical-marker target for `SC037` later
3. `RUNNER_LIMIT` — terminal later runner limit beyond the searchable explicit chain

Those targets are intentionally separated from the 70 ordinary chronology-card nodes so the node table stays aligned with the audited card corpus.

## Regeneration

Run from the repository root:

```bash
python3 Germanic/docs/sound_changes/order_tests/chronology_graph/build_first_break_graph.py
```

The exporter uses only Python's standard library and overwrites the generated TSV / DOT / JSON / summary outputs in this directory.
