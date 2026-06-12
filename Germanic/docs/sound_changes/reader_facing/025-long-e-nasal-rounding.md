# Long \emph{ē} nasal-rounding

## Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* ‘month’ and *mōna* / *mōn*-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

That is enough for a short note. The change is historically legible, but current testing does not make it a positive chronological anchor.

## SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

The implementation states the rounding step directly.

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

In prose, the rule rounds long \emph{ē} to \emph{ō} before nasals. It preserves a historically intelligible step behind month-type and moon-type outcomes without claiming more chronology than the current testing supports.

Current testing does not identify a positive historical boundary on either side. If the rule is moved earlier or later within the currently tested range, no witness word yields a historical first-break result: the earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. In reader-facing terms, this is a historically legible change whose current order evidence remains chronology-negative.
