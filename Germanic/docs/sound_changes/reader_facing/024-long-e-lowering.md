# Long \emph{ē}-lowering

## Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

The change is historically recognizable, but the checked forms provide only a later boundary.

## SC024. Lowering of long \emph{ē} before non-nasal consonants (`NWGmcLongELowering`) {#rule-NWGmcLongELowering}

```foma
define NWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

After [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), long \emph{ē} > \emph{ǣ} can no longer produce the expected West Saxon forms: PGmc \emph{*skḗpą} yields [*sċīep*]{.pred} rather than OE *sċēap* ‘sheep’, and PGmc \emph{*jḗrą} yields [*ġīer*]{.pred} rather than *ġēar* ‘year’. Earlier placement changes no checked output, so [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) has a secure upper boundary.

Its lower boundary remains a matter of handbook chronology.
