# Order-sensitivity first-break early-corridor batch report

## Summary

- rules tested: `SC014`, `SC015`, `SC016`, `SC017`, `SC018`, `SC019`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `12` directions completed
- `6` directions found historically interpretable first breaks
- `0` directions found non-historical computational first breaks
- `6` directions ended as runner-limited / no-break outcomes

This pass creates six new chronology cards, adds the early corridor to the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the committed early-corridor batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. Earlier searches that stop at bundled `PWGmcChanges` are treated as runner-limited rather than as ordinary historical boundaries, and later searches that reach the current `SC087` boundary with no real break are treated as no-break computational outcomes rather than as historical claims about `SC087`. Variant outputs written as `+?` are treated here as no-output / failed derivations, not as surface Old English forms.

## Clean reciprocal historical constraints

### SC016 OE Ws Palatal Glide / SC017 NWGmc U Lowering

- `SC016` current order: `16`
- `SC016` later boundary: order `17`, crossing `SC017` NWGmc U Lowering
- `SC017` current order: `17`
- `SC017` earlier boundary: order `16`, crossing `SC016` OE Ws Palatal Glide
- representative concrete failure:
  - PGmc `*júką` > expected OE `ġeoc`, variant `ġoc`

This is the cleanest new local early-corridor reciprocal pair. Delaying `SC016` across `SC017`, or pulling `SC017` earlier across `SC016`, breaks the same `yoke` derivation in the same way. The pair therefore gives a tight local chronology relation immediately above the runner-limited pre-`SC014` edge.

### SC017 NWGmc U Lowering / SC019 NWGmc Final Long O Raising

- `SC017` later boundary: order `19`, crossing `SC019` NWGmc Final Long O Raising
- `SC019` earlier boundary: order `17`, crossing `SC017` NWGmc U Lowering
- representative concrete failures:
  - PGmc `*núsō` > expected OE `nosu`, variant `nusu`
  - PGmc `*skúflō` > expected OE `sċofl`, variant `sċufl`
  - PGmc `*súrgō` > expected OE `sorg`, variant `surg`
- changed-output context that does **not** define the boundary:
  - PGmc `*rústō` (`rust`)
  - PGmc `*wúllō` (`wool`)

This is the main reciprocal network effect from the batch. Delaying `SC017` across `SC019`, or pulling `SC019` earlier across `SC017`, breaks the same `nose` / `shovel` / `sorrow` set in the same way. The accompanying `rust` and `wool` changed-still-passing rows show nearby instability, but they do not define the boundary.

### SC019 NWGmc Final Long O Raising / SC020 PGmc Final Z Deletion

- `SC019` later boundary: order `20`, crossing `SC020` PGmc Final Z Deletion
- already interpreted reciprocal side: `SC020` earlier boundary at order `19`, crossing `SC019`
- representative concrete failure:
  - PGmc `*rástōz` > expected OE `ræste`, variant `rast`

This is a clean near-reciprocal handoff between the newly interpreted early corridor and the already interpreted lower-early corridor. Moving `SC019` later than `SC020`, or moving `SC020` earlier than `SC019`, breaks the same `rest` derivation, so the pair now gives a tight anchor across the `SC019` / `SC020` boundary.

## One-sided historical constraints

### SC015 NWGmc I Lowering

`SC015` currently has one historically interpretable side. No earlier real break was found before the runner entered bundled `PWGmcChanges`, but moving `SC015` later than `SC036` OE Inter Stress Raising turns PGmc `*wír-àldu` into `wuruld` instead of expected OE `weorold`. This later side is historically real, but broad/far across `SC036` rather than local.

## Negative / runner-limited / no-break outcomes

### Earlier runner-limited sides at bundled PWGmcChanges

The earlier searches for `SC014`, `SC015`, `SC016`, and `SC018` all ran safely down to order `13` before the runner entered bundled `PWGmcChanges`. None of those earlier sides should be rewritten as ordinary historical boundaries.

### Negative / boundary cards: SC014 and SC018

`SC014` and `SC018` are pure negative / boundary cards in the current searchable corridor. On the earlier side, each search stops at bundled `PWGmcChanges` with no real break. On the later side, each search runs through order `86` with no real break before the current `SC087` boundary. These cards therefore record the present search limits rather than positive chronology constraints.

### Later no-break-before-boundary outcomes

The later searches for `SC014` and `SC018` found no real break before the current `SC087` boundary. Those are computational observations only. They must not be rewritten as claims that either rule historically must precede `SC087`.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC016` / `SC017`: a clean reciprocal `yoke` boundary now anchors the lower edge of the explicit early corridor.
2. `SC017` / `SC019`: the `nose` / `shovel` / `sorrow` evidence now gives a broader reciprocal early-vocalism relation, with `rust` and `wool` preserved as changed-still-passing context rather than boundary-defining failures.
3. `SC019` / `SC020`: the `rest` derivation now provides a tight bridge from the early corridor into the already interpreted lower-early corridor.
4. `SC015` remains historically informative on only one side, and that side is broad/far across `SC036` rather than a local neighboring-stage constraint.
5. `SC014` and `SC018` remain genuinely negative cards: the current searchable corridor does not yet yield a historical first break for them in either direction.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_early_corridor_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC014-nwgmc-unstressed-ai-monophthongization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC015-nwgmc-i-lowering.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC016-oe-ws-palatal-glide.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC017-nwgmc-u-lowering.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC018-nwgmc-stressed-monosyllable-o-raising.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC019-nwgmc-final-long-o-raising.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

All currently queued explicit-chain early, lower-early, upper-early, late-corridor, and far-late rules in `next_batch_candidates.tsv` are now interpreted. If further first-break coverage is wanted, the next step is no longer another ordinary contiguous explicit-chain batch; it is either consolidation of the current chronology corpus or runner work that reaches earlier bundled-stage / non-explicit positions such as `PWGmcChanges`.
