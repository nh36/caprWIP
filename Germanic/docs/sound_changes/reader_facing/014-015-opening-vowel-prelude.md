# Early unstressed vowel changes

## Historical discussion

The first change removes the remaining diphthongal quality of unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. Their chronological evidence differs: monophthongization is historically clear but not closely dated by the witness forms, whereas \emph{*i}-lowering has a diagnostic later boundary.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. The historical change is thus established, although the order test determines no closer relative position.

## SC014. Monophthongization of unstressed \emph{*ai} (`PNWGmcUnstressedAiMonophthongization`) {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

Moving [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) earlier or later changes no output. The lexicon therefore cannot refine its source-based placement among the earliest Northwest Germanic simplifications of unstressed vowels.

Ringe and Taylor's merger of unstressed \emph{*ai} with \emph{*e} establishes the historical development; the current witnesses do not distinguish its position relative to neighboring changes.

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

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering) follow with a more tightly constrained local chronology.
