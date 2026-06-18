# Early unstressed fronting and later o-shortening

## Historical discussion of early unstressed fronting and later o-shortening

The next pair forms a clearer local hinge. Campbell's account of shortening of unaccented long vowels is still relevant here, but the real value of the pair lies in the way the finite-state derivation separates an earlier fronting stage from a later shortening stage. Hogg, Ringe and Taylor, and Fulk all place these developments inside the same late weak-tail region in which shortening, syncope, and final-vowel adjustment continue to interact [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7].

The hierarchy inside the pair is not flat. [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) is the stronger hinge because it has an earlier and a later lexical breakpoint. [SC071 OELateOShortening](#rule-OELateOShortening) confirms the same seam from the right, but its later side remains open within the tested range. That imbalance is historically useful: it shows how the late weak tail is held together by small but concrete lexical breakpoints, not by one single undifferentiated rule.

## SC070. Early fronting of unstressed \emph{*a} (`OEUnstressedFrontingEarly`) {#rule-OEUnstressedFrontingEarly}

The implementation gives the early fronting stage its own named step.

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

In prose, the rule fronts unstressed \emph{*a} to \emph{*æ} at the point where the earlier shortening has already created a frontable vowel, but the later shortening of unstressed \emph{*ō} has not yet happened. This is the step that makes endings such as OE \emph{-en} possible in forms like *lungen* ‘lungs’.

Its chronology is explicit on both sides. If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*lúnganjō} yields *lunġen* rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc \emph{*búrōθi} yields *boreþ* rather than expected OE *boraþ* ‘bears’, and PGmc \emph{*mḗnōθz} yields *mōneþ* rather than expected *mōnaþ* ‘month’. This shows that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) must come before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), and that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC071 OELateOShortening](#rule-OELateOShortening).

That two-sided pattern is why [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) serves as the hinge of the pair. The later relation to [SC071 OELateOShortening](#rule-OELateOShortening) is the closer local result, while the earlier boundary at [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) mainly shows that this fronting belongs after the older palatal developments. CAPR keeps it here as an early stage inside the later unstressed-vowel sequence.

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

In prose, the rule shortens the remaining unstressed long \emph{*ō} after the earlier fronting stage has already done its work. This is the stage that leaves the later “stable a” endings behind forms such as OE *boraþ* ‘bears’ and *liornaþ* ‘learns’.

Its earlier boundary is the reciprocal side of the [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) relation. If the rule is moved before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc \emph{*búrōθi} yields *boreþ* rather than expected OE *boraþ*, and PGmc \emph{*líznōθi} yields *liorneþ* rather than expected *liornaþ*. No equally sharp later breakpoint appears within the tested range, so the available evidence shows only that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC071 OELateOShortening](#rule-OELateOShortening).

This one-sided profile is appropriate to the chapter. [SC071 OELateOShortening](#rule-OELateOShortening) is a real follower in the same pair, but it does not need to carry more chronology than the evidence supports.
