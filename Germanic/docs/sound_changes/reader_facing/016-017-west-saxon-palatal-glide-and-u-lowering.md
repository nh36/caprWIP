# West Saxon palatal glide and u-lowering

## Historical discussion of West Saxon palatal glide and u-lowering

The derivation of *ġeoc* ‘yoke’ passes through both rules. Campbell treats the West Saxon rising-diphthong spellings before back vowels, while the same handbook tradition describes the lowering of \emph{u} before a following non-high vowel separately [@Campbell1959, p. 17, §44; @Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

The first change creates the West Saxon \emph{ġeoc} type; the second carries the same material into the subsequent vowel history.

## Historical discussion of West Saxon palatal glide

West Saxon spellings such as *ġeoc* ‘yoke’, *ġeong* ‘young’, and *ġeoguþ*
‘youth’ reflect an early development before back vowels. Campbell gives the
most direct handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

The sources establish [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), although the checked forms provide only a later boundary.

## SC016. West Saxon palatal glide before back vowels (`OEWsPalatalGlide`) {#rule-OEWsPalatalGlide}

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

OE *ġeoc* ‘yoke’ fixes the close relation between glide insertion before back-vocalic \emph{u} and the following change.

If glide insertion follows [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*júką} yields [*ġoc*]{.pred} rather than expected OE *ġeoc* ‘yoke’; earlier placement changes no checked output. The witness therefore dates [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) before u-lowering without supplying an earlier boundary. The *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ* 'youth' material establishes the lexical scope of the West Saxon development.

## Historical discussion of u-lowering

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

[SC017 NWGmcULowering](#rule-NWGmcULowering) thus rests on a broader source base than the preceding West Saxon rule.

## SC017. Lowering of \emph{*u} before following non-high vowels (`NWGmcULowering`) {#rule-NWGmcULowering}

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

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* ‘yoke’, *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc \emph{*júką} yields [*ġoc*]{.pred} rather than expected OE *ġeoc* ‘yoke’. After [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*núsō} yields [*nusu*]{.pred} rather than expected *nosu* ‘nose’, PGmc \emph{*skúflō} yields [*sċufl*]{.pred} rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields [*surg*]{.pred} rather than expected *sorg* ‘sorrow’. The two witness sets place [SC017 NWGmcULowering](#rule-NWGmcULowering) after glide formation and before final long-\emph{o} raising.
