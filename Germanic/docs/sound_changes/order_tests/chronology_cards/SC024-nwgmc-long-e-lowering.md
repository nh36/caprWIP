# SC024 NWGmc Long E Lowering — chronology evidence card

## Current position
- current_order: `24`
- rule_name: `NWGmcLongELowering`
- safe computational window: `13-55` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC024 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc Long E Lowering.

## Later boundary
- first later break: order `56`
- crossed stage: `SC056` OE Ws Palatal Diphthongization
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `sheep; year`
- concrete failure example: PGmc `*skḗpą` yields expected OE `sċēap`, but the later-shifted variant yields `sċīep`; PGmc `*jḗrą` likewise yields `ġīer` instead of expected `ġēar`
- interpretation: SC024 can move later safely through order `55`, but it cannot move later across SC056. Delaying NWGmc Long E Lowering that far forward leaves unlowered high diphthong outcomes in the `sheep` and `year` derivations.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC024. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so that side remains runner-limited. The later search does find a real historical boundary at `SC056` OE Ws Palatal Diphthongization: if NWGmc Long E Lowering is moved later than that stage, PGmc `*skḗpą` yields `sċīep` rather than expected OE `sċēap`, and PGmc `*jḗrą` yields `ġīer` rather than expected `ġēar`.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far across `SC056` rather than a tight local adjacency claim; the earlier side must not be rewritten as a positive boundary because it stops at bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
