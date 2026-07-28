# J-strengthening, vocalization, and ei-contraction

## Historical discussion of j-strengthening, vocalization, and ei-contraction

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
vocalizes the remaining intervocalic \emph{*j}, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) removes the
resulting \emph{ei}-like sequence in weak verbal endings.

The output of each rule conditions the next.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) has local
lexical evidence on both sides;
[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
has a distant earlier boundary, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) has no
tested later boundary.

## SC081. Strengthening of \emph{*j} after front diphthongs (`OEJStrengtheningAfterFrontDiphthong`) {#rule-OEJStrengtheningAfterFrontDiphthong}

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

After the relevant front diphthongs, \emph{*j} first strengthened to a consonantal outcome; otherwise it would have vocalized too early.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*stráwjaną} yields [*strēaġan*]{.pred} rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields [*strīeian*]{.pred} rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

## SC082. Intervocalic vocalization of \emph{*j} (`OEIntervocalicJVocalization`) {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule vocalizes intervocalic \emph{*j} to \emph{*i}, creating the
\emph{ei}-like sequence later removed by
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak
verb forms.

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc \emph{*stráwjaną} yield [*strīeian*]{.pred} rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc \emph{*búrōjaną} yield [*boreian*]{.pred} rather than expected OE *borian* ‘bore’, PGmc \emph{*xándlōjaną} yield [*handleian*]{.pred} rather than expected *handlian* ‘handle’, and PGmc \emph{*mákōjaną} yield [*maceian*]{.pred} rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc \emph{*búrōjaną} yield [*boreian*]{.pred} rather than expected OE *borian*, PGmc \emph{*líznōjaną} yield [*liorneian*]{.pred} rather than expected *liornian*, and PGmc \emph{*líkkōjaną} yield [*licceian*]{.pred} rather than expected *liccian*. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
