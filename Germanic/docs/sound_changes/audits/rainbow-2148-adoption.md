# SC017: adoption of the early vowel history of rainbow

## Identity

- **SC id:** SC017.
- **Executable identifier:** `PNWGmcULowering`.
- **Date / branch / base commit:** 2026-10-28, `update`,
  `1bfdd0794b65d8a6abad698a651ca426a1061c29`, the completed SC087
  follow-up. Research `29ec734406d2bf1714d37a41980d453c7a4872aa` was
  incorporated intact as `164b071c`. Its earlier production base was
  `3cb109c981c8868bf383172e2be06cdc88c00fb0`.
- **Worktree at the new baseline:** tracked-clean after the SC087 push;
  unrelated untracked `Germanic/fsts/tmp_probe.foma` and
  `report.20261016.232234.70299.0.001.json` left untouched.

The original guarded research was independently reproduced in a detached
historical checkout and an owned, unmounted backend container.
`rainbow-2148-adoption/historical-reproduction.json` records both receipt
hashes. Every scientific field agrees; only the surrounding protection
maps differ between historical runs, and each map is identical before
and after its own run. The temporary container and checkout were removed.

## Question

- **Hypothesis or suspected problem (falsifiable):** early lowering of
  subordinate-stressed short *u* explains the second root of *reġnboga*
  without relying on late unstressed lowering. The grave must survive
  lowering and remain available to linking-vowel syncope.
- **Confirmation / refutation:** confirm by the independently supported
  *boga* etymology and a fresh complete trace
  `*régna-bùgô > *régna-bògô > *régnbògô > *régnbogô > reġnboga`.
  Refute the proposed implementation if it changes selected final outputs,
  loses the grave prematurely, lowers ordinary unstressed medial *u*, or
  disturbs the independently adopted world/soul paths. Final-output
  agreement alone cannot establish the history.

## Current state (before any edits)

- **Existing historical characterization:** SC017 registry:
  `historical_stage=pnwgmc`, `historical_scope=pan_pnwgmc`,
  `confidence=A`, `verdict=REFORMULATE/RETAIN`. These independent axes
  are retained. The existing verdict concerns the nasal-vowel class
  repair and qualified preference for SC017 before SC019.
- **Existing executable behavior:** word-initial consonants followed by
  plain *u* or acute *ú*, a first consonant excluding nasals and *j*,
  further consonants excluding *j*, and a non-high vowel. Thus the
  existing two clauses operate on the first nucleus; they do not
  lower the grave-marked second root. SC017 remains at execution 20.
- **Selected-input assumptions:** row 2148 retains both PROTO and
  PROTOFORM `*régna-bùgô`, target `reġnboga`, class `regular`. The
  masculine n-stem nominative, first-root primary accent and second-root
  subordinate accent are already encoded; the hyphen is input notation,
  not a boundary surviving into the lowering network.
- **Existing verdicts/dossiers consulted:** SC017/SC019 adoption and
  nasal-vowel receipts; SC016/017 adoption; current SC036/world
  adjudications; SC017 literature dossier; the 016–020, 035–037 and
  039–041 book dossiers; all original secondary-stress research.
  The original research and its guards remain frozen.

## Diagnosis

- **Complete firing census:** `rainbow-2148-adoption/before.json.gz`
  records every one of 109 canonical stage outputs for all 389 selected
  rows and all 380 immutable legacy inputs. Immediately before adoption,
  SC017 changes 39 selected rows and SC040 changes 11. All 389 inputs
  are accepted; 381 finals match; the eight mismatch IDs are 1973, 2013,
  2030, 2162, 2224, 2240, 2298 and 2300. The complete census, including
  negative/nonfiring rows, is machine-readable rather than a hand-picked
  witness list. `after.json.gz` confirms 40 early and 10 late firings:
  rainbow alone enters the former and leaves the latter. Every selected
  and immutable-380 final is identical before/after; selected intermediate
  differences are confined to 2148. World and soul retain every stage,
  not merely their final spellings.
- **Principal witness traces:** the pre-adoption canonical capture has
  unchanged `*r*é*g*n*a*b*ù*g*ô` at SC017. The original research's
  secondary-stress and explicit-compound variants both supply
  `*r*é*g*n*a*b*ò*g*ô` there; fresh post-adoption observations confirm
  this. Linking syncope preserves *ò* and deletes the linking *a*,
  then ordinary grave stripping supplies plain *o*.
- **Witness roles:** rainbow is the proposed new live application and
  syncope/annotation-lifetime witness; independent bow is the
  comparative control. World and soul are conservation controls, not
  evidence for extending SC017. High-vowel, nasal, intervening-*j*,
  ordinary weak-*u*, hawk and head controls guard against a broader law.
  The attested name *Buga* is an unresolved retention comparison.

