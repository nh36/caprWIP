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

Current testing does not identify a positive historical boundary on either side. If the rule is moved earlier or later within the currently tested range, no witness word yields a historical first-break result: the earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. In reader-facing terms, this is a historically legible change whose current order evidence remains chronology-negative. The rule remains here because the handbooks treat \emph{mn}-dissimilation as a real descriptive tendency within the same early Northwest-Germanic consonant zone, even though they do not give it a closer relative chronology.
