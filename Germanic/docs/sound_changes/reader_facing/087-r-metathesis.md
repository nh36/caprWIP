# R-metathesis

## Historical discussion

R-metathesis closes the present sequence, but it does not behave like the second half of a tidy local pair. The historical process is real enough to deserve explicit prose, yet its chronology reaches much farther back on the left than it does on the right. Sievers-Brunner gives a clear page-safe grammatical statement of the phenomenon through forms such as *berstan* ‘burst’, *forst* ‘frost’, and *cærse* ‘cress’ [@SieversBrunner1965, p. 159, §179]. Luick likewise treats metathesis as a later rearrangement whose interaction with breaking remains variable and not tightly local [@Luick1914, p. 201].

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

Its chronology is one-sided. If the rule is moved before [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*bréstaną} yields *beorstan* rather than expected OE *berstan* ‘burst’. That shows that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC087 OERMetathesis](#rule-OERMetathesis). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one.

That profile is exactly why the chapter remains modest. The checked forms fix the earlier relation but do not identify a corresponding later constraint. CAPR keeps the rule here because the sources treat r-metathesis as a late rearrangement that follows the earlier breaking and contraction history without being fixed immediately beside either one.
