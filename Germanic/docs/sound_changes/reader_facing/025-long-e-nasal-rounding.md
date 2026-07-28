# Long \emph{ē} nasal-rounding

## Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* 'month' and *mōna* / *mōn* 'moon'-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

The change is historically recognizable, but the tested forms supply no close relative chronology.

## SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

Reversing [SC025 NWGmcLongENasalRounding](#rule-NWGmcLongENasalRounding) with neighboring changes leaves every checked output unchanged. Its position beside the other \emph{ē}-developments therefore follows the handbooks.
