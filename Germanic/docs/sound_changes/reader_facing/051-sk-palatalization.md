# Palatalization of \emph{*sk} to \emph{*sc}

## Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, pp. 177--178, §440]. Barrack
treats the cluster in the same zone as his 440 series: 440a summarizes the
developments [@Barrack1975, pp. 112--113] and 440c states the
palatalization of \emph{*sk} itself [@Barrack1975, p. 113], kept beside, but
distinct from, plain velar palatalization (his rule 170a)
[@Barrack1975, p. 57], in agreement with the structural placement adopted
here. He also registers the typologically separate Late West Saxon
metathesis of the cluster in \emph{fiscas}/\emph{fixas} 'fishes' as rule
440b [@Barrack1975, p. 113], a written-period development that presupposes
the earlier palatalization boundary rather than contradicting it. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@HoggPhonology1992, pp. 106--108, 113]. Ringe and Taylor make the same sequence
explicit when they distinguish the earlier palatalization of velars and \emph{*sk} from
the later diphthongization after already palatal consonants
[@RingeTaylor2014, pp. 213--216, §§6.4.1, 6.5.1].

Luick places the cluster change within a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
identity between the cluster change and the later umlautal developments.

## SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

```foma
define OESkPalatalization Ctx([
    {*s} {*k} -> {*ʃ} || .#. _
] .o. [
    {*s} {*k} -> {*ʃ} || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
] .o. [
    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
] .o. [
    {*s} {*k} -> {*ʃ} || _ {*j}
] .o. [
    {*s} {*k} -> {*ʃ} || {*j} _
]);
```

The displacement of cluster palatalization before
[SC046 OEARestoration](#rule-OEARestoration) now changes *wascan* 'wash'
to [wæsċan]{.pred}; wash remains the current lower-boundary witness.
The old flask displacement belonged to an implementation that retained
its final nasal vowel through restoration. After the earlier ending
merger, the nominative already has a front root and gives
\emph{*flæsċe} in either order. Attested *flasce* 'flask' has an
explicitly sourced levelling analysis, after inflected *flascan* 'flask'
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161].
It must not be used as if its former executable agreement independently
proved a regular back-root nominative history. The consonantal history
of the paradigm remains distinct from that proposed root-vowel levelling.

Regular alternatives remain open, as explained in the
[weak-paradigm comparison](#weak-n-paradigms-after-apocope).
Moving only the following-vowel clause before final \emph{*ā}-fronting,
with retention or early retraction of \emph{*a} before
\emph{*skā}, derives *flasce* without the overextension to *wascan*.
That is a computational result, not independent evidence for the
new order. Wright and Wright's retention account includes other clusters,
and does not establish this narrow condition
[@Wright1908, pp. 37--38, §57].

Campbell specifically requires medial palatalization before all front
vowels, including *wasċe* 'I wash', *þersċe* 'I thresh' and *disċes*
'dish', while retaining the cluster in back-vowel *discas* 'dishes'
[@Campbell1959, pp. 177--178, §§440--441]. A high-front-only
following-vowel trigger loses the first two palatals even though it
fits the selected corpus. Conversely, the present preceding-front-vowel
clause creates a palatal cluster in a structural *discas* control in
both regular nominative variants. This unresolved conditioning must
not be hidden by their improved flask output, or by changing the
selected comparator.

Five witnesses establish the upper boundary collectively. The palatal cluster must already underlie *sċeaft* ‘shaft’, *sċēar* ‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’ before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). The \emph{*sċea-* 'sea'}/\emph{*sċie-*} set therefore places cluster palatalization before the West Saxon vowel change. The cluster change occupies the same palatalization zone as [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) while remaining distinct from plain-velar palatalization and the later vowel changes.
