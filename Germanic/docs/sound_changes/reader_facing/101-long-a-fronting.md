# North Sea Germanic fronting of long \emph{ā}

## Historical discussion

Long after the Northwest Germanic lowering of \emph{*ē₁} to \emph{*ā}, the dialects of the North Sea coast fronted the surviving oral \emph{*ā} to a low front vowel: West Saxon \emph{ǣ} in *dǣd* 'deed', *slǣpan* 'to sleep', *lǣtan* 'to let', *rǣdan* 'to read', and *mǣl* 'meal', against Anglian, Kentish, and Old Frisian \emph{ē} (*dēd*, *slēpa*, *jēr*) [@RingeTaylor2014, pp. 146--150; @Campbell1959, pp. 50--51, §128]. Old Saxon and Old High German keep the back vowel (Old Saxon *dād*, Old High German *tāt*, *slāfan*, *lāzan*), but sporadic Old Saxon spellings in ⟨e⟩ show that the fronting lapped unevenly into Old Saxon territory [@RingeTaylor2014, p. 150]. The change is therefore a North Sea Germanic development rather than an exclusively Anglo-Frisian one, though only Old English and Old Frisian carry it through systematically.

The fronting affected stressed, non-nasalized \emph{*ā}; nasalized \emph{*ą̄} was instead rounded, as treated in the rounding chapter. Ringe and Taylor further note a blocking environment before \emph{*w} not followed by a high front vocalic [@RingeTaylor2014, p. 149]; no form in the present corpus reaches that environment, so the restriction is recorded here without being encoded in the rule.

Whether this fronting restored a front vowel that had earlier been backed, or whether — as Fulk argues — the North Sea dialects simply retained an old front \emph{*ǣ} that was never backed at all, is the same dispute recorded in the lowering chapter [@Fulk2018, pp. 60--61, §4.6; @Campbell1959, pp. 50--51, §§128--129]. On the retention analysis this chapter's change dissolves into the non-event of staying put; the present model follows Ringe and Taylor's two-step reconstruction, on the strength of the runic evidence for an early [aː] and the place-adverbs *þǣr* 'there' and *hwǣr* 'where' [@RingeTaylor2014, pp. 13--14].

## SC101. Fronting of long \emph{ā} before non-nasal consonants (`EAFLongAFronting`) {#rule-EAFLongAFronting}

```foma
define EAFLongAFronting [
    {*ā} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

The rule consumes the \emph{*ā} created by [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering); displaced before the lowering, it has nothing to front, and [skḗpą]{.recon} 'sheep' surfaces as [*sċāp*]{.pred} rather than OE *sċēap*, [jḗrą]{.recon} 'year' as [*ġār*]{.pred} rather than *ġēar*, [slḗpaną]{.recon} 'to sleep' as [*slāpan*]{.pred} rather than *slǣpan*.

Two later boundaries carry real historical content. First, the fronting must precede the completion of [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization): the \emph{ā} that arose from \emph{*ai} was never fronted — *stān* 'stone', *hām* 'home', *lāþ* 'hostile', *rāp* 'rope', *tācn* 'token', *gāst* 'spirit' all keep the back vowel. Campbell draws exactly this chronological inference [@Campbell1959, pp. 52--53, §132], and Ringe and Taylor endorse it as cogent [@RingeTaylor2014, pp. 169--170]; in the present cascade the inference is enforced by rule order, and displacing the fronting after the monophthongization wrongly yields [*lǣþ*]{.pred}, [*rǣp*]{.pred}, [*tǣcn*]{.pred}, [*sǣwol*]{.pred}, and [*ġēast*]{.pred}. Historically the two changes may well have overlapped in time; the discrete ordering is the grammar's way of stating that inherited \emph{ā} had been fronted before the new \emph{ā} arose.

Second, the fronting must precede [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), which operated on the already-fronted vowel: \emph{ǣ} > \emph{ēa} after the palatals, as in *sċēap* 'sheep' and *ġēar* 'year' [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1]. Displaced after the diphthongization, the cascade yields [*sċǣp*]{.pred} and [*ġǣr*]{.pred} instead.
