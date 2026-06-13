# Running SC004-SC006 first-break tests

## Working directory

Run all commands from the repository root:

```bash
cd /Users/nathanhill/Code/capr-v3-working
```

## Why no new harness script is needed

SC004, SC005, and SC006 are inside bundled `PWGmcChanges`, but unlike SC002-SC003 they are already supported by the ordinary first-break runner through:

```bash
--order-profile expanded-pwgmc
```

That mode expands `PWGmcChanges` in memory for first-break testing only. No production FST change and no separate early-rule harness are required for these three changes.

## Dry-run commands

These commands are lightweight and safe. They verify imports, change lookup, and the resolved expanded-PWGmc order profile without compiling variants or writing TSV output:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC004 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC005 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC006 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed dry-run positions:

1. `SC004` resolves as position `1` in the expanded profile.
2. `SC005` resolves as position `2`.
3. `SC006` resolves as position `3`.

## Full commands for Nathan

These runs may be heavy. They compile many temporary variants and evaluate the full corpus after each move, so run them in a separate terminal:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC004 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC005 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC006 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv
```

## Expected output TSVs

These three files are the intended output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`

## Resume behavior

1. Re-run the same command with `--resume` to continue an interrupted crawl.
2. To recompute one change from scratch, omit `--resume` for that change only. The runner clears only that change's existing rows in the three output TSVs before recalculating them.

## How to verify success

1. Check that the summary TSV contains two completed rows for each change, one for `earlier` and one for `later`:

```bash
python3 - <<'PY'
from pathlib import Path
for line in Path("Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv").read_text(encoding="utf-8").splitlines():
    if line.startswith(("SC004\t", "SC005\t", "SC006\t")):
        print(line)
PY
```

2. Confirm that none of those rows still show `in_progress` or `skipped`.
3. If a row shows `first_break_found`, inspect the matching entries in the changes and failures TSVs for the exact wrong-output diagnostics.

## What to commit after Nathan runs the heavy commands

Commit at least:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`

Do **not** create or commit chronology cards for SC004-SC006 until a follow-up pass rewrites them from those real TSV outputs.
