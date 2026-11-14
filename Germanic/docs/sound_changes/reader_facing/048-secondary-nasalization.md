# Secondary nasalization

## SC048. Secondary nasalization before final \emph{*n} (`OESecondaryNasalization`) {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization Ctx([
    {*a} -> {*ą} || _ {*n} .#.
]);
```

The broad \emph{-an}/\emph{-en} split fixes the lower boundary of final \emph{*a} nasalization before \emph{n}. Before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc [bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* 'bake', and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* 'bind'. The upper boundary comes from back mutation. After [SC059 OEBackMutation](#rule-OEBackMutation), PGmc [stélaną]{.recon} ‘steal’ yields [*steolan*]{.pred} rather than expected OE *stelan* ‘steal’, and PGmc [wébaną]{.recon} ‘weave’ yields [*weofan*]{.pred} rather than expected *wefan* ‘weave’. Reciprocal nasal-tail failures place secondary nasalization after apocope, and the later mutation witnesses place it before back mutation; [SC046 OEARestoration](#rule-OEARestoration) retains the clearest independent historical support.

The [weak-paradigm comparison](#weak-n-paradigms-after-apocope) exposes
an additional, unresolved ordering question. Long \emph{*ō} in a
protected plural \emph{*flaskōn} 'flasks' is not a target of this
short-\emph{*a} rule. In the present sequence shortening creates
\emph{*a} too late for nasalization, so unstressed fronting yields
predicted [flascen]{.pred}. Experimental shortening after restoration
but before nasalization instead gives \emph{*flaskąn} and *flascan*.
That regular route must be assessed against the rival class-wide
ending histories, not promoted to an independent historical edge
merely because it fits the plural [@RingeTaylor2014, pp. 163--164;
@Fulk2018, pp. 90, 171--172, §§5.6, 7.32--7.33].
