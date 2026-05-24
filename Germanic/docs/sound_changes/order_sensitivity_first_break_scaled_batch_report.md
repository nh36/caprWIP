# Order-sensitivity first-break scaled batch report

## Summary

The scaled manual terminal batch extends first-break coverage across nine additional explicit-chain rules in the mid-to-late Old English corridor.

- rules tested: `SC045`, `SC047`, `SC048`, `SC051`, `SC052`, `SC056`, `SC059`, `SC072`, `SC078`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all 18 directions completed: **yes**
- 17 directions found first breaks: **yes**
- `SC056` later reached runner boundary with no real break: **yes**

Files updated / created:

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC045-oe-velar-fricative-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC047-oe-heavy-syllable-nasal-apocope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC048-oe-secondary-nasalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC051-oe-sk-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC056-oe-ws-palatal-diphthongization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC059-oe-back-mutation.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC072-oe-unstressed-long-vowel-shortening.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC078-oe-weak-tail-reduction.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_scaled_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Method

The runner uses first-break testing: it moves one rule one slot at a time earlier or later until it reaches the first **real break**.

A real break means:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

The batch itself was run manually in a normal terminal via the manifest-driven driver. No live FST order was changed; the results come from temporary reordered variants only.

## SC045 OE Velar Fricative Palatalization

- current order: `45`
- safe computational window: `45-59`
- earlier boundary: order `44`, crossing `SC044` OE Breaking, with `12` newly failing rows
- later boundary: order `60`, crossing `SC060` OE Ws Palatal Umlaut, with `1` newly failing row

Representative concrete failures:

- earlier: PGmc `*féxu` > expected OE `feoh`, variant `fehu`
- earlier: PGmc `*féxtaną` > expected OE `feohtan`, variant `fehtan`
- later: PGmc `*séxs` > expected OE `six`, variant `sihs`

Caveats:

- the earlier side is reciprocal with the already-documented SC044 later boundary
- the later side is much narrower than the earlier side

## SC047 OE Heavy Syllable Nasal Apocope

- current order: `47`
- safe computational window: `35-47`
- earlier boundary: order `34`, crossing `SC034` OE Aw Long Diphthong, with `1` newly failing row
- later boundary: order `48`, crossing `SC048` OE Secondary Nasalization, with `87` newly failing rows

Representative concrete failures:

- earlier: PGmc `*stráwą` > expected OE `strēaw`, variant `stræw`
- later: PGmc `*bákaną` > expected OE `bacan`, variant `bacen`
- later: PGmc `*bíndaną` > expected OE `bindan`, variant `binden`

Caveats:

- the later side is extremely broad and produces a large `-en` failure set
- the later boundary is reciprocal with SC048 earlier

## SC048 OE Secondary Nasalization

- current order: `48`
- safe computational window: `48-58`
- earlier boundary: order `47`, crossing `SC047` OE Heavy Syllable Nasal Apocope, with `87` newly failing rows
- later boundary: order `59`, crossing `SC059` OE Back Mutation, with `2` newly failing rows

Representative concrete failures:

- earlier: PGmc `*bákaną` > expected OE `bacan`, variant `bacen`
- earlier: PGmc `*bíndaną` > expected OE `bindan`, variant `binden`
- later: PGmc `*stélaną` > expected OE `stelan`, variant `steolan`
- later: PGmc `*wébaną` > expected OE `wefan`, variant `weofan`

Caveats:

- the earlier side is the reciprocal partner of SC047 later and carries the same large 87-row failure set
- the later side is much narrower and links SC048 into the SC059 mutation corridor

## SC051 OE Sk Palatalization

- current order: `51`
- safe computational window: `47-55`
- earlier boundary: order `46`, crossing `SC046` OE A Restoration, with `2` newly failing rows
- later boundary: order `56`, crossing `SC056` OE Ws Palatal Diphthongization, with `5` newly failing rows

Representative concrete failures:

- earlier: PGmc `*fláskōn` > expected OE `flasce`, variant `flæsċe`
- earlier: PGmc `*wáskaną` > expected OE `wascan`, variant `wæsċan`
- later: PGmc `*skáftą` > expected OE `sċeaft`, variant `sċæft`
- later: PGmc `*skéraną` > expected OE `sċieran`, variant `sċeran`

Caveats:

- both boundaries are local and historically interpretable
- the rule sits in a dense interaction zone between SC046 and SC056

## SC052 OE Velar Palatalization

- current order: `52`
- safe computational window: `51-54`
- earlier boundary: order `50`, crossing `SC050` Sievers Law Syncope, with `1` newly failing row
- later boundary: order `55`, crossing `SC055` OE I Umlaut, with `2` newly failing rows

Representative concrete failures:

- earlier: PGmc `*strákkijaną` > expected OE `streċċan`, variant `strecċan`
- later: PGmc `*kūi` > expected OE `cȳ`, variant `ċȳ`
- later: PGmc `*lúnganjō` > expected OE `lungen`, variant `lunġen`

Caveats:

- the earlier side is reciprocal or near-reciprocal with SC050 later
- the later side is reciprocal with SC055 earlier

## SC056 OE Ws Palatal Diphthongization

