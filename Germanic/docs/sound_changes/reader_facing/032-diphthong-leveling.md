# Leveling of diphthongal outputs

## Historical discussion

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* 'dew' / *hēawan* 'hew' developments.

## SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

```foma
define OEDiphthongLeveling [
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
];
```

The two edges of this interval fail differently. Before [SC030 OEAuBrightening](#rule-OEAuBrightening), PGmc [galáubijaną]{.recon} ‘believe’, [báug]{.recon} ‘bow’, and [bráudą]{.recon} ‘bread’ produce no output (\emph{+?}) instead of expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xáubudą]{.recon} ‘head’ yields [*hēafud*]{.pred} rather than expected *hēafod* ‘head’. Absence at the lower edge places diphthong leveling after fronting; the wrong surface form at the upper edge places it before medial unstressed-\emph{u} lowering.
