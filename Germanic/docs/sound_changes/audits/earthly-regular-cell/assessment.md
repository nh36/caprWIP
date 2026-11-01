# Earthly: regular-cell research assessment

## Identity

SC identity: n/a. This is a lexical investigation, not a newly opened
sound-change adjudication. Existing SC040 is relevant; no fictitious SC
number, registry verdict or completed controller workflow is created.

Executable identifiers: current `OEMedUnstressedULowering` and private
`RFoot`/`RLate`; the names identify networks, not independently proved
historical stages. The private r-syncope and final-prominence sensitivities
are experiments, not approved sound laws.

Research date: 1 November 2026. Branch: `research/earthly-regular-cell`.
Initial clean research HEAD and verified `origin/update`:
`8f7713c39f26a7f81ef04d29d54070f1b83ab0e0`.
The dedicated worktree is
`.capr-work/worktrees/earthly-regular-cell`; production remains in its
separate original worktree.

## Question

Can one complete, independently defensible inherited adjective cell produce
an OE earthly witness through regular phonology, without deriving the entire
paradigm, altering protected histories or conditioning a rule on the lexeme,
suffix or case?

Independent formation and ending evidence, the complete derivation and
comparable phonological controls can support a regular-cell hypothesis.
An incorrect ending, unsupported stress assignment or corruption of genuine
in-domain controls would refute it. Successful spelling alone cannot establish
the grammatical identity or attestation of a cell.

## Current state (before any edits)

The selected corpus contains 390 OE entries, with 382 correct outputs and
eight standing mismatches: 1973, 2013, 2030, 2162, 2224, 2240, 2298 and 2300.
Earthly is not selected. Row 2335 is filth; 2336 is unallocated at this base,
not reserved by an old directory name.

The unmodified cascade accepts `*érθa-kùnðas` but predicts *eorþcondes*.
Linking-vowel syncope and inherited-accent removal already occur before
the late lowering operation. The input's grave is an explicit compound-
accent assumption, not a surviving OE stress measurement.

The registry and current historical staging projection record
`hist_stage=oe`, `hist_scope=english_specific`, confidence `A`, with
`adjudication_status=unadjudicated`. Their characterization is: “Medial
unstressed u lowers after the earlier shortening and vowel-resolution
history; root u and following m preserve u. Youth remains a negative
application control, not current SC040-before-SC072 evidence.” The actual
operation is:

```foma
define OEMedUnstressedULowering FootCtx([
    {*u} -> {*o} || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]] [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
]);
```

The staging projection's position 87 and the assay's physical step 89 use
different inclusion/counting conventions; the assay explicitly includes
context/inline operations. Neither number independently dates the change.

The current SC065, SC066 and SC068 adjudications and physical definitions
have been read and freshly preflighted. None fires on the serious earthly
cells. The former research's feminine-ending failure cannot simply be blamed
on an obsolete SC066. Current SC040 source discussion and accepted
post-migration placement were also checked; SC040 is not yet adjudicated.

Both complete earlier earthly dossiers are preserved. Their successful
genitive experiment did not attest the target or establish the whole
adjective paradigm. Their literal-*n* ending diagnostics must not be silently
promoted into source-critical reconstructions.

## Diagnosis

The final assay is `earthly-8f7713c3-v11`, pinned to production FST SHA256
`ee259d1dac8d83508aca8f201b8fb042ab99245caf87d44ae050ec16c39d0ad7`.
It records seven models, 43 complete candidate/control inputs, every physical
stage for 390 selected and 380 original inputs, actual internal prominence/
lowering/decoding operations, composed-forward checks and formal functionality.

Every model preserves every selected and original-input final and aligned
physical-stage state. The ordinary prominence projection adds no annotation
to the selected corpus at SC040. The expanded final-overheavy sensitivity
transiently marks four selected forms, then decodes them without changing
their segments. These internal operations are recorded, not hidden behind
unchanged final outputs.

The complete current SC040 application census is the same under every model:

| Lexeme | Selected ID | Original-archive index (zero-based) |
| --- | --- | --- |
| hawk | 2060 | 326 |
| head | 2063 | 342 |
| heaven | 2068 | 345 |
| milk | 2126 | 159 |
| navel | 2133 | 165 |
| nine | 2142 | 173 |
| seven | 2174 | 257 |
| soul | 2201 | 247 |
| ten | 2242 | 277 |
| world | 2302 | 308 |

These are ordinary retained applications, not new lexical exceptions.
The machine evidence supplies every before/after string and every
nonapplication in both populations.

