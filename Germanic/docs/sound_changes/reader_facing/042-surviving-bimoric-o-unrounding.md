# Surviving bimoric \emph{*ō} unrounding

## Historical discussion

This is a narrow prefatory rule. The handbooks do not isolate one large independent sound change under exactly this label. Still, the surviving bimoric \emph{*ō} pathway behind forms such as *ræste* ‘rest’ needs to be stated explicitly if the sequence is to begin cleanly before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). Campbell, Hogg, and Ringe and Taylor all make the surrounding fronting and restoration region historically intelligible even when this particular feeder step remains model-shaped [@Campbell1959, pp. 52, 60, §§131, 157--158; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190].

That is enough for a short reader-facing note. The rule belongs here because it closes a small architectural seam on the left side of the brightening chapter, not because it should rival the broader historical weight of the chapters that follow.

## SC042. Unrounding of the surviving bimoric \emph{*ō} (`PWGmcSurvivingBimoricOUnrounding`) {#rule-PWGmcSurvivingBimoricOUnrounding}

The implementation keeps the step very small and explicit.

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

In prose, the rule unrounds a surviving bimoric \emph{*ō} to \emph{*ā} in the environment that later feeds the fronted and restored outcome in forms such as *ræste* ‘rest’.

Its chronology is exact on both sides, but the witness base is very narrow. If the rule is moved before SC020 PGmcFinalZDeletion, PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste* ‘rest’. If the rule is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), the same PGmc form again yields *rasta* instead of *ræste*. This shows that SC020 PGmcFinalZDeletion must come before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), and that [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

The rule is therefore real, but still best treated as a short feeder note. Its entire chronology is carried by the single *rest* derivation.
