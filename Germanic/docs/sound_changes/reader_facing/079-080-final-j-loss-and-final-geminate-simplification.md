# Final-j loss and final geminate simplification

## Historical discussion of final-j loss and final geminate simplification

After [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} in
heavy environments, forms such as *lungen* ‘lungs’ acquire a final geminate.
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification)
then removes the second nasal.

[SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) has a broad earlier boundary
at [SC055 OEIUmlaut](#rule-OEIUmlaut).
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is
fixed only by the final \emph{nn} outcome in the following derivation.

## SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

The rule removes \emph{*j} after the relevant heavy-syllable configurations,
after the earlier umlaut-sensitive vocalism has developed.
The affected glide is \emph{*j}.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*galáubijaną} yields [*ġelēafan*]{.pred} rather than expected OE *ġelīefan* ‘believe’, PGmc \emph{*báugijaną} yields [*bēaġan*]{.pred} rather than expected *bīeġan* ‘bow’, and PGmc \emph{*fúlgijaną} yields [*fulġan*]{.pred} rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc \emph{*lúnganjō} yields [*lungenn*]{.pred} rather than expected OE *lungen* ‘lungs’. I accordingly take [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The earlier boundary is broad, but the relation to final geminate
simplification is local.

## SC080. Simplification of final geminates (`OEFinalGeminateSimplification`) {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

The rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Moving the rule before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) makes PGmc \emph{*lúnganjō} yield [*lungenn*]{.pred} rather than expected OE *lungen* 'lungs'. These failures require [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) to follow [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
