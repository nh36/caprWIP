# A2 — Separate consonant loss from foot-marker removal

## Identity and question

SC085 `OEHLoss`; private research at `113101ac` in canonical/A/B2,
with SC083 unchanged. Can the historical consonant operation return
its input foot annotation for another consumer, and can it be factored
without changing the original relation when there is no consumer?

## Current state and exact proposal

The incumbent combines two operations:

```foma
define OEHLoss FootCtx([
    [{*x}|{*ç}] -> 0 || EnglishStarVocalic _ EnglishStarVocalic
]) .o. [{*ᶠ} -> 0];
```

For production review, preserve the public identifier and factor its
internals, with no change in when the marker is removed:

```foma
define OEHConsonantLoss FootCtx([
    [{*x}|{*ç}] -> 0 || EnglishStarVocalic _ EnglishStarVocalic
]);
define OEStripFootMarker [{*ᶠ} -> 0];
define OEHLoss [OEHConsonantLoss .o. OEStripFootMarker];
```

The two private exports are `StKeepH` and `StStrip`. In the no-op
handoff they execute contiguously, after `OEWeightCleanup` and before
`OEContraction`. Do not move removal across the incumbent contraction.
A future independently authorized post-loss rule that needs the marker
can execute between these two operations; no such rule is proposed here.

## Diagnosis

The [Foma transcript and live receipt](sc085-handoff-traces.json.gz)
check equality of the upper projections as recognizers, then check
functionality of the union. Equal domains plus one possible output in
the union establish equality of input/output relations; this does not
rely on Foma's general transducer-equivalence test. Both obligations
pass, while deliberately unequal domains and conflicting outputs give
false respectively. This proof targets the actual Foma definitions
via the shared verified image loader, which also restores macros
such as `FootCtx` that are not serialized into the definition image.

On each independently replayed order, all 790 endpoints and all
changed-stage traces outside the newly visible boundary agree.
Fusing the two stages in the receipt reconstructs the incumbent
trace exactly. The complete census in every order is:

| Observable operation | Archived and active rows (same IDs in both) |
|---|---|
| Consonant loss | 2019 ‘flee’, 2195 ‘slay’, 2242 ‘ten’, 2259 ‘toe’ |
| Marker removal only | 1943 ‘begin’, 1944 ‘believe’ |
| Both together in a recorded corpus row | None |

‘World’ retains *weorold* and has no strip firing. Independent local
comparisons preserve voiced-material position and stress separately:
post-loss ‘clay’ retains exact *æ*, ‘fringe’ retains *u* and *m*, and
the palatalized ‘strike’ probe produces hiatus without contracting it.
The source-conditioned pretonic ‘behind’, geminate ‘sieve’ and final
‘catch’ are locally protected. These are isolated stage projections,
not new complete derivations. The synthetic marked post-head positive,
with and without the outer sentence tag, loses *ç* but passes *ᶠ* to
the strip. The prior [late consumer assay](../hiatus-cycle4/STRESS_HANDOFF.md)
shows why the intervening hook matters: late prefixed plain root hiatus
can be distinguished from genuine later weak hiatus. It also reproduces
the invalid free marker lift in ‘world’; this proposal does not restore it.

## Literature and historical analysis

The existing [SC085 adjudication](../../../../docs/sound_changes/audits/sc085-adjudication.md)
documents Campbell (1959: 186–187 §§461, 464–465), Ringe & Taylor
(2014: 314–318) and Sweet (1885: 36, 41, 104, 107). They support
intervocalic loss of the singleton, not general loss of final, geminate
or pretonic *h*. They do not motivate a subsequent sound law deleting
an annotation. The annotation is a technical proxy for a local
prosodic distinction, not a reconstruction of a segment or an
independently valued secondary-stress grammar. The actual historical
loss can feed contraction; this decomposition adds no historical
ordering edge, geographical extension or analogical explanation.

## Verdict

**RETAIN** SC085 and its existing registry verdict; **DEFER**
changing the marker lifetime in production until a specific post-loss
consumer is approved. The contiguous factorization alone is safe to
adopt independently, but merits a production change only if the
named hook is useful. Neither direction should be bundled with
SC083: the correction there already sees the marker. Prefer named
helpers under the existing `OEHLoss` component; no new historical
registry row or execution-stage ID is required for that refactor.

## Propagation, validation and residue

No target or corpus migration is indicated. In a separately authorized
change, rerun the formal equivalence, archived plus current firing
census, and the protected positive/negative controls. A consumer inserted
between the operations is *not* protected by the equivalence proof:
validate that operation and its full downstream effects independently.
The proposal adds no default CI lane and does not change certification.

With the same pinned cache setup as [A1](SC083.md):

```bash
set -o pipefail
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh sc085_handoff --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay5-sc085.json.gz
```

Receipt SHA-256:
`91fc66557a95a835d38fd6b6e0fb46d17c37a2f9386795c1cdd4c0d7910ca3c8`.
