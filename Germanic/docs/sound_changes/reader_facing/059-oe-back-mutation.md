# Back mutation

## Historical discussion

Back mutation is the substantive center of this part of the sequence. Campbell treats
it as a later Old English diphthongizing development before following back
vowels, and his examples already show why forms such as *heofon* ‘heaven’ are
historically legible outcomes in their own right
[@Campbell1959, p. 86, §207]. Hogg treats the same development as a later change with
clear parallels to breaking [@Hogg1992, p. 112]. Ringe and Taylor sharpen the
picture by distinguishing West Saxon forms such as *giefan* ‘give’ and *wefan*
‘weave’ from non-West-Saxon forms such as *geofad* and *weofan*
[@RingeTaylor2014, p. 319, §6.9.4]. Fulk likewise treats back mutation as a distinct
historical phenomenon with its own profile beside the earlier umlautal
changes [@Fulk2018, p. 69, §4.8].

That makes back mutation different from the short notes that follow it. Back
mutation belongs to the same local stretch of the sequence, but it carries more
historical weight and clearer lexical consequences. Even so, its later relation
lies beyond this immediate stretch of the sequence, and the later weak-tail
region is best kept as a forward reference only.

## SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

The implementation keeps the change as one explicit rule.

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
```

In prose, the rule backs and diphthongizes earlier front vowels before a
following labial or liquid plus a back-vocalic trigger.

Its chronology is real on both sides, but not equally local. The earlier side is
already fixed by the preceding vowel and weak-tail material. If the rule is
moved too early, forms such as \emph{*gébaną} produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. \emph{*stélaną} likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. The later side is different. If
the rule is pushed too far to the right, \emph{*wébaną} yields *weofan*
‘weave’; the expected form is *wefan* ‘weave’.
That later edge is real, but it points beyond the present stretch of the sequence into the
later weak-tail reductions, so here it should remain only a forward reference.

These lexical failures show that SC048 OESecondaryNasalization must come before
[SC059 OEBackMutation](#rule-OEBackMutation) and that
[SC059 OEBackMutation](#rule-OEBackMutation) must come before
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction).

This is why the change can serve as the center here without implying that the
following weak-tail notes belong to the same historical law. The rule
marks a real local seam, but the section after it immediately becomes narrower.
