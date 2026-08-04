# Northwest Germanic u-lowering

## Historical discussion

The derivation of *ġeoc* 'yoke' passes through both this change and the
preceding West Saxon palatal glide ([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)).
Campbell treats the West Saxon rising-diphthong spellings before back vowels,
while the same handbook tradition describes the lowering of \emph{u} before a
following non-high vowel separately [@Campbell1959, p. 17, §44;
@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].
The first change creates the West Saxon \emph{ġeoc} type; u-lowering then
carries the same material into the subsequent vowel history.

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

[SC017 PNWGmcULowering](#rule-PNWGmcULowering) thus rests on a broader source base than the preceding West Saxon rule.

## SC017. Lowering of \emph{*u} before following non-high vowels (`PNWGmcULowering`) {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* 'yoke', *nosu* 'nose', *sċofl* 'shovel', and *sorg* 'sorrow'.

Before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc [júką]{.recon} 'yoke' yields [*ġoc*]{.pred} rather than expected OE *ġeoc* 'yoke'. After [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc [núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu* 'nose', PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected *sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather than expected *sorg* 'sorrow'. The two witness sets place [SC017 PNWGmcULowering](#rule-PNWGmcULowering) after glide formation and before final long-\emph{o} raising.
