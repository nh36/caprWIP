# Northern monosyllabic final \emph{*z}-loss

## Historical discussion

Long after the Proto-West Germanic loss of final \emph{*z} in unstressed syllables ([SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)), the northern West Germanic dialects lost word-final \emph{*z} in stressed monosyllables as well, with compensatory lengthening of a short nucleus. Ringe and Taylor's witness set is OE *mā* 'more' < \emph{*maiz}, the pronouns *wē* 'we', *ġē* 'you', *mē* 'me', *þē* 'thee', *hē* 'he', *hwā* 'who' < \emph{*hwaz}, and — hedged in their own print with question marks — *cū* 'cow' [@RingeTaylor2014, p. 86, §3.3.1]. The southern dialects retained the sibilant and rhotacized it: Old High German \emph{mir}, \emph{wir}, \emph{mēr}, \emph{er} answer the Old English endingless forms, which is why Fulk counts this loss among the diagnostic Ingvaeonic features [@Fulk2018, p. 18, n. 6]. Ringe and Taylor explicitly treat this as a change separate from the Proto-West Germanic unstressed loss, citing Crist's demonstration that the two must be distinguished [@RingeTaylor2014, pp. 44--45, §3.1.1].

The scholarship disagrees about the exact conditioning, and the disagreement is worth recording. An older account, represented by Campbell and going back to Luick, derived the endingless pronouns from unaccented sentence variants rather than from a regular sound change [@Campbell1959, p. 166; @Luick1914, p. 819]. Ringe and Taylor reject that analysis because *mā* 'more' and *cū* 'cow' are not plausibly unaccented words [@RingeTaylor2014, p. 86, §3.3.1]. Crist formulates an Ingvaeonic rule in which \emph{*z} is lost after front vowels, with compensatory lengthening, covering preconsonantal cases as well; his data contain no word-final back-vowel monosyllables, so forms like \emph{*hwaz} and the ancestor of *cū* fall outside what his statement can decide — a documented gap rather than a refutation [@Crist2002, pp. 1, 4, §§1, 10]. Kilday narrows the preconsonantal subcase to Old Saxon and Old Frisian while accepting the word-final monosyllabic loss for Old English, contrasting regular *meord* 'reward' with the loanword-influenced *mēd* 'reward' [@Kilday2024, pp. 1--3]. CAPR adopts Ringe and Taylor's quality-neutral formulation because it alone generates the back-vowel witnesses, while noting that the front-vowel forms are compatible with both analyses.

Apparent counterexamples are analogical, not phonological: OE *dēor* 'deer', *ār* 'oar', and *gār* 'spear' show final \emph{-r} from levelling out of inflected forms where the sibilant was word-internal and regularly rhotacized, not from retention of word-final \emph{*z} [@RingeTaylor2014, p. 86, §3.3.1, n. 24]. The change precedes rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)), which Ringe and Taylor place last in this sequence of northern developments [@RingeTaylor2014, p. 87, §3.3.1].

No selected derivation in the current corpus tests this change: the corpus happens to select oblique or plural cells for the relevant lexemes — for instance 'cow' and 'meed' enter the cascade in inflected forms whose \emph{*z}, where present, is word-internal. The rule is therefore carried as a historically genuine but presently unwitnessed change, in the same way the project retains other well-attested developments that the current word list does not happen to exercise.

## SC097. Northern monosyllabic final \emph{*z}-loss (`MonosyllabicFinalZLoss`) {#rule-MonosyllabicFinalZLoss}

```foma
define MonosyllabicFinalZLoss [
    {*a} -> {*ā}, {*á} -> {*ā},
    {*e} -> {*ē}, {*é} -> {*ḗ},
    {*i} -> {*ī}, {*í} -> {*ḯ},
    {*o} -> {*ō}, {*ó} -> {*ō},
    {*u} -> {*ū}, {*ú} -> {*ū}
        || .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
            _ {*z} .#.
] .o. [
    {*z} -> 0 ||
        .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
            EnglishStarVocalic+ _ .#.
];
```

The rule first lengthens a short nucleus standing immediately before word-final \emph{*z} in a monosyllable, then deletes the \emph{*z} after any vowel in a monosyllable. A form whose nucleus is already long or diphthongal skips the lengthening step and simply loses the sibilant, matching Ringe and Taylor's derivations of \emph{*maiz} > *mā* 'more' and of *cū* 'cow' [@RingeTaylor2014, p. 86, §3.3.1]. Synthetic checks behave as the sources predict: \emph{*hwaz} yields \emph{*hwā}, \emph{*hiz} yields \emph{*hī}, and \emph{*kūz} yields \emph{*kū} without further lengthening.

Because no corpus form reaches this rule, adding it changes no Old English output, and if the rule were moved earlier or later within its stage, no corpus output would change either; the corpus supplies no derivation that could fix its position by a wrong form, so its placement instead follows the sources. It stands after [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), since the two losses are historically distinct changes with the unstressed loss earlier [@RingeTaylor2014, pp. 44--45, §3.1.1], and before rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)), so that a word-final \emph{*z} removed here can never surface as \emph{-r} in the north [@RingeTaylor2014, p. 87, §3.3.1]. Consonant-final monosyllables are untouched: their nominative \emph{*-z}, where it ever existed, was eliminated before Proto-West Germanic under [SC096 RootNounNomZLoss](#rule-RootNounNomZLoss). Word-internal \emph{*z}, as in PGmc [déuzą]{.recon} 'deer' on its way to OE *dēor* 'deer', does not meet the environment and remains unchanged, surviving to rhotacism.
