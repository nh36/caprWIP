# Early weak front-vowel unrounding

## Historical discussion

Mutation-produced weak \emph{*y} unrounds to \emph{*i}; retained
\emph{*i} later lowers to \emph{*e}. These are quality changes, not
syncope. Hogg places the unrounding at a very early prehistoric stage
and illustrates transmitted mutation with \emph{*gaduling > gædeling}
[@HoggGrammar2011, p. 219, §6.10 and note 1].
The early component belongs to the same weak-front-vowel history whose
later lowering is [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1).
Its stable identifier is retained for scholarly cross-references; it no
longer implements high-vowel deletion.

## SC115. Early weak-front-vowel unrounding component (`OEHighLinkSyncope`) {#rule-OEHighLinkSyncope}

```foma
define OEHighLinkSyncope FootCtx([
    {*y} -> {*i} || EnglishStarVocalic OEAnyConsonant+ _
]);
```

The component excludes initial-root \emph{*y} and still-marked
subordinate \emph{*ỳ}. It is computed after
[SC065 OEMedialSyncope](#rule-OEMedialSyncope) and before
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope).
Unrounding preserves height and commutes with the bounded general
high-vowel loss; the serialization does not date unrounding after
syncope. The \emph{d/l} protection in the later light component permits
*gædeling* 'companion' on either side of that component, but this
particular comparison does not establish universal commutation.

The separate [SC116 OEHighStressDecode](#rule-OEHighStressDecode) helper
runs after the light pre-\emph{*l} component, not at this unrounding
position. It preserves secondary-vowel protection until both deletion
components have finished. Neither technical decoding nor this component's
serialized location dates disappearance of historical secondary stress.
