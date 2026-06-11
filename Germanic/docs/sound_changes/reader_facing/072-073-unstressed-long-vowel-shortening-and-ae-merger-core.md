# Unstressed long-vowel shortening and ae-merger

## Historical discussion of unstressed long-vowel shortening and ae-merger

This pair is the strongest internal seam in the late weak tail. Campbell's discussion of shortening of unaccented long vowels gives the classical background, while Ringe and Taylor place shortening of unstressed long vowels among the last prehistoric Old English changes and then carry the story forward into the immediately following developments [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7]. What the finite-state derivation adds is a very sharp distinction between the shortening itself and the later merger of unstressed \emph{*æ} with \emph{*e}.

That is why this chapter can be more substantial than the opening note or the earlier pair. [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) have a real reciprocal relation in the cards, and the chapter can show both sides of it directly. The pair also keeps its outward relations in view: [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) remains the earlier prerequisite for shortening, while SC085 OEHLoss remains the later outward handoff from the merger.

## SC072. Shortening of unstressed long vowels (`OEUnstressedLongVowelShortening`) {#rule-OEUnstressedLongVowelShortening}

The implementation keeps the shortening stage as one composed rule.

```foma
define OEUnstressedLongVowelShortening OEUnstressedLongVowelShortening1
    .o. OEUnstressedLongVowelShortening2
    .o. OEUnstressedLongVowelShortening3
    .o. OEUnstressedLongVowelShortening5
    .o. OEUnstressedLongVowelShortening6
    .o. OEUnstressedLongVowelShortening7
    .o. OEUnstressedLongVowelShortening8;
```

In prose, the rule shortens the remaining unstressed long vowels before the weak final outcomes settle into their later forms. The broad effect is visible in many weak endings, but the chronology can still be pinned down by a few particularly clear witnesses.

Its chronology is explicit on both sides. If the rule is moved before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), PGmc \emph{*fúrxtīnaz} yields *fyrhten* rather than expected OE *fyrhte* ‘fright’. If the rule is delayed until after [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre* ‘adder’, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder* ‘father’. This shows that [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), and that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

That two-sided relation makes [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) the historical center of the pair. It still depends on earlier weak-tail preparation to the left, but within the local chapter it is the shortening stage that creates the strongest seam.

## SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger OEWeakTailReduction3;
```

In prose, the rule merges unstressed \emph{*æ} with \emph{*e} after shortening has already produced the vulnerable weak final vowels. This is the stage that turns a broad set of final outcomes toward the ordinary OE \emph{-e} spellings.

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre*, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder*. If the rule is delayed until after SC085 OEHLoss, PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. This means that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before SC085 OEHLoss.

The earlier side is broader than the later side, but both are real. That is why this pair works as the strongest local core in the late weak tail. Shortening and merger are adjacent, reciprocal, and still open to meaningful outward cross-reference without having to absorb later material into the chapter.
