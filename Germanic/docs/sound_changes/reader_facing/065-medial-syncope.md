# Medial syncope before dentals

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

Loss of medial \emph{*i} before dentals belongs to the late weak-tail history
described by Hogg, Ringe and Taylor, and Fulk
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6]. In Barrack's cascade the corresponding territory is
covered by his syncope rules 347 and 351 [@Barrack1975, pp. 86--87], with
further medial losses at rules 388 and 390, the latter citing \emph{meolc}
'milk' [@Barrack1975, p. 96]; his rules are broader than the
dental-conditioned statement here and are not coextensive with it.

```foma
define OEMedialSyncope FootCtx([
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
]);
```

No diagnostic word establishes a local chronology. Moving medial syncope to
either end of the tested range leaves every output unchanged. Its
handbook placement after apocope and before later cluster simplification
therefore remains preferable, but the present lexicon cannot demonstrate it.
