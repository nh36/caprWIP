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
    {*e} -> {*eo} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] {*u}
]) .o. FootCtx([
    {*æ} -> {*ea} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]) .o. Ctx([
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
]) .o. Ctx([
    {*è} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
]) .o. Ctx([
    {*ǽ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]);
```

The older displacement tests produce predicted \emph{*ġeofan},
\emph{*steolan} and \emph{*weofan} when mutation precedes
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization).
These remain observations about the previous parallel-clause
implementation, not independent West Saxon chronology. Its shared
replacement contexts admitted an a-trigger for e despite the written
u-only condition. The separately composed clauses above enforce each
stated environment: eligible e mutates before u but retains e before a.
The corrected reversal removes the steal/weave difference while
preserving all selected outputs. West Saxon e/u mutation must be distinguished from non-West-
Saxon e/a mutation [@RingeTaylor2014, pp.319--327, especially p.325;
@HoggGrammar2011, pp.149--157, §§5.103--5.106].
The recorded later displacement across
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction), yielding predicted
\emph{*weofan}, likewise belongs to the previous implementation.
With the corrected relation, that late placement instead loses mutation
in *heofon*, *meoloc* 'milk', *seofon* 'seven' and *weorold* 'world':
their medial u triggers have already become o, whereas final u still
licenses mutation in *speoru* 'spear'. This is a dependency of the
serialized cascade, not proof that weak-tail reduction itself was the
historical boundary. The source's broader mutation chronology is not
decided by either displacement.

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
