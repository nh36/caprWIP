# Long \emph{ē}-lowering

## Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

That is enough for a short note. The change remains historically legible, but its positive chronology points outward to a later chapter.

## SC024. Lowering of long \emph{ē} before non-nasal consonants (`NWGmcLongELowering`) {#rule-NWGmcLongELowering}

The implementation keeps the lowering step explicit.

```foma
define NWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

In prose, the rule lowers long \emph{ē} to \emph{ǣ} before non-nasal consonants. This is the earlier adjustment behind the later West Saxon outputs seen in *sċēap* and *ġēar*.

Its chronology is real but one-sided. If the rule is delayed until after [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), PGmc \emph{*skḗpą} yields *sċīep* rather than expected OE *sċēap* ‘sheep’, and PGmc \emph{*jḗrą} yields *ġīer* rather than expected *ġēar* ‘year’. This shows that [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) must come before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). If the rule is moved earlier within the currently tested range, no witness word yields a historical first-break result before the search reaches bundled earlier material, so no earlier positive boundary is yet available.

The later boundary is therefore broad and distant. The earlier side remains a search-boundary limitation, not a historical anchor.
