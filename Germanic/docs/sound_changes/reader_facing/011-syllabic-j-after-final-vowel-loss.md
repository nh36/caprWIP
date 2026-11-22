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

The compatibility cascade uses this fused ending-loss and vocalization fragment after [SC010 PWGmcJGemination](#rule-PWGmcJGemination). Moving it before gemination yields [*nete*]{.pred} from PGmc [nátją]{.recon} ‘net’; a later displacement changes no endpoint in the compatibility test. Both active orders still compose the fragment, but it does not change any selected form or registered paradigm probe. Those derivations instead use separate apocope and vocalization stages: A gives direct [*nete*]{.pred}, B2 direct *nett*. The compatibility displacement is not independent evidence for dating either separate change.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* 'army' and *rice* 'kingdom' as outcomes. Both historical models allow oral loss to strand a glide before gemination; only A does so with the short nasal ending. A protected vowel, as in the shared dative of 'net', instead keeps the glide consonantal through gemination in both models.
