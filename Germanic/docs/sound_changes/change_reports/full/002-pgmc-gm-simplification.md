# Gm simplification

### Sound-change report

#### Historical formulation

SC002 `PGmcGmSimplification` appears here as a narrow Proto-Germanic consonant note. The modeled change deletes `*g` before `*m`, and the clearest inventory witnesses are the families behind `dream` and `team`.

That historical claim is plausible, but the present source base is still limited. The phenomenon is best treated as a narrow singleton note rather than as a broad historical core.

#### Source tradition

Current source support is lexical rather than expository. Kroonen derives OE `dream` from `*draugma-` and states that OE `tēam` continues `*tauma-`, whose original form was `*taugma-` and, like `*drauma- < *draugma-`, lost its `*g` [@Kroonen2013, pp. 101, 511]. Orel independently supports the dream family through his `*draumaz` entry [@Orel2003, p. 114] and the team family through `*tauxmaz` [@Orel2003, p. 403], but that second entry already reflects the simplified cluster and therefore does not itself establish the `*g`-loss.

That is enough to make the sound change historically legible. It is not yet enough to count as a full comparative-grammar discussion of the rule. No broader handbook-style phonological treatment of `*gm > *m` was recovered in this pass, so the source base remains primarily etymological. The inventory's second witness `team` is supported lexically, but the current source base still needs a clearer comparative discussion before chapter prose would be advisable.

#### CAPR implementation

CAPR isolates this development as one explicit Proto-Germanic stage:

```foma
define PGmcGmSimplification [{*g} -> 0 || _ {*m}];
```

The rule is intentionally narrow. It captures the loss of `*g` before `*m` in the lexical family represented by `dream` and `team`, without implying that every later consonant simplification belongs to the same event.

#### Place in the cascade

In the current inventory ordering, SC002 is the first historical sound change after the excluded support/input stage `SC001 EnglishProtoInput`, and it stands immediately before SC003 `EAFRhotacism`. In the implementation, however, it still sits inside the bundled Proto-Germanic consonant block rather than as an independently reorderable chain member.

That distinction still matters for backend placement. The production cascade keeps SC002 inside the bundle, but the temporary early-rule harness now expands the sandbox order so the rule can be tested as a standalone chronology target without changing the live FST.

#### Order evidence

Validated order evidence now exists through the temporary early-rule harness:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

The earlier search found no real break before the tested-chain boundary at order `2`. SC002 is already the leftmost historical rule in that temporary harness, so the earlier side is boundary-only rather than a positive chronology constraint.

The later search does find a real computational break at order `93` across `SC094` Old English Remove Stars. If PGmc Gm Simplification is delayed that far, PGmc `*dráugmaz` yields `drēagm` rather than `drēam`, and PGmc `*táugmaz` yields `tēagm` rather than `tēam`.

That later break is not an ordinary historical chronology relation. `SC094` is an orthography-surface support stage, so the validated result is computationally real but non-historical.

#### Interpretation

SC002 is now better grounded than it was when the chronology layer was still blocked by infrastructure. Even so, the result remains weak as a historical singleton: the earlier side is only a start-boundary observation, the later side breaks only at a non-historical orthography stage, and the source base is still narrow and mainly etymological.

#### Remaining cautions

The main caution remains evidential. At present the source base for SC002 is mostly etymological, not a broad comparative discussion of the sound change as such. The validated chronology card also yields no ordinary historical boundary: it records a boundary-only earlier result and a non-historical orthography-surface later break. Until the phonological literature base is broadened and a stronger historical chronology claim becomes available, SC002 should remain a backend-preparation note rather than a fully anchored historical core.
