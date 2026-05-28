# Expanded PWGmc first-break runner mode

## Purpose

`PWGmcChanges` is currently a bundled Foma definition inside `EnglishProtoToOE`. The sound-change inventory and the trace stack already expose the internal component rules as `SC004` through `SC013`, but the first-break runner parses the live `EnglishProtoToOE` chain directly. That means ordinary earlier first-break searches for `SC014+` hit the bundled `PWGmcChanges` item as their current search boundary.

This runner mode adds a **minimal optional expansion** for first-break testing only. It does **not** change the default behavior.

## New CLI option

`Germanic/tools/sound_change_order_sensitivity.py` now accepts:

```bash
--order-profile default|expanded-pwgmc
```

- `default` keeps the existing bundled `PWGmcChanges` item.
- `expanded-pwgmc` replaces that single item with its internal component sequence when `--mode first-break` is used.

The default profile remains unchanged, so existing baseline, adjacent-pilot, and first-break workflows still behave exactly as before unless the new profile is requested explicitly.

## Expanded sequence

The optional expanded profile replaces `PWGmcChanges` with:

1. `PWGmcAiMonophthongization`
2. `NWGmcAToUBeforeM`
3. `PWGmcEarlyIApocope`
4. `PWGmcFinalOrLowering`
5. `PWGmcCoronalWAssimilation`
6. `PWGmcIjContraction`
7. `PWGmcJGemination`
8. `PWGmcSyllabicJ`
9. `PWGmcLThVoicing`
10. `PWGmcDentalHardening`

The runner validates that this sequence matches both:

1. `define PWGmcChanges` in `Germanic/fsts/germanic.txt`
2. the corresponding `STAGES` slice in `Germanic/tools/oe_full_trace_report.py`

If either source drifts, the expanded profile raises an error instead of silently using a stale sequence.

## Dry-run order inspection

To inspect the resolved first-break order without compiling a variant, use:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC014 \
  --direction earlier \
  --order-profile expanded-pwgmc \
  --dry-run-order
```

This prints the live order profile with inventory IDs and marks the target rule, so it is easy to confirm that:

1. the default profile still places bundled `PWGmcChanges` immediately before `SC014`
2. the expanded profile places the ten internal PWGmc component rules before `SC014`
3. `SC004` through `SC013` appear explicitly in the expanded order
4. `SC014` is still present and movable

Dry-run order inspection is intentionally allowed with the default output paths, because it does not write any result TSVs.

## Safety and output-policy note

This is safe as an optional mode because it only changes the in-memory order list used by first-break variant generation when the expanded profile is requested. It does **not** rewrite `EnglishProtoToOE`, modify the default live runner path, or touch existing first-break TSV outputs.

The current 70-card corpus and its existing summary/graph layers remain based on the **default bundled profile**. Any future expanded-PWGmc testing must write to **separate output files** and must not overwrite the current default-profile corpus.

The runner now enforces that policy: a real `--mode first-break --order-profile expanded-pwgmc` run is refused unless all three first-break output paths are explicitly set away from the default bundled-profile files.

Suggested expanded-profile output filenames:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Safe command patterns

### Safe dry-run inspection

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC014 \
  --direction earlier \
  --order-profile expanded-pwgmc \
  --dry-run-order
```

### Intended separate-output run pattern

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC014 \
  --direction earlier \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv
```

If the expanded profile is invoked without separate output paths, the runner exits immediately with a refusal message rather than risking writes into the default bundled-profile corpus.

## Smoke pilot reference

The first manually run real expanded-profile smoke result is documented in `Germanic/docs/sound_changes/order_tests/expanded_pwgmc_smoke_pilot_01.md`. That note records the `SC014` earlier outcome as an expanded-profile result only; it does not revise the default-profile 70-card corpus.
