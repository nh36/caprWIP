# A-restoration and nasal changes

## Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}.

[SC046 OEARestoration](#rule-OEARestoration) has firmer handbook support than the two following nasal rules.

## SC046. Restoration of \emph{*a} before following back vowels (`OEARestoration`) {#rule-OEARestoration}

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

Restoration must receive fronted \emph{*æ} and return \emph{*a} before the nasal-tail changes. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*bákaną} yields *bæcan* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*fáraną} yields *færan* rather than expected *faran* ‘fare’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), \emph{*bákaną} again yields *bæcan* instead of *bacan*, while PGmc \emph{*wádaną} yields *wædan* instead of *wadan* ‘wade’. These independent witness pairs place restoration after brightening and before secondary nasalization.

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

## SC047. Heavy-syllable nasal apocope of final \emph{*ą} (`OEHeavySyllableNasalApocope`) {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

The evidence for final nasalized \emph{*ą} loss is sharply asymmetric. Before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), the single PGmc witness \emph{*stráwą} yields *stræw* rather than expected OE *strēaw* ‘straw’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a broad \emph{-en} failure set. One lower witness places apocope after long-diphthong formation; many reciprocal upper failures place it before secondary nasalization.

## SC048. Secondary nasalization before final \emph{*n} (`OESecondaryNasalization`) {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

The broad \emph{-an}/\emph{-en} split fixes the lower boundary of final \emph{*a} nasalization before \emph{n}. Before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan*, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan*. The upper boundary comes from back mutation. After [SC059 OEBackMutation](#rule-OEBackMutation), PGmc \emph{*stélaną} yields *steolan* rather than expected OE *stelan* ‘steal’, and PGmc \emph{*wébaną} yields *weofan* rather than expected *wefan* ‘weave’. Reciprocal nasal-tail failures place secondary nasalization after apocope, and the later mutation witnesses place it before back mutation; [SC046 OEARestoration](#rule-OEARestoration) retains the clearest independent historical support.
