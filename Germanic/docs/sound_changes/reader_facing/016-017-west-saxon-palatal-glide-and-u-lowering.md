# West Saxon palatal glide and u-lowering

## Historical discussion of West Saxon palatal glide and u-lowering

These two rules belong together because the same *ġeoc* ‘yoke’ derivation passes through both of them. Campbell treats the West Saxon rising-diphthong spellings before back vowels, and the standard lowering of \emph{u} before a following non-high vowel is described separately in the same handbook tradition [@Campbell1959, p. 17, §44; @Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

That relation is enough to justify one paired chapter, but the two changes still need their own historical discussions and rule sections. The first creates the West Saxon \emph{ġeoc} type; the second carries the same material into the broader vowel history that follows.

## Historical discussion of West Saxon palatal glide

West Saxon spellings such as *ġeoc* ‘yoke’, *ġeong* ‘young’, and *ġeoguþ* ‘youth’ reflect a real early development before back vowels. Campbell's short account is still the clearest handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

This makes [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) historically clear even though its current order evidence is one-sided.

## SC016. West Saxon palatal glide before back vowels (`OEWsPalatalGlide`) {#rule-OEWsPalatalGlide}

The implementation states the West Saxon glide insertion directly.

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

In prose, the rule inserts a front glide after an initial palatal before back-vocalic \emph{u}. This is the step that helps produce West Saxon forms such as *ġeoc* ‘yoke’.

Its chronology is real but one-sided. If the rule is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’. This shows that [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering). If the rule is moved earlier within the currently tested range, no witness word yields a historical first-break result before the search reaches bundled earlier material, so no earlier positive boundary is yet available.

## Historical discussion of u-lowering

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

This gives [SC017 NWGmcULowering](#rule-NWGmcULowering) a broader source base than the more narrowly West Saxon rule beside it.

## SC017. Lowering of \emph{*u} before following non-high vowels (`NWGmcULowering`) {#rule-NWGmcULowering}

The implementation keeps the lowering step explicit.

```foma
define NWGmcULowering [
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

In prose, the rule lowers \emph{u} to \emph{o} before a following non-high vowel. This is the change behind forms such as *ġeoc* ‘yoke’, *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Its chronology is explicit on both sides. If the rule is moved before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’. If it is delayed until after [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*núsō} yields *nusu* rather than expected *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. This shows that [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering), and that [SC017 NWGmcULowering](#rule-NWGmcULowering) must come before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising).
