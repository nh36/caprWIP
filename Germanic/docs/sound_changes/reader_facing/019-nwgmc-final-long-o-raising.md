# Raising of final unstressed long \emph{*ō}

## Historical discussion

Final unstressed oral bimoric \emph{*ō} became short \emph{*u} in Northwest
Germanic. The qualification matters: oral \emph{*ō}, nasalized \emph{*ǭ}
and trimoric \emph{*ô} were not interchangeable endings. Ringe and Taylor
distinguish the first two developments explicitly; Fulk also distinguishes
the quantities when reconstructing the endings [@RingeTaylor2014,
pp. 15--16, 58--60; @Fulk2018, pp. 82--86, 155--156].

The nominative singular \emph{*wullō} 'wool' and accusative singular
\emph{*wullǭ} are independently reconstructed by Ringe. Their distinct
endings must survive the comparison even when a later paradigm levels
the root vowel [@Ringe2017, pp. 242--243]. Likewise, an oral vowel
followed by \emph{*z} was not yet word-final. These distinctions explain
both the scope of raising and its interaction with later loss.

## SC019. Raising of final unstressed long \emph{*ō} (`PNWGmcFinalLongORaising`) {#rule-PNWGmcFinalLongORaising}

```foma
define PNWGmcFinalLongORaising Ctx([
    [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
    ]
]);
```

