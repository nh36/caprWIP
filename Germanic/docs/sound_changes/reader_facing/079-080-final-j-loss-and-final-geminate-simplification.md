# Final-j loss and final geminate simplification

## Historical discussion of final-j loss and final geminate simplification

The first closing pair belongs to the late verbal and weak-tail region that follows [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction), but it is not yet the strongest center of the closing cluster. Its coherence comes from a genuine derivational interaction. Once [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} after the relevant heavy environments, forms such as *lungen* ‘lungs’ can end up with an unwanted final geminate that [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) immediately removes. That interaction is close enough to justify one shared historical discussion.

The hierarchy inside the pair is still uneven. The heavier historical load lies on [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), whose broad earlier relation reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut), while [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is the narrower follower that resolves the final \emph{nn} outcome in one sharply diagnostic derivation. The chapter therefore remains compact and explicit.

## SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

The implementation gives the \emph{*j}-loss step its own rule.

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

In prose, the rule removes \emph{*j} after the relevant heavy-syllable configurations. This is the step that lets a broad set of late verbal forms move beyond earlier umlaut-sensitive vocalism.

Its chronology is explicit on both sides. If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*galáubijaną} yields *ġelēafan* rather than expected OE *ġelīefan* ‘believe’, PGmc \emph{*báugijaną} yields *bēaġan* rather than expected *bīeġan* ‘bow’, and PGmc \emph{*fúlgijaną} yields *fulġan* rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc \emph{*lúnganjō} yields *lungenn* rather than expected OE *lungen* ‘lungs’. This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), and that [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) must come before [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The left side is broad, but the right side is sharply local. Together they explain why [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) is the stronger member of the pair.

## SC080. Simplification of final geminates (`OEFinalGeminateSimplification`) {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

In prose, the rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Its earlier boundary is the reciprocal side of the [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) relation. If the rule is moved before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), PGmc \emph{*lúnganjō} yields *lungenn* rather than expected OE *lungen*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) must come before [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

That is enough for a follower rule of this kind. It is historically useful because it prevents the unwanted final geminate from surviving, but it does not need to carry more chronology than the evidence supplies.
