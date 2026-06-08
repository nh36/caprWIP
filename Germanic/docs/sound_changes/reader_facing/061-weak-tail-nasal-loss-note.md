# Weak-tail nasal loss

## Historical discussion

This is the narrowest chapter in the extension. The development is historically
legible through the pathway that leads to *dōn* ‘do’, and the broader late
weak-tail setting is supported by the usual handbook discussions of apocope and
related reduction [@Campbell1959, §§345--349; @Hogg1992, pp. 120--121;
@Fulk2018, §5.6]. But the decisive lexical tie lies much farther back in the
sequence, in the older development of \emph{*dōną}. That keeps the note real,
while also keeping it small.

Within the present section the chapter follows back mutation and West Saxon
palatal umlaut only because the sequence continues onward through this local run
of later changes. It should not be made heavier than that local role requires.

## Reduction of final nasal weak-tail endings (`OEWeakTailNasalLoss`) {#rule-OEWeakTailNasalLoss}

The implementation keeps the change as one short rule.

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

In prose, the rule reduces final weak-tail endings of the type *-ną and *-mą to
plain final *-n and *-m.

The clearest lexical witness is the pathway to *dōn* ‘do’. If the rule is moved
too early, before the older reduction that already shapes the *dōną sequence,
the derivation no longer reaches *dōn* ‘do’ at all. No equally sharp later
breakpoint appears within the tested sequence. That is why the note remains
one-sided and why its earlier relation should be understood as a distant
cross-reference only and should not reshape this local section.

The chapter is therefore meant to close the extension quietly. It keeps one real
late weak-tail adjustment visible in order, but it does not try to turn that
small adjustment into a larger chapter of its own.
