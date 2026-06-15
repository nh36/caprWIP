# SC013 PWGmc Dental Hardening — chronology evidence card

## Current position
- current_order: `13`
- rule_name: `PWGmcDentalHardening`
- safe computational window: `4-86` (both directions boundary-only)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at order 4`
- crossed stage: `SC004` PWGmc Ai Monophthongization
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC013 earlier safely across SC012, SC011, SC010, SC009, SC008, SC007, SC006, SC005, and SC004 down to order `4`, but it cannot test farther because that reaches the left edge of the tested chain. This is therefore a boundary-only result rather than an earlier historical boundary for PWGmc Dental Hardening.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC013 later safely through order `86`, but it finds no later real break before the current SC087 search boundary. This is therefore a boundary-only result rather than a later historical boundary for PWGmc Dental Hardening.

## Chronology statement
Current first-break evidence does **not** identify a historical first-break boundary for SC013 in either tested direction. The earlier search moved safely down to order `4` before stopping at the left edge of the tested expanded-PWGmc chain, and the later search moved safely through order `86` before stopping at the current SC087 boundary with no real break. This card therefore records a completed negative computational result rather than a positive chronology constraint.

## Caveats
Both sides are boundary-limited rather than historically interpretable. This card should not be used to claim that SC013 must follow any specific earlier stage or precede any specific later stage, even though the source support for the historical hardening itself is strong.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv`
