# Post-migration consistency and cleanup record

Base: `2fc696ec55aa2b1eae80aaabf0ed9bcd726921d9`, branch `update`.
This records the bounded cleanup before further SC035 research or SC036
adjudication. It is not another registry, ordering authority or scientific
baseline. Corrections belong to the existing SOURCE owners; projections
remain owned by the artifact graph.

## Working inventory

The inventory covers all 97 registered reader sources and 105 printed
definitions, all five introductions, current registry and edge projections,
accepted SC016/017, SC021 and SC035 decisions, publication filters and
reports, current source-reference consumers and the historical replay fixture.
The following items identify concrete inconsistencies rather than stylistic
preferences. Evidence and completion details are added below as each is
resolved.

| ID | Class | Problem and implication | Authoritative owner and intended correction |
| --- | --- | --- | --- |
| C01 | 2: chronology metadata | Two reciprocal displacement records still assert SC016 before SC017, contradicting the explicitly adopted orthographic interpretation and SC016/017 adjudication. | `registry/chronology_edges.tsv`; distinguish superseded experiments from the adopted relation, retain archived receipts, reproduce yoke and youth controls. |
| C02 | 1, 2: prose and chronology | SC040's youth displacement claim still requires SC040 before SC072, although the SC021 repair explicitly adopted the opposite serialization on source-backed historical grounds. | Edge registry, SC040 reader discussion and current explanatory metadata; replay current and original experiment architectures before classifying what the old failure demonstrates. No automatic reversal or rule movement. |
| C03 | 6: validation gap | Current registry validation verifies witness membership but does not diagnose directional contradictions against the canonical model. | Existing registry validation; distinguish historical constraints, technical dependencies, superseded experiments, nonordering observations and unresolved endpoints, with exact positions and evidence in diagnostics. |
| C04 | 1, 3: terminology | SC076's title and primary heading still describe prefix reduction; old Foma comments claim protected breve-e despite the adopted direct, prosodically conditioned i-to-e rule. | SC076 reader source and `germanic.txt` comments; retain SC076, executable identifier and anchor, describe pretonic i-lowering and positive context. |
| C05 | 1: introductions | Chapter 2 calls SC014/015 adjacent; Chapter 4 says SC043 opens its vowel corridor. Chapter 1 incorrectly prioritizes chapter membership over historical analysis; Chapter 3 partly derives placement from the Foma prefix. | Five authoritative introduction files; remove false adjacency and identifier-based staging claims while retaining supported thematic connections. |
| C06 | 1: repetition/classification | The SC002 publication-status paragraph repeats in Chapters 1 and 2; Chapter 5 describes all earlier material as historical sound laws despite explicit support entries. | Chapter introductions; keep one substantive explanation and acknowledge technical classifications. |
| C07 | 1, 6: stale printed implementation | Of 105 printed definitions, 67 differ textually from the canonical definition bodies. Many differences are transport wrappers or redundant grouping; the nasal low-vowel encoding and SC010 w-gemination clause are substantively stale examples of already changed implementation. | Individual reader Foma blocks, checked against shared `executable_facts`; reconcile printed code with existing accepted implementation without editing executable semantics. Classify differences rather than assuming every textual difference is a new law. |
| C08 | 4: predicted forms | SC052's raw-LaTeX predicted span loses its content through `pandoc.utils.stringify`, leaving only a dagger. | Authoritative semantic span and shared filter validation; use established semantic markup, test actual rendered form fidelity and fail on lost content. |
| C09 | 4: glyphs | Existing builds warn about U+0002 and angle-bracket glyphs. No literal U+0002 was found in current text sources or retained combined TeX. | Diagnose minimal rendering and actual PDF/font output before correcting the appropriate shared source/font layer; do not suppress unexplained warnings. |
| C10 | 4: layout | Short rule-code boxes can split awkwardly across pages; rendered SC024 proves `samepage` alone is ineffective for this verbatim environment. | Shared Foma filter uses genuinely unbreakable minipages only for blocks of at most eight lines and 80 Unicode characters per line. Long blocks remain breakable; no per-file page breaks. Verify the actual reflow rather than just wrapper presence. |
| C11 | 5: coverage | Reader coverage compares against the old change-report manifest, mislabeling retired or unpublished identities as missing and current publications as extra; it also hardcodes the obsolete SC-number opening sequence. | `build_reader_book.render_coverage_report`; registry and executable sequence determine correctness, historical comparison is secondary and explicitly classified, genuine omissions fail. |
| C12 | 5: portability | Cross-reference and generated-prose reports embed host-specific absolute paths. | Existing report generators/shared checker utilities; stable repository-relative source labels. |
| C13 | 5: misleading diagnostic | The chronology prose report labels absent displacement-keyword patterns as warnings about 71 sections, including technical and component sections. This is not evidence that their scientific accounts are deficient. | Existing report generator; distinguish a textual-cue inventory from actual chronology consistency validation. Do not rewrite arguments to manufacture keywords. |
| C14 | 6: references | Active references to retired grouped files must be separated from commit-pinned historical tests, frozen receipts and archive documentation. | Current registry pointers, preparation interface, tests and navigation; use current ownership without rewriting historical paths. |
| C15 | 6: runtime reliability | Historical SC035 replay mounts read-only directories beneath a writable temporary bind root; a minimal Docker Desktop probe reproduces delayed-release cleanup failure even with user-owned, precreated targets. | Existing historical replay fixture; all writable artifacts now live inside an explicitly owned disposable container. Remove that exact container in `finally`; no writable host temporary root, permissive deletion, swallowed errors, skipped replay or weakened expected receipts. |
| C16 | 7: unresolved science | SC035's wider raising generality, SC052 merger disagreements, the conditioned late SC105 approximation and other explicitly qualified working accounts remain research questions. | Existing adjudications and dossiers; retain their stated uncertainty and do not turn this cleanup into new scientific adjudications. |
| C17 | 1, 3: linked obsolete descriptions | SC040 Foma comments, the SC039–041 book dossier, conditioning dossier and youth model still attribute preservation to long vowels or early glide insertion, or require SC040 before SC017/072. | Current explanatory SOURCE corrected to the accepted late lowering/root-u preservation and late spelling; dated experimental receipts unchanged. |
| C18 | 2: evidence classification | SC026/027 live edges call the two components independently demonstrated successive historical chronology, although their accepted memo explicitly classifies their order as an executable dependency within one historical process. | Preserve both registered entries and archived outputs; classify these edges as technical dependencies and remove the obsolete youth result as a current reader chronology claim. |
| C19 | 1, 2: additional displaced-result mismatch | The old reciprocal early-SC040 widow failure does not survive the accepted SC021 vowel-resolution sequence. Delayed SC039 still gives wudowe; early SC040 instead preserves widow and changes world to weorald. | Paired current assays retain both observations; classify only the obsolete reciprocal record as superseded, retain the demonstrated SC039-before-SC040 relation and correct current prose. No rule movement. |
| C20 | 1, 4: rendered duplicate | Inspection of the repaired angle notation on combined page 17 exposed a verbatim repeated Campbell/Ringe–Taylor passage within SC024's alternatives paragraph. | Remove only the second copy, preserving every argument and source locator; add a focused single-copy guard, regenerate and repeat final validation/publication. |

