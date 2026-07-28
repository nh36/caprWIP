# West Saxon diphthong sequence

## Historical discussion of the West Saxon diphthong sequence

Four distinct developments shape the West Saxon diphthongal field. Campbell
discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered
diphthongization, and later Anglian smoothing in connected but separate parts
of the vowel history; Hogg likewise distinguishes the palatal-diphthongal
developments [@Campbell1959, pp. 46, 53--54, 65--70, 95--96,
§§120, 135--136, 170--176, 185, 223--227; @Hogg1992, pp. 106--107, 111--112].

The closest interaction joins \emph{ww}-simplification and long-\emph{aw} diphthongization, which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. Diphthong leveling regularizes a wider field, while long-\emph{ew} diphthongization carries \emph{ēow} into the later environment of breaking.

## Historical discussion of WW simplification

West Germanic \emph{ww} sequences lie behind forms such as *dēaw* ‘dew’ and *hēawan* ‘hew’, and Campbell treats them as part of the early West Germanic diphthong history [@Campbell1959, p. 46, §120].

[SC031 OEWWSimplification](#rule-OEWWSimplification) precedes the later
long-diphthong outcomes.

## SC031. Simplification of \emph{*ww} sequences (`OEWWSimplification`) {#rule-OEWWSimplification}

```foma
define OEWWSimplification [
    {*w} {*w} -> {*w}
];
```

The *dēaw* and *hēawan* derivations establish that doubled \emph{w} was simplified before the long \emph{ēaw} development. If [SC031 OEWWSimplification](#rule-OEWWSimplification) follows [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*dáwwō} yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. Earlier placement changes no checked output. The witnesses require simplification before the long-diphthong change and leave the lower boundary to the broader West Saxon chronology.

## Historical discussion of diphthong leveling

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* / *hēawan* developments.

## SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

```foma
define OEDiphthongLeveling [
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
];
```

The two edges of this interval fail differently. Before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*galáubijaną}, \emph{*báug}, and \emph{*bráudą} produce no output (\emph{+?}) instead of expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xáubudą} yields [*hēafud*]{.pred} rather than expected *hēafod* ‘head’. Absence at the lower edge places diphthong leveling after fronting; the wrong surface form at the upper edge places it before medial unstressed-\emph{u} lowering.

## Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from *chew*,
*four*, and *knee* [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The only checked boundary for
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) lies ahead at
[SC044 OEBreaking](#rule-OEBreaking).

## SC033. Long \emph{ēow} before following vowels and weak endings (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The long \emph{ēow} of *ċēowan*, *fēower*, and *cnēow* supplies only a terminus ante quem. If [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) follows [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*kéwwaną} yields [*ċeowan*]{.pred} rather than expected OE *ċēowan* ‘chew’, PGmc \emph{*fédwōr} yields [*feower*]{.pred} rather than expected *fēower* ‘four’, and PGmc \emph{*knéwą} yields [*cneow*]{.pred} rather than expected *cnēow* ‘knee’. Earlier placement changes no checked output. The sources associate \emph{ew} and \emph{iw} with the same diphthongal history but furnish no lower boundary.

## Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* and *hēawan*. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) follows [SC031 OEWWSimplification](#rule-OEWWSimplification) locally and must also precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

A local feeding relation and a later vowel change confine \emph{aw} > \emph{ēaw}. Before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*dáwwō} yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. After [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*skáwōjaną} yields [*sċawian*]{.pred} rather than expected OE *sċēawian* ‘show’, PGmc \emph{*skáwōθi} yields [*sċawaþ*]{.pred} rather than expected *sċēawaþ*, and PGmc \emph{*stráwą} yields [*stræw*]{.pred} rather than expected *strēaw* ‘straw’. The *dēaw* and *hēawan* forms require long-diphthong formation after simplification, while *sċēawian* requires it before brightening; the handbooks assign the same interval to the West Saxon development.
