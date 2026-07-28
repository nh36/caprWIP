# Anglo-Frisian brightening

## Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

## SC043. Fronting of low \emph{*a} outside nasal environments (`AngloFrisianBrightening`) {#rule-AngloFrisianBrightening}

```foma
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

Two derivations place low \emph{*a} > \emph{*æ} between unrounding and breaking. Before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste* ‘rest’. After [SC044 OEBreaking](#rule-OEBreaking), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. The first witness requires brightening to receive the outcome of the surviving-bimoric \emph{*ō} development; the second requires breaking to receive the fronted vowel.
