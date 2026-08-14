# \emph{mn}-dissimilation

## Historical discussion

In the inherited \emph{n}-stem paradigm the zero-grade oblique cells brought
\emph{m} and \emph{n} into direct contact, and in that adjacent cluster the
labial nasal dissimilated to a labial spirant: \emph{mn} > \emph{βn} (surfacing
as \emph{fn}). Old Norse preserves the older paradigmatic distribution, with the
labial confined to the oblique cluster (\emph{himinn} 'heaven' beside dative
\emph{hifni}); Old English and Old Saxon generalized it. Fulk treats the cluster
change for early Germanic [@Fulk2018, §6.14, p. 121], and the relevant
\emph{heofon} 'heaven' and \emph{mōnaþ} 'month' material is discussed by Campbell
[@Campbell1959, pp. 189, 195, §§470, 484].

The pattern is historically established, but the lexical evidence does not constrain its position.

## SC022. Dissimilation of adjacent \emph{mn} (`PNWGmcMnDissimilation`) {#rule-PNWGmcMnDissimilation}

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _ {*n}
];
```

The rule fires only where \emph{m} stands directly before \emph{n}. It supplies
the labial of \emph{stefn} 'stem, trunk' from the \emph{mn}-cluster of the
\emph{stamn}-family, and it is the historical change behind the labial of
\emph{heofon} 'heaven', which was generalized from the oblique cluster into the
vowel-bearing stem before the Old English vocalic changes. (An earlier
cross-syllable formulation that labialized an intervocalic \emph{m} before a
later nasal has been retired: it simulated paradigm levelling rather than a sound
law.)

Moving [SC022 PNWGmcMnDissimilation](#rule-PNWGmcMnDissimilation) earlier or later leaves every output unchanged. Its place among the early consonantal changes rests on the handbook account of \emph{mn}-dissimilation.
