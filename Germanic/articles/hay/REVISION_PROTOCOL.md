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
| D-quantity | Implemented in Cycle 19; Increment A reviewed at `f1271db1` | Qualify the R5 ‘strew’ evidence separately, then distinguish quantity from regional vowel quality in R6. No new historical verdict, calibration run, or changes to the frozen derivations, Table 4 cells or the census. R7 and later blocks remain outside scope. |
| D-morphology | Implemented in Cycle 20 against `30a73f51` | Verify Hogg's R6 citation and qualify its transition; stage and develop R7 in four increments. Relocate the continental paragraph verbatim without implementing R8. Preserve all table cells, counts, frozen derivations and production inputs. |
| D-synthesis | Implemented in Cycle 21 against `c326fe7c` | Correct the R7 comparison and notation separately; stage R8 and compare H1–H5 in three increments. Explain the regional and continental evidence and return to the ‘bed’ contrast. Preserve the abstract, appendix, all table cells, census and frozen models. |

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

**Cycle 18 checkpoints:** `aa908fea` corrected the translation;
`c8fc3781` relocated the nonquantitative spelling discussion and staged
the anchors; `4c8764fc`, `e7644250` and `28f0e780` implemented the three
R5 pairs. All five were source-only; the publication commit carries the
matching PDF. The closeout compares each unit against its immediate
parent, verifies the relocation separately by conserving the moved
words and preserving the quantitative tail byte for byte, and requires
complete R5 coverage.

**Historical review (article only):** RETAIN the conditional derivation
to hiatus; DEFER a decision between final desyllabification and contraction,
and between secondary supply and protected-stem substitution. The
comparisons support distinct mechanisms but do not date their operation
in final /e.i/. No new SC, executable diagnosis, registry verdict,
chronology edge, new experiment or baseline change was warranted.
The production book and scientific graph do not consume this standalone
article; validation concerns the scoped source and standalone publication.

**Cycle 19 checkpoints:** `75cae3bb` qualified the early ‘strew’ glosses
and connected the contraction discussion to the later ‘glee’ comparison;
`436d48d7` staged R6 without changing prose. `f1271db1` implemented the
quantity test and Farman discussion; `a3097ef8` clarified that the short
controls are classified historically, not from observed synchronic
quantity. `52ab91ae` distinguished West Saxon high vocalism and tested the
metrical and later evidence before turning to the question of levelling.
All five were source-only and individually checked against their parent
and built. Closeout requires complete R6 coverage, a cumulative scope
check, rejection of an unauthorized earlier edit and pending R6 coverage,
and visual inspection of the standalone PDF in the publication commit.

**Cycle 19 historical review (article only):** Retain both short and long
mid vowels as possibilities for the earliest Anglian forms. Farman favours
length locally, and West Saxon quality favours protected vocalism under
early apocope without determining the Anglian source or the operation of
transfer. The bounded source checks refine the status of the disputed
R5 glosses and the assumptions of the Paris scansions without changing
the historical assessment. No production inputs or scientific
certification are involved.

**Cycle 20 checkpoints:** `a7f1c0b2` confirmed Hogg's phonology volume,
added §5.163 and narrowed the R6 transition. `ebf5d658` staged R7 and
relocated existing prose, including the continental paragraph. The four
increments are `3fd62f62` (donor question and ‘yellow’), `a3994295`
(‘meal’, ‘fat’, ‘tar’ and the reconstructed paradigm), `071e8ab0`
(census, datives and scope), and `737b49f4` (‘glee’ and the component
conclusion). `e32a2476` clarifies the case-verification denominator.
These checkpoints are source-only. The publication commit carries
the inspected PDF and requires complete R7 and cumulative scope.

**Cycle 20 historical review (article only):** Retain competing
directions of levelling. Ball and Stiles motivate direct-to-inflected
transfer under their proposed chronology; the rival account of
*melu* remains viable. The census supplies attested cells, not
prehistoric frequencies. Campbell's cross-lexical comparison supports
the plausibility of limited re-formation; neither Campbell, Brunner
nor Wright establishes an accessible donor that actually supplied
the Anglian palatal. E33 and E34 remain necessary and unestablished.
There is no change to the historical verdict, the frozen models,
production inputs, or certification.

