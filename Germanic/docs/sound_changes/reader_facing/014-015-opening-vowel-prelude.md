# Early unstressed vowel changes

## Historical discussion

The first change removes the remaining diphthongal quality of unstressed \emph{*ai} word-finally; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* 'world'. Their chronological evidence differs. The word-final monophthongization is historically clear but has no witness in the dataset, whereas \emph{*i}-lowering has a diagnostic later boundary.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. The word-final case is the one modeled below; the historical change is established, although no lexical witness in the dataset carries it, so the data fix no closer relative position. The general development of \emph{*ai} to \emph{*ā} is treated separately as [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## SC014. Monophthongization of unstressed \emph{*ai} (`PNWGmcUnstressedAiMonophthongization`) {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization [
    {*ai} -> {*ē} || _ .#.
];
```

This change has no current lexical applications. No Old English witness in the dataset carries word-final unstressed \emph{*-ai}; the historical evidence for it comes from inflectional endings such as the dative singular \emph{*-ai} and the strong-adjective plural \emph{*-ai}. Moving [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) earlier or later changes no output.

Ringe and Taylor's merger of unstressed \emph{*ai} with long mid \emph{*ē} establishes the historical development; the endings that carry it are absent from the dataset as standalone words, so the witnesses do not fix its position relative to neighboring changes. The general development of \emph{*ai} to \emph{*ā} in stressed and nonfinal syllables is a separate and later change; see [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* 'world' and *weoruld* 'world' [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 PNWGmcILowering](#rule-PNWGmcILowering) with a firmer lexical basis than the preceding change.

## SC015. Leveling of early unstressed front vowels (`PNWGmcILowering`) {#rule-PNWGmcILowering}

```foma
define PNWGmcILowering [
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

The *weorold* 'world' and *weoruld* 'world' variants turn the general source claim into an ordering test. If [SC015 PNWGmcILowering](#rule-PNWGmcILowering) is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc [wír-àldu]{.recon} ‘world’ yields [*wuruld*]{.pred} rather than expected OE *weorold* ‘world’; earlier movement changes no output.

The derivation thus fixes front-vowel leveling before interstress raising while leaving its earlier boundary open.

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 PNWGmcULowering](#rule-PNWGmcULowering) follow with a more tightly constrained local chronology.
