# Early i-apocope

## Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* and *geogup* examples belong to the same pattern [@Campbell1959, §332].

This is therefore a specific kind of final-vowel loss. The crucial point is that the ending vowel disappears in a weak suffixal environment early enough to block later umlaut. That anti-umlaut timing is the historical center of the rule.

## SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

The implementation keeps the early apocope step explicit.

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

In prose, the rule deletes final \emph{*i} in remote unstressed syllables. That timing matters because later umlaut no longer sees the lost ending vowel, which is why forms like *geoguþ* ‘youth’ preserve the expected vocalism.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*skáwōθi} yields *sċēaweþ* rather than expected OE *sċēawaþ*. This shows that [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat this suffixal loss as an early step in the ending history before the later diphthongal developments.
