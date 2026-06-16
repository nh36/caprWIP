# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise treats the development of early unstressed \emph{*o} to \emph{u} before \emph{m} as one of the important similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

That makes this a small but real unstressed-vowel development in inflectional material. The point of the section is not a broad lexical sound law. The internal CAPR label is narrower and more technical than the title used here, and the strongest evidence concerns noninitial unstressed material before final \emph{*m}.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`NWGmcAToUBeforeM`) {#rule-NWGmcAToUBeforeM}

The implementation keeps the pre-\emph{*m} raising step explicit.

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

In prose, the rule raises unstressed noninitial \emph{*a} before final \emph{*m} in ending material. It preserves a narrow morphophonological step that remains visible in the `shoulder` family, but the historical case is broader than that single compact-trace witness because the strongest support comes from inflectional endings.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, it crosses [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely and reaches order `4` with no real break, so no earlier positive boundary is yet available. If it is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*skúldramiz} yields *sċoldrum* rather than expected OE *sċuldrum*. This shows that [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering) in the modeled sequence.

The later boundary is broad and distant. It is not a local adjacency claim. The earlier side remains boundary-only, and the section should be read as a cautious inflectional sound-change note. It does not claim a broad lexical law.