## Scientific boundaries

Default invariants: unchanged executable definition bodies and stage order;
unchanged canonical inputs and targets; 389 selected derivations, 381 matches
and the same eight mismatches; unchanged 167 lexical models, selections and
editorial sequence; unchanged frozen adjudication receipts and earlier
baselines. Comment-only Foma source edits legitimately change raw provenance
hashes and require canonical regeneration, not a baseline migration.

The chronology reconciliation will be recorded using the research protocol's
identity/question/diagnosis/literature/analysis/verdict/propagation/residue
structure. Correcting an obsolete edge classification does not complete the
ordinary adjudication of an otherwise unadjudicated sound law.

## Completion and verification

Completed. C01-C15 and C17-C20 are resolved at their existing SOURCE owners;
C16 is deliberately retained as unresolved scholarship, not concealed by a
passing computational baseline.

### Chronology and current explanations

The [reconciliation memo](../sound_changes/audits/post-migration-chronology-reconciliation.md)
records the original-commit and current paired assays, complete canonical
firings, page-numbered source grounds and scoped verdict. The old early-glide
yoke/youth experiments reproduce, but do not date the adopted written-surface
operation or establish early SC040. Accepted SC021 source chronology supports
the late lowering independently of that experiment. Current delayed SC039
still gives *wudowe*; advancing SC040 no longer supplies the reciprocal widow
failure after accepted vowel resolution. Four obsolete measurements remain
explicitly superseded, with their original cards and receipts unchanged.
SC026/027 retain their registered identities and single canonical historical
identity; their component dependency is technical, as their accepted memo
already requires.

SC076 terminology, SC035-related protective-vowel comments, the five
introductions, SC040 comments/dossiers and youth's lexical development now
describe the accepted model. All 105 printed definitions agree with their
canonical bodies under the shared parser. The normal manifest path rejects
stale printed implementations. Removing the duplicate SC024 passage loses
no argument, qualification or bibliographic locator.

Registry validation now distinguishes historical precedence, actual technical
dependencies, nonordering observations, superseded experiments and unresolved
endpoints. A historical stage-based relation needs a sourced explanation,
not an invented lexical witness; the existing witness-discipline test now
checks that distinction directly in SOURCE. Independently demonstrated
relations still require interpreted lexical evidence.

### Rendering, references and reports

