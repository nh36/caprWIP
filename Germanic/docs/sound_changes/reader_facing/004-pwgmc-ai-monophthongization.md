# Proto-West-Germanic ai-monophthongization

## Historical discussion

Ringe and Taylor treat the reduction of unstressed \emph{*ai} as one of the major early vowel shifts shared across the Northwest Germanic area [@RingeTaylor2014, pp. 40--41].

The historical support is strongest for unstressed \emph{*ai}, especially word-finally. The rule extends the change to nonfinal \emph{*ai > *ā}, a generalization stated more sharply than in the current handbook discussion.
Both developments have inherited \emph{*ai} as their input.

## SC004. Proto-West-Germanic ai-monophthongization (`PWGmcAiMonophthongization`) {#rule-PWGmcAiMonophthongization}

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

The soul form fixes the relation to interstress raising. If monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} ‘soul’ yields [*sāwel*]{.pred} rather than expected OE *sāwol* ‘soul’. No earlier placement changes a checked output.

This witness proves that monophthongization preceded interstress raising; it says nothing about the date of the wider nonfinal \emph{*ai > *ā} generalization. The word-final merger with long mid \emph{*ē} belongs among the early Northwest Germanic vowel shifts; the broader chronology remains less certain.
