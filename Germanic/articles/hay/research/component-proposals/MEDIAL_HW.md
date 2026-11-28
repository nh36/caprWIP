# A3 — Medial labiovelars: separate the labial from dorsal loss

## Identity and question

Private Old English candidate at `113101ac`. Is loss of *w* after an
intervocalic dorsal independently warranted beyond ‘see’, and does the
geminate undergo a related delabialization without losing its dorsal?
Initial, final, voiced and already delabialized states are controls.

## Current state and exact candidate

There is no incumbent medial devoiced dorsal–labial rule at the
tested position. `OEPostVelarWLoss` targets `*n*g*w`, not `*x*w`;
`OEHLoss` targets a **singleton** dorsal between vowels, not the
labial. Its original `FootCtx` and marker stripping are retained.
The experimental position is before `EAFBrighteningUnstressed`,
which makes the eventual breaking and dorsal-loss trajectories
visible. Two physically separate candidate definitions allow
ablation of quantity independently:

```foma
define HwMed [{*w} -> 0 || EnglishStarVocalic {*x} _ EnglishStarVocalic];
```

```foma
define HwGem [{*w} -> 0 || EnglishStarVocalic {*x} {*x} _ EnglishStarVocalic];
```

## Diagnosis

The [receipt](medial-hw-traces.json.gz) has matched baseline, singleton,
geminate and joint arms. All 394 archived and 396 active endpoints
match P0 in each order; neither new definition has **any** frozen-wide
firing, intermediate difference, or surface change. The empty
changed-form ledger is a coverage limitation, not corroboration.

| Local or full probe | Result and witness role |
|---|---|
| ‘See’, ‘lend’, ‘filter’: independently motivated singleton cluster | In each order `HwMed` deletes *w* on all three full submissions and their local counterparts. It feeds singleton *h*-loss. Full *seoan/līoan/sīoan* retain hiatus after successful cluster reduction, not completed *sēon/lēon/sēon*. |
| ‘Sieve’: source-based local geminate | `HwGem` takes `*s*i*x*x*w*ā` to `*s*i*x*x*ā`; later SC085 preserves the resulting `*x*ç` sequence. P0 *siohhwe* becomes *siohhe*. The remaining *io/eo* mismatch is in realization, not consonant quantity. `HwMed` alone does not fire. |
| ‘Arrange’ and ‘drain’ | Non-labial geminate and preconsonantal comparisons show no new *w* loss or lost dorsal. The direct endpoints are not assigned new corpus targets. |
| Initial ‘white’, ‘turn’ | Local negatives and admitted full ‘white’ retain *hw*. Full ‘turn’ fails admission; it is not counted as a negative firing witness. |
| ‘Horse’ | Edge-cluster probe *ehw* is invariant, as is separately injected published *ehu* before these rules. P0 eventually loses *h* on that latter input and gives *eou*, so the experiment does not yet explain the attested direct *eoh*. Neither probe can establish a rule for an original word-final unit labiovelar. |
| Voiced ‘filtered’ and levelled ‘lent’ | The *w* in the local voiced alternant of ‘filtered’ stays (*siowen*); ‘lent’ with levelled *ġ* is morphological evidence, not a historically identical input which failed to de-labialize. |

## Literature and historical analysis

Ringe & Taylor (2014: 48–50, 178–179, 315–317, 344–345) distinguish
the resolution of inherited unit labiovelars in West Germanic from
later positional histories. The exact font quantities in their *līhwan*
and *sīhwan* were checked from their held p. 179 in
[Cycle 4](../hiatus-cycle4/MEDIAL_HW.md). The full submissions
already represent PGmc unit labiovelars as starred sequences on
admission; they cannot test or date their earlier resolution.
In their published histories the three infinitives have already lost
their labial before deletion of the now-intervocalic dorsal, and
‘sieve’ has a labial-less geminate at the corresponding stage.

Seebold (1970: 327–328, s.v. *leihw-a-*; 389–390, s.v. *seihw-a-*)
supplies the comparative ablaut, including the voiced *w* grades,
plus independent OE, OHG and Frisian forms. Ringe & Taylor retain that
contrast in ‘filter’, but argue levelling for the velar in the ‘lend’
participle. Their ‘sieve’ noun is an inflectional/derivational family
member, not a second independent geminate root. The broader
laryngeal-loss conditioning is independently documented by Campbell
(1959: 186–187 §§461, 464–465). The exact two executable environments
are CAPR formalizations, not statements already tested by these authors.

In the singleton cases, de-labialization before singleton *h*-loss
is a **feeding** dependency on the reconstructed *hw* paths. The
particular pre-breaking insertion is **not** independently dated;
breaking witnesses with *h* and no literal *w* at the later stage
do not establish ordering relative to breaking. The related late
h-loss/contraction edge is independently motivated, but no new edge
with diphthong realization has been promoted. No permanent
lexical-origin tag or grammatical conditioner is proposed.

## Verdict

**RETAIN** narrow singleton delabialization as ready for independent
historical review; **DEFER production adoption** until attested
full paths and the wider stage/route controls are available.
**RETAIN EXPERIMENTALLY** a geminate counterpart: it supplies
the lost labial without losing the geminate, but is currently
backed by one derived family. A single quantity-neutral medial
generalization is plausible; the present evidence does not
establish that those applications are contemporaneous.
Propose no registry number, chronology edge, target, or input
migration until the scope and representation are reviewed.

## Propagation, validation and residue

The [entry proposals](medial-hw-entries.tsv) distinguish existing
development families, later entry, and blocked endpoint adoption.
A formal adoption must keep initial, voiced and geminate controls;
demonstrate actual firing on admitted historical inputs; handle
*ēo/īo* and the weak ending separately; rerun the current census
and complete the ordinary adoption and publication gates. No default
CI lane was added.

```bash
set -o pipefail
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh medial_hw --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay5-hw.json.gz
```

Use the [pinned cache warm-up](../hiatus-cycle4/PROSPECTIVE_STACK.md#identity-and-question).
Receipt SHA-256:
`ded112bd5f5aed73d79debb98d1b4e5e031443d7f39d268da70b8307cc0b333d`.
