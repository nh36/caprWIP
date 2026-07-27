# West Germanic rhotacism

## Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

The label [SC003 PGmcRhotacism](#rule-PGmcRhotacism) is historically misleading: the change is a later West Germanic rhotacism, not a Proto-Germanic one. It is also distinct from [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant becomes \emph{*r}.

## SC003. West Germanic rhotacism (`PGmcRhotacism`) {#rule-PGmcRhotacism}

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

Breaking supplies the decisive upper boundary. If rhotacism is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*líznōjaną} yields *lirnian* rather than expected OE *liornian* ‘learn’, PGmc \emph{*líznōθi} yields *lirnaþ* rather than expected *liornaþ*, PGmc \emph{*líznô} yields *lirna* rather than expected *liorna*, and PGmc \emph{*mízdai} yields *merde* rather than expected OE *meorde* ‘meed’. Moving rhotacism earlier within the tested range changes none of the checked forms.

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. Its placement after the earlier loss of final \emph{*z} rests on the historical analyses cited above.
