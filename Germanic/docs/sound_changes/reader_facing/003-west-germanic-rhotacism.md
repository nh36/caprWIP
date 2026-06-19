# West Germanic rhotacism

## Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

That historical label matters here. CAPR keeps the implementation name [SC003 PGmcRhotacism](#rule-PGmcRhotacism), but the historical change treated in this chapter is a later West Germanic rhotacism, not a Proto-Germanic one. It must also remain distinct from [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant is turned into \emph{*r}.

## SC003. West Germanic rhotacism (`PGmcRhotacism`) {#rule-PGmcRhotacism}

The implementation keeps the rhotacism step explicit.

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

In prose, the rule turns surviving medial \emph{*z} into \emph{*r} in the West Germanic line. CAPR keeps the label [SC003 PGmcRhotacism](#rule-PGmcRhotacism) for the modeled rewrite, but the historical interpretation is later than the name suggests.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*líznōjaną} yields *lirnian* rather than expected OE *liornian* ‘learn’, PGmc \emph{*líznōθi} yields *lirnaþ* rather than expected *liornaþ*, PGmc \emph{*líznô} yields *lirna* rather than expected *liorna*, and PGmc \emph{*mízdai} yields *merde* rather than expected OE *meorde* ‘meed’. This shows that [SC003 PGmcRhotacism](#rule-PGmcRhotacism) must come before [SC044 OEBreaking](#rule-OEBreaking) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat West Germanic rhotacism as a later development after the earlier \emph{*z}-loss material described above.
