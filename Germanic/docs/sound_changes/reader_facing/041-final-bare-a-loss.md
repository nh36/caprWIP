# Final bare-\emph{a} loss

## Historical discussion

The handbooks treat loss of final short low vowels as part of a broader erosion of final syllables, but that broader background still supports a short explicit rule here [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

This change belongs after the medial unstressed vowel changes because it affects final syllables and leaves the low-stress interior of the word behind. It also belongs before restoration because later fronted forms depend on the environment it leaves behind.

## SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

The implementation keeps the loss of the final vowel explicit.

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

In prose, the rule deletes a surviving final bare \emph{*a}. This is the step that prevents a large class of words from carrying a spurious final vowel into Old English.

Its chronology is broad on the left and sharper on the right. If the rule is moved before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*bárdaz} yields *bearda* rather than expected OE *beard* ‘beard’, and PGmc \emph{*kámbaz} yields *camba* rather than expected *camb* ‘comb’. If it is delayed until after [SC046 OEARestoration](#rule-OEARestoration), PGmc \emph{*kráftaz} yields *craft* rather than expected OE *cræft* ‘craft’, and PGmc \emph{*dágaz} yields *dag* rather than expected *dæġ* ‘day’. This shows that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), and that [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss) must come before [SC046 OEARestoration](#rule-OEARestoration).

The earlier boundary reaches across a wide stretch of the cascade and is best read as a broad limit, not a local pair. The later boundary is the nearer result: restoration needs final bare-\emph{a} loss to have happened already.
