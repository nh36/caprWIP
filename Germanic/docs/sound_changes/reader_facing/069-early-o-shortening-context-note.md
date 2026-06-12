# Early o-shortening

## Historical discussion

By the time the sequence reaches this point, the language has already undergone the larger palatal and umlautal reorganizations to the left. What now comes into view is a later weak-tail region in which unstressed vowels are shortened, fronted, merged, and in some forms lost altogether. Campbell's discussion of early shortening of unaccented long vowels helps place this material in the larger history, while Hogg, Ringe and Taylor, and Fulk all describe the same late region through the intertwined history of apocope, syncope, shortening, and later reductions [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening belongs at the opening of that region, but it is not its strongest hinge. The evidence is broader and more distant than it is for the rules that follow, especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening). The rule therefore works best as an opening note that makes the chronology legible without pretending that the whole late weak tail begins and ends here.

## SC069. Early shortening of unstressed \emph{*ō} before nasals (`OEEarlyOShortening`) {#rule-OEEarlyOShortening}

The implementation isolates the early shortening step as one rule.

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

In prose, the rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Its chronology is real, but it is broad and one-sided. If the rule is moved before [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss), PGmc \emph{*nḗdrōn} yields *nǣdran* rather than expected OE *nǣdre* ‘adder’, PGmc \emph{*érθōn} yields *eorþan* rather than expected *eorþe* ‘earth’, and PGmc \emph{*fláskōn} yields *flascan* rather than expected *flasce* ‘flask’. The same earlier shift also disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of failures shows that [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must come before [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening).

No equally sharp later breakpoint appears within the tested range. The current search reaches its later boundary without a real break, so the rule should not be given a spurious later limit. Early o-shortening is therefore best read as an opening adjustment in the late weak tail, not as the central chronology seam of the region.
