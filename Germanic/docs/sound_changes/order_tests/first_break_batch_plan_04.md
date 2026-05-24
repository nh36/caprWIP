# First-break batch plan 04

## Purpose

First-break testing is the computational layer that turns the runner into relative-chronology evidence for the eventual sound-change volume. Instead of exhaustively mapping every possible slot for every rule, the method finds the first earlier and later positions at which a baseline-matching Old English derivation breaks.

## Current evidence model

The workflow now has five evidence layers:

1. `order_sensitivity_first_break_pilot_03.tsv` — one row per change-direction result
2. `order_sensitivity_first_break_pilot_03_changes.tsv` — row-level changed outputs for tested variants
3. `order_sensitivity_first_break_pilot_03_failures.tsv` — only real breaks, where a previously matching row stops matching
4. `sound_change_order_sensitivity.tsv` — repo-facing summary of safe windows and failure counts
5. chronology evidence cards in `order_tests/chronology_cards/` — reusable prose-ready summaries for the book pipeline

## What counts as a boundary

A first-break boundary is a **real break**:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

Changed-still-passing outputs are still recorded in the changes TSV because they often reveal nearby instability, but they do **not** stop the search. Technical or support-stage crossings must be flagged separately from historically interpretable boundaries.

## Chronology-card prose standard

Chronology cards must state the constraint in concrete derivational terms. Each boundary statement should include:

- the Proto-Germanic input;
- the expected Old English output;
- the incorrect variant output;
- the crossed rule responsible for the boundary;
- a short explanation of why the wrong form results.

Modern English glosses such as `belly` or `cow` are useful row identifiers, but they are not sufficient as chronology prose by themselves.

## Batch-driver workflow

The manifest-driven driver runs the existing first-break runner one direction at a time and records progress after each direction.

Example commands:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --dry-run'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --only-status pending --limit 3 --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --manifest docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv --resume'
docker compose exec -T backend sh -lc "cd /usr/app && ls docs/sound_changes/order_tests/logs && tail -n 40 docs/sound_changes/order_tests/logs/SC055_earlier.log"
```

After a manual terminal batch completes cleanly, commit only the intended TSV / summary / chronology-card outputs.

## Eligibility limits

The current runner can test only rules that are individually named members of the parsed `EnglishProtoToOE` chain. It does **not** yet reorder inside bundled stages such as `PGmcConsonantRules` or `PWGmcChanges`.

For manifest classification:

- support stages are skipped
- technical markers are skipped
- orthography / surface stages are skipped
- non-explicit chain positions are skipped

Those stages can still matter interpretively, but they should not yet be treated as ordinary first-break targets.

## Completed first small batch

The first manual terminal batch is now complete for:

1. `SC041` PWGmc Final Bare A Loss
2. `SC042` PWGmc Surviving Bimoric O Unrounding
3. `SC044` OE Breaking

Those results have been folded into the first-break summary TSVs, the repo-facing order-sensitivity table, and dedicated chronology cards.

## Next proposed batch

Recommended next small batch (`6` rules):

1. `SC046` OE A Restoration — direct downstream restoration stage for the SC043 dossier
2. `SC050` Sievers Law Syncope — high-value syncope stage for weak-tail chronology
3. `SC055` OE I Umlaut — already exposed as SC063’s earlier boundary and central to many OE derivations
4. `SC059` OE Back Mutation — nearby high-value mutation stage in the same OE corridor
5. `SC072` OE Unstressed Long Vowel Shortening — already exposed as SC063’s later boundary
6. `SC078` OE Weak Tail Reduction — late weak-tail collapse stage with likely book-level interpretive value

Before running that next batch, review the SC041 earlier boundary carefully. The result is probably useful chronology evidence, but because the first break is far away at `SC020` and produces many `-a`-final failures at once, it should be narrated as a broad computational boundary rather than as a narrow local adjacency claim.

As before, heavy runs should be done manually from a normal terminal rather than inside Copilot.

## After a batch completes

Once a terminal batch run finishes cleanly, the follow-up workflow is:

1. inspect the summary, changes, and failures TSVs
2. update `sound_change_order_sensitivity.tsv`
3. generate or refresh chronology cards
4. write a batch report summarizing the new boundaries and caveats
