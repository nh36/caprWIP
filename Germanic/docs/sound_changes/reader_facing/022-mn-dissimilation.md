# \emph{mn}-dissimilation

## Historical discussion

The handbooks describe the history of \emph{mn} sequences as a limited
descriptive pattern. Campbell discusses both loss of unstressed material and
later assimilation in forms of this type, including the special status of
*month*-type evidence [@Campbell1959, pp. 189, 195, §§470, 484].

The pattern is historically established, but the checked forms do not constrain its position.

## SC022. Dissimilation of \emph{mn} sequences (`NWGmcMnDissimilation`) {#rule-NWGmcMnDissimilation}

```foma
define NWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _
           EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

Campbell's *heofon* and *month* material supports early \emph{m} > \emph{β}
before a later nasal, but supplies no ordering witness.

Moving [SC022 NWGmcMnDissimilation](#rule-NWGmcMnDissimilation) earlier or later leaves every checked output unchanged. Its place among the early consonantal changes rests on the handbook account of \emph{mn}-dissimilation.
