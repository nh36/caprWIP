# Order-sensitivity first-break batch 04 report

## Summary

Batch 04 interprets the first manual terminal batch after the SC043 / SC063 pilot.

- batch rules tested: `SC041`, `SC042`, `SC044`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all six directions completed: **yes**
- all six found first breaks: **yes**

Files updated / created:

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC041-pwgmc-final-bare-a-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC042-pwgmc-surviving-bimoric-o-unrounding.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC044-oe-breaking.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_batch_04_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Method

The runner uses first-break testing: it moves one rule one slot at a time earlier or later until it reaches the first **real break**.

A real break means:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

The batch itself was run manually in a normal terminal via the manifest-driven driver. No live FST order was changed; the results come from temporary reordered variants only.

## SC041 PWGmc Final Bare A Loss

- current order: `41`
- safe computational window: `21-45`
- earlier boundary: order `20`, crossing `SC020` PGmc Final Z Deletion, with `64` newly failing rows
- later boundary: order `46`, crossing `SC046` OE A Restoration, with `7` newly failing rows

Representative concrete failures:

- earlier: PGmc `*bárdaz` > expected OE `beard`, variant `bearda`
- earlier: PGmc `*kámbaz` > expected OE `camb`, variant `camba`
- later: PGmc `*kráftaz` > expected OE `cræft`, variant `craft`
- later: PGmc `*dágaz` > expected OE `dæġ`, variant `dag`

Caveats:

- both boundary rows are `historical_sound_change` rows rather than technical stages
- the earlier boundary is distant and very large, so it is best treated as a broad computational limit rather than as a tight local adjacency claim

## SC042 PWGmc Surviving Bimoric O Unrounding

- current order: `42`
- safe computational window: `21-42`
- earlier boundary: order `20`, crossing `SC020` PGmc Final Z Deletion, with `1` newly failing row
- later boundary: order `43`, crossing `SC043` Anglo Frisian Brightening, with `1` newly failing row

Representative concrete failure:

- PGmc `*rástōz` > expected OE `ræste`, variant `rasta`

Relation to SC043:

The later boundary is directly reciprocal with the SC043 earlier boundary. The same `rest` derivation fails on both sides, so SC042 and SC043 form a narrow local chronology constraint rather than a loose safe corridor.

## SC044 OE Breaking

- current order: `44`
- safe computational window: `44-44`
- earlier boundary: order `43`, crossing `SC043` Anglo Frisian Brightening, with `1` newly failing row
- later boundary: order `45`, crossing `SC045` OE Velar Fricative Palatalization, with `12` newly failing rows

Representative concrete failures:

- earlier: PGmc `*sláxaną` > expected OE `slēan`, variant `sleaan | slēaan`
- later: PGmc `*féxu` > expected OE `feoh`, variant `fehu`
- later: PGmc `*féxtaną` > expected OE `feohtan`, variant `fehtan`

Relation to SC043 and SC045:

SC044 is tightly pinned between the brightening stage to its left and the velar-fricative palatalization stage to its right. It cannot move across SC043 without losing the fronted input that breaking requires, and it cannot move across SC045 without losing the broken `eo`-type outputs in velar/fricative derivations.

## Cross-rule observations

The batch reinforces two reciprocal local boundaries already visible in the earlier pilot work:

1. `SC042` and `SC043` form a reciprocal boundary around `rest`
2. `SC043` and `SC044` form a reciprocal boundary around `slay`

The three batch-04 rules are not equally constrained:

- `SC041` has a broad safe window and a distant earlier boundary at `SC020`
- `SC042` has a broad earlier window but an immediate later boundary at `SC043`
- `SC044` is tightly constrained at its current slot in both directions

None of the observed boundaries in batch 04 look like mere implementation artifacts. All six first-break crossings land on `historical_sound_change` rows rather than on technical markers, support stages, or orthography/surface cleanup stages.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC041-pwgmc-final-bare-a-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC042-pwgmc-surviving-bimoric-o-unrounding.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC044-oe-breaking.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_batch_04_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Recommended next task

Run the next small manual terminal batch for:

- `SC046` OE A Restoration
- `SC050` Sievers Law Syncope
- `SC055` OE I Umlaut
- `SC059` OE Back Mutation
- `SC072` OE Unstressed Long Vowel Shortening
- `SC078` OE Weak Tail Reduction

Before running that batch, it is worth reviewing how the SC041 earlier boundary should be narrated. The result is probably useful evidence, but because the first earlier break is far away at `SC020` and produces many `-a`-final failures at once, it should be described as a broad chronology limit rather than as a narrowly local adjacency claim.
