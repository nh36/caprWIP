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

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no witness word yields a historical first-break result before the search reaches order `4`, the beginning of the current expanded-PWGmc test range, so no earlier positive boundary is yet available. If it is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. This shows that [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The later boundary is broad and distant. It is not a local adjacency claim. The earlier side remains boundary-only, and the source caution remains important: the broad modeled rule is historically plausible, but the most explicit source support still clusters around the unstressed and word-final side of the change.
