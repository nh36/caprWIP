# High-vowel apocope

## Historical discussion

Final high vowels must survive long enough to condition umlaut before apocope
removes them after heavy syllables and in the relevant trisyllabic patterns.
Campbell, Hogg, Ringe and Taylor, and Fulk agree that the loss follows
mutation, but disagree substantively over trisyllables and surrounding syncope
[@Campbell1959, pp. 144--145, §§345--349; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].
Barrack states the deletion of final high vowels as his rule 345 and
presents it as a prime case of an environment that simplifies progressively
over the rule's lifetime [@Barrack1975, pp. 85--86, 23--25]; the heavy-foot
conditioning adopted here corresponds to his most restricted, earliest
phase, while his later phases absorb the surrounding quantity developments
that the handbooks treat as separate changes.

This later loss is distinct from the West Germanic weak-word loss of
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
A selected proclitic context does not become word-final merely because its
citation spelling ends there. Its temporary boundary annotation blocks
the final-position conditions below and is removed only after their
application; it is not a segment of the linguistic reconstruction.
This contextual distinction is preserved
[@RingeTaylor2014, pp. 57--58, 284--303].

The adopted conventional account retains final high vowels after a heavy
first syllable followed by a light syllable. Thus
\emph{*hēafudu > *hēafdu}, not [hēafd]{.pred}: subsequent high-vowel syncope
does not restart apocope. The former implementation incorrectly deleted
the final vowel in this heavy--light environment
[@Campbell1959, p. 146, §353; @HoggGrammar2011, pp. 225--227, §§6.22--6.25].
Loss after two light syllables and after an immediately preceding heavy
syllable remains represented.

This is a defended working account, not unanimity. Fulk's conservative
Mercian *hēafudu*, *idelu* and *lytel(u)* material supports retention of
both high vowels before a light final syllable; he supplies phonological
weight and paradigm evidence, not merely a preference for analogy.
Ringe and Taylor instead defend syncope before apocope and reconstructed
\emph{*hēafd}, treating the attested plurals as analogical.
Hogg also offers a tentative one-syllable-reduction account without rigid
serialization [@Fulk2010, pp. 129--134, 140--142;
@RingeTaylor2014, pp. 289--293; @HoggGrammar2011, p. 227, §6.25].
The conventional serialization keeps this dispute explicit and no longer
preserves unsupported endingless selected histories by excess apocope.

## SC063. High-vowel apocope after heavy syllables and in trisyllables (`OEHighVowelApocope`) {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope Ctx([
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
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
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