### Fresh complete-trace landmarks

These are execution indices, not SC numbers or historical dates. Both
receipts retain all 109 stages, including every nonfiring stage, for both
populations. The final snapshot is independently checked against the
production wrapper.

| Execution | Stage | Actual rainbow output |
| ---: | :--- | :--- |
| 1 | EnglishProtoInput | `*r*é*g*n*a*b*ù*g*ô` |
| 20 | PNWGmcULowering | `*r*é*g*n*a*b*ò*g*ô` |
| 45 | OECompoundLinkingSyncope | `*r*é*g*n*b*ò*g*ô` |
| 46 | OEStripSecondaryStress | `*r*é*g*n*b*o*g*ô` |
| 62 | OEVelarPalatalization | `*r*é*ʝ*n*b*o*g*ô` |
| 83 | OEMedUnstressedORaising, nonfiring | `*r*é*ʝ*n*b*o*g*ô` |
| 85 | OEUnstressedLongVowelShortening | `*r*é*ʝ*n*b*o*g*a` |
| 89 | OEMedUnstressedULowering, nonfiring | `*r*é*ʝ*n*b*o*g*a` |
| 103 | OEPalatalFricativeMerger | `*r*é*j*n*b*o*g*a` |
| 106 | OldEnglishOrthography | `*r*éġ*n*b*o*g*a` |
| 108 | OldEnglishRemoveStars | `reġnboga` |
| 109 | OldEnglishSurface, nonfiring | `reġnboga` |

`controls.json.gz` independently compiles the original first-root network
and explicit-compound alternative against the adopted relation. They
agree on all 389 early-stage selected inputs. The general subordinate
clause also lowers synthetic grave-only `*b*ù*g*ô`, unlike the
explicit-compound alternative; this exposes their domain difference
rather than claiming global equivalence. Following high vowel, first
nasal, intervening j and plain medial-u negatives remain unchanged.
The later-position nasal control explicitly exposes the existing guard's
limit. The adopted sound operation passes the whole declared-domain
forward-functionality test; the parser's pre-existing `biu` ambiguity
is reproduced separately and remains unresolved.

## Literature

- **Existing CAPR dossiers checked:** those listed above; no frozen
  receipt or previously measured displacement is revised retrospectively.
- **Sources checked, with page numbers:** Campbell 1959: 43,
  §§115–116; Hogg, held 2011 reissue: 54–55, §§3.10–3.11
  (`HoggGrammar2011`, not his separately authored CHEL chapter);
  Fulk 2018: 56–57, §4.3; Ringe and Taylor 2014: 27–29; Kroonen
  2013: 82, *bugan-*; Colman 2011: 95–98. The supplied Colman original
  agrees with the research holding, SHA256
  `0af5841706ba5a00007acc5fa027b0faf4263b1287199430cb212a21326f3c9d`.
- **Source-supported phenomenon:** early stressed *u > o* before a
  following non-high vowel, restricted by nasals and intervening *j*;
  ordinary *boga* is explicitly explained this way. Kroonen's masculine
  n-stem is a stem reconstruction, not a fully specified nominative.
  Colman's *Buga/Boga* material and die/transmission qualifications
  prevent dismissal of retained *u* or indiscriminate dialect claims.
- **CAPR modelling decisions:** apply this root-vowel assimilation to
  inherited subordinate stress as well as primary stress. None of these
  passages prints the exact accented compound derivation. CAPR preserves
  its selected nominative serialization and the existing literal nasal
  guard; this is not a new adjudication of every nasal environment.

The subordinate clause is composed with the existing two-clause network
inside the same SC017 identity. A discarded development spelling put all
three rewrites in one comma group; Foma thereby broadened the shared
context, giving 44 early firings and unwanted `hafac/hēafad` for hawk/head.
The independent compound comparison detected this before adoption.
Composition preserves the original two-clause relation exactly and
adds only the intended grave rewrite. This is a formalization repair,
not evidence for a broader historical law; the rejected run is not an
adoption receipt.

## Historical analysis

- **Historical stage:** retain Northwest Germanic; no inference from the
  executable name and no new absolute date for the compound.
- **Historical scope:** retain the existing Northwest Germanic claim for
  the general process; the particular compound extension is qualified
  inference, not proof of unqualified identity across all dialects.
- **Regular phonological conditioning:** subordinate-stressed short
  *ù* lowers to *ò* before the existing non-high trigger through the
  same permitted consonants. The grave itself supplies the independent
  prosodic property. An additional preceding acute vowel would restrict
  the operation to one serialized compound shape without independent
  evidence for that extra phonetic requirement. Therefore prefer the
  general subordinate-stress clause to the research's compound-only
  variant, although both agree on the selected corpus. Neither rule
  mentions a word, morpheme or grammatical category. The first-nucleus
  plain/acute clauses are unchanged: ordinary weak medial *u* does not
  acquire an early lowering environment.
