# SC041 PWGmc Final Bare A Loss — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `41`
- rule_name: `PWGmcFinalBareALoss`
- safe computational window: `21-45`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `20`
- crossed stage: `SC020` PGmc Final Z Deletion
- crossed stage type: `historical_sound_change`
- failure count: `64`
- representative failures: `beard; bosom; bottom; calf; coat`
- concrete failure example: PGmc `*bárdaz` yields expected OE `beard`, but the earlier-shifted variant yields `bearda`; PGmc `*kámbaz` likewise yields `camba` instead of expected `camb`
- interpretation: SC041 can move earlier safely through order `21`, but it cannot move earlier across SC020. When final bare-a loss is moved too early, the derivation leaves a wide class of spurious `-a`-final outputs that the live chronology removes only after the earlier material around final `-z` has already been dealt with.

## Later boundary
- first later break: order `46`
- crossed stage: `SC046` OE A Restoration
- crossed stage type: `historical_sound_change`
- failure count: `7`
- representative failures: `craft; dale; day; hazel; mast`
- concrete failure example: PGmc `*kráftaz` yields expected OE `cræft`, but the later-shifted variant yields `craft`; PGmc `*dágaz` likewise yields `dag` instead of expected `dæġ`
- interpretation: SC041 can move later safely through order `45`, but it cannot move later across SC046. Delaying final bare-a loss changes the environment in which OE A Restoration operates, and the variant retains back-vowel outcomes where the live order yields the attested fronted forms.

## Chronology statement
First-break evidence places SC041 after `SC020` PGmc Final Z Deletion and before `SC046` OE A Restoration. The earlier side should be treated as a broad computational boundary rather than as a tight local adjacency claim: if PWGmc Final Bare A Loss is moved before `SC020`, PGmc `*bárdaz` yields `bearda` rather than expected OE `beard`, and PGmc `*kámbaz` yields `camba` rather than `camb`, because the derivation carries final `-a` material forward across a wide stretch of the cascade. The later side remains historically interpretable as a tighter boundary: if final bare-a loss is delayed until after `SC046`, PGmc `*kráftaz` yields `craft` instead of `cræft`, and PGmc `*dágaz` yields `dag` instead of `dæġ`, so the live fronted/restored outcomes are replaced by back-vowel forms.

## Caveats
Both observed boundaries are historically interpretable, because both crossed stages are `historical_sound_change` rows rather than technical markers or surface cleanup stages. The earlier boundary is far away and produces many failures at once, so it should be described as a broad computational limit rather than as a narrow local adjacency claim.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`

## Source-critical adjudication addendum — 11 November 2026

The observations and interpretations above preserve the original experiment;
they are not rewritten as measurements of the current cascade. The current
interpretation is `audits/sc041-adjudication.md`.

The original earlier displacement changed67 outputs:64 newly failed and
buck/fowl/wolf stayed failing. In the current394-row cascade, moving SC041
immediately before current SC020 changes70 outputs,66 newly failing.
Hammer's approved cell, rust's approved input and dart's admission account
for the additional three changes. Rust is an inherited mismatch, not a new
failure caused by this adjudication. SC020's old PGmc name is historical;
its accepted present identity is unstressed West Germanic final-z loss.

The current paired shifts immediately before and immediately after SC046
give one failure (fright) and eight respectively. Their difference is
exactly the original seven restoration witnesses:
craft/dale/day/hazel/mast/staff/whale. Fright fails in both because early
SC064 received final-a, not the n exposed by live SC041. Consequently the
old21–45 safe window must not be presented as a current safe transit to
restoration; no new complete first-break sweep was performed.

The mechanisms are broad **feeding** by z-loss, **bleeding** of restoration
by removal of its back-vowel trigger, and separate **technical feeding**
of n-loss. An edge's historical-stage classification alone does not prove
historical chronology. Ringe–Taylor printed46 supports z-first by
comparative economy; Fulk25n1 provides the locally interpreted kaba/kamba
witness without universal dating. Ringe–Taylor189–190 supports the
restoration trigger. Broader oral/nasal apocope before Cj gemination
(printed44–47) is not identical to the late executable fragment.

The rule, order, selected corpus and protected baselines are retained.
The frozen new snapshots, full observations, authentic receipts and checksums
are in `audits/sc041-experiments/`; the original TSVs named above are unchanged.
