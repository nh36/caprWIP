# SC065 OE Medial Syncope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `65`
- rule_name: `OEMedialSyncope`
- safe computational window: `13-86` (earlier side blocked; later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC065 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Medial Syncope.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC065 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence does **not** yet identify a historical first-break boundary for SC065 in either tested direction. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges`, and the later search ran safely through order `86` before stopping at the current `SC087` boundary with no real break. This card therefore records a negative computational result rather than a positive chronology constraint.

## Caveats
Both sides are boundary-limited rather than historically interpretable. This card should not be used to claim that SC065 must follow any specific earlier stage or precede `SC087`.

## Update (2026-10-29): independently demonstrated earlier boundary SC055 < SC065
The negative first-break result above predates the SC065 adjudication and
its lexical admission of *filth* (row 2335, *fūliþō > fȳlþ). That witness
independently demonstrates the ordering `SC055 OEIUmlaut < SC065
OEMedialSyncope`: syncope applied first deletes the umlaut-conditioning
\emph{*i} and yields unattested \emph{*fūlþ}. See
`Germanic/docs/sound_changes/audits/sc065-adjudication.md` (chronology
evidence, `independently_demonstrated`) and the corpus expansion receipt
`Germanic/docs/sound_changes/cascade_baseline/corpus_expansion_sc065.tsv`.
The first-break pilot summaries listed below were produced before that
admission and remain unmodified archives; they do not reflect this edge.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
