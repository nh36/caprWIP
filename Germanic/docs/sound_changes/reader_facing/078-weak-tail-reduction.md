# Weak-tail reduction

## Historical discussion

The last rule in the present late weak-tail cluster is stronger than the small prefix note that precedes it. Campbell, Hogg, Ringe and Taylor, and Fulk all support a late region in which apocope, shortening, contraction, and further weak-tail reductions continue to reshape final syllables [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--91, §5.6]. What makes the present rule stand out is that the finite-state chronology gives it a real boundary on both sides.

That does not make it a license to absorb later material. The later relation to SC086 OEContraction is meaningful, but it remains a cross-reference to the next cluster, not a reason to pull that cluster into the present chapter.

## SC078. Reduction of remaining weak-tail vowels (`OEWeakTailReduction`) {#rule-OEWeakTailReduction}

The implementation keeps the last weak-tail reduction as one explicit step.

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

In prose, the rule carries the remaining weak-tail reductions that prevent a broad class of spurious \emph{-en} or extra-vowel outcomes from surviving too late in the derivation.

Its chronology is real on both sides, though the two sides are not equally local. If the rule is moved before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a much wider set of comparable \emph{-en} failures. If the rule is delayed until after SC086 OEContraction, PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, and PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’. This shows that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction), and that [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) must come before SC086 OEContraction.

The asymmetry of those two boundaries is important. The earlier side is broad and should be read as a large computational limit, not a tight local adjacency claim. The later side is narrower and more directly interpretable. Together they make [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) substantial enough for its own chapter, but still not a reason to merge the next cluster into the present section.
