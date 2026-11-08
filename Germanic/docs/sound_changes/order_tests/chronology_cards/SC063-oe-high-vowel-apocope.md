# SC063 OE High Vowel Apocope — chronology evidence card

## Quantitative follow-up, 8 November 2026

The preserved displacement measurements below belong to the earlier
final-only implementation. SC063 now owns unified quantitative HVD,
retaining HLL but deleting a medial short high vowel before a heavy
following syllable. Selected filth/spindle still establish mutation
before loss and loss before degemination. Final/medial quantity is
independently tested by nēten/nētenu/nētna; the earlier SC064 law no
longer damages late nētīn. See `audits/sc063-adjudication.md`.

## Consolidated current interpretation

See `audits/sc065-adjudication.md`: the conventional account now retains a
final high vowel after a heavy first plus light second syllable. The heads
control and Fulk/Ringe--Taylor alternatives are distinguished; the two former
nominatives are comparisons, not current selections. All original experiment
positions and results below remain unchanged records.

## Position at experiment time
- order_at_experiment_time: `63`
- rule_name: `OEHighVowelApocope`
- safe computational window: `56-71`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `19`
- representative failures: `belly; birth; breeches; bride; cow`
- concrete failure example: PGmc `*kūi` yields expected OE `cȳ`, but the earlier-shifted variant yields `cū`; PGmc `*brūdiz` likewise yields `brūd` instead of expected `brȳd`
- interpretation: SC063 can move earlier safely through order `56`, but it cannot move earlier across SC055. The boundary is historically interpretable: if the final high vowel is deleted before OE i-umlaut runs, the umlaut trigger is lost and a large set of baseline-matching fronted outcomes collapses.

## Later boundary
- first later break: order `72`
- crossed stage: `SC072` OE Unstressed Long Vowel Shortening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `fright`
- concrete failure example: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the later-shifted variant yields `fyrht`
- interpretation: SC063 can move later safely through order `71`, but it cannot move later across SC072. Once unstressed long-vowel shortening has moved ahead of apocope, the derivation drops the final vowel too late and the expected weak-tail output is no longer preserved.

## Chronology statement
SC063 must follow `SC055` OE I Umlaut. If high-vowel apocope is moved before i-umlaut, PGmc `*kūi` yields `cū` rather than expected OE `cȳ`, because the final high vowel has been removed before it can condition umlaut; the same earlier shift turns PGmc `*brūdiz` into `brūd` instead of `brȳd`. SC063 must also precede `SC072` OE Unstressed Long Vowel Shortening: if apocope is moved later than that shortening stage, PGmc `*fúrxtīnaz` yields `fyrht` instead of `fyrhte`, so the live weak-tail chronology is lost.

## Caveats
Both observed boundaries are historically interpretable rather than merely technical. The adjacent technical / support crossings that sit closest to SC063 did **not** themselves trigger the boundary: the rule moves safely across `SC062` OE Weight Markers and across `SC064` NWGmc In Stem N Loss before the first real failures appear. The earlier break also has one changed-still-failing row, PGmc `*fūri`, which shifts from baseline `fȳr` to variant `fūr`; that row does not define the stopping condition because the baseline already missed expected `fȳre`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_pilot_03_report.md`
