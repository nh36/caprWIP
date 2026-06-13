# A-to-u before m

### Sound-change report

#### Historical formulation

SC005 `NWGmcAToUBeforeM` isolates the raising of unstressed noninitial `*a` to `*u` before final `*m` in a narrow set of inflectional environments. The inventory currently labels it Northwest Germanic and gives `shoulder` as the compact-trace witness, but the historical discussion recovered in this pass is broader and more morphologically oriented than that single lexical example suggests.

That mismatch is important. The change is historically plausible, but the source layer does not yet settle whether the best label is strictly Northwest Germanic, a broader North-and-West-Germanic shared development, or a still earlier PWGmc-stage adjustment inside inflectional endings. The existing `needs_human_review=yes` flag should therefore remain explicit.

#### Source tradition

Campbell describes an early development in inflectional endings by which `a > o > u before m`, citing dat.pl. endings and related finite-verb morphology [@Campbell1959, §331(6)]. Sievers/Brunner likewise treats old unstressed `o` in derivational and inflectional syllables before `m` as yielding `u` in Old English [@SieversBrunner1965, §44]. Fulk places the development of early Proto-Germanic unstressed `*o` to `u` before `m` among the important similarities shared by North and West Germanic [@Fulk2018, §5.2].

Those sources support the underlying phenomenon, but they do not align perfectly with CAPR's present label. They point most clearly to a morphologized pre-`m` raising in endings and to a wider North/West-Germanic distribution, not to a settled standalone Northwest-Germanic rule named from the single lexical trace item `shoulder`. The source base is therefore usable but not yet decisive on the staging question.

#### CAPR implementation

CAPR models the change as a narrow pre-`m` raising rule:

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

This rule is intentionally tight. It targets unstressed ending material before final `*m`, with optional `*i` and `*z` tails, rather than a general stem-wide vowel shift. The implementation is therefore more precise than the broader morphophonological prose in the handbooks, but it also inherits their uncertainty about exact stage placement.

#### Place in the cascade

In the inventory ordering, SC005 follows SC004 `PWGmcAiMonophthongization` and precedes SC006 `PWGmcEarlyIApocope`. In the live pipeline it remains part of bundled `PWGmcChanges`, and the inventory itself flags the stage label for review because the rule is Northwest-Germanic in name but still embedded inside the Proto-West-Germanic pipeline bundle.

That bundle position no longer blocks chronology testing in principle. The current first-break runner can expose SC005 through the `expanded-pwgmc` order profile, but the historical naming issue remains unresolved even if the computation path is now available.

#### Order evidence

No validated chronology card exists yet for SC005. The old batch-04 manifest marks it skipped only because the earlier first-break workflow did not expand `PWGmcChanges` into explicit reorderable stages.

The current runner can now test SC005 directly with `--order-profile expanded-pwgmc`, and the dry-run order inspection in this pass confirmed that SC005 resolves as the second rule in that expanded profile. No real first-break TSV output was produced here, however, so no earlier/later historical boundary should yet be claimed.

#### Interpretation

SC005 is a cautious singleton candidate, but it is not yet ready for manifest promotion. The source support is real enough to justify a backend report and dossiers, yet the stage label remains under human review and the chronology layer is still missing real first-break TSV evidence.

#### Remaining cautions

Three cautions remain explicit. First, the stage label is unresolved: the current literature support fits a wider North/West-Germanic inflectional development at least as well as a narrowly Northwest-Germanic singleton. Second, the compact trace currently gives only one lexical witness, `shoulder`, while the source prose is mostly morphological rather than lexical. Third, until real first-break TSV output exists, SC005 should remain out of `report_manifest.tsv`.
