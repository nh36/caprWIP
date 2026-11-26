# Controlled revision protocol

Start with the [baseline](BASELINE.md), [thesis](THESIS.md), and
paragraph ID. Open a concise change proposal in the review of the patch,
not a new comprehensive memorandum. Specify **problem; layer; IDs;
proposed change; dependent claims, paragraphs and apparatus; evidence
or editorial warrant; invariants; status** (proposed, accepted, or
rejected). Record consequential accepted/rejected decisions below with
their review or commit reference; Git retains earlier versions. A
proposal does not authorize implementation. Never silently reuse an ID;
if one is retired, record the reason and any successor, then update all
live references together.

| Change class | Required propagation and stopping point |
|---|---|
| New evidence | Record provenance and verification; update the evidence record first. Trace its proposition, reassess dependent arguments, histories and thesis as needed, then change only affected architecture, paragraphs, prose and apparatus. Do not run broad acquisition by default. |
| Historical disagreement | Name the proposition, state the competing account, weigh positive and contrary evidence under the [Germanic protocol](../../docs/RESEARCH_ADJUDICATION_PROTOCOL.md), trace consequences, record the adjudication, then propagate accepted changes. Preserve unaffected evidence and settled conclusions. |
| Rhetorical defect | Name the reader's missing premise or transition. Revise architecture and affected paragraph/notes first, then the approved passage. Compare historical claims, certainty and references against the model; a different thesis requires separate review. |
| Stylistic defect | Change expression only. Preserve purpose, paragraph role, factual claims, warrant, citation, qualification, notation and argumentative order. Any evidence addition or deletion, or change in certainty, belongs in a different proposal. |
| Publication fault | Correct notes, tables, references or typography, then rebuild and check affected material and layout. Do not re-adjudicate history to fix a publication error. |

For each authorized editorial assignment, revise at most two substantive
argumentative units per increment. Identify the units and their evidence
and apparatus before writing. Read each revision in context, check the
claims, citations and scope, and run structural and publication checks.
Commit and push each completed increment before starting the next one.
Record the parent, scope, resulting commit and PDF status. Keep mechanical
relocations and corrections to completed units in separately scoped
commits. Do not squash checkpoints or treat them as individual owner
approval. Label a checkpoint without a matching PDF as source-only.

Use `python3 Germanic/articles/hay/validate_exposition.py` for structural
and source-anchor checks. Add `--against <parent>` and a `--scope <ID>`
for each authorized block or unit to verify protected source and frozen
table cells. With no scope, the source must match exactly. Use standalone
`<!-- P-id -->` comments for implemented units and `<!-- pending:P-id -->`
for staged, unimplemented slots. Pending slots must form a trailing
sequence within a block; a slot already implemented in the comparison
revision cannot return to pending. Require `--complete <ID>` for the
block at closeout; extend the section map when more blocks are authorized.
`--trace C05` (or any proposition/paragraph/apparatus ID) lists
forward and reverse relations. Required edges and alternative branches
are distinct from supporting evidence: inspect the prose before
interpreting a reachability hit as a consequence. Human review checks
whether the claim, warrant and scope actually follow, whether the
paragraph still does its assigned job, and whether something silently
disappeared. Structural validation is not historical validation.

## Local prose handoff

For any future, separately approved use of Nathanification, provide just
the named section and paragraph IDs, rhetorical purpose, approved
sequence, upstream proposition texts, mandatory claims, evidence and
page-specific citations, limits and counterevidence, conventions (observed
⟨letters⟩, starred reconstructions, `>` for sound change, separately
labelled substitution), neighbouring argumentative context, and the
present passage if relevant. Compare the output clause by clause with
that packet: reject invented evidence, missing qualifications, changed
order or claims, and unsupported interpretation. Keep private writings
in the existing authorized local environment. This cycle does not invoke
that repository, copy writings, or transform any published passage.

## Decision record