- current order: `56`
- safe computational window: `56-86` (later side runner-bounded)
- earlier boundary: order `55`, crossing `SC055` OE I Umlaut, with `2` newly failing rows
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis

Representative concrete failures:

- earlier: PGmc `*géftiz` > expected OE `ġift`, variant `ġieft`
- earlier: PGmc `*skáiθiz` > expected OE `sċēaþ`, variant `sċǣþ`

Caveats:

- SC056 later is a no-break-before-boundary result, not a detected later historical boundary
- this rule therefore has one confirmed historical side and one runner-bounded side

## SC059 OE Back Mutation

- current order: `59`
- safe computational window: `49-76`
- earlier boundary: order `48`, crossing `SC048` OE Secondary Nasalization, with `4` newly failing rows
- later boundary: order `77`, crossing `SC078` OE Weak Tail Reduction, with `2` newly failing rows

Representative concrete failures:

- earlier: PGmc `*gébaną` > expected OE `ġiefan`, variant `ġeofan`
- earlier: PGmc `*stélaną` > expected OE `stelan`, variant `steolan`
- later: PGmc `*stélaną` > expected OE `stelan`, variant `steolan`
- later: PGmc `*wébaną` > expected OE `wefan`, variant `weofan`

Caveats:

- the same lexical pair (`steal`, `weave`) anchors the later side and the reciprocal SC048 later relation
- this rule bridges the mutation corridor and the late weak-tail zone

## SC072 OE Unstressed Long Vowel Shortening

- current order: `72`
- safe computational window: `65-72`
- earlier boundary: order `64`, crossing `SC064` NWGmc In Stem N Loss, with `1` newly failing row
- later boundary: order `73`, crossing `SC073` OE Unstressed AE Merger, with `24` newly failing rows

Representative concrete failures:

- earlier: PGmc `*fúrxtīnaz` > expected OE `fyrhte`, variant `fyrhten`
- later: PGmc `*nḗdrōn` > expected OE `nǣdre`, variant `nǣdræ`
- later: PGmc `*fádēr` > expected OE `fæder`, variant `fædær`

Caveats:

- the earlier side is narrow, while the later side is an immediate 24-row break
- SC072 already serves as the later historical boundary for SC063

## SC078 OE Weak Tail Reduction

- current order: `77`
- safe computational window: `71-84`
- earlier boundary: order `70`, crossing `SC070` OE Unstressed Fronting Early, with `87` newly failing rows
- later boundary: order `85`, crossing `SC086` OE Contraction, with `2` newly failing rows

Representative concrete failures:

- earlier: PGmc `*bákaną` > expected OE `bacan`, variant `bacen`
- earlier: PGmc `*bíndaną` > expected OE `bindan`, variant `binden`
- later: PGmc `*fléuxaną` > expected OE `flēon`, variant `flēoan`
- later: PGmc `*sláxaną` > expected OE `slēan`, variant `sleaan`

Caveats:

- the earlier side is very broad and should be narrated carefully as a large computational limit
- the later side is much tighter and easier to interpret locally

## Cross-rule observations

The scaled batch confirms several reciprocal or near-reciprocal local boundaries:

1. `SC044` / `SC045` now form an explicit reciprocal boundary around the `fee` / `fight` cluster.
2. `SC047` / `SC048` form a reciprocal boundary with a very large 87-row failure set dominated by spurious `-en` outputs.
3. `SC050` / `SC052` and `SC052` / `SC055` now form a linked set of reciprocal or near-reciprocal constraints around `stretch`, `cow`, and `lung`.
4. `SC055` / `SC056` form another reciprocal boundary around `gift` and `sheath`.
5. `SC063` / `SC072` are not reciprocal, but the scaled batch turns SC072 into a documented partner for the later boundary already seen from SC063.
6. `SC059` / `SC078` add a later weak-tail link to the back-mutation corridor.

The batch also sharpens the contrast between tightly pinned rules and broadly movable ones. `SC045` and `SC048` are pinned immediately on one side, while `SC059` has a broad safe window and `SC078` has a broad but still bounded earlier failure zone. `SC056` remains the clearest no-break-before-boundary case on the later side and must be handled separately in narrative synthesis.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC045-oe-velar-fricative-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC047-oe-heavy-syllable-nasal-apocope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC048-oe-secondary-nasalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC051-oe-sk-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC056-oe-ws-palatal-diphthongization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC059-oe-back-mutation.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC072-oe-unstressed-long-vowel-shortening.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC078-oe-weak-tail-reduction.md`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_scaled_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`

## Recommended next task

**Recommended: B. Pause and do a consolidation pass over all chronology cards so far.**

The TSV outputs remain clean and interpretable, but the chronology-card network is now large enough that a consolidation pass will likely pay off before another 8-10 rule batch. The most useful next synthesis tasks are: normalize phrasing across the cards, separate broad computational boundaries from narrow local adjacency claims, and make the runner-bounded no-break cases (`SC050` earlier, `SC056` later) explicit wherever they feed book-level prose.

Option A remains viable afterward: the next terminal batch could still target another 8-10 queued explicit-chain rules if the user wants to keep extending the coverage.
