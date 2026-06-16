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

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, it crosses [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering), [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM), and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely and reaches order `4` with no real break, so no earlier positive boundary is yet available. If it is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*fédwōr} yields *fēowwer* rather than expected OE *fēower* ‘four’. This shows that [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) must come before [SC031 OEWWSimplification](#rule-OEWWSimplification) in the modeled sequence.

The later boundary is broad and distant. It is not a local adjacency claim. The earlier side remains boundary-only, and the chapter keeps the small lexical and pronominal witness set explicit while keeping the broad CAPR rule subordinate to the historical evidence.
