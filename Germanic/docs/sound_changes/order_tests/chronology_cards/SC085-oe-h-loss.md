# SC085 OE H Loss — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `84`
- rule_name: `OEHLoss`
- safe computational window: `74-84`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `73`
- crossed stage: `SC073` OE Unstressed AE Merger
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `toe`
- concrete failure example: PGmc `*táixōn` yields expected OE `tā`, but the earlier-shifted variant yields `tāæ`
- interpretation: In the measured implementation, SC085 can move earlier safely through order `74`, but crossing SC073 leaves an extra final vowel in the `toe` derivation. This reciprocates the SC073 later observation and is classified `technical_computational` / `boundary_observation`, not independently demonstrated historical chronology.

## Later boundary
- first later break: order `85`
- crossed stage: `SC086` OE Contraction
- crossed stage type: `historical_sound_change`
- failure count: `4`
- representative failures: `flee; slay; ten; toe`
- concrete failure example: PGmc `*fléuxaną` yields expected OE `flēon`, but the later-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`; PGmc `*téxun` yields `teoon` instead of `tēon`; PGmc `*táixōn` yields `tāe` instead of `tā`
- interpretation: SC085 can move later safely through its current order, but it cannot move later across SC086. Delaying OE H Loss past OE Contraction leaves over-long vocalic sequences in four late derivations.

## Chronology statement
The current cascade keeps SC085 after SC073, but the toe result `tāæ` for expected `tā` is only a computational boundary of its merger/loss/contraction rules. It does not independently establish historical merger before loss. If Corpus 207 *thoae* preserves distinct unstressed æ, clay instead supports loss before merger in that form; whether ae distinguishes æ from e here remains unresolved (Sweet 1885, pp. 36, 41; Ringe and Taylor 2014, p. 314, §6.9.3).

The separate SC085-before-SC086 relation is unchanged. Delaying loss past contraction yields `flēoan` rather than `flēon`, `sleaan` rather than `slēan`, `teoon` rather than `tēon`, and `tāe` rather than `tā`. This later side directly reciprocates SC086 earlier and agrees with the independently attested glossary hiatus and subsequent contraction.

## Caveats
The earlier side is a narrow computational observation in the same toe derivation as SC073 later, not a historical constraint. The later side retains the separate four-row reciprocal loss/contraction evidence. Original experiment positions, counts and outputs above remain unchanged; see [the focused follow-up](../../audits/clay-fringe-chronology-followup.md).

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
