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

Its chronology is real but one-sided. If the rule is delayed until after [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), PGmc \emph{*skḗpą} yields *sċīep* rather than expected OE *sċēap* ‘sheep’, and PGmc \emph{*jḗrą} yields *ġīer* rather than expected *ġēar* ‘year’. This shows that [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) must come before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat the lowering as the earlier stage behind the later West Saxon outputs *sċēap* and *ġēar*.
