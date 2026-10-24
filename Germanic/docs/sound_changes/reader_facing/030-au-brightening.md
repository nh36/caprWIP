# English brightening of au

## Historical discussion of the brightening of \emph{*au}

The fronting of \emph{*au} is the application to a diphthong of the same
process that fronts plain \emph{*a}, the process usually called Anglo-Frisian
brightening. Campbell arrives at the point while establishing the order of the
early vowel changes, remarking
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
*āk* ‘also’, *āge* ‘eye’ and *bām* ‘tree’ [@Fulk2018, p. 73, §4.12; @RingeTaylor2014, p. 172]. A
later change supplies independent confirmation. Old English *gēac* ‘cuckoo’ has
a palatalized initial, which requires a front vowel to have followed it, while
Old Frisian *gāk* ‘cuckoo’ has none [@Fulk2018, p. 73, §4.12]. Brightening of plain
\emph{*a} is shared with Frisian; brightening of the first element of
\emph{*au} is English.

## SC030. Brightening of \emph{*au} to \emph{*æu} (`OEAuBrightening`) {#rule-OEAuBrightening}

```foma
define OEAuBrightening [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Most of the words that pass through the change carry \emph{*au} inherited
straight from Proto-Germanic. PGmc [láubą]{.recon} ‘leaf’ gives *lēaf* ‘leaf’, PGmc
[stráumaz]{.recon} ‘stream’ gives *strēam* ‘stream’, PGmc [bráudą]{.recon} ‘bread’
gives *brēad* ‘bread’, and PGmc [dráugmaz]{.recon} ‘dream’ gives *drēam* ‘dream’. Where a
following \emph{*j} or \emph{*i} survives long enough to cause \emph{i}-umlaut,
the *ēa* appears in West Saxon as *īe*, as in *ġelīefan* ‘believe’ from PGmc
[galáubijaną]{.recon} ‘believe’ and *nīed* ‘need’ from PGmc [náudiz]{.recon} ‘need’
[@Campbell1959, p. 46, §120.2]. The two words supplied by
[SC029 OEAwwjResolution](#rule-OEAwwjResolution), *hīeġ* ‘hay’ and
*strīeġan* ‘strew’, join this second group.

The proportions matter for what the rule is. This is the general Old English
treatment of \emph{*au}, to which the resolution of \emph{*awj} contributes two
further inputs; the history of *hīeġ* ‘hay’ and *strīeġan* ‘strew’ does not define it.

The fronted \emph{*æu} has no independent life. It is taken up at once by the
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), which lowers
the offglide and delivers *ēa*.
Ringe and Taylor give that order explicitly when they place the tensing and
fronting first and the unrounding and lowering later [@RingeTaylor2014, p. 172].
