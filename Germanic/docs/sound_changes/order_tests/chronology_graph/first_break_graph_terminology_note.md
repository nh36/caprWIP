# First-break graph terminology note

## Why the terminology changed

The earlier graph export used `historical` / `non-historical` as a contrast label inside the graph/documentation layer. That wording was potentially misleading for this project, because the modeled sound changes are themselves historical-linguistic objects and many of them predate attested Old English.

The intended contrast is narrower:

1. **ordinary chronology** — a first-break relation between modeled sound-change rules
2. **technical / runner / bundled-stage / search-boundary evidence** — computationally useful evidence that does not directly function as an ordinary sound-change chronology constraint

## Old-to-new label mapping

### Edge relation_type mapping

1. `reciprocal_historical` -> `reciprocal_chronology`
2. `near_reciprocal_historical` -> `near_reciprocal_chronology`
3. `one_sided_historical` -> `one_sided_chronology`
4. `broad_far_historical` -> `broad_far_chronology`
5. `non_historical_computational` -> `technical_computational`
6. `no_break_search_boundary` -> `no_break_search_boundary`
7. `runner_limited_boundary` -> `runner_limited_boundary`

### Node card_type mapping

1. `reciprocal_or_near_reciprocal` -> unchanged
2. `one_sided_historical` -> `one_sided_chronology`
3. `broad_far` -> unchanged
4. `negative_boundary` -> unchanged
5. `runner_limited_or_non_historical` -> `runner_limited_or_technical`
6. `mixed` -> unchanged

## Terminology principle

In this documentation, **ordinary chronology** means a first-break relation between modeled sound-change rules. Technical markers, bundled runner stages such as `PWGmcChanges`, and no-break search boundaries are still useful computational evidence, but they are not ordinary sound-change chronology constraints.

## What was not changed

The raw runner TSV schema was **not** migrated in this pass. If raw generated files or upstream tooling still use fields such as `historically_interpretable`, those remain unchanged unless and until the repository explicitly chooses to migrate the runner/output schema itself.
