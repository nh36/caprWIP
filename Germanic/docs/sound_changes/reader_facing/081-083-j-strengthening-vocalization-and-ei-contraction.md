# J-strengthening, vocalization, and ei-contraction

## Historical discussion of j-strengthening, vocalization, and ei-contraction

The middle closing sequence is technically tighter than the opening pair, but it is also more internally uneven. Its real center is [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) prepares the consonantal stage that the later vocalization must not erase too early, and [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) then removes the extra \emph{ei}-like sequence that would otherwise survive too long in the resulting weak verbal endings.

That hierarchy is historically meaningful. The three rules form one local chain because the output of each immediately conditions the next, but the chain is not flat. [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is the strongest member because it has the clearest local evidence on both sides, while [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) is the broad earlier flank and [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) is the one-sided follower on the right.

## SC081. Strengthening of \emph{*j} after front diphthongs (`OEJStrengtheningAfterFrontDiphthong`) {#rule-OEJStrengtheningAfterFrontDiphthong}

The implementation keeps the strengthening step as one explicit rule.

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

In prose, the rule keeps \emph{*j} as a strengthened consonantal outcome after the relevant front diphthongs and so prevents too-early vocalization.

Its chronology is explicit on both sides. If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*stráwjaną} yields *strēaġan* rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields *strīeian* rather than *strīeġan*. This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong), and that [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) must come before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The left side is broad and far, but the right side is a sharp local seam in the *strīeġan* derivation.

## SC082. Intervocalic vocalization of \emph{*j} (`OEIntervocalicJVocalization`) {#rule-OEIntervocalicJVocalization}

The implementation then turns the consonantal \emph{*j} into a vocalic outcome between vowels.

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

In prose, the rule vocalizes intervocalic \emph{*j} to \emph{*i}. This is the step that creates the extra \emph{ei}-like sequence later removed by [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak verb forms.

Its chronology is concrete on both sides. If the rule is moved before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong), PGmc \emph{*stráwjaną} yields *strīeian* rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction), PGmc \emph{*búrōjaną} yields *boreian* rather than expected OE *borian* ‘bore’, PGmc \emph{*xándlōjaną} yields *handleian* rather than expected *handlian* ‘handle’, and PGmc \emph{*mákōjaną} yields *maceian* rather than expected *macian* ‘make’. This shows that [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) must come before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), and that [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) must come before [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

That two-sided local seam is why [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is the center of the three-rule chain.

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

In prose, the rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Its earlier boundary is the reciprocal side of the [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) relation. If the rule is moved before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), PGmc \emph{*búrōjaną} yields *boreian* rather than expected OE *borian*, PGmc \emph{*líznōjaną} yields *liorneian* rather than expected *liornian*, and PGmc \emph{*líkkōjaną} yields *licceian* rather than expected *liccian*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) must come before [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

That one-sided profile is appropriate to the right follower in this chain. The rule is historically real, but it does not need to carry a stronger later boundary than the evidence provides.
