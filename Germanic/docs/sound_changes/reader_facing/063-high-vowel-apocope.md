# High-vowel apocope

## Historical discussion

By this point in the sequence the main palatal and umlautal changes are already in place, but weak-tail reduction is not finished. Final high vowels still survive in many forms until a late apocope removes them after heavy syllables and in the relevant trisyllabic patterns. Campbell, Hogg, Ringe and Taylor, and Fulk all describe this as a real Old English development, even when they differ over how much of the surrounding syncope material should be grouped with it [@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, p. 120; @RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

The rule matters because it makes many familiar Old English forms look abruptly shorter than their earlier stages. It is also a good place to show how finite-state chronology works. The derivation can say exactly which forms fail if apocope is moved too early or too late, so the late weak-tail sequence becomes visible through concrete lexical breakpoints and explicit ordering statements.

## SC063. High-vowel apocope after heavy syllables and in trisyllables (`OEHighVowelApocope`) {#rule-OEHighVowelApocope}

The implementation keeps the whole apocope system in one explicit rule.

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

In prose, the rule deletes final \emph{*i}, \emph{*u}, and \emph{*ų} when the preceding structure is heavy enough, or when a trisyllabic form behaves as equivalent to a heavy environment. The longer code box makes visible how many separate environments the transducer has to distinguish in order to realize what the handbooks describe more compactly.

Its chronology is explicit on both sides. If the rule is moved before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*kūi} yields *cū* rather than
expected OE *cȳ* ‘cow’, and PGmc \emph{*brūdiz} yields *brūd* rather than
expected OE *brȳd* ‘bride’. If the rule is delayed until after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*fúrxtīnaz} yields *fyrht*
rather than expected OE *fyrhte* ‘fright’. This means that
[SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), and that
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope) must come before
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

That placement is historically apt. The rule must come late enough for umlautal effects to have already been created, but it is not the last weak-tail event in the language. Apocope removes a major set of final high vowels, yet later weak-tail cleanup still remains.
