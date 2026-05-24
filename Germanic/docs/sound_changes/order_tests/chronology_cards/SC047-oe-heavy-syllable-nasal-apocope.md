# SC047 OE Heavy Syllable Nasal Apocope — chronology evidence card

## Current position
- current_order: `47`
- rule_name: `OEHeavySyllableNasalApocope`
- safe computational window: `35-47`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `34`
- crossed stage: `SC034` OE Aw Long Diphthong
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `straw`
- concrete failure example: PGmc `*stráwą` yields expected OE `strēaw`, but the earlier-shifted variant yields `stræw`
- interpretation: SC047 can move earlier safely through order `35`, but it cannot move earlier across SC034. Pulling heavy-syllable nasal apocope ahead of the OE Aw Long Diphthong step disrupts the live diphthongal outcome in `straw`.

## Later boundary
- first later break: order `48`
- crossed stage: `SC048` OE Secondary Nasalization
- crossed stage type: `historical_sound_change`
- failure count: `87`
- representative failures: `bake; begin; believe; bind; bore`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the later-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
- interpretation: SC047 cannot move later across SC048. Delaying heavy-syllable nasal apocope until after OE Secondary Nasalization produces a very broad set of spurious `-en` outputs across the lexicon.

## Chronology statement
SC047 must follow `SC034` OE Aw Long Diphthong. If OE Heavy Syllable Nasal Apocope is moved before that stage, PGmc `*stráwą` yields `stræw` rather than expected OE `strēaw`, because the live diphthongal development has been short-circuited. SC047 must also precede `SC048` OE Secondary Nasalization: if it is moved later than that stage, PGmc `*bákaną` yields `bacen` instead of `bacan`, and PGmc `*bíndaną` yields `binden` instead of `bindan`, showing that the live chronology avoids a broad class of spurious `-en` outcomes.

## Caveats
Both observed boundaries are historically interpretable rather than technical. The later boundary is especially broad, with 87 newly failing rows, so it should be narrated as a large computational limit rather than as a single-example adjacency claim.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
