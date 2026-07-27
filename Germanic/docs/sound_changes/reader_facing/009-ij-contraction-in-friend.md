# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc \emph{*friund} > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

The change concerns a rare sequence confined to the `friend` family and cannot safely be generalized into a broadly productive rule.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

Only the `friend` family tests this contraction. If the rare \emph{*ijō} sequence survives until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*fríjōndz} yields *friund* rather than expected OE *frēond* 'friend'; moving contraction earlier within the tested range changes no checked output.

That single contrast places [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) before diphthong leveling but gives no lower boundary. It cannot establish a productive sound law beyond this family, precisely the reservation made by Ringe and Taylor.
