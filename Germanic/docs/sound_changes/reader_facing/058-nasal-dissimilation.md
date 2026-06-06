# Nasal dissimilation

## 1. Historical discussion

Luick preserves individual outcomes such as “enitre ‘einjährig (aus *anwintri)”
without isolating a separate law around them [@Luick1914, p. 166]. Campbell
likewise reaches forms such as _heofon_ in a discussion of suffixal variation
and does not set them off in any special section on nasal dissimilation [@Campbell1959,
p. 155]. Hogg mentions _heofon_ in the course of his account of back mutation,
again without isolating a separate law [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that _enetre_ reflects “loss of the second *n by
dissimilation” [@RingeTaylor2014, p. 282].

## 2. Development of the discussion

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in _enetre_. What emerges is a limited but recurring dissimilatory pattern whose scope is far
smaller than that of the major Old English vowel laws.

## 3. Formalization in the present project

The implementation isolates the change very narrowly:

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

The code targets medial `m` in a short-vowel environment before a following
syllable containing `n`, and it rewrites that `m` as `f`. This is a stricter and
more explicit formulation than the handbooks usually give. That explicitness is
useful for the implementation, but it should not be mistaken for evidence that
the traditional scholarship isolates exactly the same rule in exactly the same
shape.

## 4. Chronological placement

The current chronology evidence is negative in both directions.

When the rule is moved earlier, the present tests find no lexical breakpoint
before the inherited West-Germanic material that lies to the left of the Old
English sequence. When it is moved later, they likewise fail to identify a
narrower lexical boundary before the far right edge of the tested Old English
sequence.

No comparable pair of lexical failures fixes a narrower slot here. The present
tests do not identify sharper evidence for an earlier or later position within
the Old English sequence.

## 5. Consequences for reconstructed forms

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the _heofon_, _fæstenn_, and _enetre_ type
discussed in the literature [@Fulk2018, p. 121, §6.11; @RingeTaylor2014, p. 282;
@Campbell1959, p. 155; @Luick1914, p. 166; @Hogg1992, p. 112]. Without an
explicit rule, those outcomes would be left to diffuse analogy or to unexplained
exception lists.

The consequence is therefore modest but real. The rule marks a narrow, partly
lexicalized dissimilation tendency inside the larger Old English system. It
leaves the larger chronology largely unchanged and keeps a historically
attested type of development visible in the model.

## 6. Remaining cautions

The evidence points to a narrow dissimilatory tendency, especially in
`mn`-type clusters and a small group of lexical outcomes. There is no support
for a regular change operating across a broad phonological field. The rule is secure
enough to model, but the available tests leave its position within the Old
English sequence underdetermined.
