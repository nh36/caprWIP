# Medial raising of shortened unstressed o

## SC099. Medial raising of shortened unstressed \emph{*o} (`OEMedUnstressedORaising`) {#rule-OEMedUnstressedORaising}

```foma
define OEMedUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* EnglishStarVocalic
];
```

After [SC071 OELateOShortening](#rule-OELateOShortening), the shortened vowel gives \emph{u} in an unstressed medial
syllable. The rule encodes Stausland Johnsen's statistically supported account
of West Saxon ō-verb pasts, not a general rule for inherited short \emph{*o}
or for nominal morphology [@StauslandJohnsen2015, pp. 28--31, 36]. His
diagnostic derivation is PGmc [wúndōdē]{.recon} ‘wounded’ > [wundode]{.pred}
> OE [wundude]{.iv lang=oe sort=wundude role=evidence_form} ‘wounded’ [@StauslandJohnsen2015, pp. 28--29].
