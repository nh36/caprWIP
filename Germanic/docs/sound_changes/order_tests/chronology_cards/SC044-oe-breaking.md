# SC044 OE Breaking — chronology evidence card

## Current adjudication at integrated control 54b15a2d

The [SC044 memo](../../audits/sc044-adjudication.md) and its pinned
experiments supersede the interpretation, not the measurements, of the
pilot card below. The old card was last committed at
`16ed33ae4090390c99c5ea87e1c69b5b44fdd5e4`.

| Experiment on all 394 rows | Output-set changes | Ambiguous rows | Matches |
|---|---:|---:|---:|
| Landed control | 0 | 0 | 386 |
| Original SC044 before stressed SC043 | 29 | 29 | 385 |
| Front-only SC044 before stressed SC043 | 26 | 0 | 360 |
| Original SC044 after voiceless SC045 | 12 | 0 | 374 |
| Adopted vowel-specific repair, original order | 0 | 0 | 386 |

The early original bundle activates its back-a fallback, yielding short
and long alternatives, including before rC/lC. Only one selected match is
lost, but 29 complete output sets change. Those are different metrics.
For slay the first difference is the inserted early breaking:
`*sláxaną -> *sléaxaną | *slḗaxaną`; later h-loss leaves `*sléaan | *slḗaan`,
which the contraction rule does not collapse. The finals are
`sleaan | slēaan`. Removing the fallback isolates the conventional
stressed low-vowel feeder: early breaking leaves á, SC043 supplies æ too
late, and the final is slæan. Calf, swallow and yarn regain their control
finals in this latter experiment; that convergence does not mean their
intermediate histories were unchanged.

The later trial gives fee feh (not the older fehu), fight fehtan,
flax flæhs, knight cneht and laugh hlehhan. Fee/fight lose the effective
velar trigger to premature x→ç. In the live order é→éo instead removes
the front-vowel context while preserving x. Laugh independently changes
the second x of xxj next to j in the live order; the displaced order
changes both x's to ç before breaking.

Supported conventional precedence is stressed SC043 feeding short
æ-breaking, and breaking bleeding effective x-palatalization in the
fee/fight witnesses. Reverse registry representations are not separate
historical before-edges or independent reciprocal measurements.
Hogg1979 pp.90–92 and Fulk1998 pp.145–146 require distinguishing effective
h-palatalization from all k/g articulation. The finite early Anglian
farmjan test instead favours post-mutation rm breaking under its
reconstruction; it does not reorder the WS cascade.

## Archived pilot card (dated evidence, not current interpretation)

The following measurements and wording are retained from the old card.
Its old order numbers, vocabulary and ambiguous-output interpretation
must not be treated as a fresh experiment on 54b15a2d.

## Position at experiment time
- order_at_experiment_time: `44`
- rule_name: `OEBreaking`
- safe computational window: `44-44`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `slay`
- concrete failure example: PGmc `*sláxaną` yields expected OE `slēan`, but the earlier-shifted variant yields `sleaan | slēaan`
- interpretation: SC044 cannot move earlier across SC043. Breaking needs the fronted output created by Anglo-Frisian Brightening; if it is moved before that stage, the derivation overproduces an uncontracted broken sequence instead of the attested outcome.

## Later boundary
- first later break: order `45`
- crossed stage: `SC045` OE Velar Fricative Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `12`
- representative failures: `fee; fight; flax; knight; laugh`
- concrete failure example: PGmc `*féxu` yields expected OE `feoh`, but the later-shifted variant yields `fehu`; PGmc `*féxtaną` likewise yields `fehtan` instead of expected `feohtan`
- interpretation: SC044 cannot move later across SC045. When breaking is delayed until after velar fricative palatalization, the live `eo`-type outcomes are lost and a cluster of velar/fricative derivations surfaces with unbroken vowels.

## Chronology statement
SC044 must follow `SC043` Anglo Frisian Brightening. If OE Breaking is moved before brightening, PGmc `*sláxaną` yields `sleaan | slēaan` rather than expected OE `slēan`, because breaking is no longer acting on the properly fronted input that the live order supplies. SC044 must also precede `SC045` OE Velar Fricative Palatalization: if breaking is moved later than that stage, PGmc `*féxu` yields `fehu` instead of `feoh`, and PGmc `*féxtaną` yields `fehtan` instead of `feohtan`, showing that the breaking step has missed the velar/fricative environment it must feed in the live chronology.

## Caveats
Both observed boundaries are historically interpretable, not technical, because both crossed stages are `historical_sound_change` rows. Unlike SC041 and SC042, SC044 is tightly constrained at its current position: it breaks immediately in both directions, and the later move across SC045 produces a broader cluster of twelve real failures in velar/fricative contexts.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
