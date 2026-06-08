# The pre-umlaut bridge and loss of *w* before *i*

## Historical discussion

The two rules gathered here are unequal in weight. The first is a narrow loss of
*w after velars in the *ngw sequence. Ringe and Taylor make the historical core
clear when they derive PGmc \emph{*singwan} to Old English *singan* ‘sing’
[@RingeTaylor2014, §6.4.2]. That gives the change a real comparative anchor, but
it does not turn it into a large chapter of its own. It is the kind of small
cleanup rule that needs a place in the sequence without claiming the status of a
major handbook law.

The second rule is historically more legible. Campbell notes the recurring loss
of *w before *i in unstressed position [@Campbell1959, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier *saiwi- / *sawi-
[@RingeTaylor2014, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, §187]. The chapter therefore belongs in the
stretch between plain palatalization and the umlautal core, but it should keep
the asymmetry visible: the first rule is a narrow bridge, the second is a
stronger glide-loss development with a specific lexical witness.

## Loss of *w* after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

The first rule handles the *ngw simplification.

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

In prose, the rule removes *w after the velar cluster in forms of the
\emph{*singwan} type.

Historically, this is a very small rule. It keeps developments such as *singan*
‘sing’ visible in the sequence, but it does not create a large family of lexical
breakpoints. The tested evidence does not fix a narrow place for it within the
later Old English sequence, so the safest reading is modest: this is a local
bridge rule that belongs before the umlautal chapter without claiming a more
precise historical frame than the evidence supports.

## Loss of *w* before final *i* (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

The second rule is the more historically legible member of the pair.

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

In prose, the rule removes non-initial *w before final unstressed *i.

The best witness is *sǣ* ‘sea’. Campbell's discussion of the loss of *w before
*i, Ringe and Taylor's derivation from earlier *saiwi- / *sawi-, and Luick's
parallel account all point to the same historical consequence
[@Campbell1959, §406; @RingeTaylor2014, §6.7.1; @Luick1914, §187]. The glide has
to disappear early enough for the preceding vowel to continue into the later
fronted and lengthened outcome. If the glide survives too long, the derivation
retains *w and misses *sǣ* ‘sea’.

This is why the chapter belongs immediately before the broader umlautal
developments discussed in [the composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).
The two rules together form a genuine bridge into that later vowel chapter, but
only the second has a strong lexical and handbook footing of its own.
