# SC046 OE A Restoration — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `46`
- rule_name: `OEARestoration`
- safe computational window: `44-47`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `19`
- representative failures: `bake; fare; flask; grave; haw`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bæcan`; PGmc `*fáraną` likewise yields `færan` instead of expected `faran`
- interpretation: SC046 can move earlier safely through order `44`, but it cannot move earlier across SC043. If OE A Restoration is moved before the brightening/fronting relation has settled, the derivation leaves these forms fronted where the live order restores them to back-vowel outcomes.

## Later boundary
- first later break: order `48`
- crossed stage: `SC048` OE Secondary Nasalization
- crossed stage type: `historical_sound_change`
- failure count: `7`
- representative failures: `bake; fare; grave; lade; wade`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the later-shifted variant yields `bæcan`; PGmc `*wádaną` likewise yields `wædan` instead of expected `wadan`
- interpretation: SC046 can move later safely through order `47`, but it cannot move later across SC048. Once OE A Restoration is delayed beyond OE Secondary Nasalization, the live restored/back-vowel outcomes are lost and the same derivations surface with fronted vowels.

## Chronology statement
SC046 must follow `SC043` Anglo Frisian Brightening. If OE A Restoration is moved before that stage, PGmc `*bákaną` yields `bæcan` rather than expected OE `bacan`, and PGmc `*fáraną` yields `færan` rather than `faran`, because the rule has been moved ahead of the brightening/fronting relation that the live order subsequently restores. SC046 must also precede `SC048` OE Secondary Nasalization: if OE A Restoration is delayed beyond that stage, PGmc `*bákaną` again yields `bæcan` instead of `bacan`, and PGmc `*wádaną` yields `wædan` instead of `wadan`, so the restored back-vowel outcomes are no longer preserved.

## Caveats
Both observed boundaries are historically interpretable rather than technical. The rule is not pinned to its immediate left edge: moving SC046 one step earlier across `SC044` changes several outputs such as `feallan | fēallan`, but those remain changed-still-passing forms rather than real failures, so the first earlier historical break is the next step at SC043.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`


## Source-critical adjudication, 17 November 2026

The [SC046 memorandum](../../audits/sc046-adjudication.md) qualifies the
historical interpretation of the preserved measurements above; none of
their counts, outputs or original inputs has been regenerated or replaced.
The new source-bound observations use the SC044-certified `aea30b03`
executable and current 394-row corpus.

Brightening supplies restoration's front input in the adopted southern
account. Displacing restoration before it demonstrates that model's
feeding, not independent evidence against blocked fronting in *dagum*.
Campbell's *slēan* argument assumes front-vowel breaking; Versloot's
alternative contraction and Hogg/Fulk's Northumbrian qualification must
be considered separately.

Two local interventions are not interchangeable. Exchanging the outer
SC046/SC048 slots with SC047 left between them gives `*bakan/*wadan`
instead of `*bakąn/*wadąn`, hence *bacen/waden*: ending exposure fails,
but root restoration still applies. Fixing SC047 before both competing
operations instead compares shared `*bækan/*wædan` inputs: SC046 then
SC048 gives `*bakąn/*wadąn`; the reverse gives `*bækąn/*wædąn`,
with remainder endpoints *bæcan/wædan*. These establish a trigger/
exposure dependency of this implementation, not a universal historical
date. Exact tokenized intermediates and all output sets are in
[the initial and follow-up records](../../audits/sc046-restoration-evidence/README.md).

The SC051 boundary concerns `OESkPalatalization`, not generic stop
palatalization. Its older wash/flask measurement remains historical;
the subsequently adopted *flascan* cell must not be read as the older
levelled *flasce* experiment. No new sk displacement is claimed here.

At the original research checkpoint, the executable revision was deferred:
a blanket geminate ban fails
independent *crabba/racca* positives and trades lap for tap; a
stressed-target restriction exposes rainbow's SC059 back-mutation/
syncope interaction. The production source, inputs and 386/394 reference
remain unchanged. Source review, evidence limitations and the unapplied
restriction belong to the memorandum, not a newly inferred broad interval.

The subsequent joint adoption restricts SC046 and SC059 together, preserving
the necessary secondary annotations through SC114. Rainbow's unstressed
linker now remains *æ* at both rules and deletes by ordinary syncope.
The historical displacement counts above are unchanged and are not fresh
measurements of this adopted source. The wider weak-vowel limitation and
source-critical residues remain in the current memorandum; no new
chronology relation follows from this correction.
