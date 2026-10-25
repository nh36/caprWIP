# High-vowel apocope

## Historical discussion

Final high vowels must survive long enough to condition umlaut before apocope
removes them after heavy syllables and in the relevant trisyllabic patterns.
Campbell, Hogg, Ringe and Taylor, and Fulk agree on this Old English
development, though they differ over the extent of the surrounding syncope
[@Campbell1959, pp. 144--145, §§345--349; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

This later loss is distinct from the West Germanic weak-word loss of
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
A selected proclitic context does not become word-final merely because its
citation spelling ends there. Its temporary boundary annotation blocks
the final-position conditions below and is removed only after their
application; it is not a segment of the linguistic reconstruction.
The vowel-replacement clauses themselves are unchanged
[@RingeTaylor2014, pp. 57--58, 284--303].

## SC063. High-vowel apocope after heavy syllables and in trisyllables (`OEHighVowelApocope`) {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope Ctx([
    # Disyllabic: long syllable (long vowel + consonant(s)) + final vowel
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    # Disyllabic: diphthong + consonant(s) + final vowel
    # LONG diphthongs are heavy (any C count). SHORT diphthongs are heavy only
    # with 2+ consonants; a short diphthong + single C is a LIGHT syllable (from
    # back-umlaut of a light stem, Campbell §345; DEV_NOTES §17.17).
    # E.g. *spéru → speoru (LIGHT, retain -u); *xérdō → heord (HEAVY, lose -u).
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Disyllabic: heavy closed syllable (short vowel + 2+ consonants) + final vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Trisyllabic: long/diphthong + unstressed syllable + final vowel (Campbell §345)
    # Pattern: LongV/Diph + C+ + shortV + C+ + final_vowel
    # Example: heofon < *xemonų: *e*o + *β + *u + *n + *ų
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with short-diphthong first syllable (from back-umlaut of a light
    # stem): trisyllabic apocope still fires regardless of stress-syllable weight
    # (Campbell §345). E.g. *xémonų → *xéomonų → heofon.
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic: short syllable + another syllable + final vowel (Campbell §345)
    # Pattern: shortV + C + shortV + C+ + final_vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with heavy-by-position first syllable (short V + 2+C) +
    # light second syllable + final high V (Campbell §345; DEV_NOTES §17.45.4).
    # E.g. *spénnilō → *spinnilu → *spinnil (then OELAdjacentSyncope + nn-degem → spinl).
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # R/T §6.6.1: vowel-hiatus contraction — word-final *i after long vowel
    # with no intervening consonant (e.g. root noun dat.sg. *kūi → cȳ)
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    # Campbell §238/§346: final -u lost after /h/ (*x) regardless of weight.
    # Must fire before intervocalic h-loss would remove the conditioning.
    # E.g. *féxu → *féoxu → feoh (not feou).
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
] .o. [{*ᶜ} -> 0]);
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
