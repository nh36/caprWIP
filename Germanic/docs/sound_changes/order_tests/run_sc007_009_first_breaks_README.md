# Running SC007-SC009 first-break tests

## Working directory

Run all commands from the repository root:

```bash
cd /Users/nathanhill/Code/capr-v3-working
```

## Why no new harness is needed

SC007, SC008, and SC009 are already exposed by the ordinary first-break runner through:

```bash
--order-profile expanded-pwgmc
```

That mode expands bundled `PWGmcChanges` in memory for first-break testing only. No production FST change and no separate harness wrapper are needed for this batch.

## Dry-run commands

These commands are lightweight and safe. They confirm that the runner resolves the expanded-PWGmc order and can target each change directly:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC007 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC008 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC009 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed dry-run positions:

1. `SC007` resolves as position `4` in the expanded profile.
2. `SC008` resolves as position `5`.
3. `SC009` resolves as position `6`.

## Full commands for Nathan

These runs may be heavy. Run them in a separate terminal:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC007 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC008 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC009 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv
```

## Expected output files

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

## Resume behavior

1. Re-run the same command with `--resume` to continue an interrupted crawl.
2. To recompute one change from scratch, omit `--resume` for that change only. The runner clears only that change's rows in the three output TSVs before recalculating them.

## How to verify success

1. Confirm that the summary TSV contains earlier and later rows for `SC007`, `SC008`, and `SC009`.
2. Confirm that none of those rows still shows `in_progress` or `skipped`.
3. If a row shows `first_break_found`, inspect the companion changes and failures TSVs for the exact wrong-output diagnostics.

## What to commit after Nathan runs the heavy commands

Commit at least:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

Do **not** create or commit chronology cards for SC007-SC009 until a follow-up pass rewrites them from those real TSV outputs.
