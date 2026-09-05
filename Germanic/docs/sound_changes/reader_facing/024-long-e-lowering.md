# Long \emph{ē}-lowering

## Historical discussion

The rule treated here compresses two historically distinct developments of Proto-Germanic \emph{*ē₁}. The first is genuinely Northwest Germanic: \emph{*ē₁} was lowered to \emph{*ā} throughout Norse and West Germanic, while Gothic kept \emph{ē}. Ringe and Taylor assemble the comparative set — for 'year', PGmc \emph{*jǣra-} > \emph{*jāra-} > Old Norse *ár*, and for 'sword' the Early Runic accusative \emph{mākija} beside Gothic \emph{mēkeis} — and note that the lowered vowel is attested epigraphically from the second half of the second century AD [@RingeTaylor2014, pp. 11--13]. The second development is much later and areally restricted: in Anglo-Frisian, non-nasalized long \emph{*ā} was fronted, giving West Saxon \emph{ǣ} against Anglian, Kentish, and Old Frisian \emph{ē}, as in *dǣd* 'deed', *slǣpan* 'to sleep', *lǣtan* 'to let', *rǣdan* 'to read', and *mǣl* 'meal' [@RingeTaylor2014, pp. 146--152; @Campbell1959, pp. 50--51, §128]. Old Saxon and Old High German keep \emph{ā} (Old Saxon *dād*, Old High German *tāt*, *slāfan*, *lāzan*), so the fronted outcome is Anglo-Frisian, not common Northwest Germanic.

Whether the Anglo-Frisian front vowel really passed through the \emph{*ā} stage, or instead directly continues \emph{*ē₁}, is an old dispute: Campbell finds the detour "tempting to assume, though not definitely demonstrable" [@Campbell1959, p. 51, §129, and p. 50, §128 n. 1], while Ringe and Taylor accept the two-step majority view on the strength of the lengthened place-adverbs *þǣr* 'there' and *hwǣr* 'where' [@RingeTaylor2014, pp. 13--14]. The single-step formulation below is compatible with both analyses.

Before nasals the same low vowel was instead nasalized and rounded, yielding *mōna* 'moon', *mōnaþ* 'month', and *spōn* 'spoon' [@RingeTaylor2014, pp. 142--144; @Campbell1959, p. 50, §127]. That nasal branch is the complementary conditioned outcome of the same development and is handled by the following rule in the cascade; the non-nasal restriction here is what keeps the two branches apart.

## SC024. Lowering of long \emph{ē} before non-nasal consonants (`PNWGmcLongELowering`) {#rule-PNWGmcLongELowering}

```foma
define PNWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

The rule takes \emph{*ē} directly to \emph{*ǣ} without an intermediate \emph{*ā}. This telescoping is deliberate: a literal two-step implementation would merge the lowered vowel with the \emph{ā} produced later by [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization), and that vowel was never fronted — *stān* 'stone' and *hām* 'home' keep \emph{ā}. Campbell draws exactly this chronological inference, that the fronting of inherited \emph{ā} preceded the completion of the \emph{ai}-monophthongization [@Campbell1959, pp. 52--53, §132], and Ringe and Taylor endorse it [@RingeTaylor2014, pp. 169--170]; the formulation above builds the required non-interaction into the vowel symbols themselves.

After [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), long \emph{ē} > \emph{ǣ} can no longer produce the expected West Saxon forms: PGmc [skḗpą]{.recon} 'sheep' yields [*sċīep*]{.pred} rather than OE *sċēap* 'sheep', and PGmc [jḗrą]{.recon} 'year' yields [*ġīer*]{.pred} rather than *ġēar* 'year'. The historical content of this boundary is that the West Saxon palatal diphthongization operated on the already-fronted vowel — \emph{ǣ} > \emph{ēa} after the palatals, as in *sċēap* and *ġēar* [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1] — so the fronting must already have applied. Earlier placement changes no output, and the earlier side of the window remains untested within the cascade; the second-century runic attestation dates only the Northwest Germanic lowering, not its position among the reconstructed rules.
