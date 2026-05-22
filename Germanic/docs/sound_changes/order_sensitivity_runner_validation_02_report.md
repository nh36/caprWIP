# Order-sensitivity runner validation 02 report

## Summary

Validation 02 corrected the variant pipeline and confirmed that the temporary variant now mirrors the live Old English transducer exactly for the current non-reordered case.

- variant pipeline corrected: **yes**
- `OEEpentheticVowel` now applied exactly once in the variant builder: **yes**
- baseline regenerated: **yes**
- identity variant compiled: **yes**
- identity variant matched live baseline exactly: **yes**
- adjacent pilots rerun: **yes**
- SC043 / SC063 results changed: **no**

## Pipeline mirroring fix

The scaffold 01 variant builder had a pipeline-mirroring bug: it applied `OEEpentheticVowel` once in `VariantOldEnglishAfterEpenthesis` and then again because the post-cascade list also began with `OEEpentheticVowel`.

That meant the temporary variant pipeline did not exactly mirror the live Old English stack, even though the pilot outputs happened not to reveal a failure from that duplication.

The fix was:

1. keep `OEEpentheticVowel` only in `VariantOldEnglishAfterEpenthesis`
2. change the post-cascade list so it begins with `OELateUnstressedAgSuffix`
3. document in code and design notes that the post-cascade list contains only the rules after `OldEnglishAfterEpenthesis`

The corrected variant now mirrors the live path:

- `OldEnglishCore`
- `OldEnglishAfterEpenthesis`
- `OldEnglishRules`
- `OldEnglishReflexes`

with `OEEpentheticVowel` applied exactly once.

## Identity-variant validation

Command used:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode identity-variant'
```

Results:

- total rows tested: `380`
- output-identical rows: `380`
- differing rows: `0`
- live match count: `373`
- identity-variant match count: `373`

Identity TSV:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_identity_variant_02.tsv`

This identity pass is the main trust check for the runner at this stage: the temporary variant now reproduces the live baseline exactly before any swapped-order variants are interpreted.

## Regenerated baseline

Command used:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode baseline'
```

Current baseline totals:

- total rows tested: `380`
- matches: `373`
- failures: `7`
- no-output rows: `0`
- multi-output rows: `0`

Baseline TSV:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_baseline_01.tsv`

Validation run context: regenerated during validation 02 on `2026-05-22`.

## Rerun adjacent pilots

Commands used:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode adjacent-pilot --change SC043'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode adjacent-pilot --change SC063'
```

### SC043

- earlier neighbor: `SC042` PWGmc Surviving Bimoric O Unrounding
- later neighbor: `SC044` OE Breaking
- one-step earlier result: `1` changed output, `1` newly failing row, representative failure `rest`
- one-step later result: `29` changed outputs, `1` newly failing row, representative failure `slay`

Comparison to pilot 01:

- results match pilot 01 exactly

### SC063

- earlier neighbor: `SC062` OE Weight Markers
- later neighbor: `SC064` NWGmc In Stem N Loss
- one-step earlier result: `0` changed outputs, `0` newly failing rows
- one-step later result: `0` changed outputs, `0` newly failing rows

Comparison to pilot 01:

- results match pilot 01 exactly

## Runner limitations after validation

The runner is more trustworthy after identity validation, but it still has important limits:

- no full earliest/latest search yet
- no all-rule batch execution yet
- no reordering inside bundled stages such as `PGmcConsonantRules` or `PWGmcChanges`
- adjacent swaps remain smoke tests, not a full chronology argument

## Files changed

- `Germanic/tools/sound_change_order_sensitivity.py` — fixed the post-epenthesis mirror bug, added identity-variant mode, and made adjacent-output rewrites remove stale rows by variant scope
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_identity_variant_02.tsv` — row-by-row live vs identity-variant validation output
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_baseline_01.tsv` — regenerated baseline output
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01.tsv` — regenerated adjacent summary after identity validation
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_adjacent_pilot_01_changes.tsv` — regenerated changed-row detail output after identity validation
- `Germanic/docs/sound_changes/order_tests/order_sensitivity_runner_design_01.md` — added validation and bundle-limit sections
- `Germanic/docs/sound_changes/order_sensitivity_runner_validation_02_report.md` — validation report
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv` — refreshed SC043 / SC063 notes to record identity validation and stable rerun results
