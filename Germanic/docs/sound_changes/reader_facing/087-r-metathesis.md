# R-metathesis

## Historical discussion

Sievers-Brunner describes r-metathesis in forms such as *berstan* ‘burst’,
*forst* ‘frost’, and *cærse* ‘cress’
[@SieversBrunner1965, p. 159, §179]. Luick likewise treats it as a later
rearrangement whose interaction with breaking remains variable
[@Luick1914, p. 201].

The evidence establishes that breaking precedes metathesis. It does not
establish an ordering relation between
[SC086 OEContraction](#rule-OEContraction) and
[SC087 OERMetathesis](#rule-OERMetathesis).

Barrack devotes his longest metathesis discussion to this change as rule
459.1, whose feature matrix moves \emph{*r} across a short vowel before
\emph{s} or \emph{n} and whose worked examples include the
\emph{cyrps} and \emph{-firiþ}/\emph{-ferþ} types; a companion rule 459.3
treats the regressive movement of \emph{r} back across an accented short
vowel before \emph{ht}, as in late West Saxon \emph{worhte} beside
\emph{wrohte} [@Barrack1975, pp. 115--118]. His account agrees that in
West Saxon the
\emph{beornan}/\emph{birnan} 'to burn' family shows metathesis operating on
the output of earlier developments, which he schematizes as 157 followed by
170a followed by 459.1; but he records that the relative order of breaking
and metathesis varies by dialect, separating the West Saxon from the Anglian
treatment [@Barrack1975, pp. 115--117]. Because his orderings are formal
rather than chronological [@Barrack1975, p. 34], that dialect-order
observation is conditioning evidence to be weighed in its own right, not a
dating; it is held for a separate adjudication in the Barrack dossier and
does not alter the West Saxon ordering adopted here.

The breadth of Barrack's formulation was tested directly against the
corpus and could not be sustained as an exceptionless law. Barrack
himself grades the generalized environments of 459.1 as "a late stage
of free variation" [@Barrack1975, p. 116], and for 459.3 he concedes
that "the evidence of this change is very meager"
[@Barrack1975, p. 118]. Campbell's survey points the same way: the
wider metathesis domain is populated by doublets such as *forst* beside
*frost*, *gærs* beside *græs*, *cerse* beside *cresse*, and *rinnan*
beside *iernan*, *eornan* [@Campbell1959, p. 184, §459]. Counterfactual
compilations of the broader rule confirm the diagnosis: a law extended
from the \emph{st} cluster to all \emph{s}/\emph{n} environments wrongly
converts attested *brandes* 'firebrand (gen.)', *drenċ* 'drink',
*strenġ* 'string', and *græs* 'grass', while deriving no new correct
form, and a regressive pre-\emph{ht} law wrongly converts attested
*fyrhte* 'fright'. The change modelled here is therefore confined to the
exceptionless West Saxon core before \emph{st}; the variable periphery
of the metathesis complex is a matter of which doublet variant each word
selects, not of a wider sound law.

## SC087. Metathesis of \emph{*r} with a following short vowel (`OERMetathesis`) {#rule-OERMetathesis}

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

The rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Moving the rule before [SC044 OEBreaking](#rule-OEBreaking) makes PGmc [bréstaną]{.recon} ‘burst’ yield [*beorstan*]{.pred} rather than expected OE *berstan* ‘burst’. On this evidence, I take [SC087 OERMetathesis](#rule-OERMetathesis) to follow [SC044 OEBreaking](#rule-OEBreaking). Moving it later within the tested sequence alters no output.

The lexical evidence fixes the earlier relation but does not identify a corresponding
later constraint. The sources treat r-metathesis as a late rearrangement after
breaking without placing it immediately beside contraction.
