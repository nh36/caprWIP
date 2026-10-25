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

OE *nett* 'net' fixes the order because the syllabic-\emph{j} development would remove the glide that conditions gemination. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) precedes [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc [nátją]{.recon} ‘net’ yields [*nete*]{.pred} rather than expected OE *nett* 'net'. Earlier movement of gemination changes no output.

The chronology is phonologically transparent: the consonant must geminate before \emph{*j} ceases to be consonantal. The witness establishes no earlier boundary.
