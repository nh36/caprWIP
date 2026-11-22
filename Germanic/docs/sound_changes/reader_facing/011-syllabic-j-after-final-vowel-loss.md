# Syllabic j after final-vowel loss

## Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

The sources establish the development, although the lexical evidence supplies
little independent support for its position. Its scope is postconsonantal j,
not high-vowel vocalization generally.

## SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

```foma
define PWGmcSyllabicJ Ctx([
    [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
]
]);
```

In the compatibility cascade, placing [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) before [SC010 PWGmcJGemination](#rule-PWGmcJGemination) yields [*nete*]{.pred} from PGmc [nátją]{.recon} ‘net’; moving it later changes no output. This contrast fixes the order for a regular direct derivation of OE *nett* 'net', but does not fix the historical order if the direct singular acquired its geminate from a protected cell.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* 'army' and *rice* 'kingdom' as outcomes. The lexicon adds only that vocalization followed gemination, not where it falls among subsequent changes.
