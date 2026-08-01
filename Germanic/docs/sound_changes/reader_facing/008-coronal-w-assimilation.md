# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of \emph{*dw} and \emph{*zw} to \emph{*ww} as a shared Proto-West-Germanic innovation supported by one example of each input cluster [@RingeTaylor2014, pp. 56--57; @Stiles1985, pp. 89--94]. The \emph{*dw} example is the numeral 'four': PGmc \emph{*feðwor} (Gothic \emph{fidwor}) → WGmc \emph{*fewwar} → OE \emph{fēower}, Old Frisian \emph{fiuwer}, Old Saxon \emph{fiuwar}. The \emph{*zw} example is the second-person plural pronoun, where two oblique case forms show the change: acc./dat.\ PGmc \emph{*izwiz} (Gothic \emph{izwis}) → OE \emph{eow}, Old Frisian \emph{iu}, Old Saxon \emph{iu}, OHG \emph{iu}; and gen.\ Ringe and Taylor's PGmc \emph{*izweraz} (Gothic \emph{izwara}) → OE \emph{eower}, OHG \emph{iuwer} [@RingeTaylor2014, p. 56]. Stiles discusses the same pronominal material using his own reconstruction conventions and explicitly treats Gothic \emph{izwara} among the relevant comparanda [@Stiles1985, pp. 89--94]. These two case forms belong to a single pronominal paradigm, not to two independent etyma.

The historical support rests on a small witness set. Both coronal inputs assimilate before \emph{*w}, but the evidence for each cluster is confined: the numeral alone supplies the \emph{*dw} instance, and the oblique case forms of the second-person plural pronoun supply the \emph{*zw} instance.

## SC008. Assimilation of coronal consonants before \emph{*w} (`PWGmcCoronalWAssimilation`) {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation must create \emph{*ww} while simplification can still reduce it. If [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [fédwōr]{.recon} ‘four’ yields [*fēowwer*]{.pred} rather than expected OE *fēower* ‘four’. Earlier placements alter no checked output.

The numeral fixes that relative order. The pronominal forms supply the parallel \emph{*zw} evidence; 'four' remains the sole \emph{*dw} witness and the sole source of the coronal-assimilation → *ww*-simplification ordering constraint. The earlier boundary of the assimilation remains undetermined.
