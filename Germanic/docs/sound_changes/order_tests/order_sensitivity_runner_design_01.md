# Order-sensitivity runner design 01

## Implemented scope

This scaffold implements a baseline lexical pass plus adjacent-swap pilot variants for two dossier-backed changes:

- `SC043` Anglo Frisian Brightening
- `SC063` OE High Vowel Apocope

It does **not** attempt a full earliest/latest window search across the 94 active stages yet.

## Baseline corpus loading

The runner reuses `Germanic/tools/oe_full_trace_report.py` helpers:

- `load_rows`
- `apply_down`
- `STAGES`

`load_rows` reads the same Old English rows used by the full trace report from `Germanic/data/germanic-aligned-final.tsv`, keeping only rows where:

- `DOCULECT = Old_English`
- `PROTOFORM` is present
- `COUNTERPART` is present and not `-`

That yields the current 380-row lexical-report denominator rather than the broader 386-row project-status denominator.

## Expected-output comparison

For each lexical row, the runner records:

- `lexical_item`
- `protoform`
- `expected_counterpart`
- transducer outputs
- whether any output matches the expected counterpart
- a note bucket such as `exact_match` or `single_output_mismatch`

Matching is currently a simple inclusion test: the row counts as passing when the expected Old English counterpart appears among the deduplicated `apply_down` outputs.

## Mapping target changes to FOMA rule names

The runner reads `Germanic/docs/sound_changes/sound_change_inventory.tsv` and uses the `rule_source_anchor` field to extract the live FOMA definition name.

For the pilot targets this maps to:

- `SC043` -> `AngloFrisianBrightening`
- `SC063` -> `OEHighVowelApocope`

Neighbor lookup comes from `current_order` in the same inventory file:

- `SC043` currently sits between `SC042` / `PWGmcSurvivingBimoricOUnrounding` and `SC044` / `OEBreaking`
- `SC063` currently sits between `SC062` / `OEWeightMarkers` and `SC064` / `NWGmcInStemNLoss`

## Variant generation

The runner parses the live `define EnglishProtoToOE (...)` composition chain from `Germanic/fsts/germanic.txt`, swaps the target rule one slot earlier or later in that chain, and appends temporary variant definitions to a copied `germanic.txt` in a temporary directory.

The variant compile flow is:

1. copy `germanic.txt` and `old_english_sandbox.txt` into a temp directory
2. append a `VariantEnglishProtoToOE` / `VariantOldEnglishReflexes` block to the temp `germanic.txt`
3. compile that temp file with `foma`
4. run the lexical corpus against the temporary `old_english_variant.bin`
5. remove the retained temporary bin after evaluation

The live FST sources are never edited.

## Compiled-bin handling

Variant bins are compiled in a temporary directory and briefly copied to `.tmp_order_sensitivity/` only so the runner can evaluate them after the compile step returns. The runner deletes those retained bins during cleanup. The intended committed outputs are the TSV summaries and prose notes only.

The checked-in baseline uses the current live `old_english.bin`. The runner now resolves that default path from whichever standard location exists in the current environment, so the same script can run either from a host checkout or from the backend container at `/usr/app`.

## Live-file protection

The scaffold avoids modifying live FST files by:

- reading the live order from `Germanic/fsts/germanic.txt`
- compiling only temporary copies
- writing repository outputs only to summary TSV and markdown report/design files

No lexical TSV source, live rule order, lexical volume file, or compiled `.bin` artifact needs to be committed for this pilot.

## Current pilot outputs

Implemented outputs:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_baseline_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01_changes.tsv`

These cover:

- the baseline live transducer
- one-step earlier swap
- one-step later swap

for `SC043` and `SC063`.

## What remains for the full runner

Still out of scope for scaffold 01:

- progressive earliest/latest window testing for each target change
- all-rule batch execution across the full active inventory
- stronger classification of failures into historical-order evidence vs implementation dependency
- automatic prose generation from the TSV outputs
- wider safeguards around technical-marker stages and non-historical neighbors
