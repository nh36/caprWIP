# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57].

That historical support is real, but the witness set is small. CAPR models both coronal inputs explicitly before \emph{*w}, while the historical prose should keep the reader's attention on the narrow cluster of forms that actually supports the change.

## SC008. Assimilation of coronal consonants before \emph{*w} (`PWGmcCoronalWAssimilation`) {#rule-PWGmcCoronalWAssimilation}

The implementation keeps the coronal-w assimilation step explicit.

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

In prose, the rule assimilates coronal consonants before \emph{*w} so that the sequence behaves as \emph{*ww}. The lexical evidence is concentrated in the pathway to *fēower* ‘four’, while the pronominal material shows that the change is not confined to one isolated noun.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*fédwōr} yields *fēowwer* rather than expected OE *fēower* ‘four’. This shows that [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) must come before [SC031 OEWWSimplification](#rule-OEWWSimplification) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `four` and pronominal material places this assimilation in the same early West Germanic cluster before the later diphthongal developments.
