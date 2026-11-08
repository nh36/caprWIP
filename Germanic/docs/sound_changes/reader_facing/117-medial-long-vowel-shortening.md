# Early medial realization of unstressed shortening

## SC117. Medial component of SC072 unstressed shortening (`OEMedLongShort`) {#rule-OEMedLongShort}

```foma
define OEMedLongShort FootCtx([
    {*ī} -> {*i} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ū} -> {*u} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ȳ} -> {*y} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ā} -> {*a} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ē} -> {*e} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ǣ} -> {*æ} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}],
    {*ō} -> {*o} || EnglishStarVocalic OEAnyConsonant+ _ OEAnyConsonant+ [EnglishStarVocalic|{*ô}]
]);
```

This separately visible component belongs to
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).
It realizes the medial quantity required before
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope),
without prematurely shortening final long vowels.
Goering distinguishes later \emph{*nētīn}, yielding *nēten* 'livestock',
from the medially shortened inflected forms that yield *nētenu*
'livestock' and *nētna* 'of livestock'
[@Goering2016, pp. 186--188; @Goering2023, pp. 67--68].
The same quantity distinction is required in the earlier comparison of
unstressed vowels [@Fulk2018, pp. 90--96, §§5.6--5.7].

The root and transmitted prominence are protected. Final long vowels
remain for the later component of shortening; this early component is
not an extra high-vowel deletion or a morphological condition.
The separately traced identifier records implementation ownership, not
a new independently dated historical sound change.
