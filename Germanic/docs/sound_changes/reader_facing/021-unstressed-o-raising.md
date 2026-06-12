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

Its chronology is real but one-sided. If the rule is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xémonų} yields *heofun* rather than expected OE *heofon* ‘heaven’. This shows that [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). If the rule is moved earlier within the currently tested range, no witness word yields a historical first-break result before the search reaches bundled earlier material, so no earlier positive boundary is yet available.

The later boundary is therefore broad and distant. The earlier side remains a search-boundary limitation, not a historical anchor.
