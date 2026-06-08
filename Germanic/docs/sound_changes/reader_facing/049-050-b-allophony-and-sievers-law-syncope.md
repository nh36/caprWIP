# B allophony and Sievers-law syncope

## Historical discussion

The two changes gathered here belong to different historical categories, and
they sit next to each other in the sequence that leads into Old English
palatalization. The first is the positional alternation of Germanic *b. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@Hogg1992, pp. 101--102]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic *b as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

Sievers' Law belongs to a different part of the historical discussion. It is a
prosodic and morphological adjustment in heavy stems, not a distributional
allophone of a stop consonant. Adamczyk treats the Old English reflexes of the
law as real historical material in weak verbs and related formations
[@Adamczyk2001]. Fulk gives the compact comparative summary through familiar
forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 28, §6.15]. The point of keeping the two chapters together is
therefore practical and chronological. The allophonic distribution of *b needs a
brief place in the book, and Sievers-law syncope is the last narrow feeder
before the palatalization sequence begins in earnest.

## Distribution of *b* after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

The first rule formalizes the stop-fricative alternation of Germanic *b.

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

In prose, the rule says that *b becomes a fricative after vowels and liquids,
while geminate *bb keeps the stop value.

Historically, this is the sort of narrow distributional statement that the
handbooks place within the consonant system and discuss only briefly on its own.
Even so, it matters because later derivations assume that the
alternation is already in place. The clearest tested consequence appears in
*reġnboga* ‘rainbow’. The compound must already have passed through the earlier
linking-vowel adjustment before the bilabial stop and fricative values settle.
No equally sharp later lexical breakpoint emerges within the tested sequence, so
the rule is best read as an early distributional adjustment whose later limit is
less tightly fixed than its earlier dependency.

## Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

The second rule removes the Sievers-law *i before *j after a consonant.

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

In plain language, the rule contracts the heavier *-CijV-* sequence to
*-CjV-*. That is why it belongs to the historical aftermath of Sievers' Law and
stands apart from the earlier stop-fricative distribution.

Its place in the sequence is clearer than that of the allophony rule. The
change must already have happened before [velar palatalization before front
vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization), because the
cluster behind *streċċan* ‘stretch’ depends on the syncope. With PGmc
\emph{*strákkijaną} in the wrong order, the development stops at *strecċan*
‘stretch’; the expected Old English form is *streċċan* ‘stretch’. That is a real chronological
consequence. No equally precise earlier lexical breakpoint fixes how far back
the syncope must stand, so the historical picture remains asymmetric. The rule
is secure as an immediate feeder into the palatalization zone, even though its
earlier limit is less sharply bounded.
