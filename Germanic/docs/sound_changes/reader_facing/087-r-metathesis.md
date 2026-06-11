# R-metathesis

## Historical discussion

R-metathesis closes the present sequence, but it does not behave like the second half of a tidy local pair. The historical process is real enough to deserve explicit prose, yet its chronology is broad and distant on the left and open on the right. Sievers-Brunner gives a clear page-safe grammatical statement of the phenomenon through forms such as *berstan* ‘burst’, *forst* ‘frost’, and *cærse* ‘cress’ [@SieversBrunner1965, p. 159, §179]. Luick likewise treats metathesis as a later rearrangement whose interaction with breaking remains variable and not tightly local [@Luick1914, p. 201].

That is why the chapter stays short. The note belongs after the contraction chapter in the assembled order, but the evidence does not justify inventing a positive claim that [SC086 OEContraction](#rule-OEContraction) must come before [SC087 OERMetathesis](#rule-OERMetathesis) simply because the two are adjacent.

## SC087. Metathesis of \emph{*r} with a following short vowel (`OERMetathesis`) {#rule-OERMetathesis}

The implementation states the metathesis directly.

```foma
define OERMetathesis [
    {*r} {*e} -> {*e} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*u} -> {*u} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*i} -> {*i} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*o} -> {*o} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*a} -> {*a} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*é} -> {*é} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*ó} -> {*ó} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*á} -> {*á} {*r} || EnglishStarConsonant _ {*s} {*t}
];
```

In prose, the rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Its chronology is one-sided and broad. If the rule is moved before SC044 OEBreaking, PGmc \emph{*bréstaną} yields *beorstan* rather than expected OE *berstan* ‘burst’. That shows that SC044 OEBreaking must come before [SC087 OERMetathesis](#rule-OERMetathesis). The later side is different: the current tests find no real break beyond the current order before the search limit, so the available evidence does not identify any later historical boundary for [SC087 OERMetathesis](#rule-OERMetathesis).

That profile is exactly why the chapter remains modest. The earlier relation is historically real, but it is broad and far away. The right side remains boundary-limited. R-metathesis therefore works best as a short closing note, not as the capstone of a tighter adjacent pair.
