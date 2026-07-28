# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57].

The historical support rests on a small witness set. Both coronal inputs
assimilate before \emph{*w}, but only the numeral and the pronominal forms
directly support the generalization.

## SC008. Assimilation of coronal consonants before \emph{*w} (`PWGmcCoronalWAssimilation`) {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation must create \emph{*ww} while simplification can still reduce it. If [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [fédwōr]{.recon} ‘four’ yields [*fēowwer*]{.pred} rather than expected OE *fēower* ‘four’. Earlier placements alter no checked output.

The numeral fixes that relative order. The pronouns extend both input clusters beyond `four`; the earlier boundary remains undetermined.
