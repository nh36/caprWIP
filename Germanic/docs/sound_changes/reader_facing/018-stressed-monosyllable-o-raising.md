# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

That is enough for a short note. The change is historically legible, but the tested forms do not by themselves determine a closer position for it.

## SC018. Raising of final stressed monosyllabic \emph{*ō} (`NWGmcStressedMonosyllableORaising`) {#rule-NWGmcStressedMonosyllableORaising}

The implementation keeps the monosyllabic raising step explicit.

```foma
define NWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

In prose, the rule raises final stressed monosyllabic \emph{*ō} to \emph{*ū}. It preserves a historically recognizable step behind forms such as *cū*, *hū*, and *tū*.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC018 NWGmcStressedMonosyllableORaising](#rule-NWGmcStressedMonosyllableORaising) before or after any specific neighboring change. The handbooks document the raising of stressed monosyllabic \emph{*ō} as part of the early history of long vowels, and CAPR accordingly keeps it in this early vowel section. The placement should be read as approximate, not as a local ordering forced by the tested forms.
