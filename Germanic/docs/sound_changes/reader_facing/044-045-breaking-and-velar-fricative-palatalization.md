# Breaking and velar-fricative palatalization

## Historical discussion of breaking and velar-fricative palatalization

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment, while velar-fricative palatalization follows it locally in the *feoh* and *feohtan* type derivations.

## SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Breaking must encounter the vowel created by brightening and must precede the fricative change seen in *feoh* ‘fee’ and *feohtan* ‘fight’. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan*. The two feeding relations place breaking between brightening and velar-fricative palatalization.

## SC045. Palatalization of velar fricatives beside front vowels (`OEVelarFricativePalatalization`) {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*ɣ} -> {*j} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*ɣ} -> {*j} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j},
    {*ɣ} -> {*j} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The local chronology comes from *feoh* and *feohtan*. Before [SC044 OEBreaking](#rule-OEBreaking), palatalization of \emph{*x} and \emph{*ɣ} beside front vowels or \emph{*j} makes PGmc \emph{*féxu} yield *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yield *fehtan* rather than expected *feohtan*. The distant upper limit comes from *six*: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc \emph{*séxs} yields *sihs* rather than expected OE *six*. Breaking therefore feeds velar-fricative palatalization directly, while palatal umlaut supplies only the broader upper limit.
