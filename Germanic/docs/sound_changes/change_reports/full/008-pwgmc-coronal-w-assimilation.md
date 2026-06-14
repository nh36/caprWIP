# Coronal-w assimilation

### Sound-change report

#### Historical formulation

SC008 `PWGmcCoronalWAssimilation` isolates the assimilation of coronal obstruents before `*w`, yielding `*ww`. In the compact trace the clearest lexical witness is `four`, while the historical discussion also depends on pronominal forms such as the plural dative and possessive `you / your`.

That makes the rule historically recognizable, but also narrow. The historical case rests on a very small number of input clusters and should be presented as such.

#### Source tradition

Ringe and Taylor call the change a shared Proto-West-Germanic innovation: the intervocalic sequences `*zw` and `*dw` were assimilated to `*ww` [@RingeTaylor2014, pp. 56--57]. Their supporting examples are PGmc `*fedwor` `four`, PGmc `*izwiz` `you (dat.pl.)`, and PGmc `*izweraz` `your (pl.)`, and they note that although there is essentially one clear lexical example of each cluster, the basic nature of the lexemes makes the change virtually certain [@RingeTaylor2014, pp. 56--57].

That is enough for a backend report. It is also a warning against overstatement: the historical support is compelling but quite concentrated.

#### CAPR implementation

CAPR models the assimilation with one formal rule covering both coronal inputs:

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

This implementation is broader than any one lexical example, but it is still directly tied to the two historically motivated cluster types recovered in the sources.

#### Place in the cascade

In the inventory ordering, SC008 follows SC007 `PWGmcFinalOrLowering` and precedes SC009 `PWGmcIjContraction`. In the production cascade it remains part of bundled `PWGmcChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That keeps the chronology path straightforward even though the live bundled cascade is unchanged.

#### Order evidence

Validated order evidence now exists through the expanded-PWGmc first-break output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

The earlier search moved SC008 safely across SC007, SC006, SC005, and SC004 down to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break. That side is therefore boundary-only rather than a positive chronology constraint.

The later search does find a real historical break at order `31` across `SC031` OE WW Simplification. If PWGmc Coronal W Assimilation is delayed that far, PGmc `*fédwōr` yields `fēowwer` rather than expected OE `fēower`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC008 works well as a narrow singleton note. The source support for the phenomenon is good, the chronology layer now yields a usable later boundary, and the pronominal support keeps the rule from collapsing into a single-example convenience. That is enough for a cautious manifest-backed note.

#### Remaining cautions

The main caution is concentration of evidence. The historical case depends on a small cluster of forms, especially `four` and the plural-pronominal material. The earlier side of the chronology card is also only boundary-only, while the later `SC031` relation is broad/far rather than local. Any later prose should keep the rule tightly bounded and should not let the broad formal implementation read as if the sources had established a much wider lexical scope.
