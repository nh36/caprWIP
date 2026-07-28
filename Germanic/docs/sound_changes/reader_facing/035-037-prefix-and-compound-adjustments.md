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

## SC036. Raising of medial \emph{*a} between stress peaks (`OEInterStressRaising`) {#rule-OEInterStressRaising}

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

## SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* 'rainbow' test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc [régna-bùgô]{.recon} ‘rainbow’ yields [*reġnefoga*]{.pred} rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).
