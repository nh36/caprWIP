# Monosyllabic lengthening before final \emph{r}

The model admits Old English *þǣr* ‘there’ and *hwǣr* ‘where’ from
source-supported short-*a* antecedents. Their quantity and the date of the
lengthening remain qualified: the forms do not establish a Proto-Germanic
date, and they do not determine the order of SC015.

## SC112. Stressed monosyllabic lengthening before inherited final \emph{r} {#rule-PNWGmcMonosyllabicFinalRLengthening}

```foma
define PNWGmcMonosyllabicFinalRLengthening [
    [
        {*á} -> {*ā},
        {*é} -> {*ē},
        {*í} -> {*ī},
        {*ó} -> {*ō},
        {*ú} -> {*ū}
        || .#. EnglishStarConsonant* _ {*r} .#.
    ]
];
```

The early working placement preserves inherited final \emph{r} before
rhotacism, so secondary \emph{r} does not trigger the rule. The guard also
excludes disyllabic forms. This is a general formalization of the two
admitted witnesses, not a lexical exception list or a claim of strict
relative chronology against SC015 or SC024.
