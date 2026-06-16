# Syllabic j after final-vowel loss

## Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

That source support is good, but the compact trace layer contributes very little live evidence of its own. This therefore stays a modest singleton note. It does not expand into a broad chapter on high-vowel vocalization.

## SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

The implementation keeps the syllabic-j step explicit.

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

In prose, the rule turns postconsonantal \emph{*j} into syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} has been lost. It keeps explicit a small but historically real step behind forms such as *here* and *rice*.

Its chronology is mixed. The earlier search breaks immediately at [SC010 PWGmcJGemination](#rule-PWGmcJGemination). If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) is moved before [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. The later search reaches order `86`, the current [SC087 OERMetathesis](#rule-OERMetathesis) boundary, with no real break. This later-side result is boundary-only. It does not provide a positive chronology constraint. This gives a tight local seam with [SC010 PWGmcJGemination](#rule-PWGmcJGemination) on the earlier side, while leaving no later-side positive boundary. In practice, [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) must come after [SC010 PWGmcJGemination](#rule-PWGmcJGemination).

The source support is real, but the live trace remains thin. That is why the chapter stays narrow and does not turn into a broader discussion of high-vowel behavior.
