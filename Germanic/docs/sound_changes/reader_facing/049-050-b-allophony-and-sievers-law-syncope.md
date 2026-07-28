# B allophony and Sievers-law syncope

## Historical discussion of B allophony

The first change is the positional alternation of Germanic \emph{*b}. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@Hogg1992, pp. 101--102]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

The distribution is narrow, but later changes presuppose the stop-fricative
alternation.

## SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

The handbooks describe \emph{*b}/\emph{*bb} as a positional alternation within the consonant system, and one compound supplies its chronological consequence. Before [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope), *reġnboga* ‘rainbow’ develops as *reġnfoga* rather than expected OE *reġnboga*; later placement creates no comparable failure. The witness places b-allophony after compound-linking syncope without turning the alternation into an independent sound law.

## Historical discussion of Sievers-law syncope

Sievers' Law concerns a different historical problem. It is a prosodic and
morphological adjustment in heavy stems, not a distributional allophone of a
stop consonant. Adamczyk treats the Old English reflexes of the law as
historical evidence from weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through
familiar forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15].

Sievers-law syncope is narrow in scope, but its relation to the following
palatalization is lexically secure. Its earlier limit is less sharply defined
than that of the preceding allophony rule.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

The Sievers-law reduction \emph{*-CijV-*} > \emph{*-CjV-*}, including loss of \emph{*i} before \emph{*j}, must precede palatalization. If [SC050 SieversLawSyncope](#rule-SieversLawSyncope) follows [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*strákkijaną} yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’; earlier placement creates no comparably precise error. The single cluster witness therefore places syncope before velar palatalization.