The original 380-input archive under the current cascade matches 366
historical targets and has 14 mismatches. This is not the active selected-
input 380 population and does not mean the experiment introduced 14 failures.
Both comparisons have zero experimental deltas; all original inputs remain
accepted and deterministic.

### Complete preferred weak-neuter trace

`weak-neuter-trace.tsv` gives all 109 stages for both models. The full
`*érθa-kùnðǭ` input is accepted by the unchanged production parser.
Dental hardening (17), linking-vowel syncope (45), the single inherited
accent strip (46) and breaking (54) establish the stem. Final nasal-long
shortening (85) changes `ǭ` to `æ`; unstressed merger (86) gives `e`.
At step 89 the unmodified cascade lowers medial *u* to *o*, whereas
computed medial prominence protects *u* and is immediately decoded.
Orthography (106) and rendering (108) yield *eorþcunde*; the final pass
(109) is unchanged. No SC065, SC066 or SC068 operation fires.

The complete ending is independently justified below. Its derivation
requires no extra parser coverage, inflectional substitution, invented
quantity reduction or additional ending/syncope rule.

### Complete fallback genitive trace

`genitive-trace.tsv` gives all 109 stages for both the current and ordinary-
prominence models. The genuinely changing developmental skeleton is:

| Physical step | Operation | Relevant result |
| --- | --- | --- |
| 1 | Input parse | The complete `*érθa-kùnðas` is accepted; both parsers yield the same starred symbols. |
| 17 | Dental hardening | `*érθa-kùndas` |
| 45 | Compound linking syncope | `*érθ-kùndas` |
| 46 | One inherited secondary-accent strip | `*érθ-kundas` |
| 51 | Unstressed ending brightening | `*-kundæs` |
| 54 | Breaking | `*éorθ-kundæs` |
| 86 | Unstressed merger | `*éorθ-kundes` |
| 89 | Current lowering versus computed prominence | Current `*-kondes`; the projection syllabifies and temporarily heads medial `*-kùndes`, protects *u* under unchanged lowering, then decodes. |
| 106 | Orthography | Surface dental and `c` representation |
| 108 | Star/stress rendering removal | Current *eorþcondes* versus experimental reconstructed `*eorþcundes` |
| 109 | Final pass | No further change |

The table abbreviates internal symbol spelling; the TSV and JSON preserve
the exact strings, including unchanged and rejected stages. Step 89 is the
first segmental divergence for this fallback input, not an inferred new
historical chronology edge.

The genitive is a live application of the computed medial-foot hypothesis.
Direct inflected *godcundne* and *godcundre* test the same medial *u* domain.
Uninflected *godcund* is a final-syllable control outside that ordinary
medial-foot projection, not a reason to claim the projection already derives
the whole suffix paradigm. World tests initial light-plus-heavy footing;
rainbow and soul protect their accepted histories. Separate light-flank,
long-vowel and absent-following-vowel controls test the limited r-syncope
sensitivity. Their exact roles and limitations are in
`prosody-and-cascade.md` and the machine evidence.

## Literature

The source-critical attestations, editions, grammatical evidence and
comparative ending authorities are in `attestation-census.md` and
`morphology.md`. Source searches and access failures are recorded separately
from verified readings. A dictionary lemma or a generated declension is not
a token; *eardcundes* is comparative evidence, not *eorþcundes*.
Three distinct loci are recovered, including the new R. Ben. dative plural;
the reported six-token DOEC concordance is not fully recovered. The
*eardcundes* citation's `Rtl.` siglum has not been independently established
as Rushworth: internal liturgical evidence instead makes the Durham Ritual
probable. It must not be published with an unverified Gospel attribution.

The prosodic review is in `prosody-and-cascade.md`. Hogg (1992/2011: 49–50,
§2.89), McCully and Hogg (1990: 323–333), Hogg (1996: 8–11) and Goering
(2023: 79–84) support examining constituent/inflection-dependent syllable
weight and medial prominence. The exact inherited grave, maximal-onset list,
five-short-vowel annotation inventory and network implementation are CAPR
modelling assumptions, not printed reconstructed words or a complete
authorial OE stress grammar.

Ringe and Taylor (2014: 264–265) and Campbell (1959: 159–160, §§388, 392)
motivate re-examining ordinary pre-liquid syncope. They do not independently
license every detail of the private late r-syncope insertion. The older
McCully–Hogg direct-reading record is reused with its original identity;
fresh access to its previously held PDF was unavailable, explicitly not a
new page-image verification.

## Historical analysis

The candidate formation/cell is a PGmc reconstruction hypothesis; the
computed prominence belongs to the OE phonological question. Neither its
stage nor its genealogical scope is inferred from a network prefix or from
the container's directory. Gothic and OE correspondences support comparison
without proving that every productive *-cund* formation is the same inherited
lexeme or that the exact accent sign is directly attested.

