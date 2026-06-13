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

That placement still matters, but the early-rule harness now exposes SC003 to standalone first-break testing without changing the production bundle. The rule is therefore no longer chronology-draft-only even though the live cascade remains bundled.

#### Order evidence

Validated order evidence now exists through the temporary early-rule harness:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

The earlier search moved SC003 safely across SC002 down to order `2` and then reached the left edge of the tested historical chain with no real break. That side is therefore boundary-only rather than a positive earlier chronology constraint.

The later search does find a real historical break at order `44` across `SC044` OE Breaking. If PGmc Rhotacism is delayed past that stage, PGmc `*líznōjaną` yields `lirnian` rather than `liornian`, `*líznōθi` yields `lirnaþ` rather than `liornaþ`, `*líznô` yields `lirna` rather than `liorna`, and `*mízdai` yields `merde` rather than `meorde`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC003 is now substantially stronger than SC002 on the chronology side. It has a validated one-sided historical boundary and exact wrong-output diagnostics, and the literature support for the phenomenon itself is already solid. The remaining reason to hold it back from manifest promotion is not chronology but historical placement: the existing sources still encourage a more cautious stage label than the inventory's simple `Proto-Germanic` framing.

#### Remaining cautions

Two cautions still matter most. First, backend prose should keep rhotacism distinct from final `*z` deletion, because the literature treats them as separate events with their own chronology. Second, the current `Proto-Germanic` stage label still needs review against the stronger West Germanic / Northwest Germanic framing in the existing sources. The chronology question is now in much better shape, but until that stage-label review is resolved, SC003 should remain out of `report_manifest.tsv`.
