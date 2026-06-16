# West Germanic j-gemination

## Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

That historical support is good, but the environment must stay explicit. This is not a general chapter on doubled consonants. The relevant setting is a short vowel before \emph{*j}.

## SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

The implementation keeps the j-gemination step explicit.

```foma
define PWGmcJGemination [
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
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

In prose, the rule doubles consonants before \emph{*j} after a short vowel. It preserves one of the steps behind OE *nett* 'net' and related West Germanic outcomes in this narrow environment.

Its chronology is useful but asymmetric. The earlier search moved the rule safely across plain-text SC009 PWGmcIjContraction, [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation), [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering), [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), plain-text SC005 NWGmcAToUBeforeM, and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) to order `4` and then reached the start of the tested expanded-PWGmc chain with no real break. This side is boundary-only. It does not provide a positive chronology constraint. The later search breaks immediately at [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ). If [SC010 PWGmcJGemination](#rule-PWGmcJGemination) is delayed past [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. This gives a tight local seam between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ). In practice, [SC010 PWGmcJGemination](#rule-PWGmcJGemination) must come before [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ).
