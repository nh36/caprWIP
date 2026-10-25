# Preservation of i before ng

## SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng} (`OEMedUnstressedILowering`) {#rule-OEMedUnstressedILowering}

The following rule reverses the lowering before \emph{*ng}.

```foma
define OEMedUnstressedILowering Ctx([
    {*e} -> {*i} || _ {*n} {*g}
]);
```

The rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Moving the rule before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) makes PGmc [skíllingaz]{.recon} ‘shilling’ yield [*sċilleng*]{.pred} rather than expected OE *sċilling* 'shilling'. On this evidence, I take [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) to follow [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1). Moving it later within the tested range creates no equally sharp failure.
