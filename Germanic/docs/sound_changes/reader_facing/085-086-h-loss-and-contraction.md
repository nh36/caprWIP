# H-loss and contraction

## Historical discussion of h-loss and contraction

This adjacent pair is the clearest compact core in the closing cluster. The interaction is direct. Once [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, the derivation is left with hiatus that [SC086 OEContraction](#rule-OEContraction) immediately resolves. That derivational dependence is exactly the kind of close interaction that justifies one shared historical discussion.

The pair is also stronger and more book-legible than the more technical three-rule chain to its left. Ringe and Taylor give the clearest modern account of the late sequence of \emph{h}-loss and contraction [@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk's discussion of contracted verbs places the same outcomes into a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick's treatment of West Germanic contractions gives older grammatical support for the same family of outcomes [@Luick1914, p. 165].

## SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

The implementation keeps the consonant loss as one explicit rule.

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

In prose, the rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

Its chronology is explicit on both sides. If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon* ‘draw’, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. This shows that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss), and that [SC085 OEHLoss](#rule-OEHLoss) must come before [SC086 OEContraction](#rule-OEContraction).

The earlier side is narrow, but the later side is a tight four-row reciprocal seam that clearly feeds the following contraction rule.

## SC086. Contraction of the resulting hiatus (`OEContraction`) {#rule-OEContraction}

The following rule contracts the hiatus left by [SC085 OEHLoss](#rule-OEHLoss).

```foma
define OEContraction [
    {*a} {*a} -> {*ā},
    {*e} {*e} -> {*ē},
    {*i} {*i} -> {*ī},
    {*o} {*o} -> {*ō},
    {*u} {*u} -> {*ū},
    {*ea} {*a} -> {*ēa},
    {*ēa} {*a} -> {*ēa},
    {*eo} {*a} -> {*ēo},
    {*ēo} {*a} -> {*ēo},
    {*eo} {*o} -> {*ēo},
    {*ēo} {*o} -> {*ēo},
    {*éo} {*o} -> {*ḗo},
    {*ḗo} {*o} -> {*ḗo},
    {*ā} {*a} -> {*ā},
    {*ā} {*e} -> {*ā},
    {*ē} {*a} -> {*ē},
    {*ē} {*e} -> {*ē},
    {*ḗ} {*a} -> {*ḗ},
    {*ḗ} {*e} -> {*ḗ},
    {*ī} {*a} -> {*ī},
    {*ī} {*e} -> {*ī},
    {*ḯ} {*a} -> {*ḯ},
    {*ḯ} {*e} -> {*ḯ},
    {*ō} {*a} -> {*ō},
    {*ō} {*e} -> {*ō},
    {*ū} {*a} -> {*ū},
    {*ū} {*e} -> {*ū}
];
```

In prose, the rule contracts the vowel sequences created after \emph{h}-loss. This is the step that turns over-long transitional forms into outcomes such as *flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Its earlier boundary is the reciprocal side of the [SC085 OEHLoss](#rule-OEHLoss) relation. If the rule is moved before [SC085 OEHLoss](#rule-OEHLoss), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon*, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan*, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon*, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC085 OEHLoss](#rule-OEHLoss) must come before [SC086 OEContraction](#rule-OEContraction).

That one-sided profile is still substantial because the earlier reciprocal seam is so clear. The already visible [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) relation also points here, but it remains a cross-reference, not a reason to absorb [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) into the same chapter.
