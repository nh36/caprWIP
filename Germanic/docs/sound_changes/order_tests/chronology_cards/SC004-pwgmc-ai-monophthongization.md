# SC004 EAF Ai Monophthongization — chronology evidence card

> **Split note (SC004 Outcome-C).** SC004 is now the general/root change
> `*ai/*ái > *ā` only (Early Anglo-Frisian / North Sea Germanic). The word-final
> unstressed `*-ai > *-ē` development that the former bundled rule also packaged
> is now the separate **SC014** (see `SC014-nwgmc-unstressed-ai-monophthongization.md`
> and the component analysis in `SC004-components-chronology.md`). The empirical
> chronology below — including the SC036 `soul` boundary — belongs entirely to
> this general component; SC014 is corpus-inert and carries none of it.

## Current position
- current_order (SC id): `4`
- executable cascade position: `25` (EAF corridor, immediately after SC028 `PNWGmcPreconsonantalXLoss`)
- rule_name: `EAFAiMonophthongization`
- former_rule_name: `PWGmcAiMonophthongization` (bundled final+general rule; retained as a documented compatibility alias)
- safe computational window: `4-35` (earlier side boundary-only; later side broad/far)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at order 4`
- crossed stage: `start of tested expanded-PWGmc chain`
- crossed stage type: `tested_chain_boundary`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile begins with SC004, so the rule cannot be moved earlier within the tested chain. This is a boundary-only computational result, not an earlier historical boundary for PWGmc Ai Monophthongization.

## Later boundary
- first later break: order `36`
- crossed stage: `SC036` OE Inter Stress Raising
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `soul`
- concrete failure example: PGmc `*sáiwalō` yields expected OE `sāwol`, but the later-shifted variant yields `sāwel`
- interpretation: SC004 can move later safely through order `35`, but it cannot move later across SC036. Delaying PWGmc Ai Monophthongization that far forward leaves the wrong vowel sequence in the `soul` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC004. The earlier search stops immediately at the left edge of the tested expanded-PWGmc chain with no real break, so that side is boundary-only rather than a positive chronology constraint. The later search does find a real historical boundary at `SC036` OE Inter Stress Raising: if PWGmc Ai Monophthongization is moved later than that stage, PGmc `*sáiwalō` yields `sāwel` rather than expected OE `sāwol`. The later side is historically real but broad/far rather than a tight local adjacency claim.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it lies far to the right of the current rule and should not be narrated as a local pair. The earlier-side result predates the split: it was produced when the bundled rule opened the expanded-PWGmc chain, whereas the general component now executes at cascade position `25` in the EAF corridor. The `*ā` outcome side is what this card describes; the early word-final `*-ē` side is now SC014 and is corpus-inert, so the source imbalance the bundled card noted is resolved by the split rather than being a weakness of SC004.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`
