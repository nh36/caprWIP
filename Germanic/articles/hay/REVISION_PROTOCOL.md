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

Use `python3 Germanic/articles/hay/validate_exposition.py` for structural
checks; `--trace C05` (or any proposition/paragraph/apparatus ID) lists
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
| D-architecture | Proposed for owner review | R0–R9 and paragraph plan; move lexical and morphological evidence only after the question it answers. Preserve the historical conclusions, verified derivations, seven tables and documentary evidence. |
| D-baseline | Accepted for this infrastructure assignment | Pin `326fa7e6d6ceba85351249c22c2a464490e6b0e4`; published prose and PDF stay unchanged. No historical adjudication, frozen model or scientific dependency change. |
