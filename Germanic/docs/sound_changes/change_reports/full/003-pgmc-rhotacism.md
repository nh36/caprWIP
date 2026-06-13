# Rhotacism

### Sound-change report

#### Historical formulation

SC003 `PGmcRhotacism` appears here as a singleton consonant report for the change of medial `*z` to `*r`. The inventory treats it as a Proto-Germanic stage, but the clearest source support places the change more cautiously in the later Germanic daughter histories, especially West Germanic.

That does not make the rule unusable. It does mean the backend apparatus should preserve the stage-label caution explicitly instead of assuming that the current inventory label is already historiographically settled.

#### Source tradition

The source support for the phenomenon itself is strong. Hogg states succinctly that Germanic `/z/` yielded `/r/` in intervocalic position in Old English, though it was generally lost finally [@Hogg1992, p. 37]. Ringe and Taylor go farther by warning that rhotacism was not uniform in West Germanic and can be shown to have occurred independently in Norse and West Germanic [@RingeTaylor2014, p. 98]. Crist's analysis of West Germanic `*z` loss then clarifies the relative chronology: word-final `*z` deletion precedes rhotacism, so the two changes must not be collapsed into one event [@Crist2002, pp. 1, 4].

This is enough source support for a backend report. It is not enough to treat the current stage label as settled. The clearest sources support the change itself more strongly than they support a simple Proto-Germanic placement.

#### CAPR implementation

CAPR models the development as one explicit rewrite in vocalic medial environments:

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

The implementation is broader than a strictly intervocalic `V_V` rule because the current model also needs to retain medial `VzC` environments. That choice matches the local FST comment, but it should still be kept distinct from the narrower formulations in the historical literature.

#### Place in the cascade

In the current inventory ordering, SC003 follows SC002 `PGmcGmSimplification` and precedes the Proto-West-Germanic developments that begin with SC004. In the implementation, however, it remains inside the same bundled Proto-Germanic consonant block that also contains final `*z` deletion.

That placement explains the present backend status. SC003 clearly belongs in the historical inventory, but it is not yet exposed to the same standalone order-testing machinery that later manifest-backed rules use.

#### Order evidence

Validated order evidence is not yet established. The existing batch manifest for first-break testing marks SC003 as `skipped`, again because the current runner does not yet reorder inside bundles or non-explicit chain positions (`Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv`).

No earlier or later historical boundary has therefore been validated for SC003 in the current order-test apparatus. No exact wrong-output diagnostic is available, and the draft chronology card created in this pass records missing chronology evidence rather than a positive chronology claim.

#### Interpretation

SC003 is stronger than SC002 in source support, but not yet ready for manifest entry. The historical phenomenon is well attested, yet the combination of missing validated order evidence and a potentially too-early inventory stage label means this rule should stay in backend preparation until the chronology and stage placement are clearer.

#### Remaining cautions

Two cautions matter most. First, backend prose should keep rhotacism distinct from final `*z` deletion, because the literature treats them as separate events with their own chronology. Second, the current `Proto-Germanic` stage label needs review against the stronger West Germanic / Northwest Germanic framing in the existing sources. Until that review and dedicated order testing are complete, SC003 should remain out of `report_manifest.tsv`.
