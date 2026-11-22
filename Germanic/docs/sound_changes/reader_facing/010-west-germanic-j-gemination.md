# West Germanic j-gemination

## Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

The change applies specifically after a short vowel before \emph{*j}, not to geminate consonants generally.

## SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

```foma
define PWGmcJGemination Ctx([
    [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j},
    # *w is an ordinary member of the same law. Campbell §407 p. 167:
    # "every consonant except r being affected after short syllables...
    # The forms in which w is doubled are dealt with in §120.2."
    # Ringe & Taylor p. 53: "it appears that that cluster too underwent
    # gemination in PWGmc." The geminate this creates is the input that
    # SC029 later resolves. Fulk §4.10 n. 1 dissents; see
    # audits/sc010-w-gemination-and-hay-depth-adjudication.md.
    {*w} -> {*w} {*w} || EnglishStarShortVowel _ {*j}
]
]);
```

OE *nett* 'net' separates two predictions for the inherited direct singular. If early nasal loss strands the glide and it vocalizes before gemination, PGmc [nátją]{.recon} ‘net’ yields [*nete*]{.pred}; if the ending protects the glide through gemination, the direct route gives *nett*. The attested geminate constrains the order only if it is inherited in that cell, rather than extended from a protected form such as the dative *nette* [@RingeTaylor2014, pp. 44--47; @HoggFulk2011, pp. 20--21, §2.23].

The chronology is phonologically transparent: the consonant must geminate before \emph{*j} ceases to be consonantal. The witness establishes no earlier boundary.

The same distinction matters with the labials. In both active models the selected genitive \emph{*xíwjas} gives *hīewes* 'of hue'; the ending protects the glide and the stem has inherited \emph{*i}, not \emph{*e}. In the direct singular of hay, B2 retains the short nasal ending through gemination and gives *hīeġ* 'hay', whereas A loses the ending, vocalizes the glide and does not geminate. This contrast depends on the order of nasal apocope, not on a change to the consonants eligible for gemination [@Campbell1959, p. 46, §120.2; @RingeTaylor2014, pp. 53, 246, 250].
