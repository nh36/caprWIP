# \emph{mn}-dissimilation

## Historical discussion

The history of \emph{mn} sequences is historically legible, but the handbooks describe it more as a small descriptive pattern than as a major isolated sound change. Campbell discusses both loss of unstressed material and later assimilation in forms of this type, including the special status of *month*-type evidence [@Campbell1959, pp. 189, 195, §§470, 484].

That is enough for a short note. The change deserves explicit prose, but the current order evidence does not make it a strong chronological marker.

## SC022. Dissimilation of \emph{mn} sequences (`NWGmcMnDissimilation`) {#rule-NWGmcMnDissimilation}

The implementation keeps the dissimilation rule explicit.

```foma
define NWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _
           EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

In prose, the rule turns an earlier \emph{m} into \emph{β} when another nasal follows later in the word. It preserves a small but historically recognizable step in the prehistory of forms such as *heofon* and *month*.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC022 NWGmcMnDissimilation](#rule-NWGmcMnDissimilation) before or after any specific neighboring change. The handbooks document \emph{mn}-dissimilation as a real but limited tendency, but they do not give it a close relative chronology. CAPR therefore keeps the note here as a small early consonant adjustment. The placement should be read as approximate, not tightly fixed.
