# Final geminate simplification

## SC080. Simplification of final geminates (`OEFinalGeminateSimplification`) {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

The rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Moving the rule before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) makes PGmc [lúnganjō]{.recon} ‘lungs’ yield [*lungenn*]{.pred} rather than expected OE *lungen* 'lungs'. These failures require [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) to follow [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
