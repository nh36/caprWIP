# Order-sensitivity runner pilot 01 report

## Summary

The pilot scaffold is in place and the existing generated TSVs were already complete in this pass, so they were reviewed rather than regenerated.

- baseline output succeeded and records `380` tested rows
- baseline totals are `373` matches and `7` fails
- pilot changes tested: `SC043` and `SC063`
- all four adjacent earlier/later variants compiled
- TSV outputs were written to `Germanic/docs/sound_changes/order_tests/summaries/`

This remains a smoke test for adjacent swaps only, not a full order-window search.

## Baseline

Baseline summary file:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_baseline_01.tsv`

Current baseline counts from that TSV:

- total rows tested: `380`
- rows matching expected: `373`
- rows failing expected: `7`
- no-output rows: `0`
- multi-output rows: `0`

The baseline denominator matches the writing-phase coverage corpus used by `oe_full_trace_report.py`, not the broader 386-row project-status denominator.

## Variant-generation method

The runner reads the live `EnglishProtoToOE` composition order from `Germanic/fsts/germanic.txt`, swaps the target rule with its immediate neighbor in a temporary copy, appends a variant transducer block, and compiles that temporary file only.

Live FST protection in this pilot:

- no edits to `Germanic/fsts/germanic.txt`
- no edits to lexical TSV source data
- no committed variant `.bin` files
- only TSV summaries plus prose notes are written back into the repository

## SC043 adjacent pilot

Target:

- `SC043` Anglo Frisian Brightening

Immediate neighbors from the active inventory:

- earlier neighbor: `SC042` PWGmc Surviving Bimoric O Unrounding
- later neighbor: `SC044` OE Breaking

### One-step earlier

- variant: `SC043_earlier_adjacent`
- compilation: `compiled`
- baseline matches: `373`
- variant matches: `372`
- changed outputs: `1`
- newly failing rows: `1`
- representative new failure: `rest`

The changed-row TSV shows:

- `rest` (`*rástōz`) shifts from expected `ræste` to `rasta`

### One-step later

- variant: `SC043_later_adjacent`
- compilation: `compiled`
- baseline matches: `373`
- variant matches: `372`
- changed outputs: `29`
- newly failing rows: `1`
- representative new failure: `slay`

Representative changed-but-still-passing rows include:

- `beard`
- `belly`
- `calf`
- `fall`
- `fern`

The changed-row TSV shows `slay` moving from expected `slēan` to `sleaan | slēaan`, producing the only newly failing row in this adjacent-later smoke test.

### Pilot interpretation

For this scaffold, both adjacent moves are diagnostically unstable:

- the earlier swap breaks `rest`
- the later swap changes many outputs and newly fails `slay`

That does **not** yet prove a full earliest/latest safe window; it only shows that immediate neighbors matter for this rule in the current implementation.

## SC063 adjacent pilot

Target:

- `SC063` OE High Vowel Apocope

Immediate neighbors from the active inventory:

- earlier neighbor: `SC062` OE Weight Markers
- later neighbor: `SC064` NWGmc In Stem N Loss

### One-step earlier

- variant: `SC063_earlier_adjacent`
- compilation: `compiled`
- baseline matches: `373`
- variant matches: `373`
- changed outputs: `0`
- newly failing rows: `0`

Runner note: this swap crosses the technical-marker stage `SC062`, so it is useful as an implementation smoke test but is not strong chronological evidence by itself.

### One-step later

- variant: `SC063_later_adjacent`
- compilation: `compiled`
- baseline matches: `373`
- variant matches: `373`
- changed outputs: `0`
- newly failing rows: `0`

### Pilot interpretation

In this limited adjacent test, neither immediate move produced output changes. That is a useful scaffold result, but it should not be over-interpreted as proof that the rule can move freely across a wider window.

## Runner limitations

This scaffold still does **not** do the following:

- no full earliest/latest search
- no all-rule batch execution
- no automatic prose generation
- no robust distinction between historical impossibility and implementation dependency except where an adjacent technical marker is obvious

## Files changed

- `Germanic/tools/sound_change_order_sensitivity.py` — added the pilot runner scaffold; this pass also fixed the default live-bin path so it resolves correctly in either a host checkout or the backend container
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_baseline_01.tsv` — baseline lexical summary
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01.tsv` — pilot variant summary
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01_changes.tsv` — row-level changed-output details
- `Germanic/docs/sound_changes/order_tests/order_sensitivity_runner_design_01.md` — scaffold design note
- `Germanic/docs/sound_changes/order_sensitivity_runner_pilot_01_report.md` — pilot report
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv` — updated `SC043` and `SC063` from `not_run` to adjacent-pilot results

## Recommended next task

**A. Extend the runner to full earliest/latest window testing for SC043 and SC063.**

The adjacent-pilot scaffold is working and already yields interpretable smoke-test outputs, so the next highest-value step is to extend this runner from immediate neighbors to progressive earlier/later movement for the same two dossier-backed rules before scaling to more changes.
