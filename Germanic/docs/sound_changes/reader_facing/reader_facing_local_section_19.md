# A sequence from early West Germanic consonant and vowel shifts to Old English r-metathesis

## Introduction

The sequence begins with early West Germanic consonant and vowel changes and ends with Old English r-metathesis.

Rhotacism, brightening, breaking, umlaut, and apocope alternate with narrowly conditioned changes whose relative order rests on particular witness words.

The evidence ranges from broadly attested sound laws to lexical constraints that establish only one chronological boundary.

## Numbering note

The sequence follows the established rule numbering.

SC038, SC062, and SC084 mark technical or prosodic stages rather than sound changes; SC077 is unused.

# West Germanic rhotacism

## Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

The label [SC003 PGmcRhotacism](#rule-PGmcRhotacism) is historically misleading: the change is a later West Germanic rhotacism, not a Proto-Germanic one. It is also distinct from [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant becomes \emph{*r}.

## SC003. West Germanic rhotacism (`PGmcRhotacism`) {#rule-PGmcRhotacism}

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

Breaking supplies the decisive upper boundary. If rhotacism is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc [líznōjaną]{.recon} ‘learn’ yields [*lirnian*]{.pred} rather than expected OE *liornian* ‘learn’, PGmc [líznōθi]{.recon} ‘learns’ yields [*lirnaþ*]{.pred} rather than expected *liornaþ* 'learns', PGmc [líznô]{.recon} ‘learn’ yields [*lirna*]{.pred} rather than expected *liorna* 'learn', and PGmc [mízdai]{.recon} ‘meed’ yields [*merde*]{.pred} rather than expected OE *meorde* ‘meed’. Moving rhotacism earlier within the tested range changes none of the checked forms.

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. Its placement after the earlier loss of final \emph{*z} rests on the historical analyses cited above.

\newpage

# Proto-West-Germanic ai-monophthongization

## Historical discussion

Ringe and Taylor treat the reduction of unstressed \emph{*ai} as one of the major early vowel shifts shared across the Northwest Germanic area [@RingeTaylor2014, pp. 40--41].

The historical support is strongest for unstressed \emph{*ai}, especially word-finally. The rule extends the change to nonfinal \emph{*ai > *ā}, a generalization stated more sharply than in the current handbook discussion.
Both developments have inherited \emph{*ai} as their input.

## \CAPRRuleHeading{SC004. Proto-West-Germanic ai-monophthongization}{PWGmcAiMonophthongization} {#rule-PWGmcAiMonophthongization}

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

The soul form fixes the relation to interstress raising. If monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} ‘soul’ yields [*sāwel*]{.pred} rather than expected OE *sāwol* ‘soul’. No earlier placement changes a checked output.

This witness proves that monophthongization preceded interstress raising; it says nothing about the date of the wider nonfinal \emph{*ai > *ā} generalization. The word-final merger with long mid \emph{*ē} belongs among the early Northwest Germanic vowel shifts; the broader chronology remains less certain.

\newpage

# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`NWGmcAToUBeforeM`) {#rule-NWGmcAToUBeforeM}

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [skúldramiz]{.recon} ‘shoulders’ yields [*sċoldrum*]{.pred} rather than expected OE *sċuldrum* 'shoulders'; earlier placements converge on the expected output. The `shoulder` family therefore tests the chronology, while the inflectional endings justify restricting the change to noninitial unstressed material before \emph{*m}.

The evidence is confined to inflectional
material.

\newpage

# Early i-apocope

## Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* 'troop' and *geogup* 'youth' examples belong to the same pattern [@Campbell1959, §332].

The ending vowel disappears in a weak suffixal environment early enough to block later umlaut. This anti-umlaut chronology distinguishes the change from later final-vowel losses.

## SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

The absence of umlaut in *geoguþ* ‘youth’ provides the historical argument for early deletion. The ordered derivation supplies a different test: if apocope is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċēaweþ*]{.pred} rather than expected OE *sċēawaþ* 'shows'.

Early i-apocope must therefore precede the long-diphthong development. Moving it earlier within the tested range leaves every checked output unchanged; its early date rests on the anti-umlaut evidence, not on a lower boundary supplied by the witness words.

\newpage

# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development and illustrate it above all with the families behind *fēower* ‘four’ and *wæter* ‘water’ [@RingeTaylor2014, pp. 58--59].

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## \CAPRRuleHeading{SC007. Lowering of final bimoric \emph{*ō} before \emph{*r}}{PWGmcFinalOrLowering} {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc [wátōr]{.recon} ‘water’ yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no checked output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. The *fēower* ‘four’ and *wæter* ‘water’ families support the narrow environment before word-final \emph{*r}; no broader lowering of \emph{*ō} is attested.

\newpage

# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57].

The historical support rests on a small witness set. Both coronal inputs
assimilate before \emph{*w}, but only the numeral and the pronominal forms
directly support the generalization.

## \CAPRRuleHeading{SC008. Assimilation of coronal consonants before \emph{*w}}{PWGmcCoronalWAssimilation} {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation must create \emph{*ww} while simplification can still reduce it. If [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [fédwōr]{.recon} ‘four’ yields [*fēowwer*]{.pred} rather than expected OE *fēower* ‘four’. Earlier placements alter no checked output.

The numeral fixes that relative order. The pronouns extend both input clusters beyond `four`; the earlier boundary remains undetermined.

\newpage

# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc [friund]{.recon} ‘friend’ > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

The change concerns a rare sequence confined to the `friend` family and cannot safely be generalized into a broadly productive rule.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

Only the `friend` family tests this contraction. If the rare \emph{*ijō} sequence survives until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc [fríjōndz]{.recon} ‘friend’ yields [*friund*]{.pred} rather than expected OE *frēond* 'friend'; moving contraction earlier within the tested range changes no checked output.

That single contrast places [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) before diphthong leveling but gives no lower boundary. It cannot establish a productive sound law beyond this family, precisely the reservation made by Ringe and Taylor.

\newpage

# West Germanic j-gemination

## Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

The change applies specifically after a short vowel before \emph{*j}, not to geminate consonants generally.

## SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

```foma
define PWGmcJGemination [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

OE *nett* 'net' fixes the order because the syllabic-\emph{j} development would remove the glide that conditions gemination. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) precedes [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc [nátją]{.recon} ‘net’ yields [*nete*]{.pred} rather than expected OE *nett* 'net'. Earlier movement of gemination changes no checked output.

The chronology is phonologically transparent: the consonant must geminate before \emph{*j} ceases to be consonantal. The witness establishes no earlier boundary.

\newpage

# Syllabic j after final-vowel loss

## Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

The sources establish the development, although the checked lexicon supplies
little independent evidence for its position. Its scope is postconsonantal j,
not high-vowel vocalization generally.

## SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

The same PGmc [nátją]{.recon} ‘net’ witness supplies the only firm boundary. Placing [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) before [SC010 PWGmcJGemination](#rule-PWGmcJGemination) yields [*nete*]{.pred} rather than expected OE *nett* 'net'; moving it later changes no checked output.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* 'army' and *rice* 'kingdom' as outcomes. The lexicon adds only that vocalization followed gemination, not where it falls among subsequent changes.

\newpage

# \emph{lþ}-voicing

## Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan* 'fold', *beald* 'bold', *wuldor* 'glory', and *gylden* 'golden' [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold* 'gold', and *feld* 'field' [@Campbell1959, p. 169, §414].

The comparative evidence supports \emph{lþ > ld} most clearly in northern West
Germanic, not as an unqualified pan-PWGmc development.

## SC012. \emph{lþ}-voicing (`PWGmcLThVoicing`) {#rule-PWGmcLThVoicing}

```foma
define PWGmcLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

The `field`, `fold`, `gold`, and `wold` families preserve \emph{*lþ} to \emph{*ld}, but none dates the change against a neighboring rule. Every checked output remains unchanged when the voicing is moved in either direction.

Comparative reconstruction therefore establishes northern West Germanic \emph{lþ > ld}, but the witness forms fix no date. Neither a pan-PWGmc attribution nor an exact local placement follows from the evidence presented here.

\newpage

# Dental hardening

## Historical discussion

Ringe and Taylor state directly that in PWGmc voiced dental fricative `*ð` became stop `*d` in all positions [@RingeTaylor2014, p. 43].

The change is systemic across early West Germanic and extends beyond any one
lexical family.

## SC013. Dental hardening (`PWGmcDentalHardening`) {#rule-PWGmcDentalHardening}

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

Dental hardening has systemic scope: voiced fricative \emph{*ð} became stop \emph{*d} throughout early West Germanic. Moving [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) earlier or later changes no checked output.

Comparative evidence establishes the sound law; the present lexicon leaves its exact position approximate.

\newpage

# Early unstressed vowel changes

## Historical discussion of the earliest unstressed vowel changes

The first change removes the remaining diphthongal quality of unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. Their chronological evidence differs: monophthongization is historically clear but not closely dated by the witness forms, whereas \emph{*i}-lowering has a diagnostic later boundary.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. The historical change is thus established, although the order test determines no closer relative position.

## \CAPRRuleHeading{SC014. Monophthongization of unstressed \emph{*ai}}{NWGmcUnstressedAiMonophthongization} {#rule-NWGmcUnstressedAiMonophthongization}

