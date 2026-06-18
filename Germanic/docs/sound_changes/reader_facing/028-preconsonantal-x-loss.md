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

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC028 NWGmcPreconsonantalXLoss](#rule-NWGmcPreconsonantalXLoss) before or after any specific neighboring change. The handbooks make preconsonantal \emph{x}-loss historically recognizable, but they do not place it precisely within this local stretch. CAPR therefore keeps it here as a short prefatory note before the better-constrained glide and fronting rules that follow. The placement should be read as approximate, not tightly fixed.
