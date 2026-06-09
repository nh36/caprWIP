# J-cluster coalescence

## Historical discussion

This chapter belongs to the later part of the palatalization and fronting
region. Campbell, Ringe and Taylor, and Fulk all discuss the same neighborhood
of palatalized and fronted outcomes that underlies forms such as *bīeġan*
‘bend’ and *sēċan* ‘seek’ [@Campbell1959, pp. 89, 107--108, §§170, 248--251;
@RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13]. None
of them turns this later cluster adjustment into a major independent headline.
The historical interest lies in the fact that it remains a real part of the
sequence even though the larger palatalization and umlaut chapters carry more of
the explanatory weight.

That narrower scale matters. Earlier chapters have already established the plain
velar and \emph{*sk} palatalizations, and the umlaut chapter has already handled the
major vowel consequences. The present rule is a later coalescence inside that
same neighborhood. It deserves explicit prose because the lexical outcomes are
clear, not because it eclipses the larger processes around it.

## SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

The implementation keeps the later cluster coalescence very small and explicit.

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

In prose, the rule coalesces \emph{*gj} and \emph{*kj} into the palatal outcomes that later
surface in forms such as *bīeġan* ‘bend’ and *sēċan* ‘seek’.

Its earlier dependency is clearer than its later limit. If the rule is moved
before [velar palatalization before front vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc `*báugijaną` yields *bēaġan* ‘bend’ rather than expected OE *bīeġan*,
and PGmc `*sōkijaną` yields *sōċan* ‘seek’ rather than expected *sēċan*. This
gives the earlier boundary `SC052 < SC057`. No comparably sharp later lexical
breakpoint emerges within the remaining sequence, so the chronology remains
short and one-sided.

That modest shape is historically appropriate. The rule is a real later member
of the palatalization region, but it does not need to absorb the umlautal
chapter behind it or the nasal-dissimilation chapter that follows it. The
later coalescence remains visible in the sequence once the
larger neighboring chapters are already in place.
