# Unstressed \emph{*o}-raising

## Historical discussion

The older history of *heofon* 'heaven' requires an unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the \emph{-o-} from an earlier unstressed environment, and the same raising is visible in Old Saxon \emph{heban} and the North-West Germanic reconstructed base \emph{*hebun} [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

The change is historically recognizable, but the checked forms provide only a later boundary.

## SC021. Raising of unstressed \emph{*o} before later \emph{*u} (`NWGmcUnstressedORaising`) {#rule-NWGmcUnstressedORaising}

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xémonų]{.recon} ‘heaven’ yields [*heofun*]{.pred} rather than expected OE *heofon* ‘heaven’; earlier placement changes no checked output. The witness therefore places [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) before medial unstressed-\emph{u} lowering.

Nothing in the present lexicon supplies the corresponding earlier boundary.
