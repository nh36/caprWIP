# SC016 OE Ws Palatal Glide — chronology evidence card

## Current position
- current_order: `16`
- rule_name: `OEWsPalatalGlide`
- safe computational window: `13-16` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC016 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Ws Palatal Glide.

## Later boundary
- first later break: order `17`
- crossed stage: `SC017` NWGmc U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `yoke`
- concrete failure example: PGmc `*júką` yields expected OE `ġeoc`, but the later-shifted variant yields `ġoc`
- interpretation: SC016 can move later safely through its current order, but it cannot move later across SC017. Delaying OE Ws Palatal Glide past NWGmc U Lowering removes the expected glide-conditioned fronting in the `yoke` derivation.

## Chronology statement
Current first-break evidence places SC016 before `SC017` NWGmc U Lowering. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so no earlier historical boundary is currently identified. The later search does find a tight historical boundary at `SC017`: if OE Ws Palatal Glide is moved later than that stage, PGmc `*júką` yields `ġoc` rather than expected OE `ġeoc`. This later side reciprocates `SC017` earlier.

## Caveats
This card is one-sided in current testing because the earlier side remains runner-limited at bundled `PWGmcChanges`. The later side, however, is a tight local reciprocal boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
