# Post-apocope \emph{*n}-loss and medial syncope

## Historical discussion of post-apocope \emph{*n}-loss and medial syncope

Evidence for post-apocope reduction is strikingly uneven. The inherited
\emph{*furht-} family makes the survival of one nasal diagnostic and fixes both
sides of stem-final n-loss [@Kroonen2013, p. 201]. No comparable witness orders
the medial syncope that follows. Hogg, Ringe and Taylor, and Fulk describe both
processes within the late history of weak syllables
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

## SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

```foma
define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];
```

Only final \emph{*n} after long \emph{*ī} is at issue, as in the inherited
family behind *fyrhte* ‘fright’.

The same proto-form fixes both edges. Before
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc
\emph{*fúrxtīnaz} yields *fyrhten* rather than expected OE *fyrhte* ‘fright’.
After [SC072
OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc
\emph{*fúrxtīnaz} again yields *fyrhten* rather than expected *fyrhte*. I
therefore order final bare-a loss, stem-final n-loss, and unstressed long-vowel
shortening in that sequence. Both boundaries are firm within the derivation,
but depend upon one lexical family.

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

Loss of medial \emph{*i} before dentals belongs to the late weak-tail history
described by Hogg, Ringe and Taylor, and Fulk
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

```foma
define OEMedialSyncope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
];
```

No diagnostic word establishes a local chronology. Moving medial syncope to
either end of the tested range leaves every checked output unchanged. Its
handbook placement after apocope and before later cluster simplification
therefore remains preferable, but the present lexicon cannot demonstrate it.