| Decision | Status | Scope and invariants |
|---|---|---|
| D-architecture | Approved in principle by owner in Cycle 15, with amendments | R0–R9 and paragraph plan; only R1–R2 authorized for implementation now. Include E32, preserve the primacy of the survival question, and give argumentative units nonprinting anchors. Later blocks require separate authorization. |
| D-baseline | Accepted in Cycle 14 | Preserve `326fa7e6d6ceba85351249c22c2a464490e6b0e4` as editorial baseline. No historical adjudication, frozen model or scientific dependency change. |
| D-introduction | Implemented against `7c37478701b2b3e70f25d8a9a81316c370b3636e` | R1: order → direct/protected trade-off → ‘hay’ predictions → E32 and the written record → survival and the fallback claim. R2: retain all frozen table cells; distinguish hiatus from dialectal endpoints and morphological replacement; move notation detail to N-trace-notation. Map E32 to future P-char-reading without changing its prose. Mark E33 and E34 jointly necessary for H2, not established or necessary for H1. Preserve all prose outside R1–R2 and defer Nathanification. |
| D-charter | Authorized in Cycle 16 against `a81760edf7110b8ea6fde2e8568e6388f6fa49d3` | R1–R2 provisionally approved and protected. Move simplex behind charter without rewriting; consolidate the charter and composition passages, then implement the eight R3 units as four separately validated and pushed pairs. No new historical verdict. Each checkpoint records its parent and scope in its commit. |
| D-simplex | Implemented in Cycle 17 against `4237e0ea` | R3 approved subject to three scoped corrections. In R4, distinguish secure case assignments, regional written targets, and Eadwine's observed readings from conventional normalization. Preserve Table 2, Appendix A, the census and historical assessments. R5 remains outside scope. |
| D-hiatus | Authorized in Cycle 18 against `177dc5a9` | Correct the Vespasian translation separately, relocate nonquantitative spelling evidence, then implement R5 in three pushed pairs. Preserve R6 and the frozen record. |

**Editorial review of D-introduction:** The direct geminate in ‘bed’
now explains why analogy is at issue before any spellings of ‘hay’
appear. The two paths predict different inherited material, not a
dialectal anomaly under Ringe and Taylor's account. The charter's
letters motivate the survival question but neither prove it nor
make the Anglian argument depend on it. The derivations end by naming
what would have to be shown about the recorded vowel and palatal,
not by treating a modeled stage as a written pronunciation.

**R3 checkpoints:** `1bd34554` moved and renumbered the existing material;
`edce076c` established the reading and positive case; `4328b85f` tested
‘highway’ and footnoted the enclosure alternative; `34b4f1ae` separated
documentary and lexical considerations; `458d0e5d` evaluated composition
and exact spellings. All five were source-only. The editorial correction
`49ab33a7` checks P-char-compound and P-char-close against `458d0e5d`
and all of R3 against `1bd34554`. The publication commit carries the
rebuilt and inspected PDF. The whole-section review
confirms that the lexical preference does not rest on avoiding a dating
anomaly, that the protected stem is a live alternative, and that the
compound cannot identify the direct case. No historical proposition
or source-verification status was changed.

**Cycle 17 checkpoints:** The charter corrections are `d421b21a`
(attribution and phonological contrast) and `230ef043` (transition).
`c89c16e1` staged the R4 anchors without rewriting prose. `8468a688`
established the principal direct witnesses and spelling distribution;
`f1791b66` distinguished Eadwine's manuscript evidence from the normalized
form. `01e96c1c` aligned the case note and Table 2 with the arguments they
support. All six were source-only; the following publication commit
carries the matching PDF. The editorial review found no basis in these
spellings to revise the historical model.

**Cycle 18 source finding (E14):** Table 3 formerly glossed Vespasian
*gecēd* as ‘calls’. Campbell §237.1b and Ringe and Taylor p. 260
distinguish the participle from the finite *gecēð*. Sweet (1885: 416)
prints *bist geced*, glossing Latin *vocaveris*. The corrected participial
gloss leaves E14's evidence for nonfinal contraction before a dental
unchanged. Pheifer §59.2 n. 1 and Hogg §5.133 n. 2 also allow an
alternative lexical identification for the early ‘strew’ glosses;
the prose now makes those spellings conditional evidence for E11.