```foma
define NWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

Moving [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) earlier or later changes no checked form. The lexicon therefore cannot refine its source-based placement among the earliest Northwest Germanic simplifications of unstressed vowels.

Ringe and Taylor's merger of unstressed \emph{*ai} with \emph{*e} establishes the historical development; the current witnesses do not distinguish its position relative to neighboring changes.

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* 'world' and *weoruld* 'world' [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 NWGmcILowering](#rule-NWGmcILowering) with a firmer lexical basis than the preceding change.

## SC015. Leveling of early unstressed front vowels (`NWGmcILowering`) {#rule-NWGmcILowering}

```foma
define NWGmcILowering [
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

The *weorold* 'world' and *weoruld* 'world' variants turn the general source claim into an ordering test. If [SC015 NWGmcILowering](#rule-NWGmcILowering) is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc [wír-àldu]{.recon} ‘world’ yields [*wuruld*]{.pred} rather than expected OE *weorold* ‘world’; earlier movement changes no checked output.

The derivation thus fixes front-vowel leveling before interstress raising while leaving its earlier boundary open.

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering) follow with a more tightly constrained local chronology.

\newpage

# West Saxon palatal glide and u-lowering

## Historical discussion of West Saxon palatal glide and u-lowering

The derivation of *ġeoc* ‘yoke’ passes through both rules. Campbell treats the West Saxon rising-diphthong spellings before back vowels, while the same handbook tradition describes the lowering of \emph{u} before a following non-high vowel separately [@Campbell1959, p. 17, §44; @Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

The first change creates the West Saxon \emph{ġeoc} type; the second carries the same material into the subsequent vowel history.

## Historical discussion of West Saxon palatal glide

West Saxon spellings such as *ġeoc* ‘yoke’, *ġeong* ‘young’, and *ġeoguþ*
‘youth’ reflect an early development before back vowels. Campbell gives the
most direct handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

The sources establish [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), although the checked forms provide only a later boundary.

## \CAPRRuleHeading{SC016. West Saxon palatal glide before back vowels}{OEWsPalatalGlide} {#rule-OEWsPalatalGlide}

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

OE *ġeoc* ‘yoke’ fixes the close relation between glide insertion before back-vocalic \emph{u} and the following change.

If glide insertion follows [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [júką]{.recon} ‘yoke’ yields [*ġoc*]{.pred} rather than expected OE *ġeoc* ‘yoke’; earlier placement changes no checked output. The witness therefore dates [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) before u-lowering without supplying an earlier boundary. The *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ* 'youth' material establishes the lexical scope of the West Saxon development.

## Historical discussion of u-lowering

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

[SC017 NWGmcULowering](#rule-NWGmcULowering) thus rests on a broader source base than the preceding West Saxon rule.

## \CAPRRuleHeading{SC017. Lowering of \emph{*u} before following non-high vowels}{NWGmcULowering} {#rule-NWGmcULowering}

```foma
define NWGmcULowering [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* ‘yoke’, *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc [júką]{.recon} ‘yoke’ yields [*ġoc*]{.pred} rather than expected OE *ġeoc* ‘yoke’. After [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc [núsō]{.recon} ‘nose’ yields [*nusu*]{.pred} rather than expected *nosu* ‘nose’, PGmc [skúflō]{.recon} ‘shovel’ yields [*sċufl*]{.pred} rather than expected *sċofl* ‘shovel’, and PGmc [súrgō]{.recon} ‘sorrow’ yields [*surg*]{.pred} rather than expected *sorg* ‘sorrow’. The two witness sets place [SC017 NWGmcULowering](#rule-NWGmcULowering) after glide formation and before final long-\emph{o} raising.

\newpage

# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

The change is historically secure, but the tested forms determine no close relative position for it.
Its input is final \emph{*ō} in a stressed monosyllable.

## \CAPRRuleHeading{SC018. Raising of final stressed monosyllabic \emph{*ō}}{NWGmcStressedMonosyllableORaising} {#rule-NWGmcStressedMonosyllableORaising}

```foma
define NWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

Campbell's *cū* 'cow', *hū* 'how', and *tū* 'two' establish final stressed monosyllabic \emph{*ō} > \emph{*ū}.

Reversing [SC018 NWGmcStressedMonosyllableORaising](#rule-NWGmcStressedMonosyllableORaising) with neighboring changes leaves every checked output unchanged. The sound change is secure, but its exact position in the early history of long vowels rests on the handbooks.

\newpage

# Final long-\emph{o} raising and final \emph{z}-deletion

## Historical discussion of final long-\emph{o} raising and final \emph{z}-deletion

The same final-syllable structure undergoes both changes. Ringe and Taylor describe the change of unstressed final non-nasalized long \emph{*ō} to short \emph{*u}, while Hogg and Crist treat word-final \emph{*z} loss as a separate later step in West Germanic [@RingeTaylor2014, p. 30; @Hogg1992, p. 37; @Crist2002, p. 1].

The derivation of *ræste* ‘rest’ fixes their order: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must still see final \emph{*ō}, and [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) removes final \emph{*z} only afterward.

## Historical discussion of final long-\emph{o} raising

The first change in the pair is the Northwest Germanic raising of unstressed final long \emph{*ō} to \emph{*u}. Ringe and Taylor state that development directly in comparative terms [@RingeTaylor2014, p. 30].

The change supplies the final vowel of forms such as *nosu* 'nose', *sċofl* 'shovel', and
*sorg* 'sorrow'.

## \CAPRRuleHeading{SC019. Raising of final unstressed long \emph{*ō}}{NWGmcFinalLongORaising} {#rule-NWGmcFinalLongORaising}

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’ fix its lower boundary.

Before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [núsō]{.recon} ‘nose’ yields [*nusu*]{.pred} rather than expected OE *nosu* ‘nose’, PGmc [skúflō]{.recon} ‘shovel’ yields [*sċufl*]{.pred} rather than expected *sċofl* ‘shovel’, and PGmc [súrgō]{.recon} ‘sorrow’ yields [*surg*]{.pred} rather than expected *sorg* ‘sorrow’. After [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc [rástōz]{.recon} ‘rest’ yields [*rast*]{.pred} rather than expected *ræste* ‘rest’. These failures place [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.

## Historical discussion of final \emph{z}-deletion

The second change is the loss of word-final \emph{*z}. Standard handbook tradition and Crist's West Germanic discussion establish the development within broader accounts of inflectional morphology [@Hogg1992, p. 37; @Crist2002, p. 1].

Final z-loss follows long-o raising and precedes the later changes in weak
syllables.

## SC020. Deletion of word-final \emph{*z} (`PGmcFinalZDeletion`) {#rule-PGmcFinalZDeletion}

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
```

The chronology of word-final \emph{*z}-loss is unusually well delimited: *ræste* 'rest' supplies its early boundary, while later weak syllables supply its late boundary.

Before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc [rástōz]{.recon} ‘rest’ yields [*rast*]{.pred} rather than expected OE *ræste* ‘rest’. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [bébruz]{.recon} ‘beaver’ yields [*befro*]{.pred} rather than expected *befer* ‘beaver’, PGmc [kwéðuz]{.recon} ‘cud’ yields [*cwedo*]{.pred} rather than expected *cwedu* ‘cud’, and PGmc [félθuz]{.recon} ‘field’ yields [*feldo*]{.pred} rather than expected *feld* ‘field’, alongside eight other newly failing rows. Final \emph{z}-loss therefore follows [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) and precedes [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The [rástōz]{.recon} ‘rest’ derivation fixes the local relation to [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising). The distant boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) shows only that word-final \emph{*z}-loss precedes the later weak-syllable sequence; its placement within that wider interval follows the handbook chronology after final \emph{*ō}-raising.

\newpage

# Unstressed \emph{*o}-raising

## Historical discussion

The older history of *heofon* ‘heaven’ requires an unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the \emph{-o-} from an earlier unstressed environment, and Ringe and Taylor place the same family within the wider West Germanic record [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

The change is historically recognizable, but the checked forms provide only a later boundary.

## \CAPRRuleHeading{SC021. Raising of unstressed \emph{*o} before later \emph{*u}}{NWGmcUnstressedORaising} {#rule-NWGmcUnstressedORaising}

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xémonų]{.recon} ‘heaven’ yields [*heofun*]{.pred} rather than expected OE *heofon* ‘heaven’; earlier placement changes no checked output. The witness therefore places [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) before medial unstressed-\emph{u} lowering.

Nothing in the present lexicon supplies the corresponding earlier boundary.

\newpage

# \emph{mn}-dissimilation

## Historical discussion

The handbooks describe the history of \emph{mn} sequences as a limited
descriptive pattern. Campbell discusses both loss of unstressed material and
later assimilation in forms of this type, including the special status of
*mōnaþ* 'month'-type evidence [@Campbell1959, pp. 189, 195, §§470, 484].

The pattern is historically established, but the checked forms do not constrain its position.

## SC022. Dissimilation of \emph{mn} sequences (`NWGmcMnDissimilation`) {#rule-NWGmcMnDissimilation}

```foma
define NWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _
           EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

Campbell's *heofon* 'heaven' and *mōnaþ* 'month' material supports early \emph{m} > \emph{β}
before a later nasal, but supplies no ordering witness.

Moving [SC022 NWGmcMnDissimilation](#rule-NWGmcMnDissimilation) earlier or later leaves every checked output unchanged. Its place among the early consonantal changes rests on the handbook account of \emph{mn}-dissimilation.

\newpage

# N-stem \emph{n}-loss

## Historical discussion

The broader history is the reduction and leveling of older n-stem endings in West Germanic. Ringe and Taylor describe the resulting syncretism in the n-stems, which is the wider morphological setting for the narrower step isolated here [@RingeTaylor2014, p. 72].

The path to *dōn* ‘do’ provides the clearest witness, but the change remains narrow in scope.

## SC023. Loss of n-stem \emph{*n} in final position (`NWGmcNStemNLoss`) {#rule-NWGmcNStemNLoss}

```foma
define NWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

After [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc [dōną]{.recon} ‘do’ fails entirely (\emph{+?}) instead of yielding expected OE *dōn* ‘do’; earlier placement changes no checked output. Thus [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must feed the later apocope.

This failed derivation supplies a terminus ante quem, while the lower boundary remains unattested.

\newpage

# Long \emph{ē}-lowering

## Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

The change is historically recognizable, but the checked forms provide only a later boundary.

## \CAPRRuleHeading{SC024. Lowering of long \emph{ē} before non-nasal consonants}{NWGmcLongELowering} {#rule-NWGmcLongELowering}

```foma
define NWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

After [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), long \emph{ē} > \emph{ǣ} can no longer produce the expected West Saxon forms: PGmc [skḗpą]{.recon} ‘sheep’ yields [*sċīep*]{.pred} rather than OE *sċēap* ‘sheep’, and PGmc [jḗrą]{.recon} ‘year’ yields [*ġīer*]{.pred} rather than *ġēar* ‘year’. Earlier placement changes no checked output, so [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) has a secure upper boundary.

Its lower boundary remains a matter of handbook chronology.

\newpage

# Long \emph{ē} nasal-rounding

## Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* 'month' and *mōna* 'moon' / *mōn* 'moon'-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

The change is historically recognizable, but the tested forms supply no close relative chronology.

## SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

Reversing [SC025 NWGmcLongENasalRounding](#rule-NWGmcLongENasalRounding) with neighboring changes leaves every checked output unchanged. Its position beside the other \emph{ē}-developments therefore follows the handbooks.

\newpage

# Nasal spirant changes

## Historical discussion of nasal loss before spirants and compensatory lengthening

The two rules state successive phases of a single development. Campbell
describes nasal loss before voiceless spirants with compensatory lengthening and
nasalization of the preceding vowel. Ringe and Taylor assign the same outcomes
to inherited northern West Germanic, before late Old English
[@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

[SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the nasal-plus-spirant sequence remains present; [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal. The first rule must therefore precede the second.

## \CAPRRuleHeading{SC026. Lengthening before nasal plus spirant}{NWGmcNasalSpirantLengthening} {#rule-NWGmcNasalSpirantLengthening}

```foma
define NWGmcNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];
```

All three witnesses require the vowel adjustment while the nasal is still present. If [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) follows [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss), PGmc [fúnxstiz]{.recon} ‘fist’ yields [*fyst*]{.pred} rather than expected OE *fȳst* ‘fist’, PGmc [gánsz]{.recon} ‘goose’ yields [*ġeas*]{.pred} rather than expected *gōs* ‘goose’, and PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. Earlier placement changes no checked output. The evidence requires lengthening to precede nasal loss without supplying a lower boundary, in agreement with the handbook treatment of the two as successive phases.

## SC027. Loss of the nasal before spirants (`NWGmcNasalSpirantLoss`) {#rule-NWGmcNasalSpirantLoss}

```foma
define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

The converse test fixes the same boundary: placing [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) before [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) produces the same errors in *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’. Later placement changes no checked output. These forms prove that the vowel was adjusted before the nasal disappeared; they provide no upper boundary for the loss.

\newpage

# Preconsonantal \emph{*x}-loss

## Historical discussion

Campbell explicitly treats loss of \emph{x} and gives forms such as *fléam* ‘flight’ and *hēla* ‘heel’ as examples of the same broad development [@Campbell1959, p. 186, §461].

The historical evidence is firmer than the chronology: the checked forms do not constrain the rule's position.

## SC028. Loss of preconsonantal \emph{*x} (`NWGmcPreconsonantalXLoss`) {#rule-NWGmcPreconsonantalXLoss}

```foma
define NWGmcPreconsonantalXLoss [
    {*x} -> 0 || _ {*s} EnglishStarConsonant
];
```

No witness word dates preconsonantal \emph{*x}-loss before \emph{*s} plus another consonant: moving [SC028 NWGmcPreconsonantalXLoss](#rule-NWGmcPreconsonantalXLoss) in either direction leaves every checked output unchanged. Its position within this stretch therefore rests on the handbook chronology for \emph{x}-loss.

\newpage

# Awj glide formation and au-fronting

## Historical discussion of awj glide formation and au-fronting

The *hīeġ* 'hay' and *strīeġan* 'strew' material undergoes both changes. Glide formation reshapes the older \emph{awj} sequence, and fronting then affects the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

Glide formation creates the input to fronting; diphthong leveling follows both.

## Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

The sources establish glide formation, while the witness forms supply only a later boundary.

## SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

The *hīeġ* 'hay' and *strīeġan* 'strew' derivations show that \emph{awj} reshaping prepared the input to fronting. If fronting is applied first, PGmc [xáwwją]{.recon} ‘hay’ yields [*hauġ*]{.pred} rather than expected OE *hīeġ* ‘hay’, and PGmc [stráwjaną]{.recon} ‘strew’ yields [*strauian*]{.pred} rather than expected *strīeġan* ‘strew’. Earlier placement of glide formation changes no checked output, so these forms supply an upper boundary without a corresponding lower one.

## Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted
diphthongal outcomes of the broader West Saxon vowel history. Campbell
describes \emph{au} > \emph{ēa} [@Campbell1959, pp. 53--54, §135].

Fronting must follow glide formation and precede diphthong leveling, which applies to a wider set of derivations.

## SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Two distinct failure sets confine fronting. Placed before glide formation, it produces the wrong forms: PGmc [xáwwją]{.recon} ‘hay’ yields [*hauġ*]{.pred} rather than expected OE *hīeġ* ‘hay’, and PGmc [stráwjaną]{.recon} ‘strew’ yields [*strauian*]{.pred} rather than expected *strīeġan* ‘strew’. Placed after diphthong leveling, PGmc [galáubijaną]{.recon} ‘believe’, [bráudą]{.recon} ‘bread’, and [dráugmaz]{.recon} ‘dream’, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. The lexical errors require fronting to follow glide formation, while the failed derivations require it to precede diphthong leveling.

The later failure set consists of failed derivations, not competing Old English
surface forms.

\newpage

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

The *dēaw* 'dew' and *hēawan* 'hew' derivations establish that doubled \emph{w} was simplified before the long \emph{ēaw} development. If [SC031 OEWWSimplification](#rule-OEWWSimplification) follows [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [dáwwō]{.recon} ‘dew’ yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc [xáwwaną]{.recon} ‘hew’ yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. Earlier placement changes no checked output. The witnesses require simplification before the long-diphthong change and leave the lower boundary to the broader West Saxon chronology.

## Historical discussion of diphthong leveling

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* 'dew' / *hēawan* 'hew' developments.

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

The two edges of this interval fail differently. Before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc [galáubijaną]{.recon} ‘believe’, [báug]{.recon} ‘bow’, and [bráudą]{.recon} ‘bread’ produce no output (\emph{+?}) instead of expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xáubudą]{.recon} ‘head’ yields [*hēafud*]{.pred} rather than expected *hēafod* ‘head’. Absence at the lower edge places diphthong leveling after fronting; the wrong surface form at the upper edge places it before medial unstressed-\emph{u} lowering.

## Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from chew,
four, and knee [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The only checked boundary for
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) lies ahead at
[SC044 OEBreaking](#rule-OEBreaking).

## \CAPRRuleHeading{SC033. Long \emph{ēow} before following vowels and weak endings}{OEEwLongDiphthong} {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The long \emph{ēow} of *ċēowan* 'chew', *fēower* 'four', and *cnēow* 'knee' supplies only a terminus ante quem. If [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) follows [SC044 OEBreaking](#rule-OEBreaking), PGmc [kéwwaną]{.recon} ‘chew’ yields [*ċeowan*]{.pred} rather than expected OE *ċēowan* ‘chew’, PGmc [fédwōr]{.recon} ‘four’ yields [*feower*]{.pred} rather than expected *fēower* ‘four’, and PGmc [knéwą]{.recon} ‘knee’ yields [*cneow*]{.pred} rather than expected *cnēow* ‘knee’. Earlier placement changes no checked output. The sources associate \emph{ew} and \emph{iw} with the same diphthongal history but furnish no lower boundary.

## Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* 'dew' and *hēawan* 'hew'. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) follows [SC031 OEWWSimplification](#rule-OEWWSimplification) locally and must also precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

A local feeding relation and a later vowel change confine \emph{aw} > \emph{ēaw}. Before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [dáwwō]{.recon} ‘dew’ yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc [xáwwaną]{.recon} ‘hew’ yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. After [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc [skáwōjaną]{.recon} ‘show’ yields [*sċawian*]{.pred} rather than expected OE *sċēawian* ‘show’, PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċawaþ*]{.pred} rather than expected *sċēawaþ* 'shows', and PGmc [stráwą]{.recon} ‘straw’ yields [*stræw*]{.pred} rather than expected *strēaw* ‘straw’. The *dēaw* and *hēawan* forms require long-diphthong formation after simplification, while *sċēawian* requires it before brightening; the handbooks assign the same interval to the West Saxon development.

\newpage

# Prefix and compound adjustments

## Historical discussion of prefixal \emph{*a}-reduction

Weakly stressed prefixes can lose their older low vowel early in Old English,
and that is the historical setting for
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction). Campbell treats the
small class of pretonic losses directly, while Ringe and Taylor's derivation of
[galaubijana]{.recon} ‘believe’ supplies the comparative witness for the same development
[@Campbell1959, p. 147, §354; @RingeTaylor2014, p. 245;
@RingeTaylor2014, p. 267].

The rule has a narrow historical range and gives prefixed forms the weak vowel inherited by later vocalic changes.

## SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

The prefix of *ġelīefan* 'believe' supplies the upper boundary for \emph{*ga-} > \emph{*ge-}. If [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) follows [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc [galáubijaną]{.recon} ‘believe’ yields [*ġealīefan*]{.pred} rather than expected OE *ġelīefan* ‘believe’. Earlier placement changes no checked output, so the witness dates prefix reduction before brightening without locating its beginning.

## Historical discussion of inter-stress raising

[SC036 OEInterStressRaising](#rule-OEInterStressRaising) has the strongest evidence of the three. Campbell's discussion of *weorold* 'world' / *weoruld* 'world' and Ringe and Taylor's derivation of [weraldu]{.recon} 'world' > [weruldu]{.recon} 'world' > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

The rule changes the vowel between stronger stress peaks, and its witnesses consequently constrain the relative chronology.

## \CAPRRuleHeading{SC036. Raising of medial \emph{*a} between stress peaks}{OEInterStressRaising} {#rule-OEInterStressRaising}

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

The two boundaries have unequal force. Before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc [sáiwalō]{.recon} ‘soul’ yields [*sāwel*]{.pred} rather than expected OE *sāwol* ‘soul’; after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), it yields [*sāwul*]{.pred} rather than *sāwol*, while PGmc [wír-àldu]{.recon} ‘world’ yields [*weoruld*]{.pred} rather than *weorold* ‘world’. The distant lower boundary places inter-stress raising after final long-\emph{o} raising, and the local upper boundary places it before medial unstressed-\emph{u} lowering. In handbook terms, medial \emph{*a} > \emph{*u} belongs to the \emph{world}- and \emph{soul}-type low-stress vocalism that followed the earlier final-vowel changes.

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* ‘rainbow’. Its only checked boundary
is the immediately following technical stress-stripping stage, which is not a
sound change.

## \CAPRRuleHeading{SC037. Syncope of compound linking vowels}{OECompoundLinkingSyncope} {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* 'rainbow' test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc [régna-bùgô]{.recon} ‘rainbow’ yields [*reġnefoga*]{.pred} rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).

\newpage

# Medial unstressed vowel changes

## Historical discussion of medial unstressed vowel changes

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* 'world' / *weoruld* 'world'
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, [weraldu]{.recon} 'world', and [jugunþi]{.recon} 'youth'
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.3.3].

[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) feeds the vowel
sequence subsequently reshaped by
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
Initial \emph{w} conditions the first change.

## SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

The *wuduwe* ‘widow’ derivation answers one narrow question about \emph{wi}-forms. If [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) follows [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe*; earlier placement changes no checked output. The witness requires combinative u-umlaut to precede medial lowering and supplies no lower boundary.

## \CAPRRuleHeading{SC040. Lowering of medial unstressed \emph{*u}}{OEMedUnstressedULowering} {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

The two witnesses date medial unstressed \emph{*u} > \emph{*o} at very different scales. Before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe* ‘widow’; after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. The local *weorold* 'world' and widow evidence places lowering after combinative u-umlaut, while the youth form supplies only the distant requirement that lowering precede unstressed long-vowel shortening.

\newpage

# Final bare-\emph{a} loss

## Historical discussion

I isolate the loss of final short low vowels within the broader erosion of final syllables described by the handbooks [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

Final bare-a loss follows the medial unstressed vowel changes and
precedes restoration, which depends on the environment left by the loss.

## SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

The two sides of final bare-\emph{a} loss rest on different evidence. Applied before final \emph{z}-deletion, the change gives the wrong outputs: PGmc [bárdaz]{.recon} ‘beard’ yields [*bearda*]{.pred} rather than expected OE *beard* ‘beard’, and PGmc [kámbaz]{.recon} ‘comb’ yields [*camba*]{.pred} rather than expected *camb* ‘comb’. Applied after restoration, PGmc [kráftaz]{.recon} ‘craft’ yields [*craft*]{.pred} rather than expected OE *cræft* ‘craft’, and PGmc [dágaz]{.recon} ‘day’ yields [*dag*]{.pred} rather than expected *dæġ* ‘day’. The distant lower limit follows final \emph{z}-loss; the local feeding relation precedes restoration, which requires the environment created by the vowel loss.

\newpage

# Surviving bimoric \emph{*ō} unrounding

## Historical discussion

The handbooks do not isolate a large independent sound change under this label.
The surviving bimoric \emph{*ō} in the pathway to *ræste* ‘rest’ nevertheless
undergoes unrounding before
[SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). Campbell, Hogg,
and Ringe and Taylor describe the surrounding fronting and restoration history
without naming this feeder separately [@Campbell1959, pp. 52, 60,
§§131, 157--158; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158,
189--190].

The sole witness establishes a local relation to brightening but supports no broader generalization.

## \CAPRRuleHeading{SC042. Unrounding of the surviving bimoric \emph{*ō}}{PWGmcSurvivingBimoricOUnrounding} {#rule-PWGmcSurvivingBimoricOUnrounding}

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The single *ræste* ‘rest’ derivation carries the chronology of bimoric \emph{*ō} > \emph{*ā}. Before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) or after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste*. Unrounding must therefore follow final \emph{z}-loss and precede brightening, although only the relation to brightening is local.

\newpage

# Anglo-Frisian brightening

## Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

## \CAPRRuleHeading{SC043. Fronting of low \emph{*a} outside nasal environments}{AngloFrisianBrightening} {#rule-AngloFrisianBrightening}

```foma
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

Two derivations place low \emph{*a} > \emph{*æ} between unrounding and breaking. Before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste* ‘rest’. After [SC044 OEBreaking](#rule-OEBreaking), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. The first witness requires brightening to receive the outcome of the surviving-bimoric \emph{*ō} development; the second requires breaking to receive the fronted vowel.

\newpage

# Breaking and velar-fricative palatalization

## Historical discussion of breaking and velar-fricative palatalization

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment, while velar-fricative palatalization follows it locally in the *feoh* 'cattle' and *feohtan* 'fight' type derivations.

## SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Breaking must encounter the vowel created by brightening and must precede the fricative change seen in *feoh* ‘fee’ and *feohtan* ‘fight’. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc [féxu]{.recon} ‘cattle’ yields [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yields [*fehtan*]{.pred} rather than expected *feohtan*. The two feeding relations place breaking between brightening and velar-fricative palatalization.

## \CAPRRuleHeading{SC045. Palatalization of velar fricatives beside front vowels}{OEVelarFricativePalatalization} {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*ɣ} -> {*j} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*ɣ} -> {*j} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j},
    {*ɣ} -> {*j} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The local chronology comes from *feoh* 'cattle' and *feohtan* 'fight'. Before [SC044 OEBreaking](#rule-OEBreaking), palatalization of \emph{*x} and \emph{*ɣ} beside front vowels or \emph{*j} makes PGmc [féxu]{.recon} ‘cattle’ yield [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yield [*fehtan*]{.pred} rather than expected *feohtan*. The distant upper limit comes from *six* 'six': after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected OE *six*. Breaking therefore feeds velar-fricative palatalization directly, while palatal umlaut supplies only the broader upper limit.

\newpage

# A-restoration and nasal changes

## Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}.

[SC046 OEARestoration](#rule-OEARestoration) has firmer handbook support than the two following nasal rules.

## \CAPRRuleHeading{SC046. Restoration of \emph{*a} before following back vowels}{OEARestoration} {#rule-OEARestoration}

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

Restoration must receive fronted \emph{*æ} and return \emph{*a} before the nasal-tail changes. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc [bákaną]{.recon} ‘bake’ yields [*bæcan*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc [fáraną]{.recon} ‘fare’ yields [*færan*]{.pred} rather than expected *faran* ‘fare’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), [bákaną]{.recon} again yields [*bæcan*]{.pred} instead of *bacan*, while PGmc [wádaną]{.recon} ‘wade’ yields [*wædan*]{.pred} instead of *wadan* ‘wade’. These independent witness pairs place restoration after brightening and before secondary nasalization.

## Historical discussion of heavy-syllable nasal loss and secondary nasalization

Heavy-syllable nasal apocope removes the final nasalized vowel; secondary
nasalization then marks the preceding \emph{a} before final \emph{n}. The
handbooks do not isolate both developments under equally prominent labels.
Campbell describes later nasal loss and the back-mutation environment; Ringe
and Taylor provide the later relation to back mutation
[@Campbell1959, pp. 86, 166, §§205--206, 403;
@RingeTaylor2014, p. 319, §6.9.4].

The reciprocal failure set fixes the order: apocope removes the ending before
secondary nasalization acts on the remaining structure. Restoration receives
the fuller historical treatment in the handbooks.

## \CAPRRuleHeading{SC047. Heavy-syllable nasal apocope of final \emph{*ą}}{OEHeavySyllableNasalApocope} {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

The evidence for final nasalized \emph{*ą} loss is sharply asymmetric. Before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), the single PGmc witness [stráwą]{.recon} ‘straw’ yields [*stræw*]{.pred} rather than expected OE *strēaw* ‘straw’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc [bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* ‘bind’, alongside a broad \emph{-en} failure set. One lower witness places apocope after long-diphthong formation; many reciprocal upper failures place it before secondary nasalization.

## \CAPRRuleHeading{SC048. Secondary nasalization before final \emph{*n}}{OESecondaryNasalization} {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

The broad \emph{-an}/\emph{-en} split fixes the lower boundary of final \emph{*a} nasalization before \emph{n}. Before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc [bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* 'bake', and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* 'bind'. The upper boundary comes from back mutation. After [SC059 OEBackMutation](#rule-OEBackMutation), PGmc [stélaną]{.recon} ‘steal’ yields [*steolan*]{.pred} rather than expected OE *stelan* ‘steal’, and PGmc [wébaną]{.recon} ‘weave’ yields [*weofan*]{.pred} rather than expected *wefan* ‘weave’. Reciprocal nasal-tail failures place secondary nasalization after apocope, and the later mutation witnesses place it before back mutation; [SC046 OEARestoration](#rule-OEARestoration) retains the clearest independent historical support.

\newpage

# B allophony and Sievers-law syncope

## Historical discussion of B allophony

The first change is the positional alternation of Germanic \emph{*b}. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@Hogg1992, pp. 101--102]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

The distribution is narrow, but later changes presuppose the stop-fricative
alternation.

## \CAPRRuleHeading{SC049. Distribution of \emph{*b} after vowels and liquids}{PGmcBAllophony} {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

The handbooks describe \emph{*b}/\emph{*bb} as a positional alternation within the consonant system, and one compound supplies its chronological consequence. Before [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope), *reġnboga* 'rainbow' develops as [*reġnfoga*]{.pred} rather than expected OE *reġnboga*; later placement creates no comparable failure. The witness places b-allophony after compound-linking syncope without turning the alternation into an independent sound law.

## Historical discussion of Sievers-law syncope

Sievers' Law concerns a different historical problem. It is a prosodic and
morphological adjustment in heavy stems, not a distributional allophone of a
stop consonant. Adamczyk treats the Old English reflexes of the law as
historical evidence from weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through
familiar forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15].

Sievers-law syncope is narrow in scope, but its relation to the following
palatalization is lexically secure. Its earlier limit is less sharply defined
than that of the preceding allophony rule.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

The Sievers-law reduction \emph{*-CijV-*} > \emph{*-CjV-*}, including loss of \emph{*i} before \emph{*j}, must precede palatalization. If [SC050 SieversLawSyncope](#rule-SieversLawSyncope) follows [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [strákkijaną]{.recon} ‘stretch’ yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’; earlier placement creates no comparably precise error. The single cluster witness therefore places syncope before velar palatalization.

\newpage

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

Luick places the cluster change within a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
identity between the cluster change and the later umlautal developments.

## SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

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

The non-fronted vowels of *flasce* ‘flask’ and *wascan* ‘wash’ fix the lower boundary of \emph{*sk} > \emph{*sc}. Before [SC046 OEARestoration](#rule-OEARestoration), the forms are fronted too soon, yielding *flæsce* ‘flask’ and *wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This places [SC051 OESkPalatalization](#rule-OESkPalatalization) after restoration.

Five witnesses establish the upper boundary collectively. The palatal cluster must already underlie *sċeaft* ‘shaft’, *sċēar* ‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’ before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). The \emph{*sċea-* 'sea'}/\emph{*sċie-*} set therefore places cluster palatalization before the West Saxon vowel change. The cluster change occupies the same palatalization zone as [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) while remaining distinct from plain-velar palatalization and the later vowel changes.

\newpage

# Velar palatalization before front vowels

## Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological sequence. The examples associated with that sequence, such as
*ceaster* ‘town’, *geaf* ‘gave’, *giefan* ‘give’, and *giest* ‘guest’, already
show that consonantal palatalization and later vowel effects stand close
together historically, even when they must be distinguished analytically
[@Luick1914, pp. 157--167, §§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as *cild* ‘child’, *dæg* ‘day’, *giefan* ‘give’, and *giest*
‘guest’, which show how palatalized velars, palatal influence, and later
umlautal outcomes meet in the same region of the lexicon without collapsing
into one process [@Campbell1959, pp. 69--72, 89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@Hogg1992, pp. 103--104]. This formulation
replaces a broad list of palatal outcomes with a phonological environment
defined by adjacency and syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and \emph{*sk} had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as \emph{weccan} ‘wake’, \emph{licgan} ‘lie’, \emph{lecgan} ‘lay’,
\emph{secg} ‘retainer’, \emph{ecg} ‘edge’, \emph{wicg} ‘horse’, and
\emph{brycg} ‘bridge’, illustrate the same point in lexical detail: front
vowels and `j` create the palatal environment in which plain `k` and `g` cease
to behave as plain velars [@RingeTaylor2014, pp. 213--214, §6.4.1].

Luick describes a broad early movement; Campbell distinguishes plain velars
from the `sk` complex; Hogg specifies the adjacency and syllable conditions;
and Ringe and Taylor order the plain-velar change before West-Saxon
diphthongization. Plain-velar palatalization thus forms part of a wider
palatalizing environment without being identical to its neighboring changes.

## \CAPRRuleHeading{SC052. Palatalization of \emph{*k} before front vowels and \emph{*j}}{OEVelarPalatalizationKFront} {#rule-OEVelarPalatalizationKFront}

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;
```

The *weccan* ‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’ set identifies front vowels and `j` as the environment for palatalization of `k` [@RingeTaylor2014, pp. 213--214, §6.4.1]. These forms establish the conditioning; different witnesses establish the chronology.

Applied before Sievers-law syncope, PGmc [strákkijaną]{.recon} ‘stretch’ yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’. Applied after i-umlaut fronting, PGmc [kūi]{.recon} ‘cow’ and [lúnganjō]{.recon} ‘lungs’ yield *ċȳ* 'cows' and *lunġen* 'lungs' rather than expected OE *cȳ* 'cows' and *lungen* 'lungs'. The front-vowel `k` change therefore follows Sievers-law syncope and precedes i-umlaut fronting.

## \CAPRRuleHeading{SC052. Velar palatalization before front vowels}{OEVelarPalatalization} {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

Plain `k` and `g` palatalization in front-vocalic and `j`-adjacent environments follows `sk`-palatalization and occupies a sharply defined pre-umlaut interval. Applied before Sievers-law syncope, PGmc [strákkijaną]{.recon} ‘stretch’ yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’. Applied after general i-umlaut, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected *cȳ* ‘cows’, and PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected *lungen* ‘lungs’. These witnesses place velar palatalization after Sievers-law syncope and before umlaut.

Luick, Campbell, and Ringe and Taylor place *cild* ‘child’ and *dæg* ‘day’ in a consonantal palatalization that precedes later vowel fronting [@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1]. The umlautal developments therefore receive plain `k` and `g` already reshaped beside front vowels and `j`.

The `sk` change belongs to the same palatalizing region with a separate scope. The *streċċan* ‘stretch’ evidence establishes a specific dependency on earlier syncope; it does not merge the two changes into one process.

\newpage

# Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

## Historical discussion of early \emph{*w}-loss before umlaut

The first rule is a narrow loss of \emph{*w} after velars in the \emph{*ngw}
sequence. Ringe and Taylor derive PGmc [singwan]{.recon} ‘sing’ to Old English *singan*
‘sing’ [@RingeTaylor2014, p. 214, §6.4.2]. This comparative evidence establishes
the change, although no checked form fixes its order relative to a neighboring
rule.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The first rule is restricted to
the \emph{*ngw} sequence; the second has a specific lexical witness and defined
earlier and later limits.

## SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

The comparative development `*singwan > singan` establishes narrow post-velar \emph{*w}-loss in the \emph{*ngw} sequence, yielding *singan* ‘sing’. Moving [SC053 OEPostVelarWLoss](#rule-OEPostVelarWLoss) earlier or later leaves every checked output unchanged. Its pre-umlaut position therefore rests on comparative evidence, while the present lexicon supplies no neighboring boundary.

## SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

The history of *sǣ* ‘sea’ explains why non-initial \emph{*w} disappeared before final unstressed \emph{*i}. Campbell describes the loss, Ringe and Taylor derive the form from \emph{*saiwi-}/\emph{*sawi-}, and Luick gives the parallel trajectory [@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. Loss of the glide allowed the preceding vowel to undergo the later fronting and lengthening.

The same witness supplies two distant limits. Before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) or after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI) yields [*sǣw*]{.pred} rather than expected OE *sǣ* 'sea'. The loss must therefore follow final \emph{z}-deletion and precede high-vowel apocope, while its exact position within that broad interval remains source-based.

\newpage

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

The cow and lung forms establish the lower boundary. If fronting precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected OE *cȳ* 'cows', and [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* 'lungs'. The consonantal change must therefore precede fronting.

The gift and sheath forms establish the upper boundary. If West Saxon palatal diphthongization precedes fronting, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. Fronting consequently follows velar palatalization and precedes the West Saxon change; the other components of i-umlaut share those bounds.

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

The chronology comes from the cow/lung and gift/sheath contrasts. Placed before velar palatalization, diphthongal mutation over-palatalizes [kūi]{.recon} ‘cow’ and [lúnganjō]{.recon} ‘lungs’; placed after West Saxon palatal diphthongization, it yields [*ġieft*]{.pred} and [*sċǣþ*]{.pred} instead of expected *ġift* 'gift' and *sċēaþ* 'sheath'. These failures place diphthongal mutation after velar palatalization and before West Saxon palatal diphthongization.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The lower boundary is consonantal. If general umlaut precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected *cȳ* 'cows', and PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected *lungen* 'lungs'. These over-palatalized forms place general umlaut after velar palatalization.

The upper boundary separates general umlaut from the narrower West Saxon process. If West Saxon palatal diphthongization precedes umlaut, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. Together the two witness pairs place general umlaut after velar palatalization and before the West Saxon process.

## \CAPRRuleHeading{SC056. West Saxon palatal diphthongization}{OEWsPalatalDiphthongization} {#rule-OEWsPalatalDiphthongization}

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

The forms *ġift* ‘gift’ and *sċēaþ* ‘sheath’ fix the lower boundary. If West Saxon palatal diphthongization precedes general i-umlaut, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected *ġift*, and PGmc [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ*. These witnesses place West Saxon palatal diphthongization after general umlaut; no tested lexical item supplies a later terminus ante quem.

The one-sided chronology reflects the difference in scale. General umlaut reorganizes the vowel system, whereas West Saxon palatal diphthongization affects a narrower dialectal class after palatal consonants. Its exact later placement remains undemonstrated by the present lexicon.

\newpage

# J-cluster coalescence

## Historical discussion

Only a small lexical group reveals the coalescence of velars with \emph{*j}.
Plain-velar and \emph{*sk} palatalization must already have run before
\emph{*gj} and \emph{*kj} acquire their later outcomes.
Campbell, Ringe and Taylor, and Fulk discuss the palatalized and fronted
outcomes in *bīeġan* ‘bend’ and *sēċan* ‘seek’ without assigning this later
cluster adjustment the status of a major sound law [@Campbell1959, pp. 89,
107--108, §§170, 248--251; @RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1,
6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13].

## SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

The forms *bīeġan* ‘bend’ and *sēċan* ‘seek’ determine the earlier boundary.
If coalescence precedes [SC052
OEVelarPalatalization](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related
forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc [báugijaną]{.recon} 'bow' yields [*bēaġan*]{.pred} rather than expected OE *bīeġan*,
and PGmc [sōkijaną]{.recon} 'seek' yields [*sōċan*]{.pred} rather than expected *sēċan*. This
demonstrates that velar palatalization preceded coalescence. Nothing in the
present lexicon supplies a terminus ante quem.

\newpage

# Nasal dissimilation

## Historical discussion

Most accounts introduce nasal dissimilation to explain individual forms rather
than as a regular sound law. Luick records *enetre* ‘yearling’ (spelled
*enitre* 'yearling' in his text) [@Luick1914, p. 166]; Campbell discusses *heofon*
‘heaven’ with suffixal variation [@Campbell1959, p. 155]; and Hogg encounters
the same form while treating back mutation [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The disagreement concerns scope. Fulk's formulation recognizes a recurrent but
irregular development in `mn`; the remaining discussions stay with particular
lexical outcomes. None warrants a sound law comparable in scope to the major
Old English vowel changes.

## \CAPRRuleHeading{SC058. Nasal dissimilation in short-vowel environments}{OENasalDissimilation} {#rule-OENasalDissimilation}

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

I adopt a narrower environment than the handbook observations might suggest.
Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “*heofon* is for
older *hefzen*” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind [@Campbell1959, p. 155;
@Hogg1992, p. 112]. The short-vowel environment adopted here covers a recurrent
subset of these outcomes, not every dissimilatory development involving nasals.

No witness word fixes the position of nasal dissimilation within the Old
English sequence. Reversing its order with any tested neighbor leaves every
checked output unchanged. A more precise relative chronology would therefore
require lexical evidence not represented here.

\newpage

# Back mutation

## Historical discussion

West Saxon *giefan* ‘give’ and *wefan* ‘weave’ stand against non-West-Saxon
*geofad* 'gave' and *weofan* 'weave'. Ringe and Taylor use this contrast to define the
dialectal profile of back mutation [@RingeTaylor2014, p. 319, §6.9.4].
Campbell's treatment of diphthongization before following back vowels includes
*heofon* ‘heaven’ [@Campbell1959, p. 86, §207], while Hogg draws the instructive
comparison with breaking [@Hogg1992, p. 112]. Fulk accordingly separates back
mutation from the earlier umlautal changes [@Fulk2018, p. 69, §4.8].

## SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
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

\newpage

# West Saxon palatal umlaut

## Historical discussion

The reflexes *miht* ‘might’ and *niht* ‘night’ place West Saxon palatal umlaut
after the principal umlautal developments. Campbell and Ringe and Taylor
describe the forms themselves; Fulk supplies the broader chronology of
palatal-vowel change [@Campbell1959, pp. 107--108, §§248--251;
@RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75,
§§4.7, 4.13].

## \CAPRRuleHeading{SC060. West Saxon palatal umlaut before \emph{*h}-clusters}{OEWsPalatalUmlaut} {#rule-OEWsPalatalUmlaut}

```foma
define OEWsPalatalUmlaut [
    {*eo} -> {*i} || _ OEHCluster .#.,
    {*io} -> {*i} || _ OEHCluster .#.,
    {*ie} -> {*i} || _ OEHCluster .#.,
    {*eo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*io} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ie} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*éo} -> {*i} || _ OEHCluster .#.,
    {*ío} -> {*i} || _ OEHCluster .#.,
    {*íe} -> {*i} || _ OEHCluster .#.,
    {*éo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ío} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*íe} -> {*i} || _ OEHCluster EnglishStarFrontVowel
];
```

The change to \emph{*i} before \emph{*h}-clusters can be ordered only on its
earlier side. If palatal umlaut precedes
[SC055 OEIUmlaut](#rule-OEIUmlaut),
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage [*mieht*]{.pred} and [*nieht*]{.pred} rather than expected OE *miht* and *niht*.
Consequently, i-umlaut precedes palatal umlaut. Reordering the latter against
any tested later change leaves both witness forms unchanged.

\newpage

# Weak-tail nasal loss

## Historical discussion

The pathway from [dōną]{.recon} ‘do’ to *dōn* ‘do’ supplies the sole lexical thread
through this reduction. Campbell, Hogg, and Fulk place such weak-tail losses
among apocope and related late reductions [@Campbell1959, pp. 144--145,
§§345--349; @Hogg1992, pp. 120--121; @Fulk2018, p. 91, §5.6]. The witness,
however, ties the change to a much older development. Its immediate neighbors
remain untested.

## \CAPRRuleHeading{SC061. Reduction of final nasal weak-tail endings}{OEWeakTailNasalLoss} {#rule-OEWeakTailNasalLoss}

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

Final weak-tail \emph{*-ną} and \emph{*-mą} accordingly yield plain
\emph{*-n} and \emph{*-m}.

Only *dōn* ‘do’ constrains the relative order. Placing this loss before
the older n-stem loss makes the derivation record no output instead of expected
OE *dōn* ‘do’. The older loss must therefore precede weak-tail nasal loss.
Nothing in the current lexicon distinguishes among its possible later
positions, and one witness cannot establish a wider historical development.

\newpage

# High-vowel apocope

## Historical discussion

Final high vowels must survive long enough to condition umlaut before apocope
removes them after heavy syllables and in the relevant trisyllabic patterns.
Campbell, Hogg, Ringe and Taylor, and Fulk agree on this Old English
development, though they differ over the extent of the surrounding syncope
[@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, p. 120;
@RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

## \CAPRRuleHeading{SC063. High-vowel apocope after heavy syllables and in trisyllables}{OEHighVowelApocope} {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

Final \emph{*i}, \emph{*u}, and \emph{*ų} cannot disappear before completing
their umlautal work. Applied before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [kūi]{.recon} ‘cow’ yields [*cū*]{.pred} rather than
expected OE *cȳ* ‘cow’, and PGmc [brūdiz]{.recon} ‘bride’ yields [*brūd*]{.pred} rather than
expected OE *brȳd* ‘bride’. Conversely, if apocope waits until after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrht*]{.pred} rather than expected OE *fyrhte*
‘fright’. The three witnesses establish the sequence i-umlaut, high-vowel
apocope, unstressed long-vowel shortening.

\newpage

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
[fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhten*]{.pred} rather than expected OE *fyrhte* ‘fright’.
After [SC072
OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc
[fúrxtīnaz]{.recon} again yields [*fyrhten*]{.pred} rather than expected *fyrhte* 'fright'. I
therefore order final bare-a loss, stem-final n-loss, and unstressed long-vowel
shortening in that sequence. Both boundaries are firm within the derivation,
but depend upon one lexical family.

## \CAPRRuleHeading{SC065. Medial syncope before dentals after heavy syllables}{OEMedialSyncope} {#rule-OEMedialSyncope}

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

\newpage

# Late syncope and degemination

## Historical discussion of late syncope and degemination

Vowel loss creates the clusters upon which later assimilation and degemination
operate. Hogg and Ringe and Taylor describe this dependence, while Brunner's
*netle* 'nettle' beside later *netele* 'nettle' supplies a concrete lexical type
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2;
@SieversBrunner1965, pp. 144--145, §§158--159]. Fulk places this syncope after
i-umlaut [@Fulk2018, p. 91, §5.6].

The three relations are not equally secure. Lexical evidence orders syncope
and degemination; the intervening dental assimilation has no independent
ordering witness.

## \CAPRRuleHeading{SC066. L-adjacent syncope in medial syllables}{OELAdjacentSyncope} {#rule-OELAdjacentSyncope}

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

The loss of medial \emph{*i} before \emph{*l} is late enough to preserve
earlier umlaut, as *netle* ‘nettle’ and *spinl* ‘spindle’ demonstrate.

Placed before i-umlaut, PGmc [nátilōn]{.recon} ‘nettle’ yields [*nætle*]{.pred} rather than
expected OE *netle* ‘nettle’, and PGmc [spénnilō]{.recon} ‘spindle’ yields [*spenl*]{.pred} rather
than expected *spinl* ‘spindle’. Placed after preconsonantal degemination, PGmc
[spénnilō]{.recon} yields [*spinnl*]{.pred} rather than expected *spinl*. The witnesses
therefore establish the sequence i-umlaut, l-adjacent syncope, preconsonantal
degemination. The first relation separates two historical phases; the second is
a direct feeding relation, since syncope creates the cluster that degemination
simplifies.

## \CAPRRuleHeading{SC067. Dental assimilation in newly formed clusters}{OEDentalAssimilation} {#rule-OEDentalAssimilation}

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

Loss of \emph{*θ} after \emph{*t} resolves a dental cluster produced by syncope
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].
No witness distinguishes its position: moving dental assimilation across every
tested neighbor leaves the outputs unchanged. I nevertheless place it after
syncope, which supplies its input, and before the more general cluster
simplification described in the handbooks. This order is phonologically
motivated, not established by a lexical contrast.

## \CAPRRuleHeading{SC068. Preconsonantal degemination before sonorants}{OEPreconsonantalDegemination} {#rule-OEPreconsonantalDegemination}

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

Preconsonantal \emph{*tt} and \emph{*nn} simplify only after syncope has
created a following sonorant cluster, as in *spinl* ‘spindle’
[@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Placed before l-adjacent syncope, PGmc [spénnilō]{.recon} ‘spindle’ yields [*spinnl*]{.pred} rather
than expected OE *spinl* ‘spindle’. Syncope must therefore create the cluster
before degemination simplifies it. Reordering degemination against any tested
later change leaves the witness unchanged, so no terminus ante quem is known.

\newpage

# Early o-shortening

## Historical discussion

After the principal palatal and umlautal changes, unstressed vowels undergo
shortening, fronting, merger, and sometimes complete loss. Campbell describes
the early shortening of unaccented long vowels, while Hogg, Ringe and Taylor,
and Fulk relate it to apocope, syncope, and the later reductions
[@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening has only a distant earlier boundary. The rules that follow,
especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
have more closely defined relations.

## \CAPRRuleHeading{SC069. Early shortening of unstressed \emph{*ō} before nasals}{OEEarlyOShortening} {#rule-OEEarlyOShortening}

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

The rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Moving the rule before
[SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss), PGmc [nḗdrōn]{.recon} ‘adder’ yields
[*nǣdran*]{.pred} rather than expected OE *nǣdre* ‘adder’, PGmc [érθōn]{.recon} ‘earth’ yields
[*eorþan*]{.pred} rather than expected *eorþe* ‘earth’, and PGmc [fláskōn]{.recon} ‘flask’ yields
[*flascan*]{.pred} rather than expected *flasce* ‘flask’. The same earlier shift also
disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of
failures requires [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening) to follow
[SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss).

If the rule is moved later within the tested sequence, no checked form yields a
form different from the expected one. The checked forms therefore do not
identify a corresponding later constraint. The sources place early
\emph{*ō}-shortening before the later weak-tail changes without fixing a closer
local order.

\newpage

# Early unstressed fronting and later o-shortening

## Historical discussion of early unstressed fronting and later o-shortening

Campbell distinguishes the shortening of unaccented long vowels, while Hogg,
Ringe and Taylor, and Fulk place fronting and shortening within a later history
of syncope and final-vowel adjustment [@Campbell1959, p. 148, §355;
@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7]. Earlier unstressed fronting precedes later
o-shortening.

[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) has both an
earlier and a later lexical breakpoint.
[SC071 OELateOShortening](#rule-OELateOShortening) confirms their reciprocal
order, but no checked form fixes its later boundary.

## \CAPRRuleHeading{SC070. Early fronting of unstressed \emph{*a}}{OEUnstressedFrontingEarly} {#rule-OEUnstressedFrontingEarly}

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

The rule fronts unstressed \emph{*a} to \emph{*æ} after the earlier shortening
has created a frontable vowel but before the later shortening of unstressed
\emph{*ō}. It produces endings such as OE \emph{-en} in *lungen* ‘lungs’.

If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc [búrōθi]{.recon} ‘bears’ yields [*boreþ*]{.pred} rather than expected OE *boraþ* ‘bears’, and PGmc [mḗnōθz]{.recon} ‘month’ yields [*mōneþ*]{.pred} rather than expected *mōnaþ* ‘month’. The witness forms require [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) to follow [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and precede [SC071 OELateOShortening](#rule-OELateOShortening).

The relation to [SC071 OELateOShortening](#rule-OELateOShortening) is local.
The earlier boundary at
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) places fronting after
the older palatal developments.

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting,
producing the later “stable a” endings in OE *boraþ* ‘bears’ and *liornaþ*
‘learns’.

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears', and PGmc [líznōθi]{.recon} ‘learns’ yield [*liorneþ*]{.pred} rather than expected *liornaþ* 'learns'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly). Moving it later within the tested range creates no equally sharp failure.

\newpage

# Unstressed long-vowel shortening and ae-merger

## Historical discussion of unstressed long-vowel shortening and ae-merger

Campbell describes the shortening of unaccented long vowels, and Ringe and
Taylor place it among the last prehistoric Old English changes before the
merger of unstressed \emph{*æ} with \emph{*e}
[@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) have a reciprocal
ordering relation. [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) supplies
the earlier boundary of shortening, and [SC085 OEHLoss](#rule-OEHLoss) the
later boundary of the merger.

## \CAPRRuleHeading{SC072. Shortening of unstressed long vowels}{OEUnstressedLongVowelShortening} {#rule-OEUnstressedLongVowelShortening}

```foma
define OEUnstressedLongVowelShortening OEUnstressedLongVowelShortening1
    .o. OEUnstressedLongVowelShortening2
    .o. OEUnstressedLongVowelShortening3
    .o. OEUnstressedLongVowelShortening5
    .o. OEUnstressedLongVowelShortening6
    .o. OEUnstressedLongVowelShortening7
    .o. OEUnstressedLongVowelShortening8;
```

The rule shortens the remaining unstressed long vowels before weak final
syllables reach their later forms. A small group of lexical witnesses fixes its
chronology.

If the rule is moved before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhten*]{.pred} rather than expected OE *fyrhte* ‘fright’. If the rule is delayed until after [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* ‘adder’, and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* ‘father’. These outputs require [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) to follow [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) and precede [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

Shortening therefore follows the earlier weak-tail preparation and immediately
precedes the merger.

## SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger OEWeakTailReduction3;
```

The rule merges unstressed \emph{*æ} with \emph{*e} after shortening has
produced the weak final vowels, yielding the ordinary OE \emph{-e} spellings.

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* 'adder', and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* 'father'. If the rule is delayed until after [SC085 OEHLoss](#rule-OEHLoss), PGmc [táixōn]{.recon} ‘toe’ yields [*tāæ*]{.pred} rather than expected OE *tā* ‘toe’. These failures show that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss).

The checked forms fix the local order after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and place the merger before the later h-loss and contraction.

\newpage

# Medial unstressed-i lowering

## Historical discussion of medial unstressed-i lowering and \emph{*ng} retention

Hogg and Ringe and Taylor treat the late weakening and merger of unstressed
vowels as a continuing history [@Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6].
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) lowers
medial unstressed \emph{i}; [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering)
preserves \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’
type.

General lowering precedes the restricted restoration before \emph{*ng}. The
evidence is narrower than that for
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

## \CAPRRuleHeading{SC074. First medial unstressed-\emph{i} lowering}{OEMedUnstressedILowering1} {#rule-OEMedUnstressedILowering1}

```foma
define OEMedUnstressedILowering1 [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

The rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding
vocalic syllable. The resulting \emph{e}-outcome is reversed before
\emph{*ng}.

If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhti*]{.pred} rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc [skíllingaz]{.recon} ‘shilling’ yields [*sċilleng*]{.pred} rather than expected *sċilling* ‘shilling’. The derivations require [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) to follow [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and precede [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side. The rule follows unstressed long-vowel
shortening and precedes the more specific \emph{*ng} preservation.

## \CAPRRuleHeading{SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng}}{OEMedUnstressedILowering} {#rule-OEMedUnstressedILowering}

The following rule reverses the lowering before \emph{*ng}.

```foma
define OEMedUnstressedILowering [
    {*e} -> {*i} || _ {*n} {*g}
];
```

The rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Moving the rule before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) makes PGmc [skíllingaz]{.recon} ‘shilling’ yield [*sċilleng*]{.pred} rather than expected OE *sċilling* 'shilling'. On this evidence, I take [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) to follow [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1). Moving it later within the tested range creates no equally sharp failure.

\newpage

# Prefix i-reduction

## Historical discussion

Late weak-tail reduction affects unstressed prefixes as well as inflectional
endings and medial vowels. Fulk's discussion of prefix vowels accounts for OE
\emph{*be-} and \emph{*ne-} [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and
Taylor place such weakening within the broader late history of unstressed
vowels [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--332,
§§6.8.3--6.9.6].

The tested forms do not determine the rule's position relative to a neighboring
change.

## \CAPRRuleHeading{SC076. Reduction of prefixal \emph{*i} in unstressed position}{OEPrefixIReduction} {#rule-OEPrefixIReduction}

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

The rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the
\emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following
vowel. The development accounts for later prefix spellings such as OE
\emph{*be-} and \emph{*ne-}.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

The handbooks attest late prefix-vowel weakening, but the precise placement
remains approximate. No lexical failure fixes it.

\newpage

# Weak-tail reduction

## Historical discussion

Campbell, Hogg, Ringe and Taylor, and Fulk describe a late history in which
apocope, shortening, contraction, and further weak-tail reductions reshape
final syllables [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--91, §5.6]. Lexical failures place the remaining weak-tail
reduction after unstressed fronting and before contraction.

## \CAPRRuleHeading{SC078. Reduction of remaining weak-tail vowels}{OEWeakTailReduction} {#rule-OEWeakTailReduction}

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

The rule reduces the remaining weak-tail vowels, preventing a broad class of
\emph{-en} and extra-vowel outcomes.

I place the change after [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and before [SC086 OEContraction](#rule-OEContraction). Moving it before
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc
[bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc
[bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* ‘bind’, alongside
a much wider set of comparable \emph{-en} failures. If the rule is delayed until
after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields
[*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, and PGmc [sláxaną]{.recon} ‘slay’
yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’.

The earlier boundary spans a wide interval and does not establish a close
neighboring relation. The later boundary is narrower:
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) precedes
[SC086 OEContraction](#rule-OEContraction).

\newpage

# Final-j loss and final geminate simplification

## Historical discussion of final-j loss and final geminate simplification

After [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} in
heavy environments, forms such as *lungen* ‘lungs’ acquire a final geminate.
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification)
then removes the second nasal.

[SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) has a broad earlier boundary
at [SC055 OEIUmlaut](#rule-OEIUmlaut).
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is
fixed only by the final \emph{nn} outcome in the following derivation.

## SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

The rule removes \emph{*j} after the relevant heavy-syllable configurations,
after the earlier umlaut-sensitive vocalism has developed.
The affected glide is \emph{*j}.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [galáubijaną]{.recon} ‘believe’ yields [*ġelēafan*]{.pred} rather than expected OE *ġelīefan* ‘believe’, PGmc [báugijaną]{.recon} ‘bow’ yields [*bēaġan*]{.pred} rather than expected *bīeġan* ‘bow’, and PGmc [fúlgijaną]{.recon} ‘follow’ yields [*fulġan*]{.pred} rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lungenn*]{.pred} rather than expected OE *lungen* ‘lungs’. I accordingly take [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The earlier boundary is broad, but the relation to final geminate
simplification is local.

## \CAPRRuleHeading{SC080. Simplification of final geminates}{OEFinalGeminateSimplification} {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

The rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Moving the rule before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) makes PGmc [lúnganjō]{.recon} ‘lungs’ yield [*lungenn*]{.pred} rather than expected OE *lungen* 'lungs'. These failures require [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) to follow [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

# J-strengthening, vocalization, and ei-contraction

## Historical discussion of j-strengthening, vocalization, and ei-contraction

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
vocalizes the remaining intervocalic \emph{*j}, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) removes the
resulting \emph{ei}-like sequence in weak verbal endings.

The output of each rule conditions the next.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) has local
lexical evidence on both sides;
[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
has a distant earlier boundary, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) has no
tested later boundary.

## \CAPRRuleHeading{SC081. Strengthening of \emph{*j} after front diphthongs}{OEJStrengtheningAfterFrontDiphthong} {#rule-OEJStrengtheningAfterFrontDiphthong}

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

After the relevant front diphthongs, \emph{*j} first strengthened to a consonantal outcome; otherwise it would have vocalized too early.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [stráwjaną]{.recon} ‘strew’ yields [*strēaġan*]{.pred} rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields [*strīeian*]{.pred} rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* 'strew' derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

## \CAPRRuleHeading{SC082. Intervocalic vocalization of \emph{*j}}{OEIntervocalicJVocalization} {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule vocalizes intervocalic \emph{*j} to \emph{*i}, creating the
\emph{ei}-like sequence later removed by
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak
verb forms.

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc [stráwjaną]{.recon} ‘strew’ yield [*strīeian*]{.pred} rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* ‘bore’, PGmc [xándlōjaną]{.recon} ‘handle’ yield [*handleian*]{.pred} rather than expected *handlian* ‘handle’, and PGmc [mákōjaną]{.recon} ‘make’ yield [*maceian*]{.pred} rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* 'bore', PGmc [líznōjaną]{.recon} ‘learn’ yield [*liorneian*]{.pred} rather than expected *liornian* 'learn', and PGmc [líkkōjaną]{.recon} ‘lick’ yield [*licceian*]{.pred} rather than expected *liccian* 'lick'. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

# H-loss and contraction

## Historical discussion of h-loss and contraction

When [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, it creates
hiatus. [SC086 OEContraction](#rule-OEContraction) immediately resolves the
resulting vowel sequence.

Ringe and Taylor describe this late sequence of \emph{h}-loss and contraction
[@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk places the contracted
verbs in a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick
describes the corresponding West Germanic contractions [@Luick1914, p. 165].

## SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc [táixōn]{.recon} ‘toe’ yields [*tāæ*]{.pred} rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields [*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, PGmc [sláxaną]{.recon} ‘slay’ yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’, PGmc [téxun]{.recon} ‘draw’ yields [*teoon*]{.pred} rather than expected *tēon* ‘draw’, and PGmc [táixōn]{.recon} yields [*tāe*]{.pred} rather than expected *tā*. These outputs require [SC085 OEHLoss](#rule-OEHLoss) to follow [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) and precede [SC086 OEContraction](#rule-OEContraction).

The earlier boundary rests on one witness; the four later witnesses establish
the immediate relation to contraction.

## SC086. Contraction of the resulting hiatus (`OEContraction`) {#rule-OEContraction}

The following rule contracts the hiatus left by [SC085 OEHLoss](#rule-OEHLoss).

```foma
define OEContraction [
    {*a} {*a} -> {*ā},
    {*e} {*e} -> {*ē},
    {*i} {*i} -> {*ī},
    {*o} {*o} -> {*ō},
    {*u} {*u} -> {*ū},
    {*ea} {*a} -> {*ēa},
    {*ēa} {*a} -> {*ēa},
    {*eo} {*a} -> {*ēo},
    {*ēo} {*a} -> {*ēo},
    {*eo} {*o} -> {*ēo},
    {*ēo} {*o} -> {*ēo},
    {*éo} {*o} -> {*ḗo},
    {*ḗo} {*o} -> {*ḗo},
    {*ā} {*a} -> {*ā},
    {*ā} {*e} -> {*ā},
    {*ē} {*a} -> {*ē},
    {*ē} {*e} -> {*ē},
    {*ḗ} {*a} -> {*ḗ},
    {*ḗ} {*e} -> {*ḗ},
    {*ī} {*a} -> {*ī},
    {*ī} {*e} -> {*ī},
    {*ḯ} {*a} -> {*ḯ},
    {*ḯ} {*e} -> {*ḯ},
    {*ō} {*a} -> {*ō},
    {*ō} {*e} -> {*ō},
    {*ū} {*a} -> {*ū},
    {*ū} {*e} -> {*ū}
];
```

The rule contracts the vowel sequences created after \emph{h}-loss, producing
*flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Moving contraction before [SC085 OEHLoss](#rule-OEHLoss) makes PGmc [fléuxaną]{.recon} ‘flee’ yield [*flēoan*]{.pred} rather than expected OE *flēon* 'flee', PGmc [sláxaną]{.recon} ‘slay’ yield [*sleaan*]{.pred} rather than expected *slēan* 'slay', PGmc [téxun]{.recon} ‘draw’ yield [*teoon*]{.pred} rather than expected *tēon* 'draw', and PGmc [táixōn]{.recon} ‘toe’ yield [*tāe*]{.pred} rather than expected *tā* 'toe'. The derivations require [SC086 OEContraction](#rule-OEContraction) to follow [SC085 OEHLoss](#rule-OEHLoss). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
The more distant [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
relation establishes only that weak-tail reduction precedes contraction.

\newpage

# R-metathesis

## Historical discussion

Sievers-Brunner describes r-metathesis in forms such as *berstan* ‘burst’,
*forst* ‘frost’, and *cærse* ‘cress’
[@SieversBrunner1965, p. 159, §179]. Luick likewise treats it as a later
rearrangement whose interaction with breaking remains variable
[@Luick1914, p. 201].

The evidence establishes that breaking precedes metathesis. It does not
establish an ordering relation between
[SC086 OEContraction](#rule-OEContraction) and
[SC087 OERMetathesis](#rule-OERMetathesis).

## \CAPRRuleHeading{SC087. Metathesis of \emph{*r} with a following short vowel}{OERMetathesis} {#rule-OERMetathesis}

```foma
define OERMetathesis [
    {*r} {*e} -> {*e} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*u} -> {*u} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*i} -> {*i} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*o} -> {*o} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*a} -> {*a} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*é} -> {*é} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*ó} -> {*ó} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*á} -> {*á} {*r} || EnglishStarConsonant _ {*s} {*t}
];
```

The rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Moving the rule before [SC044 OEBreaking](#rule-OEBreaking) makes PGmc [bréstaną]{.recon} ‘burst’ yield [*beorstan*]{.pred} rather than expected OE *berstan* ‘burst’. On this evidence, I take [SC087 OERMetathesis](#rule-OERMetathesis) to follow [SC044 OEBreaking](#rule-OEBreaking). Moving it later within the tested sequence alters none of the checked outputs.

The checked forms fix the earlier relation but do not identify a corresponding
later constraint. The sources treat r-metathesis as a late rearrangement after
breaking without placing it immediately beside contraction.

\newpage

# References

::: {#refs}
:::
