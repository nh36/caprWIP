# Running SC002-SC003 first-break validation

## Working directory

Run all commands from the repository root:

```bash
cd /Users/nathanhill/Code/capr-v3-working
```

## What this harness does

`run_early_rule_first_breaks.py` builds a **temporary expanded Old English cascade** from `fsts/old_english_sandbox.txt`, where the bundled `PGmcConsonantRules` stage is already split into explicit `PGmcGmSimplification` and `PGmcRhotacism` steps. It does **not** edit the production cascade in `Germanic/fsts/germanic.txt`.

## Lightweight dry-run commands

These are safe to run inside the agent or a normal terminal. They validate imports, target lookup, witness selection, and temporary expanded-cascade construction without compiling or searching for first breaks:

```bash
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --dry-run
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC003 --dry-run
```

## Full first-break commands for Nathan to run manually

These may be heavy because they compile many temporary variants and evaluate the full Old English corpus after each move. Run them in a separate terminal, not through an interactive agent session:

```bash
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --direction both --resume
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC003 --direction both --resume
```

## Expected runtime category

Treat the full runs as **heavy**. SC002 begins at the left edge of the explicit early-rule chain, so its later crawl may span a large portion of the full cascade. SC003 may likewise require many compile/evaluate cycles before reaching a break or a boundary.

## Expected output files

The harness writes to:

```text
Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv
Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv
Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv
```

The rows are keyed by `change_id` and `direction`, so SC002 and SC003 can be run separately into the same files.

## How to stop safely

Use `Ctrl-C` in the terminal running the harness.

The runner writes changes/failures TSV rows after each completed tested variant and updates the summary TSV after every safe step, so an interrupted run can usually be resumed without recomputing finished steps.

## How to resume or rerun

Resume an interrupted run with the same command and `--resume`:

```bash
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --direction both --resume
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC003 --direction both --resume
```

To rerun one change from scratch while leaving the other change's rows intact, rerun the command **without** `--resume` for that change:

```bash
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --direction both
```

That clears only the SC002 rows in the three output TSVs and recomputes them.

## How to verify success

1. Confirm that the summary TSV contains two completed rows for each change, one for `earlier` and one for `later`:

```bash
rg '^SC002\t|^SC003\t' Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv
```

2. Check that the `result` column is no longer `in_progress` or `skipped`.
3. If a real break was found, confirm that matching variant rows exist in:
   - `order_sensitivity_first_break_early_rules_01_changes.tsv`
   - `order_sensitivity_first_break_early_rules_01_failures.tsv`

## What to commit after a successful heavy run

Commit at least:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

If the heavy run is then used to replace the current draft chronology cards with validated cards, also commit:

4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC002-pgmc-gm-simplification.md`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC003-pgmc-rhotacism.md`
