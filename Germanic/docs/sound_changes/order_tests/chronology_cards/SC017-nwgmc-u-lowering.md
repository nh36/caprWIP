# SC017 NWGmc U Lowering — chronology evidence card

## Current position
- current_order: `17`
- rule_name: `NWGmcULowering`
- safe computational window: `17-18`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `16`
- crossed stage: `SC016` OE Ws Palatal Glide
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `yoke`
- concrete failure example: PGmc `*júką` yields expected OE `ġeoc`, but the earlier-shifted variant yields `ġoc`
- interpretation: SC017 cannot move earlier across SC016. Pulling NWGmc U Lowering ahead of OE Ws Palatal Glide removes the expected glide-conditioned fronting in the `yoke` derivation.

## Later boundary
- first later break: order `19`
- crossed stage: `SC019` NWGmc Final Long O Raising
- crossed stage type: `historical_sound_change`
- failure count: `3`
- representative failures: `nose; shovel; sorrow`
- concrete failure example: PGmc `*núsō` yields expected OE `nosu`, but the later-shifted variant yields `nusu`; PGmc `*skúflō` likewise yields `sċufl` instead of expected `sċofl`; PGmc `*súrgō` yields `surg` instead of expected `sorg`
- interpretation: SC017 can move later safely through order `18`, but it cannot move later across SC019. Delaying NWGmc U Lowering past NWGmc Final Long O Raising leaves the wrong lowered-vowel outcomes in the `nose` / `shovel` / `sorrow` set.

## Chronology statement
Current first-break evidence places SC017 after `SC016` OE Ws Palatal Glide and before `SC019` NWGmc Final Long O Raising. If NWGmc U Lowering is moved before `SC016`, PGmc `*júką` yields `ġoc` rather than expected OE `ġeoc`. If it is moved later than `SC019`, PGmc `*núsō` yields `nusu` rather than `nosu`, PGmc `*skúflō` yields `sċufl` rather than `sċofl`, and PGmc `*súrgō` yields `surg` rather than `sorg`. The earlier side reciprocates `SC016` later, while the later side reciprocates `SC019` earlier. The changed-output `rust` and `wool` rows recorded in the changes TSV show nearby instability, but they do not define the boundary.

## Caveats
Both observed boundaries are historically interpretable. The later side should be narrated from the newly failing `nose` / `shovel` / `sorrow` rows, not from the changed-still-passing `rust` / `wool` context.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
