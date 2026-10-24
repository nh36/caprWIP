# Unstressed ae-merger

## SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger SentenceCtx([
    [{*æ} -> {*e} || .#. {*ᶠ} OEAnyConsonant* _]
    .o. FootCtx(OEWeakTailReduction3)
]);
```

The rule merges unstressed \emph{*æ} with \emph{*e} after shortening has
produced the weak final vowels, yielding the ordinary OE \emph{-e} spellings.

Pretonic vowels also participate. A positively identified weak initial
syllable is eligible without the preceding-vowel condition appropriate
to post-tonic endings. The superscript `*ᶠ` records this prosodic
information, not a segment or a grammatical prefix. Stressed roots are
not thereby included in the merger. Later lowering of pretonic
\emph{*i}, including the early *gi-* of *gistīga* 'climb into/onto',
belongs to [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction);
Hogg places it marginally after the earlier merger
[@Campbell1959, pp. 153--155, §§369--370;
@HoggGrammar1992, §§6.50--6.54 (held 2011 reprint, pp. 237--239);
@RingeTaylor2014, pp. 334--335].

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* 'adder', and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* 'father'. If the rule is delayed until after [SC085 OEHLoss](#rule-OEHLoss), PGmc [táixōn]{.recon} ‘toe’ yields [*tāæ*]{.pred} rather than expected OE *tā* ‘toe’. These failures show that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss).

The lexical evidence fixes the local order after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and places the merger before the later h-loss and contraction.
