# Unstressed ei-contraction

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* 'bore', and PGmc [líkkōjaną]{.recon} ‘lick’ yield [*licceian*]{.pred} rather than expected *liccian* 'lick'. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
