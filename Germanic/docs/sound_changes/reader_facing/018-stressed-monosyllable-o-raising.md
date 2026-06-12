# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

That is enough for a short note. The change is historically legible, but current order testing does not recover a positive chronology on either side.

## SC018. Raising of final stressed monosyllabic \emph{*ō} (`NWGmcStressedMonosyllableORaising`) {#rule-NWGmcStressedMonosyllableORaising}

The implementation keeps the monosyllabic raising step explicit.

```foma
define NWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

In prose, the rule raises final stressed monosyllabic \emph{*ō} to \emph{*ū}. It preserves a historically recognizable step behind forms such as *cū*, *hū*, and *tū*.

Current testing does not identify a positive historical boundary on either side. If the rule is moved earlier or later within the currently tested range, no witness word yields a historical first-break result: the earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. In reader-facing terms, this is a historically legible change whose current order evidence remains chronology-negative.
