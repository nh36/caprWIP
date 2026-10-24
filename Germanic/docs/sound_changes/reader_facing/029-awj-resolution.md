# Resolution of awj

## Historical discussion of the resolution of \emph{*awj}

Old English *hīeġ* ‘hay’ and *strīeġan* ‘strew’ go back to forms in which
\emph{*w} preceded \emph{*j}. West Germanic doubled every consonant except
\emph{*r} before \emph{*j} after a short syllable, and \emph{*w} was an
ordinary member of that law [@Campbell1959, p. 167, §407]. Proto-Germanic
\emph{*hawja-} therefore appears as West Germanic \emph{*hauuj}
[@Campbell1959, p. 46, §120.2]. Campbell writes the sequence as \emph{auj} >
\emph{auuj} > \emph{auj}, with the diphthong restored before the Old English
developments begin.

Ringe and Taylor reach the same result and explain why it is possible
[@RingeTaylor2014, p. 53, §3.1.3]. They find the gemination of \emph{*wj}
clearest where the preceding vowel was \emph{*i}, as in Proto-Germanic
\emph{*niwjaz} ‘new’ and \emph{*siwjaną} ‘sew’, which give Old Saxon and Old
High German *niuwi* and *siuwen*. Gemination was reversible, since it merged
nothing and altered no underlying form, so the sequence Northwest Germanic
\emph{*awj} to West Germanic \emph{*[aw'w']} to pre-Old English \emph{*[auj]}
can have run its course and then undone itself. Their derivations give
Proto-Germanic \emph{*hawja} through \emph{*hauj-} to *hīeġ* ‘hay’, and
Proto-Germanic \emph{*strawjaną} through \emph{*straujan} to Anglian
*strēgan* ‘strew’ [@RingeTaylor2014, p. 173].

The strongest comparative argument for the doubled stage comes from paradigms
in which some cells had \emph{*j} in the ending and others had \emph{*i}. Only
the first group could double, and the two outcomes then sat side by side. Old
High German has *hewi* ‘hay’ beside *houwi*, and Old English itself preserves
both in one word, *glīg* ‘mirth’ from the undoubled nominative beside *glīowes* ‘of mirth’
in the genitive [@RingeTaylor2014, p. 53, §3.1.3]. The continental forms *houwi*
and *gistrouwen* ‘bestrew’, and Old Saxon *hoi* ‘hay’, point to the same West
Germanic stage, which English alone went on to resolve [@RingeTaylor2014,
p. 173].

The resolution did not treat every doubled \emph{*w} alike, and the difference
is what allows the doubling to be seen apart from it. Campbell sets the two
vowel types side by side: \emph{auj} becomes \emph{auuj} and then \emph{auj},
while \emph{iuj} becomes \emph{iuuj} and then \emph{iuj}. Thereafter they part
company, since the \emph{u} of \emph{auuj} is generally lost while the \emph{j}
of \emph{iuuj} is lost [@Campbell1959, p. 46, §120.2]. Old English *hīeġ* ‘hay’
and *hīew* ‘form, hue’ begin from shapes that differ in a single vowel and end
with different survivors. *Hīeġ* keeps its \emph{*j}, written *ġ*, while *hīew*
keeps its \emph{*w}. Campbell’s other examples of the second type are *nīowe* ‘new’,
*nīewe* ‘new’ and *glīow* ‘mirth’, *glīw* ‘mirth’.

One qualification belongs in the record. Fulk holds that \emph{*w} was never
consonantal here, so that Proto-Germanic already had \emph{*straujaną} with
its diphthong in place and there is no gemination to undo [@Fulk2018, p. 73,
§4.10 n. 1]. The account followed here is the handbook one, which the
comparative material supports: the doubled stage that the continental and
paradigm-internal forms point to is precisely the one Fulk denies ever existed.
Both accounts agree that \emph{*auj} is what enters Old English, and the
disagreement concerns whether a discrete change took place.

## SC029. Resolution of \emph{*awj} to \emph{*auj} (`OEAwwjResolution`) {#rule-OEAwwjResolution}

```foma
define OEAwwjResolution [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j}
];
```

The change is confined to the \emph{*a} type. PGmc [xáwją]{.recon} ‘hay’ is
doubled to \emph{*xáwwją} by the West Germanic law and then resolved to
\emph{*xáują}, and PGmc [stráwjaną]{.recon} ‘strew’ is doubled to
\emph{*stráwwjaną} and resolved to \emph{*stráujaną}, yielding *hīeġ* ‘hay’ and
*strīeġan* ‘strew’ once the later diphthong changes and \emph{i}-umlaut have applied.
PGmc [xíwją]{.recon} ‘form, hue’ is doubled by the same law, and there the
doubling holds: it passes through this change untouched and surfaces as *hīew* ‘form, hue’.

The resolution has to precede
[SC030 OEAuBrightening](#rule-OEAuBrightening), since the fronting needs a
diphthong to work on. Ringe and Taylor state the same dependence when they
observe that these new instances of \emph{*au} went on to share the ordinary
development [@RingeTaylor2014, p. 173].
