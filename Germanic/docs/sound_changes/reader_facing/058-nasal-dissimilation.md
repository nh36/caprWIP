# Nasal dissimilation

## Historical discussion

Luick preserves individual outcomes such as *enetre* ‘yearling’ (with the
spelling *enitre* in his text) without isolating a separate law around them
[@Luick1914, p. 166]. Campbell likewise reaches forms such as *heofon* ‘heaven’
in a discussion of suffixal variation and does not set them off in any special
section on nasal dissimilation [@Campbell1959, p. 155]. Hogg mentions *heofon*
‘heaven’ in the course of his account of back mutation, again without isolating
a separate law [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in *enetre* ‘yearling’. What emerges is a limited but
recurring dissimilatory pattern whose scope is far smaller than that of the
major Old English vowel laws.

## SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

The implementation formalizes the change as a narrow rule applying in short
vowel environments before a following `n`.

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

In plain language, the rule turns medial `m` into `f` in a restricted
short-vowel environment before a following syllable containing `n`.

Historically, the rule captures the limited type of dissimilation reflected in
forms such as *heofon* ‘heaven’, *fæstenn* ‘fasting’, and *enetre* ‘yearling’.
It is much narrower than the major vowel changes and is best understood as a
recurring but partly lexicalized pattern.

The relation between the sources and the formalization is correspondingly close
but not exact. Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “heofon is for
older hefzen” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind as those modeled here [@Campbell1959, p. 155;
@Hogg1992, p. 112]. The formal rule is therefore narrower than the total set of
handbook remarks: it models one plausible recurrent environment and does not
claim to exhaust every dissimilatory development involving nasals.

Chronologically, the order test does not by itself determine a sharper position
within the Old English sequence. If the rule is moved earlier or later within
the tested sequence, no checked form yields a form different from the expected
one. The tested forms therefore do not place
[SC058 OENasalDissimilation](#rule-OENasalDissimilation) before or after any
specific neighboring change.

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the *heofon* ‘heaven’, *fæstenn* ‘fasting’,
and *enetre* ‘yearling’ type discussed in the literature [@Fulk2018, p. 121,
§6.11; @RingeTaylor2014, p. 282; @Campbell1959, p. 155; @Luick1914, p. 166;
@Hogg1992, p. 112]. Without an explicit rule, those outcomes would be left to
diffuse analogy or to unexplained exception lists.

The evidence points to a narrow dissimilatory tendency, especially in `mn`-type
clusters and a small group of lexical outcomes. There is no support for a
regular change operating across a broad phonological field. The rule is secure
enough to model, but the available tests leave its position within the Old
English sequence underdetermined. CAPR keeps it in this middle Old English
stretch because the relevant lexical outcomes are discussed alongside
surrounding weak-vowel and suffixal developments, not because the handbooks fix
a closer relative chronology.
