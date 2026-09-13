# Long \emph{ēaw} before following vowels

## Historical discussion

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* 'dew' and *hēawan* 'hew'. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) follows [SC031 OEWWSimplification](#rule-OEWWSimplification) locally and must also precede [SC043 EAFBrightening](#rule-EAFBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

A local feeding relation and a later vowel change confine \emph{aw} > \emph{ēaw}. Before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [dáwwō]{.recon} ‘dew’ yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc [xáwwaną]{.recon} ‘hew’ yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. After [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [skáwōjaną]{.recon} ‘show’ yields [*sċawian*]{.pred} rather than expected OE *sċēawian* ‘show’, PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċawaþ*]{.pred} rather than expected *sċēawaþ* 'shows', and PGmc [stráwą]{.recon} ‘straw’ yields [*stræw*]{.pred} rather than expected *strēaw* ‘straw’. The *dēaw* and *hēawan* forms require long-diphthong formation after simplification, while *sċēawian* requires it before brightening; the handbooks assign the same interval to the West Saxon development.
