# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development and illustrate it above all with the families behind *fēower* ‘four’ and *wæter* ‘water’ [@RingeTaylor2014, pp. 58--59].

That makes the rule historically real, but narrow. This is not a broad long-vowel chapter. The relevant environment is final or pre-final \emph{*ō} before word-final \emph{*r}, and the clearest evidence remains concentrated in the `four` and `water` material.

## SC007. Lowering of final bimoric \emph{*ō} before \emph{*r} (`PWGmcFinalOrLowering`) {#rule-PWGmcFinalOrLowering}

The implementation keeps the final-\emph{*ō} lowering step explicit.

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

In prose, the rule lowers final bimoric \emph{*ō} before word-final \emph{*r}. This is the adjustment that lies behind the West Germanic vocalism of *fēower* ‘four’ and *wæter* ‘water’.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, it crosses [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), plain-text SC005 NWGmcAToUBeforeM, and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely and reaches order `4` with no real break, so no earlier positive boundary is yet available. If it is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*wátōr} yields *water* rather than expected OE *wæter* ‘water’. This shows that [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) in the modeled sequence.

The later boundary is broad and distant. It is not a local adjacency claim. The earlier side remains boundary-only, and the narrow witness set should stay visible whenever this rule is discussed.
