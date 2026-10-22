# Prefix and compound adjustments

## Historical discussion of prefixal \emph{*a}-reduction

Old English *ġelīefan* 'believe' continues a formation with inherited
\emph{*ga-}. Gothic *ga-* preserves the older vowel, while Old Saxon and
Old High German *gi-* and Old English *ge-* exhibit reduced reflexes;
Ringe and Taylor reconstruct \emph{*ga-} for both Proto-Germanic and
Proto-West-Germanic. Comparable reduced prefixes do not by themselves
establish a single shared West Germanic reduction event
[@RingeTaylor2014, p. 206].

The English development is not one securely dated replacement of
\emph{*a} by \emph{*e}. Ordinary unstressed fronting supplies an
\emph{*æ}-type vowel; early *gi-* and later *ge-* belong to the subsequent
history of unstressed front vowels. Campbell describes the general
fronting and later merger separately, while Ringe and Taylor discuss
the prefix's early *i*-spellings and eventual *e*. They leave open
whether raising after the palatal consonant was wholly regular or
influenced by the parallel prefix *bi-*; the present model does not
make that possible analogy a sound-law condition
[@Campbell1959, pp. 140--141, §§333--334; @Campbell1959, pp. 153--155,
§§369--370; @RingeTaylor2014, pp. 334--335].

Stress is crucial. The ordinary prefix is unstressed even in nouns,
unlike many other prefixes. The exceptional accented form associated
with *ġeatwe* 'armour' must be distinguished from that weak form.
Thus the historical conditioning is prosodic, not a rule applying
because a word belongs to a grammatical class
[@Campbell1959, p. 31, §74 and n. 5; @HoggPhonology1992, pp. 99--100;
@RingeTaylor2014, p. 335].

[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) compresses this
pre-Old English to Old English history into a single operation.
The weak prefix in *ġelīefan* 'believe' is source-backed, as are the different
West Saxon and Anglian root-vowel outcomes. Those derivations establish
the history to be represented, not the exact date or intermediate
symbols of the compressed rule
[@RingeTaylor2014, pp. 245, 267].

## SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

The breve in \emph{*ĕ} marks a reduced unstressed vowel in the
representation. It is not an independently reconstructed phonetic stage
or a claim of early schwa. Its surface reflex is *e*, and the marking
prevents later operations appropriate to stressed vowels from
diphthongizing the prefix. This is consistent with the historical
absence of palatal diphthongization in the weak prefix
[@RingeTaylor2014, p. 206].

The consonant-plus-vowel context is deliberately narrower than the
historical phenomenon. It covers the prefix before the root of
*ġelīefan* 'believe', but neither encodes a prefix boundary nor recognizes all
prefixed words. Ringe and Taylor's *gistīga* 'climb into/onto' >
*gestīga* 'climb into/onto',
with the prefix before a consonant cluster, illustrates a genuine
prefix shape outside this rule. Conversely, the accented root vowel
of *ġealla* 'gall' is not eligible. The selected stress representation,
not the initial letters alone, protects such roots
[@RingeTaylor2014, p. 335].

The implementation's ordering dependency concerns
SC107 EAFBrighteningUnstressed, the retained unstressed component
discussed with [SC043 EAFBrightening](#rule-EAFBrightening), not that
ordinary stressed fronting law.
Without the protective representation, the unstressed component fronts
the prefix to \emph{*æ}; later palatal diphthongization then gives
[*ġealīefan*]{.pred} rather than *ġelīefan* 'believe'. That dependency explains
the model's order but does not date a separate historical reduction
before stressed fronting: the compressed operation already represents
part of the weak vowel's fronting and merger history.
Nor does the limit of an earlier displacement experiment establish a
historical terminus after all West Germanic changes.
The development itself is secure; its precise date and the full
conditioning of the compressed proxy are less certain.

## Historical discussion of inter-stress raising

[SC036 OEInterStressRaising](#rule-OEInterStressRaising) has the strongest evidence of the three. Campbell's discussion of *weorold* 'world' / *weoruld* 'world' and Ringe and Taylor's derivation of [weraldu]{.recon} 'world' > [weruldu]{.recon} 'world' > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

The rule changes the vowel between stronger stress peaks, and its witnesses consequently constrain the relative chronology.

## SC036. Raising of medial \emph{*a} between stress peaks (`OEInterStressRaising`) {#rule-OEInterStressRaising}

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

The two boundaries have unequal force. Before [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc [sáiwalō]{.recon} ‘soul’ yields [*sāwel*]{.pred} rather than expected OE *sāwol* ‘soul’; after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), it yields [*sāwul*]{.pred} rather than *sāwol*, while PGmc [wír-àldu]{.recon} ‘world’ yields [*weoruld*]{.pred} rather than *weorold* ‘world’. The distant lower boundary places inter-stress raising after final long-\emph{o} raising, and the local upper boundary places it before medial unstressed-\emph{u} lowering. In handbook terms, medial \emph{*a} > \emph{*u} belongs to the \emph{world}- and \emph{soul}-type low-stress vocalism that followed the earlier final-vowel changes.

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* ‘rainbow’. The only boundary the lexical evidence supplies
is the immediately following technical stress-stripping stage, which is not a
sound change.

## SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* 'rainbow' test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc [régna-bùgô]{.recon} ‘rainbow’ yields [*reġnefoga*]{.pred} rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).
