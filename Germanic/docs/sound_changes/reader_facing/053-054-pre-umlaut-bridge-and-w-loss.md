# Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

## Historical discussion

The first rule is a narrow loss of \emph{*w} after velars in the \emph{*ngw}
sequence. Ringe and Taylor derive PGmc [singwan]{.recon} ‘sing’ to Old English *singan*
‘sing’ [@RingeTaylor2014, p. 214, §6.4.2]. This comparative evidence establishes
the change, although no lexical evidence fixes its order relative to a neighboring
rule.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The first rule is restricted to
the \emph{*ngw} sequence; the second has a specific lexical witness and defined
earlier and later limits.

## SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

The comparative development `*singwan > singan` establishes narrow post-velar \emph{*w}-loss in the \emph{*ngw} sequence, yielding *singan* ‘sing’. Moving [SC053 OEPostVelarWLoss](#rule-OEPostVelarWLoss) earlier or later leaves every output unchanged. Its pre-umlaut position therefore rests on comparative evidence, while the present lexicon supplies no neighboring boundary.

## SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

The history of *sǣ* ‘sea’ explains why non-initial \emph{*w} disappeared before final unstressed \emph{*i}. Campbell describes the loss, Ringe and Taylor derive the form from \emph{*saiwi-}/\emph{*sawi-}, and Luick gives the parallel trajectory [@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. Loss of the glide allowed the preceding vowel to undergo the later fronting and lengthening.

The same witness supplies two distant limits. Before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) or after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI) yields [*sǣw*]{.pred} rather than expected OE *sǣ* 'sea'. The loss must therefore follow final \emph{z}-deletion and precede high-vowel apocope, while its exact position within that broad interval remains source-based.
