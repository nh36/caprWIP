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

Épinal–Erfurt *scytil* 'balance beam', glossing Latin *momentum*, retains
medial unstressed *i*; Corpus *scytel* 'balance beam' has *e*
[@Pheifer1974, pp. 34, 101, item 632; @Sweet1885, p. 79, Corpus 1325;
@Christiansen2018, p. 583, note 3, and pp. 599--600, note 52].
After ending loss and the appropriate earlier changes, inherited
\emph{*skútilaz} retains its *i* in final closed \emph{*-til}:
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) does not delete
that vowel. It subsequently lowers to *e* under
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1),
giving normalized *sċytel* 'dart; balance beam'.
Pheifer's discussion already recognizes both retained *i* and *e*
spellings in the early glossaries and variation attributable to their
common exemplar [@Pheifer1974, p. lxxv, §63]. The contrast illustrates
retained and lowered vowel qualities, not a precisely dated interval
between surviving manuscripts; their exemplars need not have the same
dates or orthographic histories. Nor does the Corpus form by itself
establish a specifically West Saxon reflex. This medial *i/e* evidence
is separate from Christiansen's etymological argument about stressed
root *y* against an alleged connection with the *scit-* 'excrement'
family [@Christiansen2018, pp. 593--598].

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
