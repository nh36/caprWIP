# The Old English i-umlaut and West Saxon palatal diphthongization

## Historical discussion of i-umlaut \CAPRHeadingBreak and West Saxon palatal diphthongization

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> [@Luick1914, pp. 166--167, §182]

Campbell gives the most compact classical formulation in English when he writes
that “the process known as i-umlaut or i-mutation operates on practically all
the sounds which it could theoretically affect in OE” [@Campbell1959, p. 69,
§190]. He immediately defines the core conditioning environment as a following
`i` or `j`, and he goes on to trace the consequences across much of the vowel
system, including forms such as *giest* ‘guest’, *giefan* ‘give’, *hierde*
‘shepherd’, and *ieldra* ‘older’ [@Campbell1959, pp. 69--72, §§190--197].

Hogg continues in the same vein: “we come now to a change which is almost as
uncontroversial as it is important” [@Hogg1992, p. 112]. His examples, such as
*bryd* ‘bride’, *trymman* ‘strengthen’, *bedd* ‘bed’, *ciest* ‘chest’, and
*wiersa* ‘worse’, likewise emphasize that the change is a broad redistribution
of vowel quality across the Old English vowel system [@Hogg1992,
pp. 112--114].

The narrower palatal-diphthongal material is described differently. Ringe and
Taylor treat West-Saxon diphthongization after initial palatals as a distinct
process [@RingeTaylor2014, p. 215, §6.5.1], and Fulk is even more explicit about
its chronological delicacy when he calls it “diphthongization by initial
palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13]. Ringe and Taylor’s examples such as *gieldan* ‘pay’,
*scield* ‘shield’, and *scieppan* ‘create’ show that this narrower process is
triggered by already palatal consonants and leads to specifically West-Saxon
diphthongal outputs [@RingeTaylor2014, pp. 215--216, §6.5.1].

Luick, Campbell, and Hogg treat i-umlaut as a system-wide change. Ringe and
Taylor and Fulk distinguish from it a narrower West-Saxon process affecting
words after initial palatals. The two changes act in different environments and
produce different lexical consequences.

## SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

```foma
define OEIUmlautFronting [
    {*a} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ā} -> {*ǣ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*e} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*o} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ō} -> {*ē} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*u} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ū} -> {*ȳ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*á} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*é} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ó} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ú} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

The breadth of i-umlaut appears in lexical classes that share only a following high front vocoid. The forms *fylgan* ‘follow’, *gylden* ‘golden’, *wyrm* ‘worm’, and *giest* ‘guest’ exemplify the same `i`- or `j`-conditioned fronting across different vowels [@RingeTaylor2014, p. 222, §6.6.1; @Campbell1959, pp. 69--72, §§190--191].

The cow and lung forms establish the lower boundary. If fronting precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields *ċȳ* 'cows' rather than expected OE *cȳ* 'cows', and [lúnganjō]{.recon} ‘lungs’ yields *lunġen* 'lungs' rather than expected OE *lungen* 'lungs'. The consonantal change must therefore precede fronting.

The gift and sheath forms establish the upper boundary. If West Saxon palatal diphthongization precedes fronting, PGmc [géftiz]{.recon} ‘gift’ yields *ġieft* 'gift' rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields *sċǣþ* 'sheath' rather than expected *sċēaþ* 'sheath'. Fronting consequently follows velar palatalization and precedes the West Saxon change; the other components of i-umlaut share those bounds.

## SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Raising of umlauted `æ` to `e` continues the same assimilatory event as fronting and therefore shares the chronology of general i-umlaut.

The same four forms fix both boundaries. If raising precedes velar palatalization, [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} instead of expected *cȳ* 'cows' and [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} instead of expected *lungen* 'lungs'. If West Saxon palatal diphthongization precedes raising, [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. These forms place raising after velar palatalization and before West Saxon palatal diphthongization.

The sources do not describe umlaut as simple fronting alone. Campbell notes that
the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@Hogg1992, p. 112].

## SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

```foma
define OEIUmlautDiphthong [
    {*ea} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēa} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*io} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*īo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*eo} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éa} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éo} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ío} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Diphthongal outcomes belong to the same system-wide assimilation as simple-vowel fronting and raising. All three therefore belong to a single historical event.

The relevant examples are the recurring West-Saxon `ie` forms cited in the
handbooks, including *giest* ‘guest’, *giefan* ‘give’, and *hierde*
‘shepherd’ in Campbell and *ciest* ‘chest’ in Hogg
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @Hogg1992,
pp. 112--114]. These diphthongal outcomes form a distinct part of the general
umlautal development alongside simple fronting.

The chronology comes from the cow/lung and gift/sheath contrasts. Placed before velar palatalization, diphthongal mutation over-palatalizes [kūi]{.recon} ‘cow’ and [lúnganjō]{.recon} ‘lungs’; placed after West Saxon palatal diphthongization, it yields *ġieft* 'gift' and *sċǣþ* 'sheath' instead of expected *ġift* 'gift' and *sċēaþ* 'sheath'. These failures place diphthongal mutation after velar palatalization and before West Saxon palatal diphthongization.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The lower boundary is consonantal. If general umlaut precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields *ċȳ* 'cows' rather than expected *cȳ* 'cows', and PGmc [lúnganjō]{.recon} ‘lungs’ yields *lunġen* 'lungs' rather than expected *lungen* 'lungs'. These over-palatalized forms place general umlaut after velar palatalization.

The upper boundary separates general umlaut from the narrower West Saxon process. If West Saxon palatal diphthongization precedes umlaut, PGmc [géftiz]{.recon} ‘gift’ yields *ġieft* 'gift' rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields *sċǣþ* 'sheath' rather than expected *sċēaþ* 'sheath'. Together the two witness pairs place general umlaut after velar palatalization and before the West Saxon process.

## SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

West Saxon *gieldan* ‘pay’, *scield* ‘shield’, and *scieppan* ‘create’ show diphthongization after an already palatal consonant [@RingeTaylor2014, pp. 215--216, §6.5.1]. Their dialectal and phonological restriction separates this development from system-wide i-umlaut.

Hogg's *giefan* ‘give’ and *sceap* ‘sheep’ belong to the same palatal-consonant environment [@Hogg1992, pp. 108--109]. Fulk likewise assigns this diphthongization a place before front mutation and distinguishes the two processes [@Fulk2018, p. 74, §4.13].

The forms *ġift* ‘gift’ and *sċēaþ* ‘sheath’ fix the lower boundary. If West Saxon palatal diphthongization precedes general i-umlaut, PGmc [géftiz]{.recon} ‘gift’ yields *ġieft* ‘gift’ rather than expected *ġift*, and PGmc [skáiθiz]{.recon} ‘sheath’ yields *sċǣþ* ‘sheath’ rather than expected *sċēaþ*. These witnesses place West Saxon palatal diphthongization after general umlaut; no tested lexical item supplies a later terminus ante quem.

The one-sided chronology reflects the difference in scale. General umlaut reorganizes the vowel system, whereas West Saxon palatal diphthongization affects a narrower dialectal class after palatal consonants. Its exact later placement remains undemonstrated by the present lexicon.