**Cycle 21 checkpoints:** `4a912649` clarifies the structural comparison
with ‘glee’ and marks the reconstructed intermediate; `7e9cd58c` stages
R8 without changing prose. `586133bd` tests the competing Anglian
histories, `0a0cbd97` weighs regional and continental evidence, and
`6adee0ce` gives the chronological implications and conclusion.
`0ac98762` clarifies the phrasing of Boutkan's stem history and Dahl's
distinction between his general proposal and the printed derivation.
These checkpoints are source-only and were built and checked for scope
against their immediate parents. The publication commit carries the
visually inspected, matching 20-page PDF. Closeout confirms complete
R8 coverage, unchanged tables and protected prose, rejection of an
unauthorized earlier edit and incomplete R8, and no printed anchors
or unresolved internal references.

**Cycle 21 historical review (article only):** The introduction asks
whether the direct stem survived without analogy. The synthesis
distinguishes that open question (C11) from the defensible alternative
to obligatory vowel replacement (C10) and the resulting difference
in explanatory burden from ‘bed’ (C09, with E20). The charter supplies
a written match, not a pronunciation or ancestry test. The simplex
comparison stands independently. After rereading the complete article,
retain the distinct predictions and both directions of levelling;
defer actual survival, either premise of H2, and the general chronology.
Ringe and Taylor (2014: 44–53, 173), Boutkan (1995: 211–213,
435–436), Dahl (1938: 81–86, 97), Stiles (2013: 15–16), and
Hogg and Fulk (2011: §2.23) clarify the competing proposals without
changing the assessment. Dahl's different input (E30) is not the
consonantal starting point of the frozen comparison. There is no
new registry verdict, executable diagnosis, chronology edge,
experiment, or production baseline change.

| Fault test | What changes and what survives |
|---|---|
| Reverse the charter reading | Lose the written match for ‘hay’ (C05); independent direct simplex attestations and the case for C10 remain. |
| Reject final desyllabification | Lose H1 and the corresponding case for C11; retained hiatus lacks a secure spelling basis. H2 can still support C10 if both premises are defensible. |
| Reject final contraction | E33 fails, so H2 fails even if palatal supply is plausible. H1 remains separately testable. |
| Reject accessible and actual secondary palatal supply | E34 fails, so H2 cannot account for the glide even if final contraction occurred. H1 remains separately testable. |
| Weaken Farman's length inference | Lose the local preference for long-vowel histories; early Anglian quantity and the question of vowel ancestry remain open. |
| Motivate another source of West Saxon high vowels | Reduce the advantage of protected vocalism there; neither the high-vowel evidence nor the independent Anglian argument is lost. |
| Reject the direction inferred from Ball and Stiles | Weaken the mass-noun argument for outward levelling; the attested cells, competing donor possibilities, and phonological alternatives survive. |
| Show the continental ungeminated forms to be secondary | Lose their argument against late apocope, not the English comparison between the Anglian vowel and the surviving geminate of ‘bed’. |

If both H1 and H2 fail, withdraw the positive alternative under C10
and narrow C09 to the difference in regular predictions. The written
findings, the derivation to hiatus under the specified input and order,
and the limits of quantity and morphology remain. E33 and E34 are
independently necessary and neither is established.

## Cycle 22: comparative framing and publication review

Against `43332f9f`: F1 (`aad51ae0`, `e1d5053f`) restores the comparative
motivation and separates the primary survival question from its fallback.
F2 (`578aed3f`) returns to that comparison in the synthesis and conclusion.
A (`be2b7020`) revises the abstract and checks its YAML field as P-abstract;
B (`2385e964`) completes the appendix anchors and verification conventions.
C documents the continental glosses (`3c7f8afb`), separates Boutkan's oral
chronology from Hogg and Fulk's and restores a reconstruction marker
(`5c1895d1`), cites the prose Paris Psalter edition (`eb3731f4`), and removes
an active duplicate bibliography key (`3633f061`). These were source-only
checkpoints, built and checked against their immediate predecessors.

