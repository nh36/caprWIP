# PWGmc final *ō-lowering before *r

### Sound-change report

#### Historical formulation

SC007 `PWGmcFinalOrLowering` isolates the lowering of final bimoric `*ō` to `*a` before word-final `*r`. In the compact trace it is concentrated in a very small witness set, above all `four` and `water`.

That narrowness matters. This is not a general long-`ō` lowering rule, but a specific final/pre-final environment whose historical value lies in a small set of well-known forms.

#### Source tradition

Ringe and Taylor state that surviving bimoric long `ō` became PWGmc `a` word-finally and before word-final `r`, and they illustrate the outcome with `four` and `water` [@RingeTaylor2014, pp. 58--59]. Fulk likewise notes that final `r` was preserved and that `ō` before it developed to `a` in West Germanic [@Fulk2018, §5.3].

That is solid support for the underlying phenomenon. It is not broad support for a large lexical class, because the historical discussion is anchored chiefly in `four`- and `water`-type material. The report should therefore remain explicit about the rule's narrow environment.

#### CAPR implementation

CAPR models the change as a single explicit environment:

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

The implementation matches the narrow final environment described in the sources. It is also the place where an older duplicated shortening treatment was consolidated in the FST comments, so the current CAPR rule should be read as a compact formalization of a very specific historical setting.

#### Place in the cascade

In the inventory ordering, SC007 follows SC006 `PWGmcEarlyIApocope` and precedes SC008 `PWGmcCoronalWAssimilation`. In the live cascade it remains inside bundled `EarlyEnglishLineChanges`, but the first-break runner can now expose it directly through the `expanded-pwgmc` order profile.

That means the rule already has a clean chronology-test path even though it remains bundled in production.

#### Order evidence

Validated order evidence now exists through the expanded-PWGmc first-break output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

The earlier search moved SC007 safely across SC006, SC005, and SC004 down to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break. That side is therefore boundary-only rather than a positive chronology constraint.

The later search does find a real historical break at order `43` across `SC043` Anglo Frisian Brightening. If PWGmc Final Or Lowering is delayed that far, PGmc `*wátōr` yields `water` rather than expected OE `wæter`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC007 works best as a narrow singleton note. The source support is real, the chronology layer now yields one usable later boundary, and the witness set is coherent even if small. That is enough for a cautious manifest-backed note, provided the report keeps the narrow environment and limited lexical base explicit.

#### Remaining cautions

The chief caution is scope. The rule is narrowly conditioned and strongly tied to the `four` and `water` evidence. The earlier side of the chronology card is also only boundary-only, while the later `SC043` relation is broad/far rather than local. Any later prose should resist turning this into a broad long-vowel chapter or implying that the small witness set supports a much larger phenomenon than the sources actually state.
