# Northwest Germanic lowering of long \emph{ē}

## Historical discussion

Proto-Germanic \emph{*ē₁} (the long mid vowel of PIE origin, as against the later \emph{*ē₂}) split East Germanic from the rest of the family: Gothic keeps a mid vowel, written ⟨e⟩, in *gadēþs* 'deed', *slēpan* 'to sleep', *mēna* 'moon', and *jēr* 'year', while Norse and all of West Germanic show a low vowel — Old Norse *ráða*, *láta*, *ár*, *nál*, Old High German *tāt*, *slāfan*, *jār*, *māno*, Old Saxon *dād*, *slāpan*, *jār*. Ringe and Taylor assemble the comparative set and reconstruct a Northwest Germanic sound change \emph{*ē₁} > \emph{*ā} [@RingeTaylor2014, pp. 11--13]. The change is directly dated by the earliest epigraphy: the Early Runic accusative \emph{mākija} 'sword' (beside Gothic *mēkeis*) already shows ⟨a⟩ in the second half of the second century AD [@RingeTaylor2014, p. 12], and the a-rune likewise writes the stressed reflex in the Opedal stone's *swestar* 'sister', with early Proto-Scandinavian loans into Sami confirming the /aː/ value [@Stiles2017, p. 4].

The change affected stressed syllables only. Ringe and Taylor restrict it explicitly: unstressed \emph{*ē} did not lower but was eventually shortened, as in \emph{*fadēr} > \emph{*fader} 'father' [@RingeTaylor2014, p. 13, and p. 147]; in the runic material the unstressed final vowel of *faþiR* has already merged with \emph{*-i} [@Stiles2017, p. 4]. Within stressed syllables, however, the lowering was unconditioned: it applied before nasals exactly as elsewhere, and Ringe and Taylor accordingly print the intermediates \emph{*mānō} 'moon', \emph{*mānōþ-} 'month', and \emph{*spānuz} 'spoon' [@RingeTaylor2014, p. 11]. The later, dialectally narrower fates of this \emph{*ā} — fronting in the North Sea area when oral, rounding when nasalized — are separate sound changes treated in their own chapters.

The reconstruction of the intermediate value is disputed. Fulk argues that the Northwest Germanic vowel was a low front \emph{*ǣ}, retained unchanged in Anglo-Frisian, with the backing to \emph{ā} of Norse and inner West Germanic a separate areal development spreading northward from Upper German territory; on that reading the runic ⟨a⟩ spellings write a front [æː] for which the futhark had no better grapheme [@Fulk2018, pp. 60--61, §4.6]. Campbell is deliberately noncommittal, finding the \emph{*ā} stage "tempting to assume, though not definitely demonstrable" [@Campbell1959, pp. 50--51, §§128--129]. Ringe and Taylor answer with the lengthened place-adverbs *þǣr* 'there' and *hwǣr* 'where', whose front vowels are most naturally the output of fronting applied to a back \emph{*ā} [@RingeTaylor2014, pp. 13--14]. The present model adopts the two-step reconstruction while recording that the alternative remains live.

## SC024. Lowering of stressed long \emph{ē} (`PNWGmcLongELowering`) {#rule-PNWGmcLongELowering}

```foma
define PNWGmcLongELowering [
    {*ḗ} -> {*ā}
];
```

The rule reads the stressed tier \emph{*ḗ} only, in keeping with the stress restriction; unstressed \emph{*ē}, as in \emph{*fadēr} 'father', is left for the unstressed-shortening rules of the Old English stage and never lowers. No segmental environment is imposed: nasal forms such as [mḗnōþz]{.recon} 'month' and [spḗnuz]{.recon} 'spoon' pass through \emph{*mānōþ-} and \emph{*spānuz} on their way to *mōnaþ* and *spōn*, exactly as reconstructed by Ringe and Taylor [@RingeTaylor2014, p. 11].

The rule stands at the head of the Northwest Germanic block, and its output \emph{*ā} is consumed much later in the cascade by [SC025 EAFLongANasalRounding](#rule-EAFLongANasalRounding) and [SC101 EAFLongAFronting](#rule-EAFLongAFronting): if the lowering is instead displaced after those rules, [mḗnōθz]{.recon} yields [*mānaþ*]{.pred} rather than OE *mōnaþ* 'month', and [skḗpą]{.recon} yields [*sċāp*]{.pred} rather than *sċēap* 'sheep'. Within the cascade no earlier boundary has been demonstrated; the second-century runic attestation supplies the absolute dating.
