# Ij-contraction

### Sound-change report

#### Historical formulation

SC009 `PWGmcIjContraction` isolates a contraction of `*ijo` to `*iu` in the `friend` family. In the current trace and source material, that family is essentially the whole historical argument.

That narrowness is not incidental. This is exactly the kind of rule whose existence may be historically real while still being too lexically restricted to support broad generalization.

#### Source tradition

Ringe and Taylor describe a roughly similar change of `*ijo` to `*iu` in the word `friend`, giving the pathway PGmc `*frijond-` > PWGmc `*friund` > OE *friond* and related WGmc forms [@RingeTaylor2014, p. 62]. They immediately warn, however, that the word is unique: the sequence `*ijo` with stressed `*i` is so singular that it is inadvisable to attempt wider generalizations from this single history [@RingeTaylor2014, p. 62].

That is enough to justify backend documentation of the phenomenon. It is also strong reason to keep the report modest and explicit about its lexical narrowness.

#### CAPR implementation

CAPR models the contraction with an explicit environment:

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

The implementation carries a stronger general shape than the historical source base does. It should therefore be read as a CAPR formalization of a very narrow lexical development, not as a broad rule independently supported across many families.

#### Place in the cascade

In the inventory ordering, SC009 follows SC008 `PWGmcCoronalWAssimilation` and precedes SC010 `PWGmcJGemination`. In the production cascade it remains inside bundled `EarlyEnglishLineChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That means chronology testing is procedurally ready even though the historical source base remains narrow.

#### Order evidence

Validated order evidence now exists through the expanded-PWGmc first-break output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

The earlier search moved SC009 safely across SC008, SC007, SC006, SC005, and SC004 down to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break. That side is therefore boundary-only rather than a positive chronology constraint.

The later search does find a real historical break at order `32` across `SC032` OE Diphthong Leveling. If PWGmc Ij Contraction is delayed that far, PGmc `*fríjōndz` yields `friund` rather than expected OE `frēond`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC009 can now stand as a short lexical singleton note. The historical change is real enough to explain the `friend` family explicitly, and the validated chronology shows that the rule cannot simply be delayed indefinitely. The uniqueness of the `friend` family should remain part of the chapter rather than a reason to omit it.

#### Remaining cautions

The key caution is lexical uniqueness. The later `SC032` boundary is real but broad/far, while the `friend` family remains effectively the whole historical case. Any later prose should keep that family at the center and should not let CAPR's formal rule read like a major chapter-scale West Germanic vowel change.
