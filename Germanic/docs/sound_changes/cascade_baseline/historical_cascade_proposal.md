# Minimum-change historical cascade proposal (Phase 4)

## Headline result

**The current executable cascade already satisfies every supported historical
constraint.** All 13 cascade-relevant edges in the adjudicated partial order
(`historical_partial_order.tsv`) hold in the current order, the constraint graph
is acyclic, and the single counter-cascade historical relation (SC020 before
SC003, per Crist) is already realised by context-scoping rather than ordering.

Therefore the minimum-change historically valid total order is **the current
order itself**: zero changed pairwise relations, zero rule displacement.

The corrections the evidence demands are **not moves**. They are corrections to
internal identifiers, stage/scope metadata, granularity, and reader-facing prose.
This directly contradicts the earlier working hypothesis that the genuine PNWGmc
rules must be moved before the genuine PWGmc rules: the adjudicated partial order
does not license that permutation, and the current order needs no reordering to
be historically valid.

## Current order vs proposed order

| | Current | Proposed |
| --- | --- | --- |
| Executable rule sequence (`EnglishProtoToOE`, PWGmcChanges expanded) | 83 named rules, positions 1–83 | identical |
| Cascade-relevant supported edges satisfied | 13 / 13 | 13 / 13 |
| Changed pairwise ordering relations | — | **0** |
| Total displacement from current order | — | **0** |

Every pair whose relation would change under the proposal: **none.**

### Why the "PNWGmc-before-PWGmc" permutation is not adopted

The interaction matrix (Phase 5 tooling) showed 117/143 PNWGmc×PWGmc pairs
commute and only 10 non-commuting pairs would be swapped by that permutation.
But computational non-commutation is not a historical edge, and none of those 10
swaps is licensed by a supported historical relation. Moving the PWGmc-block
rules after the PNWGmc rules would change pairwise relations with **no historical
warrant** and would risk the frozen output baseline for the sake of visual
tidiness. It is therefore rejected. Cohorts are set by adjudicated evidence, not
by the FST prefix.

## The correction set (derived from the audit table)

No cascade move is proposed. The following non-order corrections are:

### Renames (FST identifier misstates the stage; metadata already agrees)

| SC | Current identifier | Proposed identifier | Basis | Confidence |
| --- | --- | --- | --- | --- |
| SC003 | `PGmcRhotacism` | West Germanic rhotacism | R/T pp.52,98,102; Crist 2001/2002; Hogg p.37 | A |
| SC020 | `PGmcFinalZDeletion` | WGmc final-*z* deletion | Hogg p.37; Crist 2002 | A (name) |
| SC026 | `NWGmcNasalSpirantLengthening` | North Sea Germanic / Ingvaeonic | Campbell §121; Fulk §4.11; R/T pp.140–141 | B |
| SC027 | `NWGmcNasalSpirantLoss` | North Sea Germanic / Ingvaeonic | Campbell §121; Fulk §4.11; R/T pp.140–141 | B |

Renames are behaviour-neutral: they change no rule text, only the identifier (and
its references). They must be executed as a controlled migration (Phase 5/7),
not piecemeal.

### Metadata / prose only (stage ≠ cascade position, or scope over-claimed)

| SC | Correction | Basis |
| --- | --- | --- |
| SC012 | narrow `pan_wgmc → north_wgmc`; downgrade confidence A→B | R/T pp.170–171; Campbell §414; reader+report+dossier reject pan-PWGmc |
| SC016 | document that OE-WS stage sits early by FST dependency (before SC017) | Campbell §44; reader 016 |
| SC042 | present as a narrow model-shaped feeder before SC043, not a chapter | change report 042 |
| SC049 | document PGmc stage vs late position (after SC010) is an FST dependency | Hogg pp.101–102; R/T p.121 |
| SC050 | document Sievers'-Law feeder role before SC051/SC052 | Adamczyk 2001; Fulk §6.15 |

### Split candidate (granularity)

| SC | Correction | Basis |
| --- | --- | --- |
| SC004 | split the early Northwest-Germanic word-final `*ai>*ē` from the less-dated nonfinal `*ai>*ā` generalization | R/T pp.40–41; reader 004 |

A split is a substantive implementation change and must be validated with the
output baseline and witness review (Phase 7). No rename of SC004 until the split
decision is made.

### Deferred (historically unresolved)

| SC | Reason |
| --- | --- |
| SC064 | registry-internal conflict (`hist_stage=nwgmc` vs chapter 4/OE), confidence C; late cascade position is well-supported but the stage label is genuinely unresolved |

## Apparently misplaced rules deliberately left unmoved

- **SC016, SC049, SC050** — their cascade positions diverge from their historical
  stage, but each divergence is a documented computational dependency (glide
  before u-lowering; β-allophony after j-gemination; Sievers feeder before
  palatalization). Moving them would break the model; the fix is prose/trace
  clarity.
- **SC003** — pre-pipeline placement (in `PGmcConsonantRules`) with rhotacism
  scoped to non-final environments already achieves Crist's historical order
  effect without a move.
- **SC064** — position after OE high-vowel apocope is cross-source supported;
  only the stage label is deferred.

## Recommended next implementation change-set

Following the task's ordering (uncontroversial renames first), the first
implementation increment after approval should be the **four behaviour-neutral
renames** (SC003, SC020, SC026, SC027) executed as one controlled identifier
migration, validated by exact output equivalence (`outputs_sha256` unchanged) and
the full-cascade equivalence machinery. The SC012 metadata narrowing and the
SC016/SC042/SC049/SC050 prose/trace clarifications follow. The SC004 split and
the SC064 stage adjudication are separate, review-gated tasks.

No production FST reordering is proposed by this analysis.
