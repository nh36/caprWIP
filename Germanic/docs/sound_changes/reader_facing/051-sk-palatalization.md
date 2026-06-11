# Palatalization of \emph{*sk} to \emph{*sc}

## Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, p. 278, §440]. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@Hogg1992, pp. 106--107, 111--112]. Ringe and Taylor make the same sequence
explicit when they distinguish the earlier palatalization of velars and \emph{*sk} from
the later diphthongization after already palatal consonants
[@RingeTaylor2014, pp. 213--216, §§6.4.1, 6.5.1].

Luick is especially useful for the larger frame. He treats
the cluster change as part of a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
excuse to merge the whole palatalization and umlaut region into one undivided
chapter.

## SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

The implementation states the \emph{*sk} rule explicitly.

```foma
define OESkPalatalization [
    {*s} {*k} -> {*ʃ} || .#. _
] .o. [
    {*s} {*k} -> {*ʃ} || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
] .o. [
    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
] .o. [
    {*s} {*k} -> {*ʃ} || _ {*j}
] .o. [
    {*s} {*k} -> {*ʃ} || {*j} _
];
```

In prose, the rule turns \emph{*sk} into a palatal outcome in the environments
that lead to Old English \emph{*sc}.

Its historical place is between the earlier restoration and the later palatal
vowel developments. If it is moved too early, the forms behind *flasce* ‘flask’
and *wascan* ‘wash’ are fronted too soon, yielding *flæsce* ‘flask’ and
*wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This gives the
earlier result. This shows that [SC046 OEARestoration](#rule-OEARestoration) must come before
[SC051 OESkPalatalization](#rule-OESkPalatalization). If it is moved too late, the cluster no longer feeds the later
West-Saxon diphthongal outcomes that appear in *sċeaft* ‘shaft’, *sċēar*
‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’. That is why
the rule sits naturally beside [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

No single later wrong form is isolated for the whole group of
\emph{*sċea-*} / \emph{*sċie-*} witnesses, but the current notes do show that the cluster
must already be palatalized before the later West-Saxon diphthongal rule
applies. This places [SC051 OESkPalatalization](#rule-OESkPalatalization)
before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

The narrower chapter shape matters. The cluster rule is real and historically
visible, but it is still only one part of the broader palatalizing sequence. The
change should therefore be read as a distinct cluster development inside that
sequence, not as a complete account of Old English palatalization.