The historical verdict and dependencies are unchanged. Frozen SC047 gives
direct ‘bed’ as A *bede*, B2 *bedd*, and dative *bedde* in both; independently
attested English protected forms are possible donors, not proof of transfer.
A still gives ‘hay’ as *hei* with syllabic final *i*. Neither proposed
continuation is an executable or certified result. Reversing the charter
reading loses corroboration but not the independent Anglian argument.
Rejecting desyllabification loses the regular-survival hypothesis; rejecting
either final contraction or actual palatal supply independently defeats
limited restoration. If both paths fail, withdraw the positive case against
obligatory replacement. If continental singletons are secondary, withdraw
their support for early loss without changing the lexical result for ‘hay’.
No historical stage, chronology edge or production input changed.

**Apparatus.** The 17 notes and seven tables keep the premises in prose and
source details retrievable. The continental gloss locators and editorial
status follow the frozen source audit and lexical ledger, not fresh
manuscript collation. No relevant Heidermanns citation was securely
identified. Hofmann (1970: 95–108) supplies a pertinent regional comparison
for ‘fen’, but its case, gender and regional caveats make it unnecessary to
the limited ‘bed’ comparison. Both Eadwine image links responded; the Paris
and Vitellius endpoints denied or failed access on recheck. The folio
locators and earlier verification statuses remain. Tables 2 and 7 make the
principal spellings and source distinctions checkable; Table 6 gives the
census, not a reproducible row-level export. A cleared occurrence-level
supplement would help an independent reader reproduce the totals, but is
not required to assess the principal historical argument.

**Editorial assessment.** The paper is a credible specialist-journal
submission after a controlled prose pass. Its contribution is not discovery
of *heiweg* or proof of a new sound law, but connecting that known spelling,
omitted in Ringe and Taylor's principal treatments, to an independently
motivated hiatus prediction. The simplex, quantity and morphology sections
then test distinct questions: what belongs to the direct cell, whether
quantity can discriminate, and what could be transferred. The conclusion
answers the opening comparative question: the apparent disadvantage of
early apocope is diminished, not eliminated. Regular survival is the
stronger, unresolved result sought; inherited vocalism with secondary
palatal supply is a separately motivated fallback. A referee's strongest
objections are the lack of an exact final /e.i/ control, the absence of
direct evidence for actual palatal transfer, and the uncertain inherited
direct ancestry of the continental glosses. These limit the inference
rather than break it.

Approximate counts, including in-text locators but excluding headings:
8,750 main-text words (introduction and derivations 1,020; attestations
1,850; phonology and quantity 2,590; morphology 1,810; synthesis,
chronology and conclusion 1,500); abstract 178; notes 1,160; tables and
captions 1,060; appendix prose 300; references 1,160. The phonological
documentation is the largest share and generally earned; repeated summaries,
rather than primary controls or manuscript notes, offer the clearest savings.
Keep the current title for this publication. Of the alternatives, “Old
English ‘hay’, paradigmatic levelling and West Germanic chronology” best
signals both the mechanism and the stakes, at the cost of length. “Old
English ‘hay’ and the chronology of West Germanic nasal apocope” is more
direct but may promise a decision; “Old English ‘hay’ and the evidence for
early nasal apocope” risks implying that ‘hay’ independently dates the loss.

**Closeout.** All 45 planned units are implemented; cumulative scope,
four negative guard cases, 58 distinct citation keys, 17 notes and unchanged
table cells passed. The standalone build reported no unresolved references.
Visual proof covered all 21 pages, including the continuation headers of
Tables 3 and 7, notes, links and bibliography. The publication commit
carries the inspected bytes. No private material or production changes
are included.

### Proposed Cycle 23 structural and rhetorical consolidation

Plan only. Use the Cycle 22 publication (`bf9194f3`) as the manuscript
baseline. The objective is to make each passage do one identifiable job
for the reader, not to make the prose sound more like the author. Keep
the title, evidential order, stable unit IDs and historical dependencies.
The cross-references below identify where the evidence belongs; they do
not enlarge the edit scope of an increment.

