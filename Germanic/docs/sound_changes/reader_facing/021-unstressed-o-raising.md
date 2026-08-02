# Unstressed \emph{*o}-raising

## Historical discussion

The older history of [*heofon*]{.iv lang=oe sort=heofon role=evidence_form} 'heaven' requires an unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the \emph{-o-} from an earlier unstressed environment, and Ringe and Taylor reconstruct northern West Germanic [hebun]{.recon .iv lang=pwgmc sort=hebun role=evidence_form} 'heaven' behind OE [*heofon*]{.iv lang=oe sort=heofon role=evidence_form} 'heaven' and OS [*heban*]{.iv lang=os sort=heban role=evidence_form} 'heaven' [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

The change is historically recognizable, but the lexical evidence establishes only a later boundary.

## SC021. Raising of unstressed \emph{*o} before later \emph{*u} (`NWGmcUnstressedORaising`) {#rule-NWGmcUnstressedORaising}

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xémonų]{.recon} ‘heaven’ yields [*heofun*]{.pred} rather than expected OE *heofon* ‘heaven’; earlier placement changes no output. The witness therefore places [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) before medial unstressed-\emph{u} lowering.

Nothing in the present lexicon supplies the corresponding earlier boundary.
