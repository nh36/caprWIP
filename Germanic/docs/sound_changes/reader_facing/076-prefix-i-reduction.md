# Prefix i-reduction

## Historical discussion

Late weak-tail reduction does not affect only inflectional endings and medial vowels. Unstressed prefixes also weaken, and that smaller development deserves a visible place in the sequence even though its chronology is much less sharply fixed. Fulk is the clearest source here, since his discussion of vowels in prefixes makes forms like OE \emph{*be-} and \emph{*ne-} historically legible outcomes in their own right [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and Taylor supply the broader late environment in which such weakening belongs, even though they do not isolate this rule as a major center of the late-tail history [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--332, §§6.8.3--6.9.6].

That is enough for a short note, but not for a major chronology anchor. Prefix reduction belongs in the late weak tail, yet the tested forms do not by themselves determine a closer position for this specific rule.

## SC076. Reduction of prefixal \emph{*i} in unstressed position (`OEPrefixIReduction`) {#rule-OEPrefixIReduction}

The implementation keeps the prefixal reduction as one rule.

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

In prose, the rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the \emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following vowel. This is the development that helps make later prefix spellings such as OE \emph{*be-} and \emph{*ne-} historically intelligible.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

That modest result is still useful. The handbooks give real support for late prefix-vowel weakening, and CAPR places the rule in this late weak-tail stretch on those historical grounds. The placement should be read as approximate and source-based, not as a local ordering forced by the tested forms.
