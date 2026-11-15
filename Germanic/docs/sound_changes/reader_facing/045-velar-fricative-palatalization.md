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
trigger, yielding [feh]{.pred} from the endingless cattle input and
[fehtan]{.pred} from the fight infinitive. This is
counterbleeding protection, not direct feeding.

*hliehhan* 'laugh' is a distinct live application: after breaking,
\emph{*hleaxxjan-} still has a second fricative adjacent to \emph{j},
which becomes palatal. In the reversed order both fricatives become
palatal before breaking can apply. It must not be counted as another
instance of the nonapplication illustrated by *feoh*. The effective
\emph{h}-palatalization argument does not date every \emph{k/g}
articulation [@Hogg1979, pp.90--92; @Fulk1998, pp.145--146].

The distant *six* 'six' displacement test supplies only a broader
constraint: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut),
PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected
OE *six*. Neither test dates voiced g. Its articulation and disputed
merger are separately treated under
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].
