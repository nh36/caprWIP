# North Sea Germanic rounding of nasalized long \emph{ā}

## Historical discussion

In the coastal West Germanic dialects, the long low vowel \emph{*ā} — centrally the vowel produced from \emph{*ē₁} by the Northwest Germanic lowering — was nasalized before nasal consonants and rounded, yielding the \emph{ō}-vocalism of Old English *mōna* 'moon', *mōnaþ* 'month', and *spōn* 'spoon', against Old High German *māno*, *mānōd*, *spān* and Old Norse *máni*, *mánaðr*, *spánn*. Ringe and Taylor treat the rounding of nasalized low vowels as part of the pre-Old-English development of the North Sea coast [@RingeTaylor2014, pp. 150--152], and Campbell describes the same split of Germanic \emph{ǣ¹} before nasals [@Campbell1959, p. 50, §127].

The geographical scope is broader than Anglo-Frisian alone. Old Saxon shows the rounding variably — *ōdar* 'other' and *sōd* 'true' beside unrounded *quān* 'wife' and *sāno* 'immediately' — which demonstrates that the nasalization reached Old Saxon even where the rounded outcome did not generalize [@RingeTaylor2014, pp. 150--151]. The change is therefore best located in the North Sea Germanic dialect continuum, with uneven Old Saxon participation, rather than assigned mechanically to Anglo-Frisian.

The rounding is the nasal counterpart of the fronting of oral \emph{*ā} treated in the fronting chapter: nasalized \emph{*ą̄} rounds while oral \emph{*ā} fronts, and together the two exhaust the fate of the old low vowel in this area. The comparative material does not order the two branches against each other, and no such ordering is claimed here.

## SC025. Rounding of long \emph{ā} before nasals (`EAFLongANasalRounding`) {#rule-EAFLongANasalRounding}

```foma
define EAFLongANasalRounding [
    {*ā} -> {*ō} || _ EnglishStarNasal
];
```

The rule consumes the \emph{*ā} created by [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering): displacing the lowering after this rule leaves the rounding without an input, and [mḗnōθz]{.recon} 'month' surfaces as [*mānaþ*]{.pred} rather than OE *mōnaþ*, [spḗnuz]{.recon} 'spoon' as [*spān*]{.pred} rather than *spōn*.

Equally important is what the rule must precede. The monophthongization of \emph{*ai} in [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) creates a new long \emph{ā}, and that vowel was never rounded before nasals: *stān* 'stone' and *hām* 'home' keep \emph{ā}. If the rounding is displaced after the monophthongization, the cascade wrongly yields [*stōn*]{.pred} and [*hōm*]{.pred}. This is the same chronological inference Campbell draws for the fronting — the treatments of the old low vowel were complete, or at least under way, before \emph{ai}-monophthongization supplied a new one [@Campbell1959, pp. 52--53, §132; @RingeTaylor2014, pp. 169--170].
