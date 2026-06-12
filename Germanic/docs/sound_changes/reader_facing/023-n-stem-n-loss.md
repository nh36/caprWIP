# N-stem \emph{n}-loss

## Historical discussion

The broader history is the reduction and leveling of older n-stem endings in West Germanic. Ringe and Taylor describe the resulting syncretism in the n-stems, which is the wider morphological setting for the narrower step isolated here [@RingeTaylor2014, p. 72].

Within the current sequence, the clearest witness is the path to *dōn* ‘do’. That makes the change historically legible, but still modest in scope.

## SC023. Loss of n-stem \emph{*n} in final position (`NWGmcNStemNLoss`) {#rule-NWGmcNStemNLoss}

The implementation states the n-loss directly.

```foma
define NWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

In prose, the rule removes the final \emph{n} of the relevant n-stem ending and leaves the nasalized long vowel that later developments can reshape. In the current sequence, this is the step that keeps the derivation of *dōn* on track.

Its chronology is real but one-sided. If the rule is delayed until after [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*dōną} no longer yields expected OE *dōn* ‘do’, and the row records no output at all (\emph{+?}). This shows that [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must come before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope). If the rule is moved earlier within the currently tested range, no witness word yields a historical first-break result before the search reaches bundled earlier material, so no earlier positive boundary is yet available.

The later boundary is therefore historically real but broad and distant. The bad outcome must be read as a failed derivation, not as a competing Old English surface form.
