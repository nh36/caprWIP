# Final bare-\emph{a} loss

## Historical discussion

I isolate the loss of final short low vowels within the broader erosion of final syllables described by the handbooks [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

Final bare-a loss follows the medial unstressed vowel changes and
precedes restoration, which depends on the environment left by the loss.

## SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

The two sides of final bare-\emph{a} loss rest on different evidence. Applied before final \emph{z}-deletion, the change gives the wrong outputs: PGmc \emph{*bárdaz} yields *bearda* rather than expected OE *beard* ‘beard’, and PGmc \emph{*kámbaz} yields *camba* rather than expected *camb* ‘comb’. Applied after restoration, PGmc \emph{*kráftaz} yields *craft* rather than expected OE *cræft* ‘craft’, and PGmc \emph{*dágaz} yields *dag* rather than expected *dæġ* ‘day’. The distant lower limit follows final \emph{z}-loss; the local feeding relation precedes restoration, which requires the environment created by the vowel loss.
