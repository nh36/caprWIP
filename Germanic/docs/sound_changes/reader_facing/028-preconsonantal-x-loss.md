# Preconsonantal \emph{*x}-loss

## Historical discussion

Campbell explicitly treats loss of \emph{x} and gives forms such as *fléam* ‘flight’ and *hēla* ‘heel’ as examples of the same broad development [@Campbell1959, p. 186, §461]. That is enough to make this a historically legible change.

The present order evidence is much lighter than the historical description. This chapter therefore stays brief: the change belongs in the sequence, but current testing does not make it a strong chronological marker.

## SC028. Loss of preconsonantal \emph{*x} (`NWGmcPreconsonantalXLoss`) {#rule-NWGmcPreconsonantalXLoss}

The implementation keeps the deletion rule explicit.

```foma
define NWGmcPreconsonantalXLoss [
    {*x} -> 0 || _ {*s} EnglishStarConsonant
];
```

In prose, the rule deletes \emph{*x} before \emph{*s} plus another consonant. It preserves a historically recognizable part of the older consonant history without assigning it more order-testing force than the current evidence supports.

Current testing does not identify a positive historical boundary on either side. If the rule is moved earlier or later within the currently tested range, no witness word yields a historical first-break result: the earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. In reader-facing terms, this is a historically legible change whose current order evidence remains chronology-negative. The rule is placed here because the comparative literature treats preconsonantal \emph{*x}-loss as background to the glide and fronting developments that follow. The current test does not identify a closer relative chronology than that.
