# Back mutation

## Historical discussion

West Saxon *giefan* ‘give’ and *wefan* ‘weave’ stand against non-West-Saxon
*geofad* 'gave' and *weofan* 'weave'. Ringe and Taylor use this contrast to define the
dialectal profile of back mutation [@RingeTaylor2014, p. 319, §6.9.4].
Campbell's treatment of diphthongization before following back vowels includes
*heofon* ‘heaven’ [@Campbell1959, p. 86, §207], while Hogg draws the instructive
comparison with breaking [@HoggPhonology1992, p. 113]. Fulk accordingly separates back
mutation from the earlier umlautal changes [@Fulk2018, p. 69, §4.8].
Barrack likewise states back mutation apart from the earlier mutations, as
his rules 210 and 212 with a continuation at 220
[@Barrack1975, pp. 63--66]; his residual-ordering discussion uses a back
umlaut form, \emph{heolap}, as the worked example of a rule pair whose
formal order must be reversed for a residue (210 against his rule 355.5)
[@Barrack1975, p. 36], which illustrates his insistence that such orderings
are logical rather than chronological relations [@Barrack1975, p. 34].

## SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

```foma
define OEBackMutation FootCtx([
    {*e} -> {*eo} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]) .o. Ctx([
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*è} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*ǽ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]);
```

Three witness forms bracket the chronology. If back mutation precedes
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), forms such as
[gébaną]{.recon} ‘give’ produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. [stélaną]{.recon} ‘steal’ likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. At the other edge, delaying
back mutation until after
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) makes
[wébaną]{.recon} ‘weave’ yield *weofan* ‘weave’; the expected form is *wefan* ‘weave’.
Thus back mutation follows secondary nasalization but precedes the weak-tail
reductions.

## Stress and the compound linker

Restoration and back mutation must distinguish the stressed target from
the following vowel that conditions it. Purnell, Raimy and Salmons
explicitly state a stressed front-vowel target, including short
\emph{æ} [@PurnellRaimySalmons2019, pp. e461--e463].
West Saxon *ealu* 'ale' supplies a relevant short-\emph{æ} comparison
within a liquid environment: Hogg explains its earlier \emph{*ælu}
through mutation in the inflected paradigm, not Mercian second fronting
[@HoggGrammar2011, pp. 156--157, §5.106 and n.6].

Under the inherited analysis of *reġnboga* 'rainbow', the unstressed
linker need undergo neither [SC046 OEARestoration](#rule-OEARestoration)
nor [SC059 OEBackMutation](#rule-OEBackMutation). It can remain short \emph{æ} until
[SC114 OENonHighSyn](#rule-OENonHighSyn), while the subordinate root's
\emph{o} has already arisen by
[SC017 PNWGmcULowering](#rule-PNWGmcULowering). This joint restriction
reaches the selected endpoint; restricting restoration alone instead
exposes the linker to back mutation.
The adopted joint implementation preserves the relevant secondary
low/front annotation through syncope rather than infer stress from an
unmarked medial vowel. Later weak-vowel processing remains a limitation
for constructed subordinate-root controls, not a dated stress-loss law.
The compound's spelling does not distinguish this inherited history from
later composition of the developed rain and bow words.
