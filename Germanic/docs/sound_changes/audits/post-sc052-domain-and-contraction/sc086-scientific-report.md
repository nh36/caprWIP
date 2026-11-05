# SC086: contraction, representations and historical licensing

## Identity

SC086, `OEContraction`; 5 November 2026,
`research/full-cascade-functionality`, base
`efd9ec412a36aa5e9705ccacb63038c114e39fa3`. This is a bounded research
report following the adjudication template, not an adopted verdict.

## Question

Does context scoping remove the actual contraction ambiguity? Can an
independently justified historical analysis choose among competing
contractions without output-fitting, lexical exceptions or grammatical
conditioning? A complete compiled certificate can settle functionality;
it cannot establish the history or license a reconstructed compound.

## Current state (before any edits)

The registry characterizes SC086 as `oe/english_specific`, confidence A,
status `unadjudicated`, with an empty verdict. Its note describes
“OE intervocalic h-loss and subsequent vowel contraction.”
The reader is `reader_facing/086-contraction.md`; the owning account is
`book_dossiers/079-087-final-j-contraction-and-metathesis-cluster.book-dossier.md`.
Neither is edited.

The executable has 27 unconditional parallel clauses
(`Germanic/fsts/germanic.txt:3705–3745`): five identical-short-vowel
contractions, eight diphthong absorptions and fourteen long-vowel
absorptions. SC085 is physical stage 99 and SC086 stage 100 of the
expanded 110-stage relation; these positions do not date the changes.
The accepted 391 inputs, original-380 archive, four approved cells,
SC114 account and prospective find classification are untouched.

## Diagnosis

The fresh actual prefix through stage 99 is functional: 1,227,402 arcs,
3,355,552 reachable twins, 409,632 live twins, delay 5, ATT SHA-256
`f86d0d78e5a062bbfb8a888bea4d485eb7eadee0ac5801fc820a1ead64fa3495`.
SC086 introduces the retained broad-domain ambiguity.

The complete `é-ìwi` trace has only these changes before contraction:

| Physical stage | Change | Role |
|---|---|---|
| 1, parser | `é-ìwi → *é*ì*w*i` | compound separator deleted |
| 46, secondary-stress stripping | `*é*ì*w*i → *é*i*w*i` | secondary accent removed |
| 65, w-loss before final i | `*é*i*w*i → *é*i*i` | first three adjacent vowel tags |
| 67, i-umlaut | `*é*i*i → *i*i*i` | first three identical eligible vowels |
| 99, h-loss | no change | negative: no original h |
| 100, contraction | `*i*i*i → *i*ī / *ī*i` | overlapping pair choice |
| 109, star removal | `iī / īi` | both survive the surface filter |

The original `ò-oxun → oōn / ōon` counterexample is also preserved.
The isolated identical-vowel pair rule already has this overlap: no
additional grouping peculiarity is necessary. For each of the 27 A+B
clauses, an A+B+B context also permits the following B+B contraction in
the complete expression. Repeated four-vowel inputs admit different
nonoverlapping pairings as well.

There is a second, distinct issue. Braces spell strings, not indivisible
vowel tags: a centre ending in `{*e}` can consume the beginning of `{*eo}`.
For `*ā*eo*o`, the original outputs `*ā*ēo` and `*āo*o`.
A whole-tag right guard removes the second path but does not choose
between genuinely overlapping pairs.

The retained firing census is exactly flee, slay, ten, three and toe,
all in the original-380 population. These are live applications. The
artificial compound witnesses are raw-domain diagnostics with unproved
historical licensing, not new historical lexemes.

## Literature

Directly inspected originals:

