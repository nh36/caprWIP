# Prefix and compound adjustments

## Historical discussion of prefixal \emph{*a}-reduction

Weakly stressed prefixes can lose their older low vowel early in Old English, and that is the historical setting for [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction). Campbell treats the small but real class of pretonic losses directly, while Ringe and Taylor's derivation of \emph{*galaubijana} gives the clearest comparative witness for the same development [@Campbell1959, p. 147, §354; @RingeTaylor2014, p. 245; @RingeTaylor2014, p. 267].

The result is a modest rule with a narrow historical range. It matters because it gives prefixed forms the weak vowel shape that later vocalic rules inherit.

## SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

The implementation states the prefixal reduction directly.

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

In prose, the rule reduces prefixal \emph{*ga-} to unstressed \emph{*ge-}. This is the step that gives forms such as *ġelīefan* ‘believe’ their expected prefix vowel.

Its chronology is one-sided but concrete. If the rule is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*galáubijaną} yields *ġealīefan* rather than expected OE *ġelīefan* ‘believe’. This shows that [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). The earlier direction remains boundary-limited in current testing: the search reaches bundled earlier material without finding an ordinary historical break, so the card does not yet show what this rule must follow.

## Historical discussion of inter-stress raising

The strongest member of this chapter is [SC036 OEInterStressRaising](#rule-OEInterStressRaising). Campbell's discussion of *weorold* / *weoruld* and Ringe and Taylor's derivation of \emph{*weraldu} > \emph{*weruldu} > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

This is more than a small spelling adjustment. The rule changes the vowel that stands between stronger stress peaks, which is why its witnesses remain so useful for chronology.

## SC036. Raising of medial \emph{*a} between stress peaks (`OEInterStressRaising`) {#rule-OEInterStressRaising}

The implementation keeps both parts of the raising rule together.

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

In prose, the rule raises medial unstressed \emph{*a} to \emph{*u} in the low-stress position between stronger syllables. This is the stage behind forms such as *sāwol* ‘soul’ and *weorold* ‘world’.

Its chronology is explicit on both sides. If the rule is moved before SC019 NWGmcFinalLongORaising, PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*sáiwalō} yields *sāwul* rather than expected *sāwol*, and PGmc \emph{*wír-àldu} yields *weoruld* rather than expected *weorold* ‘world’. This shows that SC019 NWGmcFinalLongORaising must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising), and that [SC036 OEInterStressRaising](#rule-OEInterStressRaising) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The earlier boundary is real, but it reaches farther back than the immediate neighborhood. The later boundary is the more local result inside this part of the sequence.

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

That is the historical setting for [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope). The rule is worth stating explicitly because compounds such as *reġnboga* ‘rainbow’ depend on it, even though its chronology is narrower and less ordinary-historical than the rule beside it.

## SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

The implementation deletes the weak linking vowel in the relevant compound environment.

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

In prose, the rule removes a weak linking vowel inside compounds before a following grave-stressed member. This is the step that yields forms such as *reġnboga* ‘rainbow’.

Its chronology is boundary-limited. If the rule is delayed until after SC038 OEStripSecondaryStress, PGmc \emph{*régna-bùgô} yields *reġnefoga* rather than expected OE *reġnboga* ‘rainbow’. This shows that [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) must come before SC038 OEStripSecondaryStress, but that conclusion is technical rather than ordinary-historical because SC038 OEStripSecondaryStress is not an ordinary sound change. The earlier direction also reaches bundled earlier material without finding a historical break, so the present evidence remains one-sided and boundary-limited.
