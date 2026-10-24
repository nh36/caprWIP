# Late o-shortening

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*o} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting. The
shortened vowel is then resolved by the following medial/final distribution,
not directly as \emph{a} [@StauslandJohnsen2015, pp. 28--31].

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly).
