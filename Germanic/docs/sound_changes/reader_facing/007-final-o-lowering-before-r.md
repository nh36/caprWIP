# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development [@RingeTaylor2014, pp. 58--59]. The primary comparative evidence comes from kinship-term \emph{*r}-stems: PGmc \emph{*fadér} 'father' (OHG \emph{fater}, OE \emph{fæder}) and comparable \emph{*r}-stem nouns show a short vowel in the final syllable before \emph{*r}, demonstrating the lowering across noun paradigms. PGmc \emph{*fedwōr} 'four' (OE \emph{fēower}, OFris \emph{fiuwer}) and \emph{*watōr} 'water' (OE \emph{wæter}) each provide an independent etymon with final \emph{*ō} before \emph{*r}.

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## SC007. Lowering of final bimoric \emph{*ō} before \emph{*r} (`PWGmcFinalOrLowering`) {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc [wátōr]{.recon} ‘water’ yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no checked output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. The \emph{*r}-stem kinship nouns (PGmc \emph{*fadér} 'father', OE \emph{fæder}; and related \emph{*r}-stems) support the change's occurrence; the numeral \emph{*fedwōr} 'four' (OE \emph{fēower}) and the \emph{*watōr} 'water' etymon (OE \emph{wæter}) each independently demonstrate the same lowering environment, with \emph{wæter} additionally supplying the ordering constraint before brightening. No broader lowering of \emph{*ō} is attested.
