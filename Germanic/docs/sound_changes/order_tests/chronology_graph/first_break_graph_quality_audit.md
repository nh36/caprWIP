# First-break graph quality audit

## Scope

This pass audits the first-break chronology graph export for regeneration determinism, file-to-file consistency, controlled vocabulary compliance, target validity, reciprocal-group consistency, and summary-prose restraint. No new first-break computations were run.

Files checked:

1. `Germanic/docs/sound_changes/order_tests/chronology_graph/README.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_graph/build_first_break_graph.py`
3. `Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_nodes.tsv`
4. `Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.tsv`
5. `Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.dot`
6. `Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.json`
7. `Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_graph_summary.md`

Source layers rechecked against the graph export:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
2. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_quality_audit.md`
4. `Germanic/docs/sound_changes/order_sensitivity_first_break_consolidated_overview.md`
5. selected `Germanic/docs/sound_changes/order_tests/chronology_cards/SC*.md`

## Regeneration determinism

The exporter was rerun from the repository root with:

```bash
python3 Germanic/docs/sound_changes/order_tests/chronology_graph/build_first_break_graph.py
```

Determinism result:

1. The first rerun from the clean `b49a639d` checkout produced no unintended diffs.
2. After the QA fixes below were made, the exporter was rerun again and regenerated the modified graph files consistently.
3. `git diff --check` remained clean throughout the audit.

This means the exporter is stable and dependency-free in the current repository state.

## Node and edge counts

The generated files are internally consistent:

1. `first_break_nodes.tsv` has `70` data rows.
2. `first_break_edges.tsv` has `140` data rows.
3. `first_break_edges.json` contains `70` nodes and `140` edges.
4. `first_break_graph_summary.md` reports the same totals.
5. `first_break_edges.dot` contains `140` edge statements, matching the TSV/JSON edge count exactly.

No count mismatch was found.

## Controlled vocabulary result

The node `card_type` values are all within the allowed controlled vocabulary:

1. `reciprocal_or_near_reciprocal`
2. `one_sided_historical`
3. `broad_far`
4. `negative_boundary`
5. `runner_limited_or_non_historical`
6. `mixed`

The edge `relation_type` values are all within the allowed controlled vocabulary:

1. `reciprocal_historical`
2. `near_reciprocal_historical`
3. `one_sided_historical`
4. `broad_far_historical`
5. `non_historical_computational`
6. `no_break_search_boundary`
7. `runner_limited_boundary`

No stray vocabulary values were found.

## Target validity result

Source IDs and target IDs are valid:

1. Every `source_change_id` is one of the 70 ordinary chronology-card node ids.
2. Every `target_change_id` is either one of those 70 ordinary node ids or one of the allowed diagnostic targets actually used by the export:
   - `PWGmcChanges`
   - `SC038`
   - `RUNNER_LIMIT`

Additional checks:

1. No unexpected diagnostic target ids were introduced.
2. `SC087` appears only as an ordinary node target for `no_break_search_boundary` edges, not as a separate diagnostic-target class.
3. `PWGmcChanges` is used only for `runner_limited_boundary` or `non_historical_computational` edges.
4. `SC037 -> SC038` is exported only as `non_historical_computational`.

## Reciprocal group result

Every `reciprocal_historical` or `near_reciprocal_historical` edge has a non-empty `reciprocal_group_id`, and every reciprocal group has the expected reversed partner edge.

No malformed reciprocal groups were found.

### Fixes made

Two graph-layer interpretation fixes were made:

1. `SC031 -> PWGmcChanges` and `SC033 -> PWGmcChanges` had initially been exported as plain `runner_limited_boundary` edges.
   - This was too weak: the cards explicitly describe both sides as real computational breaks that cross bundled `PWGmcChanges`.
   - They now export as `non_historical_computational`.

2. `SC064 / SC072` had initially been exported as `reciprocal_historical`.
   - The cards do support reciprocity, but the evidence is narrow, concentrated in the same `fright` derivation, and spans a non-local corridor.
   - The pair now exports as `near_reciprocal_historical`, and the summary explicitly warns that `near_reciprocal_historical` and `broad_far_historical` entries are not immediate local adjacency claims.

### Special pair check

The three audit-focus pairs now behave correctly:

1. `SC047 / SC048` — exported as `broad_far_historical`, not tight local reciprocity.
2. `SC064 / SC072` — exported as `near_reciprocal_historical`, not tight local reciprocity.
3. `SC072 / SC073` — exported as `broad_far_historical`, not tight local reciprocity.

## Boundary-edge result

The graph export now keeps the diagnostic boundary classes separate from ordinary historical chronology edges:

1. `no_break_search_boundary` edges remain search-boundary observations only and are not described as historical must-precede constraints.
2. `runner_limited_boundary` edges to `PWGmcChanges` remain search-limit observations rather than historical first breaks.
3. `SC031 -> PWGmcChanges` and `SC033 -> PWGmcChanges` are explicitly marked as non-historical computational breaks rather than ordinary runner-limited non-events.
4. `SC037 -> SC038` remains a technical-marker edge and is not exported as ordinary chronology evidence.

## Summary prose result

`first_break_graph_summary.md` now stays within the audited interpretive limits:

1. broad/far constraints are separated from tighter reciprocal relations;
2. `broad_far_historical` and `near_reciprocal_historical` clusters are explicitly warned against adjacency-style reading;
3. runner-limited and no-break edges are explicitly described as diagnostic search-boundary observations rather than historical constraints tied to `PWGmcChanges` or `SC087`;
4. technical-marker and bundled-stage cases are explicitly isolated in the non-historical section.

No remaining wording was found that materially overstates the graph evidence.

## Remaining caveats

The export is usable, but a few interpretation caveats remain inherent to the corpus:

1. some reciprocal or near-reciprocal groups are constructionally strong but still narrow in lexical coverage;
2. broad/far relations remain computationally real without implying local adjacency;
3. the largest current blind spot is still the bundled earlier corridor inside `PWGmcChanges`, which the graph can label but not yet unpack historically.

## Recommendation for the next phase

The graph export now passes QA and is stable enough for reuse.

The next **substantial technical phase** should be **runner work to expose or split `PWGmcChanges`**, because that is now the clearest remaining limit on the chronology network. A lightweight rendered visualization pass based on the DOT file is also safe to do, but it should be treated as presentation work rather than the main technical next step.
