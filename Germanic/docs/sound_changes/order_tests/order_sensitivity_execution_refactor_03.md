# Order-sensitivity execution refactor 03

## Problem

Long first-break runs are fragile inside the Copilot agent even when the underlying shell command succeeds. A first-break crawl may require many compile/evaluate cycles, and the agent-side API can time out or fail while trying to stream or retrieve the command output.

That makes the linguistic method sound but the interactive execution path unreliable for longer runs such as `SC063`.

## Current validated state

Validation 02 remains the prerequisite state for this refactor:

- identity variant matched live baseline on `380 / 380` rows
- live baseline and identity variant both matched the expected Old English form on `373 / 380` rows
- adjacent pilots remained stable
- `SC043` still breaks immediately one step earlier (`rest`) and one step later (`slay`)

During this refactor, a pre-refactor Copilot run also left local WIP first-break TSVs, including completed-looking `SC063` rows. Those files were preserved rather than discarded, and the refactored terminal reruns were then completed outside Copilot before the pilot-03 outputs were treated as commit-ready.

## Refactor

The runner was refactored in three ways.

### Batch flookup evaluation

The script now supports batched lexical evaluation:

- one `flookup` subprocess per compiled transducer
- all 380 Old English forms sent through that subprocess in one batch
- output grouping preserved row-for-row

Validation command:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode validate-batch'
```

This refactor pass validated batch mode against the old row-wise path on the full 380-row baseline and got an exact row-for-row match.

### Resumable first-break mode

First-break mode now supports:

- `--direction earlier|later|both`
- `--resume`
- incremental TSV writes after every tested variant

The summary TSV keeps one row per `change_id` / direction. While a crawl is incomplete, that row is written as `result = in_progress` and stores resume metadata in `notes`. When a direction finishes, the same row is replaced with the terminal result such as `first_break_found` or `no_break_before_boundary`.

The changes and failures TSVs are written per variant immediately after each tested variant finishes, so a later rerun does not need to recompute already-recorded variants just to keep the detail files coherent.

### External terminal commands

The runner is now meant to be driven from a normal terminal for longer jobs:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC043 --direction both --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC063 --direction earlier --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/sound_change_order_sensitivity.py --mode first-break --change SC063 --direction later --resume'
```

The script prints one short status line per tested variant and writes the detailed evidence to:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`

## First-break semantics

The stopping rule is unchanged and should remain strict.

A **real break** means:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

Changed outputs that still contain the expected form are still important evidence and remain recorded in the changes TSV, but they do **not** stop the crawl.

Once a real break is found in a direction, the runner stops that direction immediately.

## Dynamic-programming path

This refactor improves execution cost, but it does not yet change the core compile-per-variant architecture.

The next optimization path is:

1. keep batched lexical evaluation as the immediate speed win
2. precompile or cache reusable atomic rule transducers where feasible
3. cache prefix / suffix / segment compositions so nearby variants do not always require a full fresh compile
4. for the finite 380-row corpus, propagate sets of forms through cached segments instead of recompiling the full variant transducer every time

Any future dynamic or memoized engine must still pass identity validation against the live baseline before its chronology evidence is trusted.

## Recommended next action

1. Commit the completed pilot-03 TSV outputs and the updated chronology summary files.
2. Use the refactored terminal workflow for the next batch of non-bundled reader-facing rules.
3. Keep identity validation and batch validation as prerequisites for any future execution-engine optimization.
