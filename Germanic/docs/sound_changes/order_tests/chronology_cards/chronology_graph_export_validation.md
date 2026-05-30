# Chronology graph export validation

This note validates the first exported chronology graph TSV layer before any visualization planning or graph generation. The review used the committed export TSVs, the export report, the relation-review TSV, and the existing node/index metadata only. No sound-change computations or visual graph outputs were run.

## 1. File presence

All five expected export-layer files are present:

1. `chronology_graph_edges_core.tsv`
2. `chronology_graph_edges_contextual.tsv`
3. `chronology_graph_edges_excluded.tsv`
4. `chronology_graph_nodes.tsv`
5. `chronology_graph_export_report.md`

## 2. Row counts

The committed row counts match the export report:

1. `chronology_graph_edges_core.tsv`: 45 data rows
2. `chronology_graph_edges_contextual.tsv`: 21 data rows
3. `chronology_graph_edges_excluded.tsv`: 50 data rows
4. `chronology_graph_nodes.tsv`: 70 data rows

## 3. Schema stability

The core and contextual edge TSVs use the same stable edge schema:

`edge_id`, `source_change_id`, `target_change_id`, `graph_layer`, `relation_kind`, `support_count`, `supporting_rows`, `supporting_cards`, `representative_failures`, `broad_far`, `reciprocal`, `runner_limited`, `supplementary`, `notes`

The excluded TSV uses the stable exclusion schema:

`excluded_id`, `relation_review_row`, `source_card`, `source_change_id`, `boundary_side`, `target_change_id`, `target_stage_label`, `graph_policy_bucket`, `relation_kind`, `reason_excluded`, `supporting_card`, `representative_failures`, `notes`

The node TSV uses the stable node schema:

`change_id`, `current_order`, `rule_name`, `card_file`, `in_core_edges`, `in_contextual_edges`, `has_excluded_relations`, `has_supplementary_expanded_profile_note`, `notes`

## 4. Policy compliance

The exported edge layer is policy-compliant:

1. No core edge has `graph_layer` other than `core`.
2. No core edge has `runner_limited=yes`.
3. No core edge has `supplementary=yes`.
4. No core edge has `broad_far=yes`.
5. No contextual edge has `graph_layer` other than `contextual`.
6. No contextual edge has `runner_limited=yes`.
7. No contextual edge has `supplementary=yes`.
8. No runner-limited or no-break-to-runner-boundary relation appears in the core or contextual TSVs.
9. The expanded-PWGmc supplementary relations appear only in `chronology_graph_edges_excluded.tsv`:
   - `excluded_049`: `SC031 -> SC011`
   - `excluded_050`: `SC033 -> SC008`

No edge TSV corrections were needed.

## 5. Traceability

Traceability checks passed cleanly:

1. Every `supporting_rows` reference in the core and contextual TSVs resolves to an existing `relation_row_###` entry derived from `chronology_graph_candidate_relation_review.tsv`.
2. Every `supporting_cards` entry in the core and contextual TSVs names an existing ordinary `SC*.md` card.

## 6. Deduplication sanity

Deduplication checks also passed:

1. No duplicate `edge_id` appears within `chronology_graph_edges_core.tsv`.
2. No duplicate `edge_id` appears within `chronology_graph_edges_contextual.tsv`.
3. Core edges with `support_count=2`: 24
4. Contextual edges with `support_count=2`: 2

These counts are consistent with reciprocal support being merged into single exported edges where expected.

## 7. Chronological direction sanity

Using `chronology_graph_nodes.tsv` current-order data, every core and contextual edge points from a lower `current_order` to a higher `current_order`.

No included edge runs backward, and no included edge has missing node-order data.

## 8. Node coverage

Node coverage is complete:

1. `chronology_graph_nodes.tsv` covers all 70 ordinary chronology-card changes.
2. The node set matches the ordinary-card index exactly.
3. Every `source_change_id` and `target_change_id` in the core and contextual TSVs is present in `chronology_graph_nodes.tsv`.

## 9. Mechanical node-note clarification

One wording issue was found in the node TSV. Twelve rows had:

1. `in_core_edges=no`
2. `in_contextual_edges=yes`
3. `has_excluded_relations=yes`

but still said `currently represented only in contextual edges`, which understated the simultaneous presence of excluded relation rows.

That wording was mechanically clarified to:

`no core edges; represented in contextual edges and excluded relation rows`

This change was applied only to the affected node rows and did not alter evidence, counts, policy buckets, or edge exports. The affected changes are:

`SC015`, `SC021`, `SC023`, `SC024`, `SC033`, `SC035`, `SC037`, `SC049`, `SC057`, `SC061`, `SC069`, `SC087`

For `SC033`, the existing supplementary-note suffix was preserved.

## 10. Recommendation

Validation passes after the node-note clarification. The next task should be a **documentation-only visualization planning task**, not graph generation.

That planning task should decide the output format and styling conventions for a first graph preview, especially:

1. whether the first preview should be DOT, Mermaid, or another text-based intermediary;
2. how core versus contextual edges should be distinguished;
3. how excluded rows should remain documented without being rendered as ordinary graph edges.
