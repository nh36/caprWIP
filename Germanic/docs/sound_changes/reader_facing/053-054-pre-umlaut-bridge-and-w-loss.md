# Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

## Historical discussion of early \emph{*w}-loss before umlaut

The two rules gathered here are unequal in weight. The first is a narrow loss of
\emph{*w} after velars in the \emph{*ngw} sequence. Ringe and Taylor make the historical core
clear when they derive PGmc \emph{*singwan} to Old English *singan* ‘sing’
[@RingeTaylor2014, p. 214, §6.4.2]. That gives the change a real comparative anchor, but
it does not turn it into a large chapter of its own. It is the kind of small
local sound change that needs a place in the sequence without claiming the status of a
major handbook law.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The chapter therefore belongs in the
stretch between plain palatalization and the umlautal core, but it should keep
the asymmetry visible: the first rule is a narrow loss in the \emph{*ngw} sequence, and the second is a
stronger glide-loss development with a specific lexical witness.

## SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

The first rule handles the \emph{*ngw} simplification.

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

In prose, the rule removes \emph{*w} after the velar cluster in forms of the
\emph{*singwan} type.

Historically, this is a very small rule. It keeps developments such as *singan*
‘sing’ visible in the sequence, but it does not create a large family of lexical
breakpoints. Current testing does not recover a positive earlier or later
boundary: the search reaches older material on the left and the later Old
English search limit on the right with no decisive wrong form. If the rule is
moved either earlier or later within the tested sequence, no lexical witness yet
provides a sharper wrong/expected pair. The safest reading is therefore modest:
this is a local pre-umlaut rule that belongs before the umlautal chapter without
claiming a sharper chronological slot than the evidence supports.

## SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

The second rule is the more historically legible member of the pair.

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

In prose, the rule removes non-initial \emph{*w} before final unstressed \emph{*i}.

The best witness is *sǣ* ‘sea’. Campbell's discussion of the loss of \emph{*w} before
\emph{*i}, Ringe and Taylor's derivation from earlier \emph{*saiwi-} / \emph{*sawi-}, and Luick's
parallel account all point to the same historical consequence
[@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. The glide has
to disappear early enough for the preceding vowel to continue into the later
fronted and lengthened outcome. If the glide survives too long, the derivation
retains \emph{*w} and misses *sǣ* ‘sea’. If the rule is moved before
[SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), the same witness yields *sǣw* ‘sea’ rather than
expected OE *sǣ*. This shows that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before
[SC054 OEWLossBeforeI](#rule-OEWLossBeforeI). If the rule is delayed until after
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), the same witness again yields *sǣw*
rather than expected *sǣ*. This places [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI)
before [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope).

This is why the chapter belongs immediately before the broader umlautal
developments discussed in [SC055 OEIUmlaut](#rule-OEIUmlaut).
The two rules together form a genuine lead-in to that later vowel chapter, but
only the second has a strong lexical and handbook footing of its own.
