# Expanded PWGmc plumbing check

## Commands run

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --help

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC014 \
  --direction earlier \
  --order-profile expanded-pwgmc \
  --dry-run-order
```

## What the check confirmed

1. `--help` shows both `--order-profile {default,expanded-pwgmc}` and `--dry-run-order`.
2. The expanded dry-run order lists `SC004` through `SC013` explicitly before `SC014`.
3. `SC014` is present in the resolved order and is marked as the target.
4. No real first-break computation was run for this check.
5. No expanded-PWGmc first-break TSV outputs were written.

## Current interpretation

This confirms that the expanded-PWGmc runner plumbing is wired correctly at the CLI/order-resolution layer and that the expanded sequence is visible to first-break dry-run inspection without touching the default bundled-profile corpus.

## Next step

When we are ready for a real expanded-PWGmc smoke pilot, it should be run manually in a normal terminal with separate output paths, not by the agent.
