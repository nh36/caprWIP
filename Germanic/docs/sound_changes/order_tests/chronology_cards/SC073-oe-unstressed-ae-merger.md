# SC073 OE Unstressed AE Merger — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `73`
- rule_name: `OEUnstressedAEMerger`
- safe computational window: `73-83`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `72`
- crossed stage: `SC072` OE Unstressed Long Vowel Shortening
- crossed stage type: `historical_sound_change`
- failure count: `24`
- representative failures: `adder; earth; father; find; flask`
- concrete failure example: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the earlier-shifted variant yields `nǣdræ`; PGmc `*fádēr` likewise yields `fædær` instead of expected `fæder`
- interpretation: SC073 cannot move earlier across SC072. Moving OE Unstressed AE Merger one step earlier turns a broad set of live final `-e` outputs into merged `-æ` forms.

## Later boundary
- first later break: order `84`
- crossed stage: `SC085` OE H Loss
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `toe`
- concrete failure example: PGmc `*táixōn` yields expected OE `tā`, but the later-shifted variant yields `tāæ`
- interpretation: In the measured implementation, SC073 can move later safely through order `83`, but crossing SC085 leaves an extra final vowel in the `toe` derivation. This is a `technical_computational` / `boundary_observation` result, not independently demonstrated historical chronology.

## Chronology statement
The SC072-before-SC073 relation retains its existing historical evidence. If OE Unstressed AE Merger is moved earlier than `SC072`, PGmc `*nḗdrōn` yields `nǣdræ` rather than expected OE `nǣdre`, and PGmc `*fádēr` yields `fædær` rather than `fæder`. The separate SC073/SC085 displacement only locates a computational boundary of the current rules: moving SC073 later than SC085 yields toe `tāæ` instead of `tā`. It does not independently establish merger before h-loss historically.

The reader's conditional comparison remains open. If Corpus 207 *thoae* represents distinct unstressed æ, clay supports h-loss before merger in that form. If ae does not distinguish æ from e there, this spelling cannot establish their relative order (Sweet 1885, pp. 36, 41; Ringe and Taylor 2014, p. 314, §6.9.3). No opposite historical edge is adopted.

## Caveats
The earlier boundary is broad, with 24 newly failing rows, and it directly reciprocates the existing SC072 later boundary. The later side is much narrower and should be keyed to `SC085` OE H Loss as recorded in the TSV even though the variant id is `later_order_84`. Its preserved direction and one-sided experiment classification do not turn this boundary observation into a historical constraint; see [the focused follow-up](../../audits/clay-fringe-chronology-followup.md).

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
