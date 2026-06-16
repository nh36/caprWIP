# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc \emph{*friund} > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

That narrowness is part of the history, not an objection to writing the section. This is a short lexical sound-change note on a rare sequence in the `friend` family, not a broadly productive rule for many unrelated forms.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

The implementation keeps the contraction step explicit.

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

In prose, the rule contracts the rare \emph{*ijō} sequence in the family behind OE *frēond* 'friend'. The section belongs here because a continuous account of the early sequence should explain that development openly, even though the source base remains effectively one family.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, it crosses [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation), [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering), [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM), and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely and reaches order `4` with no real break, so no earlier positive boundary is yet available. If it is delayed until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*fríjōndz} yields *friund* rather than expected OE *frēond*. This shows that [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) in the modeled sequence.

The later boundary is broad and distant. It does not turn this into a productive sound law. The earlier side remains boundary-only, and the rule is best read as a short lexical note on the `friend` family.
