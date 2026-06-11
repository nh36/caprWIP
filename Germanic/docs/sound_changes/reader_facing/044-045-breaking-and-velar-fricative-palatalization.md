# Breaking and velar-fricative palatalization

## Historical discussion of breaking and velar-fricative palatalization

These two rules belong together because the first establishes the local vocalic environment that the second must read. Breaking creates the \emph{eo}-type outputs before \emph{h}, \emph{rC}, and \emph{lC}, and the following velar-fricative palatalization then operates in that already reshaped environment. Campbell, Ringe and Taylor, and Fulk all make breaking a standard part of the post-brightening sequence, while the local fricative palatalization is historically narrower but still clear enough to stand beside it [@Campbell1959, pp. 54, 166, §§139, 405--406; @RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2; @Fulk2018, pp. 73--74, §4.13].

That interaction is close enough to justify a shared historical discussion. Even so, the hierarchy remains uneven. Breaking is the clearer handbook center, while velar-fricative palatalization is the tighter local follower whose chronology becomes especially visible through the *feoh* and *feohtan* type derivations.

## SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

The implementation keeps the breaking stage as one composed rule.

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

In prose, the rule breaks front vowels into diphthongal outcomes before the relevant consonantal environments. This is the step that yields forms such as *feoh* ‘fee’ and *feohtan* ‘fight’.

Its chronology is concrete on both sides. If the rule is moved before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. If it is delayed until after [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh* ‘fee’, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan* ‘fight’. This shows that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC044 OEBreaking](#rule-OEBreaking), and that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization).

That two-sided local seam is why [SC044 OEBreaking](#rule-OEBreaking) works so well as the main center of the pair.

## SC045. Palatalization of velar fricatives beside front vowels (`OEVelarFricativePalatalization`) {#rule-OEVelarFricativePalatalization}

The following rule handles the local fricative palatalization.

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

In prose, the rule palatalizes \emph{*x} and \emph{*ɣ} beside front vowels or before \emph{*j}. In this chapter it is the local follower to breaking, not a general article on all Old English palatalization.

Its chronology is explicit on both sides. If the rule is moved before [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan*. If it is delayed until after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc \emph{*séxs} yields *sihs* rather than expected OE *six*. This shows that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), and that [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization) must come before [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut).

The later relation to [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut) remains a cross-reference, not a reason to enlarge the chapter. The core local pair is still [SC044 OEBreaking](#rule-OEBreaking) and [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization).
