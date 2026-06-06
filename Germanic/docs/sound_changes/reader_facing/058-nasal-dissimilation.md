# Nasal dissimilation

## 1. Historical discussion

This is not a chapter-sized textbook sound law. The strongest newer
English-language formulation recovered in the local sources is Fulk's cautious
statement: “In the cluster mn, the first consonant tends to lose its nasality
by dissimilation, though the results are hardly regular”
[@Fulk2018, p. 121, §6.11].
That is already a warning about scale: the phenomenon is real, but not neat or
uniform.

The older German material is thinner and more lexical. Luick preserves outcomes
such as “enitre ‘einjährig (aus *anwintri)” rather than building a separate
chapter around them [@Luick1914, p. 166]. Campbell and Hogg likewise reach
forms such as _heofon_ in other discussions without isolating a major Old
English “nasal-dissimilation” law [@Campbell1959, p. 155; @Hogg1992, p. 112].

The historical discussion must therefore begin by lowering expectations. The
change belongs in the book because the sources preserve scattered evidence for
the pattern, not because the handbooks present it as a major canonical law.

## 2. Comparison of the traditions

The contrast between traditions is instructive.

Newer English-language scholarship, especially Fulk, is willing to formulate a
general tendency in `mn` clusters, while immediately warning that the results
are irregular [@Fulk2018, p. 121, §6.11]. Ringe and Taylor are more lexical
still: their clearest direct statement is simply that *enetre* reflects “loss of
the second *n by dissimilation” [@RingeTaylor2014, p. 282]. The older German tradition,
represented here by Luick, preserves useful lexical traces but does not make
them into a chapter heading [@Luick1914, p. 166].

That comparison is the right historical scale for the present section. The rule
is not fictitious, but it is better treated as a residual pattern than as a
large named law comparable to i-umlaut or breaking.

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

That means the chapter cannot be written like the stronger pilot cases. There is
no _stretch_, _cow_, or _gift_-style failure here to prove a narrow local slot.
The honest statement is simpler: the search found **no lexical evidence for a
narrower earlier or later boundary** within the tested window.

## 5. Consequences for reconstructed forms

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the _heofon_, _fæstenn_, and _enetre_ type
discussed in the literature [@Fulk2018, p. 121, §6.11; @RingeTaylor2014, p. 282;
@Campbell1959, p. 155; @Luick1914, p. 166; @Hogg1992, p. 112]. Without an
explicit rule, those outcomes would be left to diffuse analogy or to unexplained
exception lists.

The consequence is therefore modest but real. The rule marks a narrow, partly
lexicalized dissimilation tendency inside the larger Old English system. It does
not reorganize the whole chronology, but it keeps a historically attested type
of development visible in the model.

## 6. Remaining cautions

This section should stay short.

The literature does not justify treating nasal dissimilation as a chapter center
of the same rank as the major textbook sound laws. Nor do the present tests
justify a narrow slot fixed by lexical breakpoints on both sides. The right
reader-facing stance is therefore deliberately modest: the rule is explicit in
the present implementation, historically supported in scattered examples, and
chronologically underdetermined within the tested range.
