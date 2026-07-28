# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development and illustrate it above all with the families behind *fēower* ‘four’ and *wæter* ‘water’ [@RingeTaylor2014, pp. 58--59].

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## SC007. Lowering of final bimoric \emph{*ō} before \emph{*r} (`PWGmcFinalOrLowering`) {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc \emph{*wátōr} yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no checked output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. The *fēower* ‘four’ and *wæter* ‘water’ families support the narrow environment before word-final \emph{*r}; no broader lowering of \emph{*ō} is attested.
