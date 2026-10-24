# Medial unstressed-u lowering

## SC040. Lowering of medial unstressed \emph{*u} (`OEMedUnstressedULowering`) {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

The two witnesses date medial unstressed \emph{*u} > \emph{*o} at very different scales. Before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe* ‘widow’; after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. The local *weorold* 'world' and widow evidence places lowering after combinative u-umlaut, while the youth form supplies only the distant requirement that lowering precede unstressed long-vowel shortening.