SC052's ordinary semantic span visibly produces italic predicted
*dejæ* with the dagger marker. Raw or empty predicted-form content fails
instead of silently disappearing. U+0002 originated in Markdown `\*` embedded
inside a raw TeX heading, not source-byte corruption; corrected heading
handling eliminates that math-command interpretation. The angle glyphs were
missing from the prose font; shared math-font mappings preserve the notation.
Final rendered PDFs contain no U+0002 and the publication log contains no
missing-character diagnostic for those defects.

An actual forced-boundary PDF places the complete five-line Foma fixture on
the next page. Short boxes use minipages, not the ineffective `samepage`
wrapper; long rules remain breakable. Final SC024 heading and box stay
together on combined physical page 18. There are no empty-text pages or
new per-source page breaks. The existing short Contents and Index title
leaves are intentional, not blank pages.

| Presentation | Migration receipt | Final cleanup |
| --- | ---: | ---: |
| Reader pages | 102 | 103 |
| Lexical pages | 158 | 158 |
| Combined pages | 295 | 296 |

Rendered inspection covers all five introductions, SC016/017/035/040/052/
072/073/076, the SC103 heading, angle notation, neighboring sections,
bibliography and Index Verborum. In the combined PDF, SC016 is on physical
page 103, SC017 on 31, SC052 spans 77-79, SC035 begins after its discussion
on 79 with its intact primary rule on 80, SC040 is on 94, SC072/073 on 93,
and SC076 on 95. Youth's corrected development is visible in the standalone
lexical volume on page 109. These are observed locators, not layout inputs.

Current coverage is registry/executable-model coverage: retired SC021/058,
deliberately unpublished identities and published support stages are
explicitly classified. The old report-manifest comparison is secondary;
genuine omissions still fail. Generated prose/cross-reference source labels
are repository-relative. The chronology keyword report is explicitly
non-normative; scholarly paragraphs were not rewritten to manufacture cues.
Publication logs retain the existing Pandoc runtime `Ticker` diagnostics;
these are not missing-glyph or unresolved-reference warnings and were not
suppressed.

Every registry document pointer resolves. All 97 publication reading lists
select their current unique reader sources; direct SC035/SC040 preparation
was also exercised. Of the 18 deleted grouped reader paths, the only active
Python/shell consumer hits are the deliberately historical semantic-baseline
builder and the commit-pinned SC035 source-preservation test. Historical
reader builders, aggregates and receipts remain records, not supported
current entry points. No replacement registry or ordering authority was added.

### Final validation

| Check | Result |
| --- | --- |
| Complete strict `python3 -m pytest -q Germanic/tests` | 1,570 passed; 9,071 subtests passed; no skips; one complete release invocation, 3,645.85 seconds |
| Supported portable runner | All five gates passed; 1,529 tests and 9,038 subtests passed; 41 runtime tests explicitly not run |
| Full artifact graph / provenance | `CONTROL PLANE CLEAN` |
| Strict combined wrapper with `INDEX_VERBORUM_STRICT=1` | Reader, lexical, introduction and combined PDFs built successfully |
| Publication identity/order parity | All 97 identities match the canonical eligible executable sequence exactly |
| Reader cross-references | 97 sources, 312 links, zero issues |
| Rendered references and bibliography | Zero unresolved internal references; zero unnormalized section locators |
| Semantic/gloss and index checks | Passed, including actual TeX/index checks and all 18 negative index fixtures |
| Historical runtime reliability | Actual commit-pinned replays reproduce their complete immutable receipts; lifecycle tests cover success and start/source/build/body failures |

Earlier complete runs and intermediate rendering attempts are not combined
to manufacture the release result above. After rendered inspection exposed
the duplicate passage and ineffective short-box wrapper, publication and
the complete strict suite were rerun against the corrected implementation.
Portable validation is not certification of runtime or original-image
capabilities; those facilities were provisioned for the separate strict run.
No new source-image certification is claimed.

### Scientific preservation and residue

All 389 normalized executable definitions and all 109 physical stages are
identical to the migration base and recorded pre-cleanup state. All 210
protected/current scientific files under the data, existing audits and
baseline directories are byte-identical; the sole additional generated
equivalence receipt changes only legitimate raw-source provenance hashes.
Fresh production/sandbox equivalence covers all 389 rows.

The frozen baseline remains 389 selected, 381 matches and the same eight
mismatches, with unchanged output, lexical-projection and original-380
fingerprints. The complete 167-row lexical selection/editorial manifest is
byte-identical. Generated manuscript/index/source-location changes are
legitimate projections, never manual repairs. Frozen adjudication receipts,
prior baseline snapshots and original local scratch files remain untouched.

SC035's wider generality, the explicitly disputed SC052 merger account and
ordinary SC040/072 adjudication/conditioning review remain separate research
work. None is resolved by output fit or this consistency pass. No sound law,
execution order, selected reconstruction or target was changed, and SC036
was not begun.
