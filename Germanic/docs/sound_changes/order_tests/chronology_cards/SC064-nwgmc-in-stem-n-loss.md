# SC064 NWGmc In Stem N Loss — chronology evidence card

## Current interpretation, 8 November 2026

The measurements below are preserved original experiments, not the current
historical date. The SC064 adjudication identifies early post-PWGmc loss
after unstressed ī. SC041 exposes final n in the selected fright encoding;
SC072 preserves its long-i environment. Both are implementation visibility
bounds. The rule now follows bare-a exposure, before mutation and later
HVD. Late nētīn is outside the old law; Campbell473 attributes retained n
to inflected forms. Independent strenge/pyle controls corroborate n-loss
without an abstract-class restriction. See `audits/sc064-adjudication.md`.

## Position at experiment time
- order_at_experiment_time: `64`
- rule_name: `NWGmcInStemNLoss`
- safe computational window: `42-71`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `41`
- crossed stage: `SC041` PWGmc Final Bare A Loss
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `fright`
- concrete failure example: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the earlier-shifted variant yields `fyrhten`
- interpretation: SC064 can move earlier safely through order `42`, but it cannot move earlier across SC041. Pulling NWGmc In Stem N Loss ahead of that point preserves an unwanted nasal segment in the `fright` derivation.

## Later boundary
- first later break: order `72`
- crossed stage: `SC072` OE Unstressed Long Vowel Shortening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `fright`
- concrete failure example: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the later-shifted variant again yields `fyrhten`
- interpretation: SC064 can move later safely through order `71`, but it cannot move later across SC072. Delaying NWGmc In Stem N Loss until after OE Unstressed Long Vowel Shortening preserves the same unwanted nasal segment in the same derivation.

## Chronology statement
Current first-break evidence places SC064 after `SC041` PWGmc Final Bare A Loss and before `SC072` OE Unstressed Long Vowel Shortening. If NWGmc In Stem N Loss is moved before `SC041`, PGmc `*fúrxtīnaz` yields `fyrhten` rather than expected OE `fyrhte`; if it is moved later than `SC072`, the same PGmc input again yields `fyrhten` instead of `fyrhte`. This gives a reciprocal later boundary with the existing `SC072` earlier result and strengthens the `fright`-based chronology relation in the weak-tail corridor.

## Caveats
Both observed boundaries are historically interpretable, but the evidence is narrow and currently concentrated in the same `fright` derivation on both sides. The later side is nevertheless important because it directly reciprocates the existing SC072 earlier boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
