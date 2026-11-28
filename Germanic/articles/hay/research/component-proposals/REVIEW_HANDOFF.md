# Component proposals and short ‘hay’ — review handoff

The research assignment is complete through historical and production-adoption
review. The recommendations below are independent. None changes the released
models, targets, article or PDF.

## Production and separate research decisions

| Component | Recommendation | Basis and gate |
|---|---|---|
| [SC083 foot guard](SC083.md) | **Advance to formal adoption review.** | The bounded `FootCtx` repair preserves the three frozen orders, including protected roots, while permitting genuine unstressed contraction. It guards the existing one-pretonic marking convention, not a general historical prosody model. The isolated upstream ‘love’ discrepancy and A/B2 prefixed development endpoints are not SC083 fixes. |
| [SC085 marker handoff](SC085_HANDOFF.md) | **Optional equivalent refactor only.** | The contiguous replacement has the same upper domain and mapping; the three-order replay also agrees. A later stripping site is a different proposal and requires an approved consumer and a new equivalence or impact claim. |
| [Medial singleton labiovelars](MEDIAL_HW.md) | **Historically supported; defer production.** | Singleton reduction can feed singleton dorsal loss in the developmental ‘see’, ‘lend’, and ‘filter’ paths. Freeze genuinely independent, exact cellular positives and voiced/final retention controls, admitting any affixes rather than scoring the bare stem against a prefixed witness. Later contraction is independent. |
| [Medial geminate labiovelars](MEDIAL_HW.md) | **Experimental.** | ‘Strainer’ retains the dorsal after the separate reduction; its nucleus and inflected forms are unresolved. Keep separate from singleton loss; require exact geminate witnesses and an independent negative. |
| [SC086 `CtBrAe` and `CtBrE`](SC086.md) | **Restricted historical review; defer adoption.** | Exact local positives justify considering the broken-front arms independently. Frozen non-firing, even over three orders, is not a negative panel; require independent retention and contraction witnesses with exact weak vowels. |
| [SC086 other arms](SC086.md) | **Marked parity and twins experimental; defer general high-vowel absorption.** | Keep the three overlays independent. ‘Fringe’ and the exact ‘clay’ and Anglian ‘see’ states constrain generalization; unsupported rounded or lowered proxies cannot settle feeding. |
| [Corpus](CORPUS_EXTENSION.md), [labial stems](LABIAL_STEMS.md), [early nuclei](EARLY_NUCLEI.md), [representation](STAGE_ENTRY_REPRESENTATION.md) | **Separate research, no migration.** | Review exact weak vowels, quantity in ‘claw’, and direct versus renewed cells; then address early nuclear formation versus later regional realization. Document stage-level alphabets and consumers before extending typed light/heavy nuclei, stress assignment, or entry routes beyond the local proof of concept. |

Any later adoption needs its own adjudication of the actual production change;
the accompanying records are proposals, not registry verdicts or publication
certificates.

## Historical and editorial decision

The strongest publishable claim is positive but conditional. **If independent
comparative evidence places apocope early, the inherited ungeminated direct
singular regularly reaches short *he.i* after labial loss, without invoking
transfer from an oblique.** Final consonantal desyllabification would give
short *hej*: an economical continuation if independently applicable, not a
demonstrated OE sound law. The Vespasian ⟨heg⟩ is compatible with it, but the
independently long ⟨leg⟩ and short ⟨weg⟩ make the spelling non-diagnostic of
quantity. Farman's evidence is local; West Saxon high vocalism supports the
protected type there, not the date or mechanism of transfer to Anglian.
Keep long direct histories and transfer on the table rather than preferring
shortness for the surviving Vespasian token by model fit.

Inherited mutated ‘river’ obliques are better supported than an otherwise
unmotivated early replacement and are adverse to uniform final short
gliding. A distinction by time of hiatus creation is independently
credible; it requires new evidence to date **resolution** inside that
interval. Evidence that would change the judgment is an independent,
quantity-secure short final front sequence of the same relative age that
demonstrably becomes consonantal or remains hiatal; an independently
controlled quantity or nuclear analysis for Anglian ‘hay’; or positive
morphological evidence that the actual mutated ‘river’ oblique is renewed.
Additional ⟨eg⟩ spellings alone cannot do it.

Recommend historical review of the [versioned argument](HAY_EDITORIAL_PROPOSAL_V2.md)
and [editorial change table](argument-proposal-v2.tsv), independently of
production adoption. Keep the existing article and model in place. The
[priority supplement](SCHOLARLY_PRIORITY_SUPPLEMENT.md) separates established
precedents, new comparisons and unestablished generalizations.

