# Prefix i-reduction

## Historical discussion

Late weak-tail reduction does not affect only inflectional endings and medial vowels. Unstressed prefixes also weaken, and that smaller development deserves a visible place in the sequence even though its chronology is much less sharply fixed. Fulk is the clearest source here, since his discussion of vowels in prefixes makes forms like OE \emph{*be-} and \emph{*ne-} historically legible outcomes in their own right [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and Taylor supply the broader late environment in which such weakening belongs, even though they do not isolate this rule as a major center of the late-tail history [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--332, §§6.8.3--6.9.6].

That is enough for a short note, but not for a major chronology anchor. Prefix reduction belongs in the late weak tail, yet the current tests do not recover a positive earlier boundary or a positive later boundary for this specific rule.

## SC076. Reduction of prefixal \emph{*i} in unstressed position (`OEPrefixIReduction`) {#rule-OEPrefixIReduction}

The implementation keeps the prefixal reduction as one rule.

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

In prose, the rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the \emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following vowel. This is the development that helps make later prefix spellings such as OE \emph{*be-} and \emph{*ne-} historically intelligible.

The chronology evidence is weak on both sides. If the rule is moved earlier, the current tests do not find a real lexical break before the search reaches bundled earlier material. If the rule is delayed, they do not find a real lexical break before the tested range ends at [SC087 OERMetathesis](#rule-OERMetathesis). No exact wrong early or late output is currently available, so the prose does not claim a sharper ordering relation than the evidence supports.

That modest result is still useful. The rule has historical legitimacy from the prefix-vowel literature, and it belongs in this late weak-tail region for that reason. Its place in the sequence should therefore be read as a source-based approximation, not as a positive lexical hinge fixed by the current test.
