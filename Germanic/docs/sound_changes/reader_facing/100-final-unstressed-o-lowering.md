# Final lowering of shortened unstressed o

## SC100. Final lowering of shortened unstressed \emph{*o} (`OEFinalUnstressedOLowering`) {#rule-OEFinalUnstressedOLowering}

```foma
define OEFinalUnstressedOLowering [
    {*o} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* .#.
];
```

In a final syllable the same shortened vowel gives \emph{a}. Thus the existing
month control continues PGmc [mḗnōθz]{.recon} ‘month’ through shortened
\emph{*o} to OE [mōnaþ]{.iv lang=oe sort=monath role=evidence_form} ‘month’, while [wúndōdē]{.recon} ‘wounded’ takes
[SC099 OEMedUnstressedORaising](#rule-OEMedUnstressedORaising)
instead. The medial/final contrast and its chronology after long-vowel
shortening are Stausland Johnsen's analysis [@StauslandJohnsen2015,
pp. 28--31].
