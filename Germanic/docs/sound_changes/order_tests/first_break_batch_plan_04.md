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

## Completed second batch

The next manual terminal batch is now complete for:

1. `SC046` OE A Restoration
2. `SC050` Sievers Law Syncope
3. `SC055` OE I Umlaut

Those results extend the chronology-card set into the SC043 / SC044 / SC048 restoration zone and into the SC052 / SC056 corridor around SC055. They also show that SC050 currently has an earlier runner-boundary result rather than a detected earlier historical break.

## Completed scaled batch

The scaled manual terminal batch is now complete for:

1. `SC045` OE Velar Fricative Palatalization
2. `SC047` OE Heavy Syllable Nasal Apocope
3. `SC048` OE Secondary Nasalization
4. `SC051` OE Sk Palatalization
5. `SC052` OE Velar Palatalization
6. `SC056` OE Ws Palatal Diphthongization
7. `SC059` OE Back Mutation
8. `SC072` OE Unstressed Long Vowel Shortening
9. `SC078` OE Weak Tail Reduction

These results greatly expand the chronology-card network and add several reciprocal or near-reciprocal constraints, especially SC044 / SC045, SC047 / SC048, SC052 / SC055, and SC055 / SC056.

## Remaining eligible queued / pending rules

Remaining eligible explicit-chain rules now still in `queued` / `pending` status are:

1. Early corridor: `SC014`, `SC015`, `SC016`, `SC017`, `SC018`, `SC019`, `SC020`, `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC027`, `SC028`, `SC029`, `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, `SC040`
2. Mid corridor: `SC049`, `SC053`, `SC054`, `SC057`, `SC058`, `SC060`, `SC061`
3. Late corridor: `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC073`, `SC074`, `SC075`, `SC076`, `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`

## Recommended next step

Recommended next step: pause for a consolidation pass over the chronology cards and summary table before launching another large terminal batch. The TSV outputs remain clean, but the interpretation layer is now large enough that it is worth normalizing prose, checking reciprocal links, and separating broad computational boundaries from narrow local ones.

If the user prefers to keep running the driver instead, another 8-10 rule batch is now operationally reasonable.

## Narrative synthesis cautions

Keep three synthesis cautions in view:

1. The SC041 earlier boundary remains a broad computational limit rather than a narrow adjacency claim.
2. The SC050 earlier side ends at a runner boundary inside `PWGmcChanges`, so it should not be narrated as if a historical earlier first-break boundary had been found.
3. The SC056 later side found no real break before the runner boundary, so it must not be rewritten as a claim that SC056 must precede `SC087`.

## Scaling note

The driver has now survived several manual terminal batches cleanly. Future terminal runs no longer need to stay at three rules per batch: a 6-10 rule batch is now a reasonable target when the selected rules are all eligible explicit-chain members and the user wants a longer run.

As before, heavy runs should be done manually from a normal terminal rather than inside Copilot.

## After a batch completes

Once a terminal batch run finishes cleanly, the follow-up workflow is:

1. inspect the summary, changes, and failures TSVs
2. update `sound_change_order_sensitivity.tsv`
3. generate or refresh chronology cards
4. write a batch report summarizing the new boundaries and caveats
