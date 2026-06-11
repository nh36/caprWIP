# Medial unstressed-i lowering

## Historical discussion of medial unstressed-i lowering and \emph{*ng} retention

The next pair belongs to the same late weak-tail region as the shortening and merger chapter to the left, but it is smaller and more locally conditioned. Hogg and Ringe and Taylor both treat the late weakening and merger of unstressed vowels as part of a continuing history, and that background helps explain why the present chapter reads best as a narrow follow-on, not a new center of gravity [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6]. The specific value of the pair is derivational. [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) generalizes a medial unstressed-\emph{i} lowering, while [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) immediately narrows that result by preserving \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’ type.

That close interaction is why the two rules still belong in one small chapter. The history is not simply adjacency in the cascade. The second rule directly repairs the overbroad outcome that the first would otherwise leave behind in the \emph{*ng} environment. Even so, the pair remains narrower and more witness-limited than [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

## SC074. First medial unstressed-\emph{i} lowering (`OEMedUnstressedILowering1`) {#rule-OEMedUnstressedILowering1}

The implementation gives the first lowering step its own rule.

```foma
define OEMedUnstressedILowering1 [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

In prose, the rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding vocalic syllable. This is the broader step that would spread the \emph{e}-outcome through the late weak tail if it were left uncorrected.

Its chronology is explicit on both sides. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*fúrxtīnaz} yields *fyrhti* rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc \emph{*skíllingaz} yields *sċilleng* rather than expected *sċilling* ‘shilling’. This shows that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1), and that [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) must come before [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side, but it is still real. The rule belongs between the stronger shortening/merger chapter and the more specific \emph{*ng} preservation that follows it.

## SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng} (`OEMedUnstressedILowering`) {#rule-OEMedUnstressedILowering}

The following rule gives the local \emph{*ng} restriction its own explicit step.

```foma
define OEMedUnstressedILowering [
    {*e} -> {*i} || _ {*n} {*g}
];
```

In prose, the rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Its earlier boundary is the reciprocal side of the [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) relation. If the rule is moved before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1), PGmc \emph{*skíllingaz} yields *sċilleng* rather than expected OE *sċilling*. No equally sharp later breakpoint appears within the tested range, so the available evidence shows only that [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) must come before [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

That one-sided profile is enough for a follower rule of this kind. It is historically useful because it keeps the \emph{*ng} forms from being swallowed by the broader lowering, but it does not need to carry more chronology than the evidence supplies.
