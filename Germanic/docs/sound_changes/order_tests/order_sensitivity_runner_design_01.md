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

## Validation and pipeline mirroring

Validation 02 adds an identity-variant check before trusting any reordered variant.

The identity-variant flow:

1. parse the live `EnglishProtoToOE` order with no swaps
2. build a temporary variant transducer from that unchanged order
3. compile the variant
4. run the same 380-row Old English corpus through both the live baseline and the temporary identity variant
5. compare outputs row by row in `order_sensitivity_identity_variant_02.tsv`

This test exists because the variant pipeline must mirror the live `OldEnglishReflexes` stack exactly before any adjacent-swap results can be trusted.

The live stack being mirrored is:

- `OldEnglishCore = EnglishProtoInput .o. PGmcConsonantRules .o. EnglishProtoToOE`
- `OldEnglishAfterEpenthesis = OldEnglishCore .o. OEEpentheticVowel`
- `OldEnglishRules = OldEnglishAfterEpenthesis .o. OELateUnstressedAgSuffix .o. OECjCleanup .o. OEXsMerge .o. OldEnglishOrthography .o. OEGlideUToEO .o. OldEnglishRemoveStars`
- `OldEnglishReflexes = OldEnglishRules .o. OldEnglishSurface`

`OEEpentheticVowel` is therefore handled separately and applied exactly once in the variant builder. The post-epenthesis rule list contains only the rules that follow `OldEnglishAfterEpenthesis` in the live cascade.

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
- the identity variant with unchanged live order
- one-step earlier swap
- one-step later swap

for `SC043` and `SC063`.

## Reordering limits in scaffold 01 / validation 02

The current runner only parses and reorders the explicit `EnglishProtoToOE` composition chain.

That is suitable for `SC043` and `SC063`, because both appear as individually named stages inside that chain. It does **not** yet support moving rules inside bundled stages such as:

- `PGmcConsonantRules`
- `PWGmcChanges`

unless those bundles are explicitly expanded in the variant-generation method.

## What remains for the full runner

Still out of scope for scaffold 01:

- progressive earliest/latest window testing for each target change
- all-rule batch execution across the full active inventory
- reordering inside bundled stages such as `PGmcConsonantRules` or `PWGmcChanges`
- stronger classification of failures into historical-order evidence vs implementation dependency
- automatic prose generation from the TSV outputs
- wider safeguards around technical-marker stages and non-historical neighbors

## Execution refactor 03

The runner now has a cheaper execution path for repeated variant testing.

### Batch evaluation

The baseline and variant evaluators now support batched `flookup` execution: the runner sends the whole Old English corpus through one `flookup` subprocess per compiled transducer instead of spawning a fresh subprocess for every lexical row.

The batch path preserves the existing semantics:

- deduplicated outputs stay deduplicated
- multi-output rows remain multi-output rows
- no-output rows still serialize as `+?`
- expected-match status is still a simple inclusion test against the deduplicated output set

Validation command:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode validate-batch'
```

This must pass before batched evaluation is trusted for longer first-break runs.

### Resumable first-break mode

First-break mode is now directional and resumable:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC043 --direction both --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC063 --direction earlier --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC063 --direction later --resume'
```

The runner:

1. tests one adjacent move at a time in the requested direction
2. writes per-variant changed rows and failure rows immediately after each tested variant
3. updates the summary TSV with an `in_progress` resume marker after every safe step
4. stops as soon as it finds the first real break, a compile failure, or a hard boundary

`--resume` reads the existing summary row for that `change_id` and direction, reconstructs the already-safe position, and skips directions already marked complete.

### First-break semantics

The stopping condition is still a **real break**, not merely any changed output:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

Changed outputs that still include the expected form are still recorded in the changes TSV, but they do not stop the crawl.

### External-terminal usage

Longer crawls should be run from an ordinary terminal, not through a live Copilot session, because the shell command can finish successfully even when the agent-side output retrieval times out.

The intended operator pattern is:

1. validate batch mode once
2. run a quick SC043 sanity check if desired
3. run SC063 earlier and later separately with `--resume`
4. inspect the TSV outputs after the terminal run finishes cleanly