- **Counterexamples and falsification:** retained *u* in *Buga*,
  *fugol*, *wulf*, *wulle* and other inherited words remains a real
  problem, not an optional sound law or a name exemption. The precise
  reconstructed compound accent is not directly attested. The existing
  guard blocks only a first intervening nasal; a later nasal is not
  newly excluded. That discrepancy remains visible in controls rather
  than being repaired incidentally.
- **Positive evidence for analogy:** no consulted source demonstrates
  replacement from the simplex in this compound. Such influence is
  possible but is not preferred over the supported regular account.
- **Historical phenomenon / proxy:** the operation models the
  subordinate-root extension of early assimilation; the literal
  consonantal guard and serialized stress annotations do not exhaust a
  complete dialectal or prosodic reconstruction.
- **Chronology evidence:** SC017 before the Old English syncope and late
  lowering is `stage_entailed`, not a new independently dated edge.
  SC037 before SC038 is the existing model-local annotation dependency:
  syncope reads the grave, including lowered *ò*. SC038 before SC036
  remains the world weak-vowel dependency. Rainbow no longer supplies
  evidence for SC038 before SC040: its root is already *o*. No order,
  accent-stripping operation or second historical deaccentuation is
  introduced. The existing qualified SC017/SC019 relation is retained,
  not proved afresh by this compound.

## Verdict

- **Verdict:** REFORMULATE the SC017 executable to include
  subordinate-stressed *ù* / RETAIN its historical placement, scope,
  confidence, existing clauses and qualified SC019 relationship.

Registry-verdict: SC017=REFORMULATE/RETAIN

- **Justification:** ordinary *boga* independently supports early
  lowering, while the compound supplies the same vowel/trigger sequence
  under already reconstructed subordinate accent. The minimal
  accent-conditioned extension preserves that accent for the existing
  syncope. This supersedes only the older SC017/SC019 memo's retention
  of the two-clause rewrite, not its nasal-class repair or chronology.

## Propagation (only after verdict)

- **Affected files/registries:** SC017 executable and reader; concise
  SC036/037/040 cross-references; current dossier/card sections and
  registry commentary; mature rainbow model and source ledger;
  editorial certification; Colman bibliography and holding registration.
  All downstream book, registry and index projections use the artifact
  graph. Historical measurements remain identified as historical.
- **Regression tests:** the fresh capture checks all 109 stages and
  both populations, confines selected intermediate differences to
  rainbow, compares all final outputs and checks unchanged definition
  identities/order. Focused controls and publication checks accompany
  the final receipt. No experimental earthly helper enters production.
  The pre-adoption CLI additionally requires the recorded source hash,
  preventing a later model from silently replacing `before.json.gz`.
- **Baseline/fingerprint effect:** none; no corpus, context, stage,
  class or target edit, and no baseline migration or refreeze.
  At the recorded production base the mature book has 167 entries,
  including 89 regular entries (world is already regular), not 88.
  Canonical assembly now reports 168 and 90; this is publication inclusion,
  not corpus expansion.

### Publication-gate repairs

The target's explicit index tag belongs on its published prose occurrence,
not the source's introductory table, which the assembler intentionally
removes. A scoped index override excludes the computed `*régnbògô`
intermediate from lexical-citation candidates. Eight exact semantic-index
additions authorize the new entry and its source-backed comparison forms;
no scientific fingerprint is changed.

The paragraph-gloss report also required contextual corrections for
previously glossed lemmas and explicitly paired inflections. Its small,
literal-context allowances require an established or local shared gloss;
ordinary unrelated repeats still fail. The new fixtures exercise both
acceptance and rejection. SC087's first mention of *gærs* now actually
supplies 'grass'; no scientific claim or rule is changed. Scholarly prose
has not been rewritten to conceal the report's false positives.

Rendered inspection caught two genuine presentation problems in the new
model: trailing-hyphen Markdown emphasis spilled into surrounding prose,
and plain index spans were not italicized in the standalone lexical
volume. Explicit LaTeX emphasis for the bound forms and emphasized span
contents repair both without changing any lexical or semantic identity.
The first full-suite invocation was stopped before completion so that the
final suite could run against these stabilized publication sources.

### Revised SOURCE inventory

Paths below are relative to `Germanic/docs/`, except `docs/refs.bib`.
Generated projections, rendered publications and their existing checker
reports are regenerated outputs, not additional editorial authorities.

