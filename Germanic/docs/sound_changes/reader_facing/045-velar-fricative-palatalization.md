# Velar-fricative palatalization

## SC045. Palatalization of velar fricatives beside front vowels (`OEVelarFricativePalatalization`) {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization Ctx([
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j}
]
    .o. EnglishStarAlphabet*);
```

The live population concerns voiceless x, as in *hēafod* 'head' and
*heofon* 'heaven', not voiced-fricative merger. In *feoh* 'cattle' and
*feohtan* 'fight', breaking removes the original front-vowel context:
they do not change at this rule in the live derivation. Moving the rule
before [SC044 OEBreaking](#rule-OEBreaking) instead consumes its velar
trigger, yielding [*fehu*]{.pred} and [*fehtan*]{.pred}. This is
counterbleeding protection, not direct feeding.

The distant *six* 'six' displacement test supplies only a broader
constraint: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut),
PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected
OE *six*. Neither test dates voiced g. Its articulation and disputed
merger are separately treated under
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].
