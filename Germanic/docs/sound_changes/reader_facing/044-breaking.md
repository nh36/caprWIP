# Breaking

## Historical discussion

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment. The *feoh* 'cattle' and
*feohtan* 'fight' type derivations preserve its velar-fricative trigger;
they do not subsequently undergo velar-fricative palatalization.

Fulk cautions that breaking before \emph{h} does not necessarily date
the articulation of \emph{k/g}: the consonantal histories must be
distinguished. His English and later Frisian breaking processes are
also not one inherited event [@Fulk1998, pp. 145--146, 152].

## SC044. Breaking before \emph{h}, \emph{rC}, \emph{lC}, and conditioned \emph{w} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking FootCtx(OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI);
```

Short \emph{e} and \emph{i} also develop short \emph{eo} and
\emph{io} before singleton \emph{w}, except when a high front vowel
or \emph{j} follows it. This is the regular pre-ending history of
*cneowe* 'knee (dat.sg.)', not long-diphthong promotion
[@Luick1914, p. 139, §134; @HoggGrammar2011, p. 86, §5.22;
@RingeTaylor2014, pp. 187--188, §6.2.4].
The shared w conditioner makes that exclusion explicit:

```foma
define EnglishBreakingWContext [
    {*w} [[EnglishStarVocalic | EnglishStarConsonant]
        - [{*i} | {*ì} | {*í} | {*ī} | {*ḯ} | {*j}]] |
    {*w} .#.
];
```

Root stress notation does not determine vowel length. The short
knee dative is the selected comparison; long endingless *cnēo*
'knee' and the restored \emph{w} of *cnēow* 'knee' are separate paradigm
histories, discussed with
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong).

Breaking must encounter the vowel created by brightening and must precede
the rule that would otherwise palatalize its velar trigger in *feoh*
'cattle' and *feohtan* 'fight'. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc [féxu]{.recon} ‘cattle’ yields [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yields [*fehtan*]{.pred} rather than expected *feohtan*. The fronting relation feeds breaking. The fee/fight relation instead protects
breaking's velar trigger from premature palatalization: those forms are
displacement negatives, not live
[SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization)
applications.

## SC044. Stress-sensitive short-i breaking (`OEBreakingI`) {#rule-OEBreakingI}

```foma
define OEBreakingI [
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingRContext,
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingWContext
] .o. [
    {*í} -> {*ío} || _ EnglishBreakingRContext,
    {*í} -> {*ío} || _ EnglishBreakingHContext,
    {*í} -> {*ío} || _ EnglishBreakingWContext,
    {*ì} -> {*io} || _ EnglishBreakingRContext,
    {*ì} -> {*io} || _ EnglishBreakingHContext,
    {*ì} -> {*io} || _ EnglishBreakingWContext
];
```

Breaking is not an ordinary unstressed-vowel development. *fulwiht*
'baptism' and *nawiht* 'nothing' supply independent negative evidence;
the latter has separately explained stressed byforms. A plain vowel can
nevertheless represent the stressed initial nucleus after an earlier
accent-consuming change. This component therefore admits that nucleus,
explicit primary *í*, and preserved subordinate *ì*, but excludes plain
medial *i*. Positive pretonic foot marking retains its existing scope
[@HoggGrammar2011, pp. 217--218, §§6.7--6.8;
@Campbell1959, pp. 54--56, §§139--144; @RingeTaylor2014, pp. 187--188].

In the conditional *seleweard* history the retained medial *i* causes
mutation without breaking and later lowers to *e*. This is a general
stress distinction, not suppression of a diphthong by lexical identity.
The second root's subordinate marker survives until its phonological
consumers; its technical decoding is not a date for obligatory historical
destressing [@Russom2001, pp. 39--64].
