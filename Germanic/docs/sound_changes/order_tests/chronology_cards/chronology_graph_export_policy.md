# Chronology graph/export policy

## 1. Purpose and scope

The chronology graph/export layer should be treated as a **presentation layer** over already documented default first-break evidence.

It is **not** a new computation layer, and it is **not** a replacement for the ordinary chronology cards. The cards remain the primary human-readable evidence record. Any later graph/export output should therefore be a derived summary layer whose claims stay traceable back to the current card corpus and relation-review rows.

This policy only defines how the existing relation-review layer should feed later edge exports. It does **not** authorize graph generation in the present task.

## 2. Controlling inputs

Later graph/export work should use these inputs, in this order:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_candidate_relation_review.tsv`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_candidate_relation_review_report.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_corpus_audit.tsv`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
5. the individual `SC*.md` chronology cards as the human-readable evidence source

The relation-review TSV is the operational input for later edge generation. The report, corpus audit, card index, and card files remain supporting interpretation and traceability layers.

## 3. Row-level evidence versus graph-level edges

The relation-review TSV contains **evidence rows**. A later graph/export layer should contain **deduplicated chronological edges**.

This distinction matters:

1. `SC016` later -> `SC017` and `SC017` earlier -> `SC016` are two support rows in the review TSV, but they represent one graph edge: `SC016 before SC017`.
2. Reciprocal relations should therefore be merged into one edge while keeping both support rows recorded in export metadata.
3. One-sided relations should remain one edge with one support row.
4. Counts in `chronology_graph_candidate_relation_review_report.md` are row counts unless they are explicitly identified as deduplicated edge counts.

So later export tasks should never copy relation-review row counts directly into graph-edge counts without deduplication.

## 4. Core graph policy

`include_core` should define the **default graph layer**.

The core graph should include:

1. clear local historical relations;
2. reciprocal historical relations;
3. one-sided local historical relations, if a later review row is explicitly bucketed as `include_core`.

The core graph should **not** include:

1. runner-limited boundaries;
2. no-break-to-runner-boundary observations;
3. technical-marker relations;
4. supplementary expanded-profile relations;
5. broad/far contextual relations unless a later task explicitly opts into a separate contextual overlay.

This keeps the default graph conservative and prevents it from overstating search-limit or review-layer evidence as normal chronology structure.

## 5. Contextual graph policy

`include_contextual` should be treated as a **separate optional layer**, not as part of the default core graph.

Contextual edges should include:

1. broad/far historical relations;
2. one-sided relations that are historically meaningful but not local;
3. relations already marked as requiring policy judgement.

If these edges are later exported, they must be visually or structurally distinguished from the core graph. Reasonable descriptive labels for later export metadata include:

1. `broad_far`
2. `one_sided`
3. `contextual`

This policy does **not** choose exact visualization styling. The important constraint is that contextual edges must not be mistaken for tight local adjacency claims.

## 6. Exclusion policy

These graph-policy buckets are excluded from default graph edges:

1. `exclude_runner_boundary`
2. `exclude_technical_marker`
3. `supplementary_only`

They are excluded for different reasons:

1. runner-boundary and no-break rows are search-limit observations, not ordinary chronology claims;
2. technical-marker rows reflect implementation/scaffolding boundaries rather than historical sound-change order relations;
3. supplementary expanded-PWGmc rows are review-layer evidence and do not replace the default bundled-profile chronology corpus.

Excluded rows should remain visible in review/export reporting, but they should not become default graph edges.

## 7. Treatment of expanded-PWGmc notes

The current expanded-PWGmc supplementary notes on `SC031` and `SC033` should remain supplementary in graph/export policy.

That means:

1. `SC031 -> SC011` and `SC033 -> SC008` may be mentioned in documentation or in a supplementary review appendix;
2. they should **not** appear in the default graph/export layer;
3. they should enter a graph/export edge layer only if a later task explicitly creates a separate expanded-profile graph or appendix export.

So the default graph policy continues to respect the default bundled-profile corpus even while the supplementary expanded-PWGmc documentation remains available.

## 8. Proposed later export files

Do **not** create these files in the current task. For a later edge-export task, the likely file set should be:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_edges_core.tsv`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_edges_contextual.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_edges_excluded.tsv`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_nodes.tsv`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_graph_export_report.md`

Likely columns for later edge TSVs:

1. `edge_id`
2. `source_change_id`
3. `target_change_id`
4. `graph_layer`
5. `relation_kind`
6. `support_count`
7. `supporting_rows`
8. `supporting_cards`
9. `representative_failures`
10. `broad_far`
11. `reciprocal`
12. `runner_limited`
13. `supplementary`
14. `notes`

The important principle is that later export files must preserve support-row traceability instead of collapsing the evidence into opaque edge claims.

## 9. Validation and review principles

A later export task should follow these rules:

1. derive edges from `chronology_graph_candidate_relation_review.tsv`;
2. preserve support-row traceability;
3. deduplicate reciprocal evidence into one edge;
4. keep contextual edges separate from the core graph;
5. create **no** graph visualization until TSV edge policy is confirmed;
6. run `git status -sb` and `git diff --check`.

This keeps the export layer auditable and prevents policy drift between row-level review and later graph material.

## 10. Recommendation for next task

The next task should be:

**generate deduplicated edge TSVs only, not visual graph files yet.**

That task should take the reviewed relation rows, deduplicate them into core/contextual/excluded edge layers, preserve support metadata, and stop before any diagram, DOT, Mermaid, or other visualization output is produced.
