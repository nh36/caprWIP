# Order-sensitivity first-break far-late batch report

## Summary

- rules tested: `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `16` directions completed
- `12` directions found first breaks
- `4` directions ended as no-break / boundary-limited outcomes
- later no-break searches reached the current `SC087` runner boundary for `SC080`, `SC083`, and `SC086`
- the `SC087` later search found no real break beyond current order `86` before the current runner limit

This pass creates eight new chronology cards, updates the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the far-late batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. No live FST order was changed in this pass, and no new first-break computations were run.

## Strong reciprocal chronology constraints

### SC079 OE J Loss After Heavy / SC080 OE Final Geminate Simplification

- `SC079` current order: `78`
- `SC079` earlier boundary: order `55`, crossing `SC055` OE I Umlaut
- `SC079` later boundary: order `79`, crossing `SC080` OE Final Geminate Simplification
- `SC080` earlier boundary: order `78`, crossing `SC079` OE J Loss After Heavy
- representative concrete failures:
  - PGmc `*galáubijaną` > expected OE `ġelīefan`, variant `ġelēafan`
  - PGmc `*báugijaną` > expected OE `bīeġan`, variant `bēaġan`
  - PGmc `*fúlgijaną` > expected OE `fylġan`, variant `fulġan`
  - PGmc `*lúnganjō` > expected OE `lungen`, variant `lungenn`

This pair combines a broad earlier boundary with a tight local reciprocal boundary. `SC079` cannot move earlier across `SC055` without undoing a wide swath of umlaut-sensitive outputs, but its later side is tightly pinned by `SC080` around the `lungen` / `lungenn` contrast. `SC080` confirms that same local relation from the opposite side.

### SC081 OE J Strengthening After Front Diphthong / SC082 OE Intervocalic J Vocalization

- `SC081` current order: `80`
- `SC081` earlier boundary: order `55`, crossing `SC055` OE I Umlaut
- `SC081` later boundary: order `81`, crossing `SC082` OE Intervocalic J Vocalization
- `SC082` earlier boundary: order `80`, crossing `SC081` OE J Strengthening After Front Diphthong
- representative concrete failures:
  - PGmc `*stráwjaną` > expected OE `strīeġan`, earlier variant `strēaġan`, later variant `strīeian`

This pair also combines a broad earlier side with a tight reciprocal local boundary. `SC081` reaches back to `SC055` on the earlier side, but the local relation between `SC081` and `SC082` is very tight: moving either rule across the other turns expected `strīeġan` into `strīeian`.

### SC082 OE Intervocalic J Vocalization / SC083 OE Unstressed EI Contraction

- `SC082` later boundary: order `82`, crossing `SC083` OE Unstressed EI Contraction
- `SC083` earlier boundary: order `81`, crossing `SC082` OE Intervocalic J Vocalization
- representative concrete failures:
  - PGmc `*búrōjaną` > expected OE `borian`, variant `boreian`
  - PGmc `*xándlōjaną` > expected OE `handlian`, variant `handleian`
  - PGmc `*mákōjaną` > expected OE `macian`, variant `maceian`

This is a strong reciprocal eight-row verbal boundary. The wrong forms all preserve an extra `ei`-like sequence where the live chronology expects contracted `-ian` outcomes, so the pair gives a clean constructional relation rather than just a single-example adjacency.

### SC085 OE H Loss / SC086 OE Contraction

- `SC085` earlier boundary: order `73`, crossing `SC073` OE Unstressed AE Merger
- `SC085` later boundary: order `85`, crossing `SC086` OE Contraction
- `SC086` earlier boundary: order `84`, crossing `SC085` OE H Loss
- representative concrete failures:
  - PGmc `*fléuxaną` > expected OE `flēon`, variant `flēoan`
  - PGmc `*sláxaną` > expected OE `slēan`, variant `sleaan`
  - PGmc `*téxun` > expected OE `tēon`, variant `teoon`
  - PGmc `*táixōn` > expected OE `tā`, variant `tāe`

This is another tight reciprocal local boundary. `SC085` later and `SC086` earlier produce the same four-row contraction set, while `SC085` earlier also links back to the already documented `SC073` later toe relation.

## Broad / far earlier constraints

### SC079 earlier across SC055

`SC079` earlier is historically real, but it is broad and far away rather than a tight local adjacency. Moving OE J Loss After Heavy earlier than `SC055` creates 26 newly failing rows, including PGmc `*galáubijaną` > `ġelēafan` instead of expected `ġelīefan`, PGmc `*báugijaną` > `bēaġan` instead of `bīeġan`, and PGmc `*fúlgijaną` > `fulġan` instead of `fylġan`.

### SC081 earlier across SC055

`SC081` earlier also reaches back to `SC055`, though the currently attested failure set is narrow. Moving OE J Strengthening After Front Diphthong earlier than `SC055` turns PGmc `*stráwjaną` into `strēaġan` instead of expected `strīeġan`, so this side should still be described as broad/far rather than as a local neighboring-stage boundary.

### SC087 earlier across SC044

`SC087` earlier is a real boundary, but it is far away across `SC044`. Moving OE R Metathesis earlier than OE Breaking turns PGmc `*bréstaną` into `beorstan` instead of expected `berstan`, so this side should be narrated as a broad/far computational limit rather than as a tight local adjacency claim.

## No-break / runner-bounded later outcomes

### SC080 later

- no real later break before boundary; last safe order `86`, boundary row `SC087` OE R Metathesis

This is a computational no-break result, not a claim that SC080 historically had to precede `SC087`.

### SC083 later

- no real later break before boundary; last safe order `86`, boundary row `SC087` OE R Metathesis

This is also a computational no-break result, not a positive historical adjacency claim.

### SC086 later

- no real later break before boundary; last safe order `86`, boundary row `SC087` OE R Metathesis

Again, this is a search-boundary result rather than a discovered later historical constraint.

### SC087 later

- no real later break beyond current order `86`; current runner limit reached

This is the end of the currently searchable explicit chain, not a discovered historical later boundary.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC079` / `SC080`: a tight reciprocal `lungen` / `lungenn` boundary sits inside a broader `SC079` earlier relation to `SC055`.
2. `SC081` / `SC082`: a reciprocal `strew` boundary tightens the front-diphthong / vocalization corridor.
3. `SC082` / `SC083`: an eight-row reciprocal `borian` / `boreian`-type boundary clarifies the far-late verbal contraction corridor.
4. `SC085` / `SC086`: a reciprocal four-row contraction boundary sharpens the final late-OE tail around `flēon`, `slēan`, `tēon`, and `tā`.
5. `SC085` earlier also ties neatly back into the already documented `SC073` later toe relation.
6. `SC080`, `SC083`, and `SC086` later, plus `SC087` later, all remain computational boundary observations rather than historically meaningful `SC087` adjacency claims.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_far_late_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC079-oe-j-loss-after-heavy.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC080-oe-final-geminate-simplification.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC081-oe-j-strengthening-after-front-diphthong.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC082-oe-intervocalic-j-vocalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC083-oe-unstressed-ei-contraction.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC085-oe-h-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC086-oe-contraction.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC087-oe-r-metathesis.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

The far-late batch is now interpreted, so the next terminal batch should shift back to the remaining upper-early explicit corridor:

1. `SC030` OE Au Fronting
2. `SC031` OE WW Simplification
3. `SC032` OE Diphthong Leveling
4. `SC033` OE Ew Long Diphthong
5. `SC034` OE Aw Long Diphthong
6. `SC035` OE Prefix A Reduction Early
7. `SC036` OE Inter Stress Raising
8. `SC037` OE Compound Linking Syncope
9. `SC039` OE WI Combinative U Umlaut
10. `SC040` OE Med Unstressed U Lowering

That ten-rule set fills the upper-early gap immediately below the completed `SC041` region without reopening the already interpreted far-late corridor.
