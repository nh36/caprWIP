# SC047 OE Heavy Syllable Nasal Apocope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `47`
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
First-break evidence places SC047 after `SC034` OE Aw Long Diphthong and before a broad later computational boundary at `SC048` OE Secondary Nasalization. On the earlier side, if OE Heavy Syllable Nasal Apocope is moved before `SC034`, PGmc `*stráwą` yields `stræw` rather than expected OE `strēaw`, because the live diphthongal development has been short-circuited. On the later side, the evidence is much broader: if SC047 is moved later than `SC048`, PGmc `*bákaną` yields `bacen` instead of `bacan`, and PGmc `*bíndaną` yields `binden` instead of `bindan`, representing a large reciprocal `-en` failure set rather than a single-example adjacency effect.

## Caveats
Both observed boundaries are historically interpretable rather than technical. The later boundary is especially broad, with 87 newly failing rows, so it should be narrated as a large computational limit rather than as a single-example adjacency claim.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`


## SC047/SC048 source-critical update,18 November2026

The current [SC047 memorandum](../audits/sc047-adjudication.md) and
[SC048 memorandum](../audits/sc048-adjudication.md) supersede earlier
interpretations, not the measurements above/below. SC047 is the
weight-independent nasal fragment of SC041's early low-vowel apocope;
SC048 is the final-n proxy for a wider historical coda-nasal domain.
The historical87 reversal is one experiment, now89 with sow/betray.
The late loss can move beside SC041 or after rhotacism without selected
endpoint changes; pre-gemination movement alone crosses other consumers.
The literal back-mutation relation still produces steolan/weofan when
nasalization is delayed, but strict separated WS clauses remove that
dependence. No independent WS historical edge follows from those words.
The wider early-coda candidate and direct blocking with strict WS triggers
both preserve394 selected outputs; source paradigm and glide limits
remain explicit. Earlier161/89 censuses,87 expectations and local
experimental prose are dated historical evidence, not current censuses.

## Corrected-control follow-up after SC059 adoption

The preceding update describes its experiment-time implementation.
SC059's separately composed WS clauses are now adopted at d83324ce;
the old delayed-nasalization steal/weave effects are absent.
The first new controlled comparison preserves all40 lowering firings
when SC017 is moved alone, and recovers all twelve changed root vowels
when it precedes pre-gemination SC047. Deer, door length and straw
remain separate endpoint differences. After ordinary final-z loss,
door still lengthens to dōr; after rhotacism or SC041 all394 outputs
are preserved. This sampled comparison is not a new first-break sweep.
The early glide candidate reaches source rīkī and rīċe but leaves
searu unresolved and changes hay/net/hue in addition to those three
dependencies. SC047 remains a late executable fragment of historically
early, weight-independent loss. See sc047-adjudication.md and
sc047-sc048-followup-evidence/README.md; original cards/tables are
preserved measurements, not current historical bounds.
