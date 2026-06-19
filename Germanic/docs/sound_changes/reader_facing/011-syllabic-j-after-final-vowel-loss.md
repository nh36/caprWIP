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

Its chronology is mixed. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) is moved before [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. This shows that [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) must come after [SC010 PWGmcJGemination](#rule-PWGmcJGemination). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one. The checked forms therefore fix the earlier relation between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), but do not identify a corresponding later constraint. CAPR keeps the rule here because the sources treat syllabic \emph{*j} as the follower to final-vowel loss once the earlier consonant adjustments are already in place.

The source support is real, but the live trace remains thin. That is why the chapter stays narrow and does not turn into a broader discussion of high-vowel behavior.
