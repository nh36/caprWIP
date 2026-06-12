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

This is a narrow consonantal distribution with limited independent scope, but it
matters because later derivations already assume that the alternation is in
place.

## SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

The first rule formalizes the stop-fricative alternation of Germanic \emph{*b}.

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

In prose, the rule says that \emph{*b} becomes a fricative after vowels and
liquids, while geminate \emph{*bb} keeps the stop value.

Historically, this is the sort of narrow distributional statement that the
handbooks place within the consonant system and discuss only briefly on its own.
Even so, it matters because later derivations assume that the
alternation is already in place. The clearest tested consequence appears in
*reġnboga* ‘rainbow’. If the rule is moved before the earlier linking-vowel
adjustment, the derivation yields *reġnfoga* ‘rainbow’ rather than expected OE
*reġnboga* ‘rainbow’. This shows that [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) must come
before [SC049 PGmcBAllophony](#rule-PGmcBAllophony).
No equally sharp later lexical breakpoint emerges within the tested sequence, so
the rule has no explicit later boundary within the present sequence.

## Historical discussion of Sievers-law syncope

Sievers' Law belongs to a different historical problem. It is a prosodic and
morphological adjustment in heavy stems, not a distributional allophone of a
stop consonant. Adamczyk treats the Old English reflexes of the law as real
historical material in weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through
familiar forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15].

That makes the change historically narrower but chronologically important. It is
the last small feeder before the palatalization sequence begins in earnest, and
its place in the cascade is clearer than that of the preceding allophony rule.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

The second rule removes the Sievers-law \emph{*i} before \emph{*j} after a consonant.

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

In plain language, the rule contracts the heavier \emph{*-CijV-*} sequence to
\emph{*-CjV-*}. That is why it belongs to the historical aftermath of Sievers' Law and
stands apart from the earlier stop-fricative distribution.

Its place in the sequence is clearer than that of the allophony rule. If the
change is delayed until after [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), the cluster
behind *streċċan* ‘stretch’ is affected too late. With PGmc
\emph{*strákkijaną} in the wrong order, the derivation yields *strecċan*
‘stretch’. The expected Old English form is *streċċan* ‘stretch’. That is a real chronological
consequence. No equally precise earlier lexical breakpoint fixes how far back
the syncope must stand, so the historical picture remains asymmetric. The rule
is secure as an immediate feeder into the palatalization zone, even though its
earlier limit is less sharply bounded. The evidence therefore places
[SC050 SieversLawSyncope](#rule-SieversLawSyncope) before
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization).
