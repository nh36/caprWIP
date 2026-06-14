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

No validated chronology card exists yet for SC008. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC008 resolves as the fifth rule in that expanded profile.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should be claimed.

#### Interpretation

SC008 is a narrow backend singleton candidate. The source support for the phenomenon is good, but the number of core historical examples is very small. That makes the rule appropriate for backend preparation, but still too thin to stand alone as a fully anchored historical note in the absence of validated chronology output.

#### Remaining cautions

The main caution is concentration of evidence. The historical case depends on a small cluster of forms, especially `four` and the plural-pronominal material. Any later prose should keep the rule tightly bounded and should not let the broad formal implementation read as if the sources had established a much wider lexical scope.
