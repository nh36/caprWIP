# Long \emph{ē} nasal-rounding

## Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* ‘month’ and *mōna* / *mōn*-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

That is enough for a short note. The change is historically legible, but the tested forms do not make it a close chronological anchor.

## SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

The implementation states the rounding step directly.

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

In prose, the rule rounds long \emph{ē} to \emph{ō} before nasals. It preserves a historically intelligible step behind month-type and moon-type outcomes without claiming more chronology than the current testing supports.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC025 NWGmcLongENasalRounding](#rule-NWGmcLongENasalRounding) before or after any specific neighboring change. The handbooks document month-type and moon-type outcomes from older long \emph{ē} before nasals, but they do not give the change a close local chronology of its own. CAPR keeps the note here beside the surrounding \emph{ē}-developments for that reason. The placement should be read as approximate and source-based.
