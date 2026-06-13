# Gm simplification

### Sound-change report

#### Historical formulation

SC002 `PGmcGmSimplification` appears here as a narrow Proto-Germanic consonant note. The modeled change deletes `*g` before `*m`, and the clearest inventory witnesses are the families behind `dream` and `team`.

That historical claim is plausible, but the present source base is still limited. The phenomenon is best treated as a backend singleton candidate rather than as a report already ready for volume use.

#### Source tradition

Current source support is lexical rather than expository. Kroonen derives OE `dream` from `*draugma-` and states that OE `tēam` continues `*tauma-`, whose original form was `*taugma-` and, like `*drauma- < *draugma-`, lost its `*g` [@Kroonen2013, pp. 101, 511]. Orel independently supports the dream family through his `*draumaz` entry [@Orel2003, p. 114].

That is enough to make the sound change historically legible. It is not yet enough to count as a full comparative-grammar discussion of the rule. No broader handbook-style phonological treatment of `*gm > *m` was recovered in this pass, so the source base remains primarily etymological. The inventory's second witness `team` is supported lexically, but the current source base still needs a clearer comparative discussion before chapter prose would be advisable.

#### CAPR implementation

CAPR isolates this development as one explicit Proto-Germanic stage:

```foma
define PGmcGmSimplification [{*g} -> 0 || _ {*m}];
```

The rule is intentionally narrow. It captures the loss of `*g` before `*m` in the lexical family represented by `dream` and `team`, without implying that every later consonant simplification belongs to the same event.

#### Place in the cascade

In the current inventory ordering, SC002 is the first historical sound change after the excluded support/input stage `SC001 EnglishProtoInput`, and it stands immediately before SC003 `PGmcRhotacism`. In the implementation, however, it still sits inside the bundled Proto-Germanic consonant block rather than as an independently reorderable chain member.

That distinction matters for backend placement. The rule has a clear place in the modeled cascade, but the current order-test infrastructure still treats it as part of a bundle rather than as a validated standalone chronology node.

#### Order evidence

Validated order evidence is not yet established. The existing batch manifest for first-break testing marks SC002 as `skipped`, with the explicit note that the current runner does not yet reorder inside bundles or non-explicit chain positions (`Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv`).

That means no earlier or later historical boundary has yet been tested in a way comparable to the manifest-backed SC014-SC087 material. No exact wrong-output diagnostic is currently available, and the draft chronology card created in this pass therefore records missing chronology evidence rather than a positive chronology claim.

#### Interpretation

SC002 is adequate for backend preparation but not yet for manifest entry. The historical phenomenon is real enough to justify a production-style source report and dossiers, but it still lacks validated order evidence and would benefit from stronger phonological source support beyond the lexical dictionary entries now in hand.

#### Remaining cautions

The main caution is evidential. At present the source base for SC002 is mostly etymological, not a broad comparative discussion of the sound change as such. The current order-test infrastructure also skips the rule entirely, so no chronology statement should be inferred from the absence of failures. Until dedicated order evidence exists and the phonological literature base is broadened, SC002 should remain out of `report_manifest.tsv`.
