# Order-sensitivity first-break batch 05 report

## Summary

Batch 05 interprets the next manual terminal batch after the first SC041 / SC042 / SC044 documentation pass.

- batch rules tested: `SC046`, `SC050`, `SC055`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all six directions completed: **yes**
- five directions found first breaks: **yes**
- `SC050` earlier reached runner boundary with no real break: **yes**

Files updated / created:

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC046-oe-a-restoration.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC050-sievers-law-syncope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC055-oe-i-umlaut.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_batch_05_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Method

The runner uses first-break testing: it moves one rule one slot at a time earlier or later until it reaches the first **real break**.

A real break means:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

The batch itself was run manually in a normal terminal via the manifest-driven driver. No live FST order was changed; the results come from temporary reordered variants only.

## SC046 OE A Restoration

- current order: `46`
- safe computational window: `44-47`
- earlier boundary: order `43`, crossing `SC043` Anglo Frisian Brightening, with `19` newly failing rows
- later boundary: order `48`, crossing `SC048` OE Secondary Nasalization, with `7` newly failing rows

Representative concrete failures:

- earlier: PGmc `*bákaną` > expected OE `bacan`, variant `bæcan`
- earlier: PGmc `*fáraną` > expected OE `faran`, variant `færan`
- later: PGmc `*bákaną` > expected OE `bacan`, variant `bæcan`
- later: PGmc `*wádaną` > expected OE `wadan`, variant `wædan`

Caveats:

- both observed boundaries are `historical_sound_change` rows rather than technical stages
- the immediate earlier crossing over `SC044` changes several forms but only as changed-still-passing outputs, so the first real earlier break is the next step at `SC043`

## SC050 Sievers Law Syncope

- current order: `50`
- earlier no-break-before-boundary result: no real break found down to order `13`, then runner boundary at bundled `PWGmcChanges`
- later boundary: order `52`, crossing `SC052` OE Velar Palatalization, with `1` newly failing row

Representative concrete failure for the later boundary:

- PGmc `*strákkijaną` > expected OE `streċċan`, variant `strecċan`

Caveat:

The earlier direction is bounded by the current runner limitation rather than by a detected historical break. Batch 05 therefore provides a real later boundary for SC050, but not yet a corresponding earlier historical constraint.

## SC055 OE I Umlaut

- current order: `55`
- safe computational window: `53-55`
- earlier boundary: order `52`, crossing `SC052` OE Velar Palatalization, with `2` newly failing rows
- later boundary: order `56`, crossing `SC056` OE Ws Palatal Diphthongization, with `2` newly failing rows

Representative concrete failures:

- earlier: PGmc `*kūi` > expected OE `cȳ`, variant `ċȳ`
- earlier: PGmc `*lúnganjō` > expected OE `lungen`, variant `lunġen`
- later: PGmc `*géftiz` > expected OE `ġift`, variant `ġieft`
- later: PGmc `*skáiθiz` > expected OE `sċēaþ`, variant `sċǣþ`

Relation to SC063:

SC055 is already the earlier historical boundary for `SC063` OE High Vowel Apocope. Batch 05 therefore turns SC055 from a rule inferred indirectly from the SC063 pilot into a documented node in the growing chronology network.

## Cross-rule observations

SC046 sits in the same fronting/restoration zone already exposed by `SC043`, `SC044`, and now `SC048`. Its first-break results show that restoration is locally constrained on both sides, but not so tightly that every adjacent swap is itself a real failure.

SC050 is asymmetric. The current runner finds no earlier break before the bundled `PWGmcChanges` boundary, but it does find a later historical break at `SC052`, so the current evidence is one-sided rather than fully bounded.

SC055 is tightly constrained between `SC052` on the earlier side and `SC056` on the later side. Because SC055 is also the earlier boundary for `SC063`, the chronology cards are beginning to form a network of reciprocal or near-reciprocal constraints rather than a set of isolated pairwise observations.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC046-oe-a-restoration.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC050-sievers-law-syncope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC055-oe-i-umlaut.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_batch_05_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Recommended next task

The next terminal batch can now scale beyond three rules.

**A. Conservative:** run the remaining high-priority pending rules only:

- `SC059` OE Back Mutation
- `SC072` OE Unstressed Long Vowel Shortening
- `SC078` OE Weak Tail Reduction

**B. Scaled:** run a larger 8-10 rule batch via the batch driver, centered on the same eligible corridor:

- `SC045` OE Velar Fricative Palatalization
- `SC047` OE Heavy Syllable Nasal Apocope
- `SC048` OE Secondary Nasalization
- `SC051` OE Sk Palatalization
- `SC052` OE Velar Palatalization
- `SC056` OE Ws Palatal Diphthongization
- `SC059` OE Back Mutation
- `SC072` OE Unstressed Long Vowel Shortening
- `SC078` OE Weak Tail Reduction
