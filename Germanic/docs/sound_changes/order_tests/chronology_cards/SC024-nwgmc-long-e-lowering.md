# SC024 NWGmc Long E1 Lowering — chronology evidence card

## Current position
- current_order: `12`
- rule_name: `PNWGmcLongELowering`
- former_rule_name: `NWGmcLongELowering`
- safe computational window: earlier side runner-bounded; later side bounded by SC025/SC101 (feeding)
- status: `adjudicated_displacement_probes` (post-split; pre-split pilot first-break results superseded)

## Earlier boundary
- first earlier break: `none found before runner boundary` (pre-split pilot ran safely down to order 13 into bundled `PWGmcChanges`; the rule now sits at order 12, at the head of the NWGmc block)
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: Not an earlier historical boundary. The historical lower bound is external to the cascade: Early Runic *mākija* (later 2nd c. AD; Grønvik 1998: 87 apud R/T 2014 p. 12) and early Proto-Scandinavian loans into Sami (Stiles 2017: 4) already show the *ā reflex.

## Later boundary
- first later break: SC025 `EAFLongANasalRounding` (order 26) and SC101 `EAFLongAFronting` (order 27), by displacement probe
- crossed stage type: `historical_sound_change` (feeding)
- failure count: `5`
- representative failures: `month; spoon; sheep; year; sleep`
- concrete failure example: PGmc `*mḗnōθz` yields expected OE `mōnaþ`, but with SC024 displaced after SC025/SC101 the cascade yields `mānaþ`; `*spḗnuz` yields `spān` for `spōn`; `*skḗpą` yields `sċāp` for `sċēap`; `*jḗrą` yields `ġār` for `ġēar`; `*slḗpaną` yields `slāpan` for `slǣpan`
- interpretation: SC024 feeds both later rules: they consume the *ā it creates (R/T's own intermediates *mānōþ-, *spānuz, p. 11). Independently demonstrated inside the model; historically the feeding is trivially real (several centuries separate the changes).

## Chronology statement
SC024 is now Change A of the *ē₁ complex: early pan-NWGmc stressed *ē₁ > *ā, unconditioned (nasal forms included), executable `{*ḗ} -> {*ā}` at order 12. Its later boundary is the pair of EAF-stage consumers SC025/SC101 (feeding, displacement-verified). The earlier side remains runner-limited in-cascade; absolute early anchoring is external (Runic/Sami evidence, 2nd–3rd c. AD).

## Caveats
The pre-split pilot first-break card (one-step *ē > *ǣ telescope, SC056 sheep/year boundary) is superseded: the sheep/year SC056 edge attaches to SC101, the rule that supplies the fronted vowel WS palatal diphthongization presupposes. Do not read the runner-limited earlier side as a positive lower boundary. Reconstruction of the intermediate value is disputed (Fulk 2018 §4.6 favors retained *ǣ); confidence B.

## Source files
- `Germanic/docs/sound_changes/audits/sc024-sc025-sc101-e1-complex-adjudication.md`
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv`
