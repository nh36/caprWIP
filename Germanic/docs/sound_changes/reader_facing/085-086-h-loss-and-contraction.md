# H-loss and contraction

## Historical discussion of h-loss and contraction

When [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, it creates
hiatus. [SC086 OEContraction](#rule-OEContraction) immediately resolves the
resulting vowel sequence.

Ringe and Taylor describe this late sequence of \emph{h}-loss and contraction
[@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk places the contracted
verbs in a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick
describes the corresponding West Germanic contractions [@Luick1914, p. 165].

## SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon* ‘draw’, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. These outputs require [SC085 OEHLoss](#rule-OEHLoss) to follow [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) and precede [SC086 OEContraction](#rule-OEContraction).

The earlier boundary rests on one witness; the four later witnesses establish
the immediate relation to contraction.

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

The rule contracts the vowel sequences created after \emph{h}-loss, producing
*flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Moving contraction before [SC085 OEHLoss](#rule-OEHLoss) makes PGmc \emph{*fléuxaną} yield *flēoan* rather than expected OE *flēon*, PGmc \emph{*sláxaną} yield *sleaan* rather than expected *slēan*, PGmc \emph{*téxun} yield *teoon* rather than expected *tēon*, and PGmc \emph{*táixōn} yield *tāe* rather than expected *tā*. The derivations require [SC086 OEContraction](#rule-OEContraction) to follow [SC085 OEHLoss](#rule-OEHLoss). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
The more distant [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
relation establishes only that weak-tail reduction precedes contraction.
