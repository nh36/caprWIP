# Chronology graph export report

This export layer derives deduplicated edge TSVs from the committed relation-review TSV, following the chronology graph/export policy and preserving row-level traceability through `relation_row_###` references back to `chronology_graph_candidate_relation_review.tsv` data rows.

## Source input used

1. `chronology_graph_export_policy.md` as the controlling guide.
2. `chronology_graph_candidate_relation_review.tsv` as the operational input.
3. `chronology_graph_candidate_relation_review_report.md`, `chronology_card_index.tsv`, and the existing ordinary-card corpus only as supporting context.

## Summary

1. **Core edge rows:** 45
2. **Contextual edge rows:** 21
3. **Excluded rows:** 50
4. **Node rows:** 70
5. **Reciprocal relations deduplicated:** 26 total (24 core, 2 contextual)
6. **Expanded-PWGmc supplementary rows:** kept out of the default/core graph layer and recorded only in `chronology_graph_edges_excluded.tsv`.
7. **Visual graph files generated:** none.

## Layer notes

1. `chronology_graph_edges_core.tsv` contains only deduplicated `include_core` relations.
2. `chronology_graph_edges_contextual.tsv` keeps `include_contextual` relations separate from the core graph and preserves broad/far or one-sided policy sensitivity through `relation_kind`, `broad_far`, and `notes`.
3. `chronology_graph_edges_excluded.tsv` preserves runner-boundary, technical-marker, and supplementary expanded-PWGmc rows with explicit exclusion reasons instead of turning them into default graph edges.
4. `chronology_graph_nodes.tsv` covers all 70 ordinary chronology-card changes, including cards represented only through excluded relations.

## Clean interpretation check

All `include_core` and `include_contextual` rows mapped cleanly to chronological edges.

## Recommendation

The next task should review these exported TSV layers for policy compliance and naming/column stability before any visualization or graph styling step is attempted.
