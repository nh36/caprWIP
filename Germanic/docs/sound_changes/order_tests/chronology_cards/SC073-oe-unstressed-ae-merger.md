# SC073 OE Unstressed AE Merger — chronology evidence card

## Tested sources and current candidate recheck

The original SC073-later measurement below was published at
`25ca025f5b065671092fc8c7a4107611588cdcf9` (25 May 2026).
The FST source at that publication has SHA256
`11ca1917c5f257b37dddc005709501f64f128bd1f6f3946844aac4dcb2766173`.
The original positions, search window and counts below belong to that
experiment, not to the current 394-row candidate.

A fresh identity and two separately compiled displacements were measured
on `4b232d22ad3d55ecf0eb2111b736dcf4349a4bde`, FST SHA256
`6b019ee2df2db8238b1ee552b249f356aec36b6c68eb37bb1a9c82ccaa272539`.
Identity toe: `*t*ā*ç*æ → *t*ā*ç*e → *t*ā*e → *t*ā → tā`.
Moving SC073 immediately after SC085 instead gives
`*t*ā*ç*æ → *t*ā*æ`; both SC073 and SC086 leave that hiatus unchanged,
and the final is `tāæ`. Moving SC085 immediately before SC073 was measured
separately and gives the same relevant states and final.
These are toe-only displacement probes, not a new all-corpus displacement
census or safe-window search. The unperturbed full-corpus identity control
has 394 accepted, 385 matches, nine mismatches and zero output deltas
against the reviewed candidate.

The [source-pinned recheck](../../audits/sc073-085-candidate-boundary-recheck.md)
retains complete orders, stage traces, full-composition checks and receipts.
Classification remains `technical_computational` / `boundary_observation`.

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
The SC072-before-SC073 relation retains its existing historical evidence. Its earlier experiment, not remeasured here, gives `nǣdræ` rather than expected OE `nǣdre` and `fædær` rather than `fæder` when merger crosses shortening. The separate SC073/SC085 displacement locates a computational boundary. Both the original dated experiment and the fresh reviewed-candidate replay yield toe `tāæ` instead of `tā`; the latter's intermediates and tested source are recorded above. Neither independently establishes merger before h-loss historically.

The reader's conditional comparison remains open. If Corpus 207 *thoae* represents distinct unstressed æ, clay supports h-loss before merger in that form. If ae does not distinguish æ from e there, this spelling cannot establish their relative order (Sweet 1885, pp. 36, 41; Ringe and Taylor 2014, p. 314, §6.9.3). No opposite historical edge is adopted.

## Caveats
The earlier boundary is broad, with 24 newly failing rows, and it directly reciprocates the existing SC072 later boundary. The later side is much narrower and should be keyed to `SC085` OE H Loss as recorded in the TSV even though the variant id is `later_order_84`. Its preserved direction and one-sided experiment classification do not turn this boundary observation into a historical constraint; see [the focused follow-up](../../audits/clay-fringe-chronology-followup.md).

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