| Source | Finding relevant here |
|---|---|
| Campbell 1959, p.98 §234 and footnote | Older as well as h-loss hiatus is treated; ū+a remains exceptional. WS ī+e and non-WS ī+e require different treatment. |
| Campbell 1959, p.100 §237 | W-loss and contraction are attested in nī- compounds, including nīcenned, and discussed for glīman with an explicit spelling qualification. |
| Ringe–Taylor 2014, p.259 | Histories of sea/law and combining *niwi-, *gliwi; OE compounds illustrate the latter. These are not supplied as complete reconstructed PGmc compounds. |
| Ringe–Taylor 2014, p.318 | W-loss and inherited hiatus also contract. Identical-vowel coalescence may precede unlike-vowel contraction; one late episode is possible, not demonstrated uniquely. Sea/law alone do not distinguish contraction from apocope. |

Existing adjudicated `audits/sc082-adjudication.md` was also consulted.
It explicitly calls the residual j-vocalization sequence a normalization
proxy, not a universal physical VjV sound law; its cited Hogg 2011
pp.283–286 and Ringe–Taylor p.228 qualifications remain authoritative.
No new historical conclusion about Fulk1998 or Seiler2019 is proposed.

## Historical analysis

Contraction cannot simply be restricted to newly h-created hiatus:
the cited w-loss and inherited cases independently refute that account.
Conversely, generalizing a late parallel replacement over every string
of adjacent tagged vowels is not yet a complete account of contraction.

The acute and grave in `é-ìwi` establish marked formal heads, not a
reconstruction of both stems, their inflections, their combination or
the date of compound formation. No consulted source licenses this
particular compound or a comparable inherited three-nucleus sequence.
The source-backed examples above primarily establish two-nucleus
contacts. The canonical three-vowel representation for three is partly
created by SC082's disclosed proxy and must not automatically be read
as three historical nuclei.

The bounded controls distinguish these issues:

| Control and status | Actual stage-100 contact or outcome | Interpretation |
|---|---|---|
| accepted flee `fléuxaną` | `*ēo*a → *ēo`; `flēon` | h-loss feeding |
| accepted slay `sláxaną` | `*ea*a → *ēa`; `slēan` | h-loss feeding |
| draw control `téuxaną` | `*ēo*a → *ēo`; `tēon` | separate from selected ten |
| accepted toe `táixōn` | `*ā*e → *ā`; `tā` | long-vowel absorption |
| accepted three `θréjez` | `*i*i*e → *ī*e`; `þrīe` | proxy-derived triple; conservative target |
| source-staged *niwi-, *gliwi | formal `níwi/glíwi` probes give `nii/glii` | retained acute *í is not covered by the plain *i+*i clause |
| sea/law comparisons `sáiwi/áiwi` | `sǣ/ǣ`, final i lost at stage 75 | not positive evidence that SC086 contracted them |
| source noncontracting ū+a contact | `*ū*a → *ū`; formal `būaną → būn` | broad executable scope fails Campbell's explicit negative |

The current SC086 reader misglosses selected `téxun` as draw; the selected
cell is ten. The separate draw control above does not silently change that
cell or claim a new adjudicated reader correction.

The last stem probes do not certify new PGmc reconstructions or corpus
cells. Their source-supported window is the later stem/contact, not a
complete PGmc compound. An exploratory `níwi-kènþaz` string is
parser-rejected and has no independently established second-stem
reconstruction; it is explicitly not a licensed historical control.
The grammar admits only a or zero as a linking vowel. The attestation
of OE nīcenned does not by itself date its formation to Proto-Germanic.

A non-output-defined regular test family was also compiled:
`D_raw ∩ pgrmOnsetCore.u V́ x aną`, where V́ is the explicitly listed
acute vowel/diphthong set in `contact_worker.py`. Its boundaries 99/100
and full relation have complete certificates. It is a structural
infinitival template, not a lexicon licensing all its possible roots
and not a definition of all `D_historical`. Its full relation is
functional but not total: surviving-ɣ input `ɣúxaną` is an exact
domain-inclusion counterexample. No theorem over the entire historical
language is inferred from this template or the lexical controls.

