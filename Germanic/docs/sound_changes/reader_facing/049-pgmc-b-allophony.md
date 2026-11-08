# B allophony

## Historical discussion

The positional alternation of Germanic \emph{*b} is a Proto-Germanic distributional feature. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@HoggGrammar2011, pp. 29--30, §§2.53--2.54]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

The distribution is narrow, but later changes presuppose the stop-fricative
alternation. CAPR implements the rule at a late cascade position for computational
reasons: the alternation must interact with consonant environments shaped by
intermediate rule applications. The inherited distribution is Proto-Germanic;
the position at which CAPR realizes it is not a new Proto-Germanic event.

Hogg distinguishes the early bilabial fricative, still an allophone of
inherited /b/, from its later split and merger with /f/. Campbell's spelling
discussion likewise distinguishes inherited labial realization from
secondary voicing of /f/ [@HoggGrammar2011, pp. 29--30, §§2.53--2.54;
@Campbell1959, pp. 179--181, §§444--448]. CAPR retains underlying
\emph{*b} until ordinary nonhigh syncope has established its conditioning
environment. This removes the need for early compound deletion; it does
not insert a later \emph{*β > *b} sound law.

The distinction matters: already represented \emph{*β} and inherited
\emph{*f} remain fricatives after nasals, whereas underlying \emph{*b}
has stop realization there. Initial, postnasal and geminate stops are
preserved; intervocalic \emph{*b} receives fricative realization.
Syncope-created velar clusters do not license analogous hardening:
Ringe and Taylor contrast *syngian* 'sin' with inherited stop clusters
[@RingeTaylor2014, p. 4]. The chosen serialization precedes the labial
split in the model, not a newly demonstrated strict historical boundary.

## SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony Ctx([
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
]);
```

Realization before [SC114 OENonHighSyn](#rule-OENonHighSyn) gives
[*reġnfoga*]{.pred} instead of *reġnboga* 'rainbow'; realization afterward
preserves the selected output. This discriminates the representations,
not an independently dated new lenition law or compound-specific exemption.
