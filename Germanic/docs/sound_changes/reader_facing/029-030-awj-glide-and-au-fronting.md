# Awj resolution and the English brightening of au

## Historical discussion

Two changes stand between the Proto-Germanic diphthong \emph{*au} and its Old
English reflex *ēa*. The earlier one repairs a West Germanic gemination and
restores a diphthong that the gemination had obscured. The later one fronts the
first element of every \emph{*au}, whether inherited or newly created, and
belongs with Anglo-Frisian brightening.

The two are separate developments with separate domains. The first concerns a
handful of words in which \emph{*w} stood before \emph{*j}. The second concerns
the whole Old English history of \emph{*au}, for which *lēaf* ‘leaf’,
*strēam* ‘stream’ and *brēad* ‘bread’ are ordinary witnesses, and to which the
first change merely adds two more inputs.

## Historical discussion of the resolution of \emph{*awj}

Old English *hīeġ* ‘hay’ and *strīeġan* ‘strew’ go back to forms in which
\emph{*w} preceded \emph{*j}. West Germanic doubled consonants before
\emph{*j}, and the doubling applied here as well, so that Proto-Germanic
\emph{*hauja-} appears as West Germanic \emph{*hauuj} [@Campbell1959, p. 46,
§120.2]. Campbell writes the sequence as \emph{auj} > \emph{auuj} > \emph{auj},
with the diphthong restored before the Old English developments begin.

Ringe and Taylor reach the same result and explain why it is possible
[@RingeTaylor2014, p. 53, §3.1.3]. Gemination was reversible, since it merged
nothing and altered no underlying form, so the sequence Northwest Germanic
\emph{*awj} to West Germanic \emph{*[aw'w']} to pre-Old English \emph{*[auj]}
can have run its course and then undone itself. Their derivations give
Proto-Germanic \emph{*hawja} through \emph{*hauj-} to *hīeġ*, and
Proto-Germanic \emph{*strawjaną} through \emph{*straujan} to Anglian
*strēgan* ‘strew’ [@RingeTaylor2014, p. 173].

The change is confined to English. Old High German *houwi* ‘hay’ and
*gistrouwen* ‘bestrew’, and Old Saxon *hoi* ‘hay’, keep the geminate
[@RingeTaylor2014, p. 173].

One qualification belongs in the record. Fulk holds that \emph{*w} never
doubled before \emph{*j} at all, the second element having been vocalic
throughout [@Fulk2018, §4.10 n. 1]. On that account there is no gemination to
undo. Both accounts agree that \emph{*auj} is what enters Old English, so the
rule below is stated in a form that is neutral between them; the disagreement
concerns whether a discrete change took place.

## SC029. Resolution of \emph{*awj} to \emph{*auj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

Two corpus words undergo the change. PGmc [xáwwją]{.recon} ‘hay’ becomes
\emph{*xáują}, and PGmc [stráwjaną]{.recon} ‘strew’ becomes \emph{*stráujaną},
yielding *hīeġ* and *strīeġan* once the later diphthong changes and
\emph{i}-umlaut have applied.

The resolution has to precede the fronting of SC030, since the fronting needs a
diphthong to work on. Reversing the two leaves the older sequence untouched and
produces [*hauġ*]{.pred} for *hīeġ* and [*strauian*]{.pred} for *strīeġan*.
Ringe and Taylor state the same dependence when they observe that these new
instances of \emph{*au} went on to share the ordinary development
[@RingeTaylor2014, p. 173].

## Historical discussion of the brightening of \emph{*au}

The fronting of \emph{*au} is the same change as the fronting of plain
\emph{*a} that is usually called Anglo-Frisian brightening. Campbell arrives at
the point while establishing the order of the early vowel changes, remarking
that the normal development of Proto-Germanic \emph{*au} to Old English *ēa*
shows that the change of \emph{a} to \emph{æ} would affect the first element of
a diphthong [@Campbell1959, p. 52, §132]. His ordered list accordingly places
West Germanic \emph{a} > Old English \emph{æ} and West Germanic \emph{*au} >
Old English \emph{*æu} in one and the same step. Fulk puts it in a single
sentence, saying that this fronting of \emph{a} applied also to the diphthong
\emph{au} in Old English [@Fulk2018, p. 73, §4.12].

The intermediate stage is directly attested. Ringe and Taylor describe
\emph{*au} as first tensed and fronted to \emph{*æu}, a spelling still found
occasionally in eighth-century documents, with the offglide unrounded and
lowered only later [@RingeTaylor2014, p. 172]. Early spellings such as
*Eadbald* with an initial \emph{aeo} preserve the rounded offglide, and the
rounding survives in late Northumbrian [@Fulk2018, p. 73, §4.12]. The outcome
of the whole sequence is the *ēa* of *dēaþ* ‘death’, *ēage* ‘eye’ and
*lēaf* ‘leaf’ [@Campbell1959, p. 53, §135].

The geographical reach of the diphthongal fronting is narrower than that of the
plain one. Old Frisian shows no such fronting and has \emph{ā}, so that Old
English *ēac* ‘also’, *ēage* ‘eye’ and *bēam* ‘tree’ stand against Old Frisian
*āk*, *āge* and *bām* [@Fulk2018, p. 73, §4.12; @RingeTaylor2014, p. 172]. A
later change supplies independent confirmation. Old English *gēac* ‘cuckoo’ has
a palatalized initial, which requires a front vowel to have followed it, while
Old Frisian *gāk* has none [@Fulk2018, p. 73, §4.12]. Brightening of plain
\emph{*a} is shared with Frisian; brightening of the first element of
\emph{*au} is English.

## SC030. Brightening of \emph{*au} to \emph{*æu} (`OEAuFronting`) {#rule-OEAuFronting}

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Eighteen corpus derivations pass through the change, and sixteen of them carry
\emph{*au} inherited straight from Proto-Germanic. PGmc [láubą]{.recon} ‘leaf’
gives *lēaf*, PGmc [stráumaz]{.recon} ‘stream’ gives *strēam*, PGmc
[bráudą]{.recon} ‘bread’ gives *brēad*, and PGmc [dráugmaz]{.recon} ‘dream’
gives *drēam*. Where a following \emph{*j} or \emph{*i} survives long enough to
cause \emph{i}-umlaut, the *ēa* appears in West Saxon as *īe*, as in
*ġelīefan* ‘believe’ from PGmc [galáubijaną]{.recon} and *nīed* ‘need’ from
PGmc [náudiz]{.recon} [@Campbell1959, p. 46, §120.2]. The two words supplied by
SC029, *hīeġ* and *strīeġan*, join this second group.

The proportions matter for what the rule is. This is the general Old English
treatment of \emph{*au}, to which the resolution of \emph{*awj} contributes two
further inputs; the history of *hīeġ* and *strīeġan* does not define it.

The fronted \emph{*æu} has no independent life. It is taken up at once by the
diphthong leveling of SC032, which lowers the offglide and delivers *ēa*.
Ringe and Taylor give that order explicitly when they place the tensing and
fronting first and the unrounding and lowering later [@RingeTaylor2014, p. 172].
Displacing the fronting past the leveling therefore leaves an \emph{*æu} that
nothing consumes, and the affected derivations yield no output at all. That
failure shows that \emph{*æu} is an internal stage with no Old English surface
form; the historical order comes from the sources.
