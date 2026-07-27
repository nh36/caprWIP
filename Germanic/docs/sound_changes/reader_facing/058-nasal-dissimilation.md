# Nasal dissimilation

## Historical discussion

Most accounts introduce nasal dissimilation to explain individual forms rather
than as a regular sound law. Luick records *enetre* ‘yearling’ (spelled
*enitre* in his text) [@Luick1914, p. 166]; Campbell discusses *heofon*
‘heaven’ with suffixal variation [@Campbell1959, p. 155]; and Hogg encounters
the same form while treating back mutation [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The disagreement concerns scope. Fulk's formulation recognizes a recurrent but
irregular development in `mn`; the remaining discussions stay with particular
lexical outcomes. None warrants a sound law comparable in scope to the major
Old English vowel changes.

## SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

I adopt a narrower environment than the handbook observations might suggest.
Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “*heofon* is for
older *hefzen*” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind [@Campbell1959, p. 155;
@Hogg1992, p. 112]. The short-vowel environment adopted here covers a recurrent
subset of these outcomes, not every dissimilatory development involving nasals.

No witness word fixes the position of nasal dissimilation within the Old
English sequence. Reversing its order with any tested neighbor leaves every
checked output unchanged. A more precise relative chronology would therefore
require lexical evidence not represented here.
