# Anglo-Frisian brightening

## Historical discussion

This chapter carries more historical weight than the narrow note before it. The change usually called Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments, and later Old English developments repeatedly presuppose that fronted stage even when they partly conceal it. Campbell gives the classical statement of the fronting itself, Hogg supplies the standard modern label pair, and Ringe and Taylor make the local chronology with breaking and restoration unusually clear [@Campbell1959, p. 52, §131; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

That is why the chapter is more than a general handbook excursus. The finite-state evidence shows that the rule fronts a vowel and also creates the input that [SC044 OEBreaking](#rule-OEBreaking) must read and that [SC046 OEARestoration](#rule-OEARestoration) later partly reverses before back vowels.

## SC043. Fronting of low \emph{*a} outside nasal environments (`AngloFrisianBrightening`) {#rule-AngloFrisianBrightening}

The implementation keeps the brightening as one composed rule.

```foma
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

In prose, the rule fronts low \emph{*a} to \emph{*æ}-type outcomes outside nasal environments. The composed definition reflects the fact that the transducer handles stressed, unstressed, and long-final branches separately even though the historical rule is normally discussed more compactly.

Its chronology is explicit on both sides. If the rule is moved before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste* ‘rest’. If it is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. This shows that [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), and that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC044 OEBreaking](#rule-OEBreaking).

That position is historically apt. The rule is early enough to feed later breaking, but not so early that the surviving-bimoric \emph{*ō} pathway on its left can be ignored. It is one of the main vocalic pivots of this part of the sequence.
