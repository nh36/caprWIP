# SC023 NWGmc N Stem N Loss — chronology evidence card

## Current position
- current_order: `23`
- rule_name: `NWGmcNStemNLoss`
- safe computational window: `13-46` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC023 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc N Stem N Loss.

## Later boundary
- first later break: order `47`
- crossed stage: `SC047` OE Heavy Syllable Nasal Apocope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `do`
- concrete failure example: PGmc `*dōną` yields expected OE `dōn`, but the later-shifted variant yields `+?` (no output)
- interpretation: SC023 can move later safely through order `46`, but it cannot move later across SC047. Delaying NWGmc N Stem N Loss that far forward collapses the `do` derivation instead of preserving the live Old English output.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC023. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so that side remains runner-limited. The later search does find a real historical boundary at `SC047` OE Heavy Syllable Nasal Apocope: if NWGmc N Stem N Loss is moved later than that stage, PGmc `*dōną` no longer yields expected OE `dōn`, and the variant row records no output at all (`+?`).

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far across `SC047` rather than a tight local adjacency claim, and the bad outcome must be narrated as a failed derivation rather than as a competing surface form.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
