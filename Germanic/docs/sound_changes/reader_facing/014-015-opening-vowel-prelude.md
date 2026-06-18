# Early unstressed vowel changes

## Historical discussion of the earliest unstressed vowel changes

These two rules stand at the start of the current sequence. One removes the remaining diphthongal quality of unstressed \emph{*ai}; the other carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. They do not carry equal chronological weight: [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) is historically clear but not closely fixed by the tested forms, whereas [SC015 NWGmcILowering](#rule-NWGmcILowering) has the stronger diagnostic constraint.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. That is enough to make [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) historically recognizable even though the order test does not by itself determine a closer relative position.

## SC014. Monophthongization of unstressed \emph{*ai} (`NWGmcUnstressedAiMonophthongization`) {#rule-NWGmcUnstressedAiMonophthongization}

The implementation keeps the monophthongization step explicit.

```foma
define NWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

In prose, the rule removes the unstressed diphthongal quality of \emph{*ai} and merges the result with unstressed \emph{*e}. It preserves a historically plausible opening step in the early Northwest Germanic vowel history.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) before or after any specific neighboring change. CAPR places it at the beginning of the unstressed-vowel prelude because the comparative sources treat unstressed \emph{*ai} monophthongization as part of the earliest Northwest Germanic simplification of unstressed vowels. The placement should be read as approximate, not as a local ordering forced by the tested forms.

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

Its chronology is real but one-sided. If the rule is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*wír-àldu} yields *wuruld* rather than expected OE *weorold* ‘world’. This shows that [SC015 NWGmcILowering](#rule-NWGmcILowering) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising). Moving the rule earlier within the tested sequence, however, did not produce a diagnostic contrast among the checked forms before the search reached the start of the tested early sequence, so the order test does not yet give a closer earlier constraint.

Together these two early notes hand the sequence forward to [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering), where the local chronology becomes tighter and the derivations more crowded.
