# West Saxon diphthong sequence

## Historical discussion of the West Saxon diphthong sequence

The four rules gathered here belong to one West Saxon diphthongal zone, but they do not all arise from a single historical event. Campbell discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered diphthongization, and later Anglian smoothing in connected but separate parts of the vowel history, and Hogg likewise treats the palatal-diphthong side as real yet uneven [@Campbell1959, pp. 46, 53--54, 65--70, 95--96, §§120, 135--136, 170--176, 185, 223--227; @Hogg1992, pp. 106--107, 111--112].

The closest interaction inside the sequence is between [SC031 OEWWSimplification](#rule-OEWWSimplification) and [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) and [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) still belong here, but they point to different parts of the same history: [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) regularizes a wider diphthongal field, while [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) carries the long \emph{ēow} side into the later environment of [SC044 OEBreaking](#rule-OEBreaking).

## Historical discussion of WW simplification

West Germanic \emph{ww} sequences lie behind forms such as *dēaw* ‘dew’ and *hēawan* ‘hew’, and Campbell treats them as part of the early West Germanic diphthong history [@Campbell1959, p. 46, §120].

[SC031 OEWWSimplification](#rule-OEWWSimplification) is the first explicit step in that sequence. It is small in form, but the later long-diphthong outcomes depend on it.

## SC031. Simplification of \emph{*ww} sequences (`OEWWSimplification`) {#rule-OEWWSimplification}

The implementation states the simplification directly.

```foma
define OEWWSimplification [
    {*w} {*w} -> {*w}
];
```

In prose, the rule reduces a doubled \emph{w} to a single \emph{w}. That simplification is what allows the later \emph{ēaw} rule to work with the shape seen in *dēaw* and *hēawan*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. This shows that [SC031 OEWWSimplification](#rule-OEWWSimplification) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong). A farther-left computational break is also visible: PGmc \emph{*fédwōr} yields *fēowwer* instead of expected OE *fēower* ‘four’, and PGmc \emph{*xáwwją} yields *hēai* instead of expected *hīeġ* ‘hay’. Because that break appears only before the earlier sequence is divided into ordinary historical rules, it does not identify a normal earlier boundary for [SC031 OEWWSimplification](#rule-OEWWSimplification).

## Historical discussion of diphthong leveling

By the time the sequence reaches forms such as *hēafod* ‘head’, diphthongal outcomes are already being redistributed across a wider set of words. Campbell's discussion of smoothing and related later monophthongization is the clearest handbook anchor for that layer of the history, even though the rule kept here is more tightly drawn than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

This makes [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) a real member of the sequence, even if its evidence is less self-contained than the *dēaw* / *hēawan* pair.

## SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

The implementation keeps the leveling rule explicit.

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

In prose, the rule regularizes several diphthongal outcomes into the West Saxon patterns that appear later in the sequence. It is the step that helps keep forms such as *hēafod* ‘head’ in their expected shape.

Its chronology is explicit on both sides. If the rule is moved before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*galáubijaną}, \emph{*báug}, and \emph{*bráudą} fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xáubudą} yields *hēafud* rather than expected *hēafod* ‘head’. This shows that [SC030 OEAuFronting](#rule-OEAuFronting) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), and that [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). The earlier side is real, but it is expressed as failed derivations rather than as alternate surface forms.

## Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow* ‘knee’ belong to the same West Saxon vowel region, though their clearest ordering relation points forward. Campbell's treatment of early \emph{eu} in Old English and Ringe and Taylor's examples from *chew*, *four*, and *knee* show that this is a real part of the diphthong history [@Campbell1959, pp. 53--54, §136; @RingeTaylor2014, pp. 188, 202].

That makes [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) an essential member of the sequence, even though its strongest boundary lies ahead at [SC044 OEBreaking](#rule-OEBreaking).

## SC033. Long \emph{ēow} before following vowels and weak endings (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

The implementation states the long-diphthong development directly.

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

In prose, the rule turns \emph{ew} and \emph{iw} sequences into long \emph{ēow}. This is the step behind forms such as *ċēowan*, *fēower*, and *cnēow*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*kéwwaną} yields *ċeowan* rather than expected OE *ċēowan* ‘chew’, PGmc \emph{*fédwōr} yields *feower* rather than expected *fēower* ‘four’, and PGmc \emph{*knéwą} yields *cneow* rather than expected *cnēow* ‘knee’. This shows that [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) must come before [SC044 OEBreaking](#rule-OEBreaking). A farther-left computational break also appears when the search reaches undivided earlier material: PGmc \emph{*fédwōr} yields *feower* instead of *fēower*. Because that break does not cross an ordinary historical rule, it does not identify a normal earlier boundary for [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong).

## Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* and *hēawan*. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) therefore closes the nearest local pair in the chapter and also points onward to [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

The implementation keeps the long-\emph{ēaw} step explicit.

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

In prose, the rule turns \emph{aw} before a following vowel into long \emph{ēaw}. This is the stage that yields forms such as *dēaw* and *hēawan*.

Its chronology is explicit on both sides. If the rule is moved before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. If it is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*skáwōjaną} yields *sċawian* rather than expected OE *sċēawian* ‘show’, PGmc \emph{*skáwōθi} yields *sċawaþ* rather than expected *sċēawaþ*, and PGmc \emph{*stráwą} yields *stræw* rather than expected *strēaw* ‘straw’. This shows that [SC031 OEWWSimplification](#rule-OEWWSimplification) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), and that [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).