The ordinary experimental protection is phonological: an eligible nonfinal
heavy syllable can head a medial foot after accommodation of the initial
foot. It does not test suffix identity, grammatical case or lexical identity.
Its limited onset and vowel coverage must be retained as limitations. The
single-onset sensitivity does not alter the serious genitive result.

A blanket dental-nasal exemption is not supplied by Hogg's labial-nasal
discussion; ordinary *-un* lowering is an objection to inventing one.
Preserving the inherited grave until late lowering is not reconsidered:
independently computed OE prominence and technical decoding are distinct
from the one historical annotation-removal operation.

The Oxford *u* and its inflectional vowel are separate issues. Ordinary
prominence yields *eorþcundere* from the experimental `*-aizōz` input. The
additional general r-syncope slice yields *eorþcundre*, without changing
SC065/066/068. That is a genuine new computational result, not proof that
its full morphology or exact late chronology is settled. The `*-izōz`
alternative gives *y* through umlaut and cannot simply be substituted for
the preferred stem vocalism.

Genesis is now grammatically better founded: *eorþcunde* agrees with neuter
*eád* as weak accusative singular, and the absence of an overt specifier is
licensed by the independently described poetic use of weak adjectives
(Fulk 2018: 216; Campbell 1959: §638). It is not the earlier experiment's
strong feminine accusative. Fulk's weak-adjective/n-stem bridge
(2018: 168 n.1, 169–170 §§7.29–7.31) independently supplies the complete
OE-relevant bimoric nasal ending `*-ōⁿ`, attached to the unaugmented
compound stem, not an inserted oblique `-an-`. Inspection of the original
printed glyph confirms the macron. CAPR `ǭ` faithfully represents this
quantity, so `*érθa-kùnðǭ → eorþcunde` is a complete executed derivation.
Fulk's preceding masculine trimoric-origin problem is separate; it does
not require an invented 3-to-2-mora transition in this neuter cell.
His inherited PIE account supports regular morphology; the cited Boutkan
alternative derives the ending by analogical extension from the neuter
plural. Retain that competing prehistory: executable success does not
decide between them or establish every n-stem ending.

The rejected `*érθa-kùnðôⁿ` trial arose from a superseded source
misreading, not Fulk's actual OE-neuter ending. Its authentic v10 label
and rejection remain archived; v11 corrects the label without changing
the compilation or any prediction.

The newly recovered prose *eorþcundum* is masculine dative plural by
agreement with *lustum*. Its OE ending is uncontroversial synchronically,
but that is not a successful inherited *-aimiz* history. Production rejects
the full input. A private generic ending with the canonical single `*ai`
symbol yields *eorþcundem* and the matching *godcundem*, not *-um*.
The stem's retained *u* is solved by prominence; the ending remains a
different phonological/morphological question. No analogical account is
invented merely to declare this failure regular or irregular.

No analogy is invented to explain the fallback genitive merely because
that cell is unattested. Documentary absence is not phonological irregularity.
Specific remodelling questions for attested cells remain governed by the
grammatical evidence, not by success or failure of a serialization.

Chronology edges: n/a to promotion in this lexical study. Existing accepted
positions are retained. The experiment records physical ordering and
nonfirings, but supplies no independently demonstrated new historical edge.

## Verdict

### Comparative cell decision