## Execution and identities

All seven receipts bind the FST source, corresponding Python runner,
compiled networks and canonical/A/B2 order identities. A1–A4 include
wide comparisons against archived and active captures; B2–B4 use
explicitly scoped local controls. Their frozen
production reference is `113101ac5f169b589e1a9647cdf24d32cdd4d919`, not the
tip of this research branch. The launcher also pins first-cycle tools to
`f220d31157eaa10fcb9a3785ac349bdfac8d6c22` and cycles two/three to
`5a480e470c19c8877d23b428bad89772f22192d3`.
Start with the [cache instructions](../hiatus-cycle4/PROSPECTIVE_STACK.md#identity-and-question)
inside the Compose backend (Foma `0.10.0alpha`), then run the
[private launcher](../hiatus-cycle4/run-container.sh) from the root as
`bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh MODE --stage-cache "$cache"`.
Use `set -o pipefail` and `gzip -n -9` if saving a receipt. Compare structural
traces, not elapsed times or compiled binary byte hashes.

| Mode | Receipt stem (`-traces.json.gz`) | SHA-256 of recorded receipt |
|---|---|---|
| `sc083` | `sc083` | `fdef0b834262641061ca4546ca004b6cd10ccc0756f659a0b5af393c6f5d8552` |
| `sc085_handoff` | `sc085-handoff` | `91fc66557a95a835d38fd6b6e0fb46d17c37a2f9386795c1cdd4c0d7910ca3c8` |
| `medial_hw` | `medial-hw` | `ded112bd5f5aed73d79debb98d1b4e5e031443d7f39d268da70b8307cc0b333d` |
| `sc086` | `sc086` | `38d99e76b1dfbc450342f2ff5b739f0ddf5c2a6350e550e2aa2373c18712fbae` |
| `labial_stems` | `labial-stems` | `f28f179787a40a27f724824d31783816320a18afdd8239b5f61871cf667debd1` |
| `early_nuclei` | `early-nuclei` | `1022c51f2b77e86d84c7cf98a3a3b7714ac446447ba527948ba6b472713b8c17` |
| `stage_entries` | `stage-entries` | `465b64a9912c54d6b793a4d94522426c0994613edd2e446696f9939d443cb0a2` |

The complete change set since `d4df5c97f4e690300b2987222854992270046d6b`
is confined to this proposal directory, the opt-in fourth-cycle launcher and
the fourth-cycle research outline (the corrected ‘flock’ chronology).
In particular, the Canterbury dossier, canonical/A/B2 captures, frozen
research receipts and panels, source models, target corpus, benchmarks and
certificates have identical tracked contents. The maintained DRAFT,
ARGUMENT_CYCLE13, OUTLINE_CYCLE13, derivations, bibliography, build record
and PDF also match `bf9194f3c5bce2f767e447dbfb305ed57c8312e2`.
PDF SHA-256: `75968371a1fcc8d998c41afabb33c10e6ba7a9d3d7431c86956bc569fcb3d335`.
FST SHA-256: `43188e9a8e5bcbd028043675586c6655f81394beba55f0a4bb4044792db4050f`.
PR #21 remains open against `update` at the pinned head above.
These are research replays and protection checks, not fresh strict validation.

## Chronological commit ledger

| Commit | Increment |
|---|---|
| `83a9ba90` | A1 — SC083 foot guard |
| `5b32d419` | A2 — SC085 equivalent handoff |
| `95834944` | C1 — Independent desyllabification evidence |
| `7c95dd1b` | A3 — Medial labiovelar branches |
| `7cbaa8e9` | C2 — ‘River’ morphology |
| `a623d10f` | A4 — Narrow SC086 components |
| `54abbb35` | C4 — Vespasian quantity controls |
| `3625c9c7` | C3 — Relative chronology |
| `2e69b36e` | C5 — Comparative histories |
| `8c11f539` | C6 — Prospective argument model |
| `62eedeb5` | B2 — Early labial stems and quantity |
| `c9e8aecb` | B3 — Early nuclei and dialectal merger |
| `7eb04397` | B4 — Stage-aware entry and consumer audit |
| `05e5ec57` | B1 — Corpus-extension tranche |
| `f614eec4` | Scholarly priority supplement |
| This commit | Review handoff and protection checks |

Stop here for historical and production-adoption review. No corpus
migration, actual article revision, Cycle 23, or Nathanification follows
from this handoff.
