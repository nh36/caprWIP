# Postvelar labial loss

## SC053. Postvelar labial loss (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

```foma
define OEPostVelarWLoss Ctx([
    {*w} -> 0 || {*n} {*g} _,
                EnglishStarVocalic [{*x}|{*ç}] _ EnglishStarVocalic
]);
```

West Germanic resolved inherited unit labiovelars into a dorsal plus a glide. The later English loss of the glide after a noninitial dorsal accounts both for \emph{*singwan} > *singan* 'sing' and for the labial-less stage of \emph{*sehwan} > \emph{*seohan} > *sēon* 'see'. In ‘see’, the first loss leaves a dorsal, whose subsequent intervocalic deletion belongs to [SC085 OEHLoss](#rule-OEHLoss). The final contraction is another operation. The voiced comparison *sewen* 'seen' lacks a voiceless dorsal before *w* and is not an exception [@RingeTaylor2014, pp. 48–50, 178, 214–215, 315–317, 344–345; @Campbell1959, pp. 186–187].

The hard stop of *þicce* 'thick' supplies the independent argument for retaining the labial during [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization); the written geminate in this word is a stop, not a witness to the exact date of loss after a fricative. The implementation uses the same post-palatalization slot for the two environments. It does not infer a date from the earlier successful computational insertion. The singleton-fricative environment accepts the two executable articulations of the voiceless singleton, but not a voiced consonant, a geminate or a word edge [@RingeTaylor2014, pp. 49–50, 214–215].

The whole simplex infinitive of ‘see’ reaches \texttt{*s*éo*x*w*ą*n} in the compatibility cascade; this rule yields \texttt{*s*éo*x*ą*n}. The later loss of the dorsal leaves hiatus: the current transducers give [*seoan*]{.pred}, not the attested *sēon* 'see'. The related ‘lend’ and ‘filter’ histories support the same separation. The selected *sēoh* 'strain!' has a final dorsal and no medial labial for this rule to remove; the model keeps that dorsal in [*sīoh*]{.pred}. In contrast, the derived *seohhe* 'strainer' preserves a geminate dorsal after the labial is lost. That family supports the distinction in dorsal quantity but does not independently date fricative-geminate delabialization. The geminate extension is not implemented [@RingeTaylor2014, pp. 49, 178–179; @Seebold1970, pp. 327–328, 389–390; @Campbell1959, p. 187].