| Cell and documentary status | Full input/ending authority | Inflection and regularity assessment | Current / experimental complete prediction | Required change or remaining doubt |
| --- | --- | --- | --- | --- |
| Genesis A 1627 *eorþcunde*, attested through dictionary and Thorpe's edition OCR | `*érθa-kùnðǭ`: bare compound stem + Fulk's OE-relevant bimoric nasal `*-ōⁿ` (§§7.29–7.31); whole accented compound assembled, not printed by Fulk | Weak neuter acc.sg; poetic syntax and inherited n-stem account independently supported; Boutkan's alternative origin retained | *eorþconde* / *eorþcunde* | General medial prominence only; manuscript/critical-apparatus inspection still lacking, but no quantity/parser gap |
| An. Ox. 691 *eorþcundre*, dictionary quotation; underlying edition/ms not checked | `*érθa-kùnðaizōz` versus `*-izōz`, Fulk 2018: 209–211 | Strong fem.gen.sg; source's pronominal alternatives and timing remain qualified | *eorþcondere* / *eorþcundere*; extra r-syncope sensitivity *eorþcundre* | Prominence and separately adjudicated ending/syncope history; `*-izōz` instead produces *y* |
| R. Ben. 139,27/28 *eorþcundum*, one dictionary-located token, not two | `*érθa-kùnðaimiz`, Fulk 2018: 209–211 | Strong masc.dat.pl; synchronic ending secure, inherited derivation not demonstrated | Production parser rejection / private coverage *eorþcundem* | Parser coverage plus independently justified history of *-um*; the same failure occurs in *godcund* |
| Predicted `*eorþcundes`, no occurrence recovered | `*érθa-kùnðas`, Fulk 2018: 209–211; related *eardcundes* and *godcundes* are not this lexeme's attestations | Strong masc./neut.gen.sg; regular inherited-cell hypothesis without a required analogy | *eorþcondes* / *eorþcundes* | General medial prominence only; whole-word accent/formation assembled, target documentary gap explicit |
| Genitive alternatives, still unattested | `*-as(a)` and neuter `*-es(a)`, Fulk's printed paradigm | Legitimate grammatical alternatives, not interchangeable invented endings | Private `*-asa`/`*-es` plus prominence: *eorþcundes* | Not needed for preferred already accepted `*-as`; optional endings require parser coverage |
| Strong neut.nom/acc.sg, no token recovered | `*érθa-kùnðą`, source's nasalized short `*-aⁿ` | Not the Genesis weak cell | *eorþcond* / ordinary *eorþcond*, expanded final sensitivity *eorþcund* | Extra final-prominence hypothesis, not ordinary medial proof |
| Strong masc.acc.sg, no token recovered | `*érθa-kùnðanǭ`, source's `*-anōⁿ` | Correct nasal notation; complete ending still fails | *eorþcondene* / *eorþcundene* | Further ordinary ending history required; literal `*-anōn` was not an accurate PGmc transcription |

Recommend attested Genesis *eorþcunde*, weak neuter accusative singular,
from complete `*érθa-kùnðǭ`. It is the best independently justified
regular cell under Fulk's inherited n-stem account and the general
medial-prominence hypothesis. Its successful complete derivation survives
the current SC065/066/068 cascade and every prominence sensitivity without
parser expansion or an ending repair. The alternative morphological
prehistory and lack of manuscript/apparatus inspection remain explicit;
neither is concealed by a spelling match.

The strong masculine/neuter genitive `*eorþcundes`, from `*érθa-kùnðas`,
remains a demonstrably successful regular, reconstructed and unattested
fallback. No occurrence has been recovered; related *eardcundes* is not
an attestation of earthly. One regular cell, not the whole paradigm, is
the admission objective.

Production admission is deferred pending explicit scientific authorisation,
a real SC040 decision about the general projection, the approved population
extension and the lexical publication gates. This is a recommendation for
one cell, not certification of all *-cund* inflection, complete OE stress
or immediate production readiness.

Machine-readable registry verdict: n/a; no SC adjudication has been opened
or completed by this assignment, and no registry row is edited.

## Propagation (only after verdict)

Research propagation only: the new dossier, evidence, reproducible harness
and focused evidence tests. No Foma source, corpus row, accepted conclusion,
generated projection, canonical runtime bin or protected baseline changes.
The prospective scientific/corpus/editorial implementation is specified in
`admission-checklist.md`; it is not performed here.

Focused tests cover the complete successful weak-neuter and genitive, population and aligned-
trace preservation, the feminine ending's current failure and experimental
success, controls, composed checks and runtime/source protection. Strict
production adoption/publication validation is not claimed for unadopted
research.

The final focused run passed 26 tests and 537 subtests. Eleven snapshots
and the archived logs for 63 receipt files were hash-verified; full bundle
identity and reproduction limits are recorded in the README. The actual
main production status was successfully verified, separately from an
earlier research-context receipt invalidated by contemporaneous prose edits.
Production remains 390 selected, 382 correct, with the same eight mismatches.
No canonical refresh, strict publication rebuild or new Level C certification
was performed for this research-only addition.

## Residue

Retain the census's actual access limitations, the unattested genitive, the
distinction between inherited formation and productive parallel formation,
the explicit compound-accent assumption, incomplete foot/onset/vowel
coverage, the older syllabifier/parser diagnostics, and the unsettled
Oxford ending/late-syncope question. These are finite adoption conditions,
not permission to fabricate missing tokens or reopen protected histories.
The corrected masculine accusative's extra vowel is a separate ending/
nonhigh-vowel-syncope-before-*n* finding for controlled investigation if pursued. It
does not by itself refute or amend the accepted i-only scope of SC065,
nor establish a new chronological edge.

Resolve the separate population-enrolment authorisation before claiming
operational admission readiness. A same-population cell-migration command
cannot authorise a new identity. The research does not reopen the closed
infrastructure project to design a different framework.