| Order and priority | Units | Reader problem and proposed operation | What must survive; risk to check |
|---|---|---|---|
| 1 · High | P-char-verdict, P-char-close | Two verdicts make the charter argument seem to restart after the composition test. Put the lexical preference and its grounds in P-char-verdict; use P-char-close for the bounded exact-match comparison and the reason to turn to case-assigned simplex forms. Leave P-char-compound as the test of stem ancestry. | C04–C05 and E10: Sweet's reading, the converging contextual and spelling arguments, the Worcester contrast and `early-hei` note. Preserve the rival in P-char-phon and the protected first-member possibility. Risk: making an exact written match a quantity, pronunciation or ancestry test. |
| 2 · High | P-hiatus-result, P-quantity-test | The same short/long predictions are introduced on both sides of the section break. Let P-hiatus-result close with what each history inherits; let P-quantity-test state what independent length or shortness would exclude and move directly to the witness evidence. | C06–C07, H1–H3; keep the phonological demonstrations and Table 3 in P-hiatus-glide/P-hiatus-contract, the Ritt/Aldred distinction in P-quantity-test and the Farman calibration in its own unit. Risk: treating absence of length marking as shortness or a conditional prediction as an attested quantity. |
| 3 · High | P-morph-census, P-morph-scope | The datives are introduced twice before the reader learns what they can discriminate. Keep their substantive demonstration in P-morph-census; have P-morph-scope begin with what overt and endingless datives allow without diagnosing transfer. Use P-compare-forms only for the consequence of that test. | E17–E19, E29, C08 and H2–H3; retain Tables 5–6, the `morph-case` note, Paris and Colloquy loci, overlapping dates and uncertainty of Farman's case. Risk: treating an ending as a stem contrast, frequency measure or date of levelling. |
| 4 · High | P-compare-forms, P-compare-failure | Repeated mini-derivations postpone the new comparison. Compare the candidates once against the shared spelling, quantity and grammatical constraints; make the next unit a counterfactual about what fails if gliding or either H2 premise fails. Refer back to §§3.2 and 4.3 instead of repeating the demonstrations. | C05, C07–C08, C10–C11 and E33–E34; retain the argument's independence from the charter, both necessary H2 conditions, and the distinction between Campbell's cross-lexical precedent and an actual donor. Risk: treating H3 as an automatic default or allowing C10 to survive rejection of both inherited-nucleus routes. |
| 5 · Medium | P-compare-regions, P-compare-bed | §5.2 should use the regional findings to distinguish histories rather than restate the diagnostics, and §6 should explain how those histories affect the chronological comparison. Review whether the §5.2 heading still aids navigation after tightening; retain it unless the regional contrast remains equally visible without it. | C07, C09–C10, E20 and H3–H5; §3.3 owns Farman's local length inference and the West Saxon quality evidence; §6 owns the *bed* gloss note, conditional singleton ancestry and Boutkan alternative. Risk: reading regional spelling as evidence for distinct early orders or counting analogies as if that settled chronology. |
| 6 · Final alignment | P-abstract, P-conclusion | Keep the abstract intelligible on its own; make the conclusion answer the opening comparative question rather than reprising the whole paper. Check both against P-thesis without reopening it. Change only where the earlier consolidation makes a sentence redundant or weakens the signposting. | C01–C05, C07, C09–C11 and the discriminating evidence proposed in P-conclusion. Keep regular survival possible, limited restoration conditional, and the objection to early loss diminished rather than eliminated. Risk: promoting possibility to proof or turning a criticism of obligatory replacement into a verdict on West Germanic chronology. |

Keep the worked introduction, charter rival, Paris scansions and ‘glee’
comparison unless the review identifies a specific structural problem.
In each increment, examine paragraph joins and repeated question-openers
before changing headings. Trim a repeated qualification only where the
reader can still recover its warrant from the definitive passage. Validate
one or two units against the immediate parent, build, commit and push
before proceeding. At closeout reread the revised opening and ending
together, run the Cycle 22 fault tests, and check that all seven tables
and evidence locators survive. Defer vocabulary, syntax, cadence, register
and habits of disagreement to the separately authorized author-specific
pass; do not invoke or develop Nathanification as part of consolidation.
