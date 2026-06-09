# Weak-tail nasal loss

## Historical discussion

The development belongs to the narrower end of the later weak-tail sequence. It is historically
legible through the pathway that leads to *dōn* ‘do’, and the broader late
weak-tail setting is supported by the usual handbook discussions of apocope and
related reduction [@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, pp. 120--121;
@Fulk2018, p. 91, §5.6]. But the decisive lexical tie lies much farther back in the
sequence, in the older development of \emph{*dōną}. That keeps the note real,
while also keeping it small.

Within this later run of changes it follows back mutation and West Saxon
palatal umlaut, but the evidence remains slighter than theirs.

## SC061. Reduction of final nasal weak-tail endings (`OEWeakTailNasalLoss`) {#rule-OEWeakTailNasalLoss}

The implementation keeps the change as one short rule.

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

In prose, the rule reduces final weak-tail endings of the type \emph{*-ną} and
\emph{*-mą} to plain final \emph{*-n} and \emph{*-m}.

The clearest lexical witness is the pathway to *dōn* ‘do’. If the rule is moved
too early, before the older reduction that already shapes the \emph{*dōną}
sequence,
the derivation records no output instead of expected OE *dōn* ‘do’. No equally
sharp later breakpoint appears within the tested sequence. That is why the note remains
one-sided and why its earlier relation should be understood as a distant
cross-reference only and should not reshape the broader sequence.

This gives the earlier boundary `SC023 < SC061`. No comparably sharp later
boundary is available.

The development is best treated as a small late weak-tail adjustment. It remains
visible in the sequence because it affects the pathway to *dōn* ‘do’, but the
evidence does not support treating it as the center of a wider historical
development.
