# Proto-Germanic loss of a nasal before \emph{*x}

## Historical discussion

The oldest change treated in this book is common to the whole family. In the
group [-nx-]{.recon} the nasal consonant was lost, the preceding vowel was
lengthened in compensation, and that lengthened vowel was nasalized. Its results
are shared by every daughter language: Gothic *þeihan* ‘thrive’, *brāhta* ‘brought’, *þūhta* ‘seemed’ stand
beside Old High German *dīhan* ‘thrive’, *brāhta*, *fūht* ‘damp’ and Old English *þēon* ‘thrive’,
*brōhte* ‘brought’, *þūhte* ‘seemed’, *fūht* ‘damp’
[@Campbell1959, p. 44, §119; @Fulk2018, p. 55, §4.1;
@Ringe2017, pp. 149--150, §3.2.7]. Because no daughter keeps the nasal, the
change belongs to Proto-Germanic itself, and it precedes every Northwest
Germanic, West Germanic, North Sea Germanic and Anglo-Frisian development
described in the chapters that follow.

Only [a]{.recon}, [i]{.recon} and [u]{.recon} occur in this position. Germanic
had already raised [e]{.recon} to [i]{.recon} and [o]{.recon} to [u]{.recon}
before a nasal followed by a consonant, so the mid vowels are absent from the
input [@Fulk2018, p. 55, §4.1].

The vowel that the change creates is long and nasalized, and it is not yet
rounded. Fulk emphasizes that the lengthened vowels remained nasalized for a
considerable time, well past the close of the Northwest Germanic period, since
the nasalized low vowel produced in this way went on to develop to *ō* in
Anglo-Frisian and did not fall together with the Old English *ā* that came from
[ai]{.recon} [@Fulk2018, p. 55, §4.1]. The comparative material makes the same
point directly: Gothic, Old Norse, Old High German and Old Saxon all reflect the
Proto-Germanic nasalized low vowel as unrounded *ā*, and only Old English and
Old Frisian show *ō* [@Campbell1959, p. 44, §119; @Fulk2018, p. 72, §4.11].
Ringe describes Proto-Germanic \emph{*hanhaną} as \emph{*[xą̄xaną]} and observes
that its low vowel was rounded, along with the other nasalized low vowels, in
the northernmost West Germanic dialects [@Ringe2017, pp. 149--150, §3.2.7].
That rounding is a separate and much later change, and it is treated in the
chapter on the rounding of the long nasalized low vowel.

Barrack's formal cascade states this development as his Proto-Germanic
rule 119 [@Barrack1975, pp. 42--43] and, in agreement with the comparative
argument above, keeps it distinct from the later North Sea law, which he
states separately as Ingvaeonic rule 121 and explicitly orders after 119
[@Barrack1975, p. 44]. His rule numbers are anchors to Campbell's paragraph
numbering [@Barrack1975, p. 21], and his orderings are formal rather than
chronological [@Barrack1975, p. 34], so the agreement concerns the identity
and conditioning of the two laws, not an independent dating.

## SC103. Proto-Germanic nasal loss before \emph{*x} (`PGmcNasalLossBeforeX`) {#rule-PGmcNasalLossBeforeX}

```foma
define PGmcNasalLossBeforeX Ctx([
    [
    {*a} -> {*ã} || _ EnglishStarNasal {*x},
    {*i} -> {*ī} || _ EnglishStarNasal {*x},
    {*u} -> {*ū} || _ EnglishStarNasal {*x},
    {*á} -> {*ã} || _ EnglishStarNasal {*x},
    {*í} -> {*ī} || _ EnglishStarNasal {*x},
    {*ú} -> {*ū} || _ EnglishStarNasal {*x}
] .o. [
    EnglishStarNasal -> 0 || _ {*x}
]
]);
```

The rule performs the three parts of the change together: it lengthens the
vowel, it marks the lengthened low vowel as nasalized, and it then removes the
conditioning nasal. The low vowel is written [ą̄]{.recon} and the high vowels are
written [ī]{.recon} and [ū]{.recon}, because the nasality of the high vowels has
no further consequence: they go on to develop exactly as the inherited long
[ī]{.recon} and [ū]{.recon} do [@Campbell1959, p. 47, §121]. The nasality of the
low vowel is carried forward because its later fate depends on it. In the
executable definitions, `ã` is the single-symbol encoding of long nasalized
\emph{*ą̄}, not a different or short vowel. The historical notation in the
discussion retains its explicit length mark.

The corpus witnesses both branches of the rule. The high branch is
[fúnxstiz]{.recon} ‘fist’, which becomes [fū́xsti]{.recon} ‘fist’ and, after the loss of
[x]{.recon} before the cluster in
[SC028 PNWGmcPreconsonantalXLoss](#rule-PNWGmcPreconsonantalXLoss), gives Old
English *fȳst* ‘fist’. The long vowel of Old High German *fūst* ‘fist’, Dutch *vuist*
and German *Faust* shows that the word belongs here and to no later law
[@Kroonen2013, p. 160]. The rule also supplies the [xst]{.recon} cluster on
which the loss of [x]{.recon} before a consonant operates, so the two stand in a
feeding relation.

The low branch is [θánxtē]{.recon} ‘thought’, the preterite of the verb ‘to think’, whose
principal parts are reconstructed as [þankijaną]{.recon} ‘to think’, [þanhtē]{.recon} ‘thought’,
[þanhtaz]{.recon} ‘thought (past participle)’ with the nasal still standing before the fricative
[@Ringe2017, p. 281; @Ringe2017, p. 136]. Here the rule yields
[θą̄xtē]{.recon} ‘thought’, and the nasalized low vowel is later rounded by
[SC104 EAFNasalizedLowRounding](#rule-EAFNasalizedLowRounding) to give Old
English *þōhte* ‘thought’. This is the form the handbooks themselves cite for
the Anglo-Frisian rounding of the vowel produced here [@Fulk2018, p. 55, §4.1]. It does not enter the loss of [x]{.recon} before a
consonant, in which respect it differs from ‘fist’, so the fricative survives to
the surface and the word displays the vowel history alone.
