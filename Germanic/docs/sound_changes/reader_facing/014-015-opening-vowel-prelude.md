# Early unstressed vowel changes

## Historical discussion of the earliest unstressed vowel changes

These two rules stand at the start of the current sequence. One removes the remaining diphthongal quality of unstressed \emph{*ai}; the other carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. They do not carry equal chronological weight: [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) is historically legible but boundary-limited, while [SC015 NWGmcILowering](#rule-NWGmcILowering) has the stronger witness and the one live positive boundary.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. That is enough to make [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) historically recognizable even though current order testing does not recover a positive local boundary.

## SC014. Monophthongization of unstressed \emph{*ai} (`NWGmcUnstressedAiMonophthongization`) {#rule-NWGmcUnstressedAiMonophthongization}

The implementation keeps the monophthongization step explicit.

```foma
define NWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

In prose, the rule removes the unstressed diphthongal quality of \emph{*ai} and merges the result with unstressed \emph{*e}. It preserves a historically plausible opening step in the early Northwest Germanic vowel history.

Current testing does not identify a positive historical boundary on either side. If the rule is moved earlier or later within the currently tested range, no witness word yields a historical first-break result: the earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. In reader-facing terms, this is a historically legible change whose current order evidence remains chronology-negative. The rule is placed here because the comparative literature treats unstressed \emph{*ai} monophthongization as part of the earliest Northwest Germanic simplification of unstressed vowels. This position should therefore be read as an informed opening placement rather than as a slot fixed by a neighboring diagnostic failure.

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* and *weoruld* [@Campbell1959, pp. 141--142, 154--155]. That gives [SC015 NWGmcILowering](#rule-NWGmcILowering) a clearer historical center than the change beside it.

## SC015. Leveling of early unstressed front vowels (`NWGmcILowering`) {#rule-NWGmcILowering}

The implementation keeps the lowering step explicit.

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

In prose, the rule lowers or levels early front-vowel quality in unstressed syllables. In the current sequence, that adjustment is especially visible in the pathway to *weorold* ‘world’.

Its chronology is real but one-sided. If the rule is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*wír-àldu} yields *wuruld* rather than expected OE *weorold* ‘world’. This shows that [SC015 NWGmcILowering](#rule-NWGmcILowering) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising). If the rule is moved earlier within the currently tested range, no witness word yields a historical first-break result before the search reaches bundled earlier material, so no earlier positive boundary is yet available.

Together these two early notes hand the sequence forward to [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering), where the local chronology becomes tighter and the derivations more crowded.
