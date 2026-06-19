# Proto-West-Germanic ai-monophthongization

## Historical discussion

Ringe and Taylor treat the reduction of unstressed \emph{*ai} as one of the major early vowel shifts shared across the Northwest Germanic area [@RingeTaylor2014, pp. 40--41].

That historical support is strongest for the unstressed and especially word-final side of the change. CAPR makes a wider inherited \emph{*ai} treatment explicit in one rule, but the broader nonfinal \emph{*ai > *ā} side is more sharply packaged in the implementation than in the current handbook discussion.

## SC004. Proto-West-Germanic ai-monophthongization (`PWGmcAiMonophthongization`) {#rule-PWGmcAiMonophthongization}

The implementation keeps the monophthongization step explicit.

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

In prose, the rule monophthongizes inherited \emph{*ai}. The clearest source support is for the word-final unstressed outcome, where \emph{*ai} merges with long mid \emph{*ē}; CAPR then keeps the broader inherited \emph{*ai} treatment visible in the same modeled step.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. This shows that [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the broader inherited \emph{*ai} treatment here because the clearest source support places unstressed \emph{*ai} reduction among the early Northwest Germanic vowel shifts.
