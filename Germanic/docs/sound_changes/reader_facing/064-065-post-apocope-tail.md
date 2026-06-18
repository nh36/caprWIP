# Post-apocope \emph{*n}-loss and medial syncope

## Historical discussion of post-apocope \emph{*n}-loss and medial syncope

After high-vowel apocope the weak tail is still not entirely settled. Hogg, Ringe and Taylor, and Fulk all describe a late region in which further medial reduction and cluster pressure remain active, even though the evidence is much less even than it was for the main apocope rule [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4; @Fulk2018, p. 91, §5.6]. The inherited \emph{*furht-} family adds one especially narrow witness of its own, because it shows that a single surviving nasal can still decide whether the weak-tail output is right or wrong [@Kroonen2013, p. 201].

This chapter is therefore intentionally modest. One rule has real positive chronology on both sides, but only through a single witness family. The other belongs naturally to the same late region without yet producing a comparably sharp first-break result. Keeping both visible makes the weak-tail aftermath more honest than either silence or overstatement would.

## SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

The first rule is extremely narrow in form.

```foma
define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];
```

In prose, it removes a final \emph{*n} after long \emph{*ī}. That looks tiny on the page, but the effect is real in the inherited family behind *fyrhte* ‘fright’.

The chronology is two-sided even though the witness base is not broad. If the
rule is moved before [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc \emph{*fúrxtīnaz} yields
*fyrhten* rather than expected OE *fyrhte* ‘fright’. If the rule is delayed
until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the same PGmc form again
yields *fyrhten* rather than expected *fyrhte*. This shows that
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss) must come before
[SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), and it places
[SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) before
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

That symmetry does not make the rule large. Both boundaries are carried by the same witness family, so the evidence is real but narrow. The value of the rule lies in showing that even a very small formal step can still have a concrete lexical place in the chronology.

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

The second rule formalizes one narrower slice of late medial syncope.

```foma
define OEMedialSyncope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
];
```

In prose, it deletes medial \emph{*i} before a following dental after a heavy syllable. The broader historical background is secure enough, since the handbooks do treat late medial syncope as part of the same weak-tail region [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4; @Fulk2018, p. 91, §5.6].

The finite-state chronology is much weaker, however. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC065 OEMedialSyncope](#rule-OEMedialSyncope) before or after any specific neighboring change. CAPR places it here because the handbooks treat late medial syncope as part of the post-apocope weak-tail sequence that continues into the later syncope-and-cluster-simplification material. The placement should be read as approximate, not as a local ordering forced by the tested forms.

That limitation is worth stating plainly. Late medial syncope belongs in the history of the weak tail, but this particular rule does not yet have a diagnostic constraint of its own on either side.
