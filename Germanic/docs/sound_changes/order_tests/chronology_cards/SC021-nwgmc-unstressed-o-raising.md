# SC021 NWGmc Unstressed O Raising — chronology evidence card

## Current position
- current_order: `21`
- rule_name: `PNWGmcUnstressedORaising`
- former_rule_name: `NWGmcUnstressedORaising`
- safe computational window: `13-39` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC021 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc Unstressed O Raising.

## Later boundary
- first later break: order `40`
- crossed stage: `SC040` OE Med Unstressed U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `heaven`
- concrete failure example: PGmc `*xémonų` yields expected OE `heofon`, but the later-shifted variant yields `heofun`
- interpretation: SC021 can move later safely through order `39`, but it cannot move later across SC040. Delaying NWGmc Unstressed O Raising that far forward leaves the wrong unstressed vowel in the `heaven` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC021. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so that side remains runner-limited. The later search does find a real historical boundary at `SC040` OE Med Unstressed U Lowering: if NWGmc Unstressed O Raising is moved later than that stage, PGmc `*xémonų` yields `heofun` rather than expected OE `heofon`.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far across `SC040` rather than a tight local adjacency claim; the earlier side must not be rewritten as a positive boundary because it stops at bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