Historical stage and geographical scope remain those of the existing
OE account; dialect and hiatus-type distinctions need further source-led
analysis. The model-local execution dependencies w-loss→i-umlaut→contraction are
trace observations, not proposed historical chronology edges.
The retained SC085→SC086 relation is `independently_demonstrated` for
h-created contacts by Campbell p.98 and the stated feeding witnesses;
it does not date every process pooled into SC086. No `stage_entailed`
edge or new chronology edge is entered.
No positive evidence for analogy is introduced or needed by this report.

## Candidate experiments and independent results

All comparisons retain the source's earlier 99 stages. Each candidate
has 43,010 selected stage comparisons: shared preceding stages plus
actual output-set comparison at stages 100–110.

| Treatment | Exact intervention | Complete result | Selected consequences |
|---|---|---|---|
| independently scoped | single commas → double commas inside SC086 | same component ATT as original; nonfunctional | no stage changes |
| guarded parallel | append `|| _ [{*} | .#.]` | removes partial tags, retains triple ambiguity | no stage changes |
| homorganic-first serial | compose the 27 guarded clauses in source order | component, prefix100 and full relation remain nonfunctional | three: `þrīe → þrī` at 100–110 |
| per-centre directional | guarded clauses with each `->` changed to `@->` | still nonfunctional, including `*ea*a*a` | no selected stage changes |
| unified directional comparator | union all 27 centre/output cross-products, then one `@->` and whole-tag guard | component, raw prefix100 and full cascade independently functional | no selected stage changes |

Per-centre directional rewriting still admits
`éu-òxun → ēoon / ēoōn`: h-loss creates `*ēo*o*o*n`.
Thus superficially adding directional arrows is not a global choice
over the combined centre language. The unified relation makes such a
choice genuinely, but only as an explicit formal convention.

Its complete full certificate covers 1,891,009 arcs, 3,172,994 reachable
twins, 389,838 live twins and delay 3; ATT SHA-256
`b0d89d77889fa73a810d3dc727bd09d4e2068f5f9e30701da0636d6b584a95a5`.
Its prefix100 certificate covers 1,259,315 arcs and 441,861 live twins.
These are whole-graph results, not native-checker assertions or sampled
word tests. They do not prove the leftmost convention historically
correct, ensure repeated historical coalescence or establish totality.
Epsilon and `ḗô` remain rejected by its full relation.

Neither serial nor unified treatment solves the independent stressed-i
and ū+a controls. Serial application additionally reinterprets the
selected three proxy and changes an approved target. Iteration/order
therefore cannot be justified merely by the desire to remove all
apparent adjacent vowel tags.

## Verdict

Research recommendation: defer production reformulation. No registry
verdict is issued: its verdict field remains empty and status
`unadjudicated`. The machine-readable adjudication line is intentionally
not fabricated for an unaccepted proposal.

The precise unresolved decision is whether a source-supported
decomposition of identical-vowel coalescence, diphthong formation and
later absorption can both respect the proxy/true-nucleus distinction
and resolve independently licensed overlapping contacts. A formal
leftmost convention is available and proved functional, but the
consulted sources do not license it as the historical answer.

## Propagation (only after verdict)

None. No rule, registry, corpus, baseline or reader is propagated.
The proposed guard, serial decomposition, directional relations and
mandatory-root parser are private experiments. All 391 accepted
derivations and original-380 protections remain canonical.

## Residue and evidence

Before any adoption, establish stress-sensitive coverage, the general
ū+a/ī+e distinctions, historical construction dates and atomization of
proxy-derived diphthongs; then repeat protected source-bound validation
on the actual proposed source. Do not repair these by lexical IDs,
grammatical conditioning or selecting whichever path matches a target.

See `evidence.zip` directories `post-sc052-contraction-01`,
`post-sc052-unified-01` and `post-sc052-contact-01`, their
`results/{outputs,proofs}/`, and `analysis/complete-paths.json`.
Every negative certificate has two complete replayed accepting paths;
every positive certificate enumerates and verifies all live twins.
The original overlapping witnesses and all failed/inconclusive
instrumentation remain preserved. Compiler and accepted-source identities
are given in the canonical-domain assessment; no host Foma was used.
