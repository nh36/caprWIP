# R-metathesis

## Historical discussion

Sievers-Brunner describes r-metathesis in forms such as *berstan* ‘burst’,
*forst* ‘frost’, and *cærse* ‘cress’
[@SieversBrunner1965, pp. 146--147, §179]. Luick likewise treats it as a later
rearrangement whose interaction with breaking remains variable
[@Luick1914, p. 201].

For the selected West Saxon *berstan*, the evidence places breaking before
metathesis; this is not a chronology for every dialectal metathesis. It does not
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
dating, and does not alter the West Saxon ordering adopted here.

Barrack describes generalized environments of 459.1 as "a late stage
of free variation" [@Barrack1975, p. 116], while grading the evidence
for 459.3 as meagre [@Barrack1975, p. 118]. These are descriptions of
the distribution of forms, not an explanation by optional sound change.
Campbell records byforms such as *forst* beside
*frost*, *gærs* beside *græs*, *cerse* beside *cresse*, and *rinnan*
beside *iernan*, *eornan* [@Campbell1959, p. 184, §459].
Regular sound change remains exceptionless within its phonological,
chronological and dialectal domain. Distinct dialect histories, transmission
of earlier and later forms, borrowing or independently evidenced analogy
could account for coexistence; the byforms alone do not decide among them.

The categorical operation below correctly handles the selected *berstan*
and *forst*. Controlled comparisons extending only the vowel inventory
to include \emph{*æ} and \emph{*y}, while retaining \emph{st}, alter no
selected output. With that same inventory, removing the \emph{t}
requirement changes *græs* 'grass' to attested *gærs*. Thus the selected
forms discriminate these implementations, although neither spelling
establishes which conditioning was historically productive. The earlier
zero-difference comparison before \emph{s} versus \emph{st} depended on
an enumeration excluding \emph{*æ}. A further extension to nasal
environments also alters selected *brandes* 'firebrand (gen.)',
*drenċ* 'drink' and *strenġ* 'string'; a regressive pre-\emph{ht}
operation changes selected *fyrhte* 'fright'. These are reasons not to
adopt those operations unchanged across the present selections, not proof
that broader regular metathesis was historically impossible.

The cress family supplies independent evidence beyond \emph{st}:
Campbell and Hogg describe *cresse* through reconstructed
\emph{*cersse} to *cerse*, with simplification of the geminate
[@Campbell1959, p. 190, §476; @HoggGrammar2011, p. 288, §7.80].
Ringe and Taylor give *cærse* from reconstructed \emph{*cræsse}
[@RingeTaylor2014, p. 263]. Campbell's Middle English *kers* evidence
also places the metathesis after assibilation
[@Campbell1959, p. 184, §459 n. 1]. These forms merit discussion even
without selecting a new corpus target: their inherited stem and exact
attested cell and dialect must be established separately. The retained
operation represents the changes presently required by the selected forms;
it does not delimit the whole historical phenomenon.

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
later constraint. For the selected West Saxon history, the sources support a late
rearrangement after breaking without placing it immediately beside contraction.