- Readers: `sound_changes/reader_facing/017-nwgmc-u-lowering.md`,
  `036-inter-stress-raising.md`, `037-compound-linking-syncope.md`,
  `040-medial-unstressed-u-lowering.md`, and the first-gloss correction
  in `087-r-metathesis.md`, all in the same reader directory.
- Registry: `sound_changes/registry/sc_registry.tsv`,
  `sc_inventory_notes.tsv`, and `chronology_edges.tsv`.
- Literature dossier:
  `sound_changes/literature_dossiers/017-nwgmc-u-lowering.dossier.md`.
- Book dossiers, all under `sound_changes/book_dossiers/`:
  `016-020-early-vocalic-final-corridor.book-dossier.md`,
  `035-037-prefix-and-compound-adjustments.book-dossier.md`,
  `039-041-medial-lowering-and-final-loss-bridge.book-dossier.md`.
- Chronology cards, all under `sound_changes/order_tests/chronology_cards/`:
  `SC017-nwgmc-u-lowering.md`, `SC036-oe-inter-stress-raising.md`,
  `SC037-oe-compound-linking-syncope.md`,
  `SC040-oe-med-unstressed-u-lowering.md`.
- Scoped prior-memo closeouts: `sound_changes/audits/sc017-sc019-adoption.md`
  and `sound_changes/audits/sc036-adjudication.md`; the original research
  dossier and frozen receipts are unchanged.
- Lexical source and ledger:
  `lexeme_reports/model_entries/2148-rainbow-reġnboga.model.md` and
  `2148-rainbow-reġnboga.source_ledger.md`.
- Lexical certification/holding: `lexeme_reports/pgmc_integration/editorial_cases.tsv`
  and `lexeme_reports/pgmc_reconstructions/sources.tsv`.
- Editorial live counts: `assembly/README.md` and
  `lexeme_reports/report_schema.md`; programme closeout: `CURRENT_STATE.md`.
- Index decisions: `book/index_verborum_overrides.tsv` and
  `book/index_semantic_fingerprint_allowlist.tsv`.
- Bibliography: repository-root `docs/refs.bib`.
- Adoption authority: this memo and its new `rainbow-2148-adoption/`
  capture, controls, before/after and historical-reproduction receipts.
  The executable authority remains `Germanic/fsts/germanic.txt`.

## Residue

- The exact prehistoric accent/junction, complete retained-*u*
  distribution, possible analogy and literal nasal-guard limitations
  remain qualified. The existing `biu` parser ambiguity and experimental
  stress-helper diagnostics are not repaired. Earthly and soul remain
  separate research; no *-cund* accommodation is adopted.
- **Validation closeout:** the strict full run executed 1,616 tests:
  1,611 passed, with 9,133 subtests passed, and five stale live guards
  failed. They concerned the independently authorized SC017 definition
  delta in two older preservation tests, the 40-versus-39 live census,
  Colman's 94th catalogue registration, and the eight new rainbow
  semantic-index approvals. Complete traces, live runtime checks,
  functionality and scientific-corpus conservation checks all passed.
  The five guards were updated without changing SOURCE or frozen
  evidence. The new publication test additionally pins all eight exact
  approval records and preservation of every prior record.
  All five repaired selectors and all five adoption tests then passed
  together (10 tests, including fresh container capture/private controls).
  The isolated live evidence-interface run subsequently passed all
  24 tests. Thus all 1,640 distinct tests were genuinely executed and
  passed across the complete run and its explicit repaired-selector
  rerun, not a second claimed all-green full invocation. JUnit reports
  confirm zero skips and that every full-run failure is covered by a
  passing rerun. No executable, scientific input or publication source
  changed after the complete run.

The final strict build used
`INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 bash Germanic/docs/assembly/build_capr_book_draft_docker.sh`.
It regenerated both standalone volumes and the combined book; index,
semantic, paragraph-gloss, bibliography, reference, heading, TeX/print-index
and 18 negative-fixture checks passed. There are zero unresolved internal
references and zero remaining `sect/sects` citation locators.

Actual page images were inspected, not just extracted text: combined
printed pages 29–30 (SC017 prose and exact composed definition),
69 (SC037), 71 (SC036 and preserved soul discussion), 99 (SC040),
159–160 (the mature rainbow entry), 297 (Colman bibliography), and
304 (rainbow and its attested forms in the Old English index).
The standalone mature lexical PDF was inspected on pages 40–41, including
the corrected emphasis and bound-form typography. The mature volume has
168 entries, 90 regular; the complete presentation retains 389 derivations.
The final canonical refresh reported `CONTROL PLANE CLEAN`, and SC017's
strict propagation check passed after this administrative closeout.
