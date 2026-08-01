# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`NWGmcAToUBeforeM`) {#rule-NWGmcAToUBeforeM}

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [skúldramiz]{.recon} ‘shoulders’ yields [*sċoldrum*]{.pred} rather than expected OE *sċuldrum* 'shoulders'; earlier placements converge on the expected output. The scope of the change is established by inflectional evidence: the a-stem dat.pl. *-um*, the strong-adjective dat.sg., and the 1pl. present indicative all show *-um* consistently across Old Norse, Old English, Old Saxon, and Old High German, while Gothic preserves the conservative *-am-* forms. The derivation of *sċuldrum* 'shoulders' supplies a CAPR ordering witness for the relative chronology, but the cognate set for 'shoulder' does not contribute comparative evidence for the rule's historical scope.

The evidence is confined to inflectional
material.
