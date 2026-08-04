# West Germanic rhotacism

## Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

The internal identifier [SC003 EAFRhotacism](#rule-EAFRhotacism) places the change in CAPR's Early Anglo-Frisian corridor, the operational post-Proto-West-Germanic stage on the English line; historically the change is a West Germanic rhotacism, later than Proto-Germanic. It is also distinct from [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant becomes \emph{*r}.

## SC003. West Germanic rhotacism (`EAFRhotacism`) {#rule-EAFRhotacism}

```foma
define EAFRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

Breaking supplies the decisive upper boundary. If rhotacism is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc [líznōjaną]{.recon} ‘learn’ yields [*lirnian*]{.pred} rather than expected OE *liornian* ‘learn’, PGmc [líznōθi]{.recon} ‘learns’ yields [*lirnaþ*]{.pred} rather than expected *liornaþ* 'learns', PGmc [líznô]{.recon} ‘learn’ yields [*lirna*]{.pred} rather than expected *liorna* 'learn', and PGmc [mízdai]{.recon} ‘meed’ yields [*merde*]{.pred} rather than expected OE *meorde* ‘meed’. Moving rhotacism earlier within the tested range changes no output.

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. Its placement after the earlier loss of final \emph{*z} rests on the historical analyses cited above.
