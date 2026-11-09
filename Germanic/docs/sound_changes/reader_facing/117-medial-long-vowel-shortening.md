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
The later singular's final consonant is paradigmatically preserved or
restored, not a survival through early final-n loss; the source does not
fix the restoration's date [@Campbell1959, p. 189, §473].

The root and transmitted prominence are protected. Final long vowels
remain for the later component of shortening; this early component is
not an extra high-vowel deletion or a morphological condition.
The separately traced identifier records implementation ownership, not
a new independently dated historical sound change.

The selected oblique *fyrhte* 'fright' supplies a final-quantity control.
Its inherited \emph{*fúrxtīnaz} exposes final \emph{*ī} after early
ending and final-\emph{*n} loss; that vowel remains long here
[@RingeTaylor2014, pp. 87--88, 380--381]. Premature shortening makes it
a target of [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), wrongly
giving [*fyrht*]{.pred}. The later component, not this medial realization,
licenses the regular final vowel of *fyrhte*.

The inherited neuter plural \emph{*nautīnō} provides the complementary
positive dependency: West Saxon *nīetenu* 'animals, livestock' requires
medial shortening before quantitative deletion
[@Fulk2018, p. 92, §5.6; @Sweet1871, p. 109, lines 8--11;
@Goering2016, pp. 186--188]. Shortening produces HLL
\emph{*nīetinu}, retaining both high vowels; omission wrongly gives
[*nīeten*]{.pred}. The selected *lȳtelu* 'little' already has a short
medial vowel and is unchanged by the same omission. This full inherited
plural protects the dependency without relying on a singular with
restored final *n* or inventing another sound law.
