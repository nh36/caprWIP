# Final lowering of shortened unstressed o

## SC100. Final lowering of shortened unstressed \emph{*o} (`OEFinalUnstressedOLowering`) {#rule-OEFinalUnstressedOLowering}

```foma
define OEFinalUnstressedOLowering Ctx([
    {*o} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* .#.
]);
```

In a final syllable the same shortened vowel gives \emph{a}. Thus the existing
month control continues PGmc [mḗnōθz]{.recon} ‘month’ through shortened
\emph{*o} to OE [mōnaþ]{.iv lang=oe sort=monath role=evidence_form} ‘month’, while [wúndōdē]{.recon} ‘wounded’ takes
[SC099 OEMedUnstressedORaising](#rule-OEMedUnstressedORaising)
instead. The medial/final contrast and its chronology after long-vowel
shortening are Stausland Johnsen's analysis [@StauslandJohnsen2015,
pp. 28--31].

In the adopted weak-noun history, newly final \emph{*-ōn} also reaches
this late route. Nominative plural \emph{*fláskōniz} and dative
singular \emph{*fláskōni} share \emph{*flaskōn > *flaskon > *flaskan},
giving attested *flascan* 'flasks' and 'flask'. The long vowel has
survived early shortening and fronting; this rule supplies only the
last lowering, not the earlier nasal survival or root restoration.
The inherited singular still gives predicted [flæsċe]{.pred},
not attested *flasce* 'flask'; its root-vowel problem is separate.
