# Contraction after h-loss

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

Moving contraction before [SC085 OEHLoss](#rule-OEHLoss) makes PGmc [fléuxaną]{.recon} ‘flee’ yield [*flēoan*]{.pred} rather than expected OE *flēon* 'flee', PGmc [sláxaną]{.recon} ‘slay’ yield [*sleaan*]{.pred} rather than expected *slēan* 'slay', PGmc [téxun]{.recon} ‘draw’ yield [*teoon*]{.pred} rather than expected *tēon* 'draw', and PGmc [táixōn]{.recon} ‘toe’ yield [*tāe*]{.pred} rather than expected *tā* 'toe'. The derivations require [SC086 OEContraction](#rule-OEContraction) to follow [SC085 OEHLoss](#rule-OEHLoss). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
The more distant [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
relation establishes only that weak-tail reduction precedes contraction.
