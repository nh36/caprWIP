# SC085 OE H Loss — chronology evidence card

## Tested sources and current candidate recheck

The original SC085-earlier measurement below was published at
`196b8f6b73d825d86830bb8612834f50f865b9e4` (25 May 2026).
The FST source at that publication has SHA256
`11ca1917c5f257b37dddc005709501f64f128bd1f6f3946844aac4dcb2766173`.
The original positions, search window and counts below belong to that
experiment, not to the current 394-row candidate.

A fresh identity and two separately compiled displacements were measured
on `4b232d22ad3d55ecf0eb2111b736dcf4349a4bde`, FST SHA256
`6b019ee2df2db8238b1ee552b249f356aec36b6c68eb37bb1a9c82ccaa272539`.
Identity toe: `*t*ā*ç*æ → *t*ā*ç*e → *t*ā*e → *t*ā → tā`.
Moving SC085 immediately before SC073 removes ç from `*t*ā*ç*æ`,
giving `*t*ā*æ`. SC073 no longer has its consonantal context; SC086
does not contract that sequence. The final is `tāæ`.
Moving SC073 immediately after SC085 was measured separately and gives
the same relevant states and final. These are toe-only displacement
probes, not a new all-corpus census or safe-window search.

The [source-pinned recheck](../../audits/sc073-085-candidate-boundary-recheck.md)
retains the complete orders, stage traces, full-composition checks and
receipts. Classification remains `technical_computational` /
`boundary_observation`; neither SC085/SC086 registry record changes.

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
The reviewed candidate keeps SC085 after SC073. Its fresh toe result `tāæ` for expected `tā`, separately substantiated above rather than inferred from the original experiment, remains only a computational boundary of its merger/loss/contraction rules. It does not independently establish historical merger before loss. If Corpus 207 *thoae* preserves distinct unstressed æ, clay instead supports loss before merger in that form; whether ae distinguishes æ from e here remains unresolved (Sweet 1885, pp. 36, 41; Ringe and Taylor 2014, p. 314, §6.9.3).

The separate SC085-before-SC086 relation is unchanged. Delaying loss past contraction yields `flēoan` rather than `flēon`, `sleaan` rather than `slēan`, `teoon` rather than `tēon`, and `tāe` rather than `tā`. This later side directly reciprocates SC086 earlier and agrees with the independently attested glossary hiatus and subsequent contraction.

## Caveats
The earlier side is a narrow computational observation in the same toe derivation as SC073 later, not a historical constraint. The later side retains the separate four-row reciprocal loss/contraction evidence. Original experiment positions, counts and outputs above remain unchanged; see [the focused follow-up](../../audits/clay-fringe-chronology-followup.md).

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
