# Velar palatalization before front vowels

## Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological sequence. The examples associated with that sequence, such as
*ceaster* ‘town’, *geaf* ‘gave’, *giefan* ‘give’, and *giest* ‘guest’, already
show that consonantal palatalization and later vowel effects stand close
together historically, even when they must be distinguished analytically
[@Luick1914, pp. 157--167, §§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as *cild* ‘child’, *dæg* ‘day’, *giefan* ‘give’, and *giest*
‘guest’, which show how palatalized velars, palatal influence, and later
umlautal outcomes meet in the same region of the lexicon without collapsing
into one process [@Campbell1959, pp. 69--72, 89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@Hogg1992, pp. 103--104]. This formulation
replaces a broad list of palatal outcomes with a phonological environment
defined by adjacency and syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and \emph{*sk} had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as \emph{weccan} ‘wake’, \emph{licgan} ‘lie’, \emph{lecgan} ‘lay’,
\emph{secg} ‘retainer’, \emph{ecg} ‘edge’, \emph{wicg} ‘horse’, and
\emph{brycg} ‘bridge’, illustrate the same point in lexical detail: front
vowels and `j` create the palatal environment in which plain `k` and `g` cease
to behave as plain velars [@RingeTaylor2014, pp. 213--214, §6.4.1].

Luick describes a broad early movement; Campbell distinguishes plain velars
from the `sk` complex; Hogg specifies the adjacency and syllable conditions;
and Ringe and Taylor order the plain-velar change before West-Saxon
diphthongization. Plain-velar palatalization thus forms part of a wider
palatalizing environment without being identical to its neighboring changes.

## SC052. Palatalization of \emph{*k} before front vowels and \emph{*j} (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront}

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;
```

The *weccan* ‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’ set identifies front vowels and `j` as the environment for palatalization of `k` [@RingeTaylor2014, pp. 213--214, §6.4.1]. These forms establish the conditioning; different witnesses establish the chronology.

Applied before Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* rather than expected OE *streċċan* ‘stretch’. Applied after i-umlaut fronting, PGmc \emph{*kūi} and \emph{*lúnganjō} yield *ċȳ* ‘cows’ and *lunġen* ‘lungs’ rather than expected OE *cȳ* and *lungen*. The front-vowel `k` change therefore follows Sievers-law syncope and precedes i-umlaut fronting.

## SC052. Velar palatalization before front vowels (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

Plain `k` and `g` palatalization in front-vocalic and `j`-adjacent environments follows `sk`-palatalization and occupies a sharply defined pre-umlaut interval. Applied before Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* rather than expected OE *streċċan* ‘stretch’. Applied after general i-umlaut, PGmc \emph{*kūi} yields *ċȳ* rather than expected *cȳ* ‘cows’, and PGmc \emph{*lúnganjō} yields *lunġen* rather than expected *lungen* ‘lungs’. These witnesses place velar palatalization after Sievers-law syncope and before umlaut.

Luick, Campbell, and Ringe and Taylor place *cild* ‘child’ and *dæg* ‘day’ in a consonantal palatalization that precedes later vowel fronting [@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1]. The umlautal developments therefore receive plain `k` and `g` already reshaped beside front vowels and `j`.

The `sk` change belongs to the same palatalizing region with a separate scope. The *streċċan* ‘stretch’ evidence establishes a specific dependency on earlier syncope; it does not merge the two changes into one process.
