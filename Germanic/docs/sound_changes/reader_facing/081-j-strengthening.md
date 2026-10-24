# J-strengthening after front diphthongs

## Historical discussion

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
normalizes part of the inherited intervocalic \emph{*j} domain, and
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

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [stráwjaną]{.recon} ‘strew’ yields [*strēaġan*]{.pred} rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields [*strīeian*]{.pred} rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* 'strew' derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).
