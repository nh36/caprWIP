# Medial weak front-vowel quality changes

## Historical discussion

Hogg and Ringe and Taylor treat the late weakening and merger of unstressed
vowels as a continuing history [@HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6].
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) lowers
medial unstressed \emph{i}; [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering)
preserves \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’
type.

Two stages must be distinguished. Mutation-produced weak \emph{*y}
unrounds to \emph{*i}; retained \emph{*i} later lowers to \emph{*e}.
Hogg dates the unrounding to a very early prehistoric stage and gives
\emph{*gaduling > gædeling}, with root mutation transmitted through the
weak vowel. Initial-root \emph{*y} and still marked subordinate
\emph{*ỳ} are not weak-vowel applications
[@HoggGrammar2011, p. 219, §6.10 and note 1].

The unrounding component is computed after general high-vowel syncope
and before the later light pre-\emph{*l} loss. It is separate from both
deletion and later lowering. Unrounding preserves vowel height and
commutes with the bounded general high-vowel deletion; this adjacency
does not prove an unrounding-after-syncope chronology. With the
source-supported \emph{d/l} retention condition, *gædeling* 'companion'
also survives on either side of the light pre-\emph{*l} component.
That particular result does not establish universal commutation.

The early component is printed at its actual executable location under
[SC115 OEHighLinkSyncope](#rule-OEHighLinkSyncope), a support component
of this vowel-quality history, not a second historical syncope law.
The separate technical decoder runs after the light pre-\emph{*l}
component and before ordinary lowering. It does not turn protected
subordinate \emph{*ỳ} into an application of weak unrounding.

General lowering precedes the restricted restoration before \emph{*ng}. The
evidence is narrower than that for
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

## SC074. First medial unstressed-\emph{i} lowering (`OEMedUnstressedILowering1`) {#rule-OEMedUnstressedILowering1}

```foma
define OEMedUnstressedILowering1 FootCtx([
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
]);
```

The rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding
vocalic syllable. The resulting \emph{e}-outcome is reversed before
\emph{*ng}.

If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhti*]{.pred} rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc [skíllingaz]{.recon} ‘shilling’ yields [*sċilleng*]{.pred} rather than expected *sċilling* ‘shilling’. The derivations require [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) to follow [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and precede [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side. The rule follows unstressed long-vowel
shortening and precedes the more specific \emph{*ng} preservation.
