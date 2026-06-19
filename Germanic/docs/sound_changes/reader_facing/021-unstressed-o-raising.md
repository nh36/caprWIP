# Unstressed \emph{*o}-raising

## Historical discussion

The older history of *heofon* ‘heaven’ preserves a small but real unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the visible \emph{-o-} from an earlier unstressed environment, and Ringe and Taylor keep the same family legible in the wider West Germanic record [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

That is enough for a short note. The change is historically recognizable, but its current order evidence is one-sided and reaches outward to a later chapter.

## SC021. Raising of unstressed \emph{*o} before later \emph{*u} (`NWGmcUnstressedORaising`) {#rule-NWGmcUnstressedORaising}

The implementation keeps the unstressed raising step explicit.

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

In prose, the rule raises unstressed \emph{*o} to \emph{*u} before a later \emph{*u}. This is the adjustment that helps keep the *heofon* derivation on its attested path.

Its chronology is real but one-sided. If the rule is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xémonų} yields *heofun* rather than expected OE *heofon* ‘heaven’. This shows that [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the *heofon* family belongs to the same early unstressed-vowel history described above.
