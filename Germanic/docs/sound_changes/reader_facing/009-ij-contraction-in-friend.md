# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc \emph{*friund} > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

That narrowness is part of the history. This is a short lexical sound-change note on a rare sequence in the `friend` family, and it belongs in a continuous account of the early sequence even though it is not a broadly productive rule.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

The implementation keeps the contraction step explicit.

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

In prose, the rule contracts the rare \emph{*ijō} sequence in the family behind OE *frēond* 'friend'. The section belongs here because a continuous account of the early sequence should explain that development openly, even though the source base remains effectively one family.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*fríjōndz} yields *friund* rather than expected OE *frēond*. This shows that [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat the `friend` development as a narrow early change within the same sequence. It remains a one-family note, not a productive sound law. From here the sequence passes into the tighter local seam between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ).
