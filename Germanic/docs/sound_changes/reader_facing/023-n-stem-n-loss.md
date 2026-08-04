# N-stem \emph{n}-loss

## Historical discussion

The broader history is the reduction and leveling of older n-stem endings in West Germanic. Ringe and Taylor describe the resulting syncretism in the n-stems, which is the wider morphological setting for the narrower step isolated here [@RingeTaylor2014, p. 72].

The path to *dōn* ‘do’ provides the clearest witness, but the change remains narrow in scope.

## SC023. Loss of n-stem \emph{*n} in final position (`PNWGmcNStemNLoss`) {#rule-PNWGmcNStemNLoss}

```foma
define PNWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

After [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc [dōną]{.recon} ‘do’ fails entirely (\emph{+?}) instead of yielding expected OE *dōn* ‘do’; earlier placement changes no output. Thus [SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss) must feed the later apocope.

This failed derivation supplies a terminus ante quem, while the lower boundary remains unattested.