The preceding vowel and consonants select a polysyllabic input. The
distinct stressed-monosyllable development is retained separately in
[SC018 PNWGmcStressedMonosyllableORaising](#rule-PNWGmcStressedMonosyllableORaising);
it is not absorbed into this unstressed ending law.

### Lowering before raising: the preferred account

Fulk argues that *scolu* 'troop, shoal', from \emph{*skulō}, requires
lowering of the root before final \emph{*ō} became \emph{*u}. If raising
had already removed the non-high conditioner, an unchanged nominative
would retain root \emph{*u} [@Fulk2018, p. 56]. CAPR provisionally follows
this order:
[SC017 PNWGmcULowering](#rule-PNWGmcULowering), then final oral raising.
It regularly gives the low roots of *nosu* 'nose', *sċofl* 'shovel' and
*sorg* 'sorrow', rather than requiring a later root-vowel generalization
for each selected form.

This is an argument from explanatory economy, not from the number of
matching outputs. Fulk supplies the direct *scolu* argument; the comparison
of its explanatory costs with the other selected paradigms is CAPR's
assessment. The witnesses are not equally independent. *Nosu* already
depends on an earlier remodeled zero-grade stem beside the comparative
\emph{*nasō-}; it is not an untouched inherited nominative
[@Kroonen2013, p. 383; @Campbell1959, p. 43, §115]. For *sċofl* 'shovel', Luick
also infers an earlier high-root doublet, \emph{*scufel}, beside
*scofel* 'shovel'; that inference makes an alternating paradigm credible
but does not establish its direction of levelling [@Luick1914,
pp. 105--106, §78]. The comparative formations of shovel and sorrow
support the selected short-vowel stems, not a directly attested early
English levelling operation [@Orel2003, p. 347; @Kroonen2013, p. 493].
The preferred sequence avoids those additional operations, but it does
not thereby explain every retained high vowel.

### Raising before lowering: a coherent alternative

Stiles expressly places final \emph{*ō} raising before a-umlaut of
\emph{*u} [@Stiles2012, p. 45]. Ringe and Taylor explain how *wull*
'wool' and *lufu* 'love' could preserve a nominative root \emph{*u} by
generalizing it through a paradigm whose other cells had lowered
\emph{*o}; they also leave open genuine exceptions [@RingeTaylor2014,
p. 32]. With the nasal accusative correctly recognized, the alternative
has the following regular consequences. The table gives reconstructed
sound-law predictions, not unattested forms promoted to attestations.

| Paradigm | Lowering before raising | Raising before lowering |
| --- | --- | --- |
| Wool: nominative / accusative | \emph{*woll} / \emph{*wolle} | \emph{*wull} / \emph{*wolle} |
| Love: nominative / accusative | \emph{*lofu} / \emph{*lofe} | \emph{*lufu} / \emph{*lofe} |
| Shoal: nominative / accusative | \emph{*sċolu} / \emph{*sċole} | \emph{*sċulu} / \emph{*sċole} |

The inherited ending opposition follows Ringe's reconstructed paradigm
and the independently described ō-stem inflections; it is not a special
ending invented to rescue wool [@Ringe2017, pp. 242--243;
@Fulk2018, pp. 154--156]. Under earlier raising, nominative-to-oblique
generalization can account for attested *wull* and *lufu/lufe* 'love'.
Conversely, generalization of the lowered oblique root can account for
*scolu* without replacing its nominative ending. The same possibility
exists for nose, shovel and sorrow. Neither particular direction is
directly witnessed in the reconstructed early English paradigms.

There is independent evidence that levelling occurred: Ringe and Taylor
discuss early *Holtijaz* and the daughter and ox paradigms, while Stiles
distinguishes conditioned Runic forms from analogical generalizations
[@RingeTaylor2014, pp. 33--34; @Stiles2012, pp. 47--48]. That establishes
the mechanism's credibility, not its occurrence in every inconvenient
lexeme. Continental *skola* is not an untouched nominative control
either: Fulk describes accusative-ending generalization into the
nominative in Old Saxon and Old High German [@Fulk2018, pp. 154--155].
Thus his *scolu* argument is strong only conditional on the inherited
nominative root not having been remodeled. It does not refute Ringe
and Taylor's phonologically coherent wool account.

There is a further lexical caution: Fulk elsewhere calls *scolu* 'host'
a loan from Latin *schola* 'school', whereas his chronology argument
expressly starts from inherited \emph{*skulō} [@Fulk2018, pp. 47, n. 1,
56]. These analyses cannot silently supply independent confirmation of
one another. The comparison here evaluates his inherited analysis.

The balance nevertheless favors retaining lowering first as a working
account: several independently selected low-root forms follow without
additional, individually unproved levelling. Wool and love remain its
real explanatory cost. Ringe and Taylor's alternative is plausible but
unproved, not a demonstrated error. Analogy belongs to the separately
argued history of a paradigm, not to the exceptionless sound laws.

### What the Runic evidence dates

Fulk cites *horna* 'horn' on the Gallehus horn, about 400, for lowering
and *waritu* 'I write' on the Järsberg stone, about 450, for final oral
raising [@Fulk2018, pp. 56, 82]. These are separate positive chronological
bounds. An occurrence of raising around 450 does not establish that it
began after 400. Nor does a written final *o* in another inflection
establish retention of oral bimoric \emph{*ō}: nasalization, quantity
and a following consonant must first be identified. Stiles's treatment
of the Runic distribution also requires distinguishing conditioned
realization, phonemicization and analogical extension [@Stiles2012,
pp. 47--48, 54--60]. No new general revaluation law follows from those
distinctions.

Fulk's note cites Ringe and Taylor on lowering and final \emph{*-az}
loss, not as an explicit rebuttal of their wool explanation
[@Fulk2018, p. 57, n. 1; @RingeTaylor2014, pp. 27--34]. Stiles predates
their book. Luick discusses alternation and rejects a proposed labial
protection law using regular low-root counterexamples; Campbell and
Bülbring list retained-high-vowel cases [@Luick1914, pp. 104--106,
§§77--79; @Campbell1959, p. 43, §115; @Bulbring1902, pp. 45--46,
§116]. None of these checked passages supplies our exact comparative
economy argument. No specific later criticism or defence was verified
in the bounded literature search; this is not a claim of novelty or
of its absence from all scholarship. The Campbell and Bülbring passages
remain text-checked rather than newly certified against original images.

### Final consonants and later ending reduction

In \emph{*rástōz} 'rest', \emph{*z} protects oral \emph{*ō} from this
raising. After [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), the
newly final long vowel can undergo
[SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding)
and later fronting and shortening, yielding *ræste* 'rest'.
Moving raising after final consonant loss wrongly exposes that vowel
and gives \emph{*rast} instead. This relation is retained separately;
qualifying the lowering/raising comparison does not weaken it.

Nasal \emph{*ǭ} does not raise here. Its later reduction yields the
accusative ending in \emph{*wolle}; the current serialization carries
the nasal symbol to that reduction rather than claiming that nasality
historically lasted until then. The genitive alternatives must also
remain distinct: Ringe and Taylor reconstruct bimoric \emph{*-ōz},
where Fulk argues for trimoric \emph{*-ôz} [@RingeTaylor2014,
pp. 59, 299; @Fulk2018, p. 155]. The trimoric genitive's complete
pathway remains unmodeled; it is not silently replaced by a bimoric
genitive or covered by the present nasal-vowel repair.
