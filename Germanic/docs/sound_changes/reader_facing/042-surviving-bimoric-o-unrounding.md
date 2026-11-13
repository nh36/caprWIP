# Surviving bimoric \emph{*ō} unrounding

## Historical discussion

The development has independent comparative support, not merely a successful derivation of one Old English word. Ringe and Taylor explicitly reconstruct surviving bimoric \emph{*ō} as West Germanic \emph{*ā} word-finally and before final \emph{*r}; trimoric vowels instead give \emph{*ō}, while the two quantities merge as \emph{*ō} in other unstressed environments [@RingeTaylor2014, pp. 58--60]. Quantity, finality and the remaining consonants are therefore essential to their account. A phonological law, not membership in a declension, distinguishes the outcomes.

Their comparative examples include the histories of *wæter* 'water' and *fēower* 'four' before final \emph{*r}, and final-vowel histories continued by *ġiefe* 'gift', *tunge* 'tongue' and *heorte* 'heart'. The different quantity underlying *nama* 'name' supplies a contrast, not an exception. They place unrounding before shortening before final \emph{*r} and argue for a West Germanic development partly from the retention of rounded vowels in Early Runic [@RingeTaylor2014, pp. 59--60]. These are the authors' comparative and runic arguments, not additional applications of the operation printed below or new independent readings of inscriptions.

The quantity analysis is not uniform across handbooks. Hogg discusses nasal-associated low-vowel outcomes and the survival and shortening of long vowels, but includes the genitive singular among the endings considered in his trimoric-vowel discussion and explicitly qualifies the security of that classification [@HoggGrammar2011, p. 64, §3.32; pp. 227--228, §§6.26--28, especially §6.27 n. 2]. Ringe and Taylor instead explicitly assign the relevant genitive a bimoric input and reconstruct long \emph{*ā} followed by long \emph{*ǣ} on its way to final *-e* [@RingeTaylor2014, pp. 59, 299--300]. The length is consequently not an invention required only to obtain a particular output, although the detailed prehistoric quantity remains a matter for source criticism.

Campbell's discussion of fronting and restoration, Hogg's separate historical chapter, and Ringe and Taylor's English restoration account explain the surrounding English developments, rather than independently establishing the West Germanic unrounding law [@Campbell1959, pp. 52, 60--61, §§131, 157--158; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 189--190]. The grammar cited for long-vowel quantity above is Hogg's monograph in its 2011 pagination, not that 1992 chapter.

## SC042. Unrounding of the surviving bimoric \emph{*ō} (`PWGmcSurvivingBimoricOUnrounding`) {#rule-PWGmcSurvivingBimoricOUnrounding}

```foma
define PWGmcSurvivingBimoricOUnrounding Ctx([
    [{*ō}|{*ǭ}] -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
]);
```

The operation merges surviving final oral and nasal bimoric vowels in
\emph{*ā} before English final-vowel fronting. Its preceding-nucleus and
intervening-consonant guard selects a polysyllabic shape; it does not
independently reconstruct historical stress. The restriction to the final
vowel preserves nasalized roots and the separate trimoric quantity.
Before-final-\emph{*r} histories remain distributed: the selected water
and four inputs already contain \emph{*a} there.

The complete current population has twenty-two applications: the oral
ending in *ræste* 'rest', from selected genitive \emph{*rástōz}, and
twenty-one nasal-final histories. These include *mære* 'nightmare',
*tunge* 'tongue', *heorte* 'heart' and *sāwle* 'soul'.
The selected gift input remains \emph{*gíftiz}: the literature's
\emph{*gebōz} is a separate control, not another corpus application.
No lexical list or grammatical condition selects the endings.

After [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) exposes \emph{*rástō}, unrounding gives \emph{*rástā}. [SC043 EAFBrightening](#rule-EAFBrightening) fronts the root, and the final-vowel support [SC108 EAFBrighteningLongFinal](#rule-EAFBrighteningLongFinal) gives \emph{*ræstǣ}; subsequent shortening and merger yield *ræste* 'rest'. The final support carries quantity in the model and is not another independently dated sound law. The West Germanic long-vowel reconstruction has a source basis, but this exact serialized chain remains a computational representation of the selected history.

For *mære* 'nightmare', the final nasal vowel becomes \emph{*ā} here,
then \emph{*ǣ} under [SC108 EAFBrighteningLongFinal](#rule-EAFBrighteningLongFinal).
The front ending no longer conditions root retraction under
[SC046 OEARestoration](#rule-OEARestoration). Subsequent shortening and
merger yield the selected short-vowel nominative. Attested *mare*
'nightmare' instead has independently identified levelling from obliques
such as *maran* 'nightmare' [@Hall2007, pp. 301--302, §2].
The analogous nominative calculation for *flasce* 'flask' produces
\emph{*flæsċe}, not the attested comparator: Campbell and Luick explicitly
identify levelling from inflected forms there
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161].

Moving the operation before z-loss still gives
[rasta]{.pred example-input="*rástōz" example-stage=PGmc example-expected=ræste}
instead of *ræste* 'rest'. This trial also crosses nasal-ending exposure;
its changed nominatives are not additional witnesses specifically for
z-loss. Moving it after final support changes twenty-one finals, whereas
moving it after ordinary stressed fronting but before final support
preserves every final. The component dependencies are final-environment
exposure and final-vowel support, not a local feeding requirement before
ordinary stressed fronting. The independently argued West Germanic
development precedes the English history in the adopted account; its late
executable placement does not date it.
