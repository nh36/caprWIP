# SC037 compound linking-vowel syncope adjudication

## Identity

- **SC id:** SC037
- **Executable identifier:** `OECompoundLinkingSyncope`; not a stage claim.
- **Date / branch / base commit:** 2026-11-06 / `update` /
  `46956200397c7002bcffb68da6b429b630fcf0a1`.
  The evidence-only commit is not a new scientific comparison baseline.

Consolidation first verified clean trees and `update...research` counts
0/41, then fast-forwarded existing `update` from
`8f7713c39f26a7f81ef04d29d54070f1b83ab0e0` to the base SHA above and
confirmed that exact remote tip. Annotated remote rollback tag
`rollback/update-before-certified-consolidation-2026-11-06` preserves
the earlier `update`. Certified scientific evidence, selected records
and publication assets were preserved; no squash, rebase or force-push.

Older integration/scientific refs are ancestors. The two divergent
one-commit compound-secondary-stress and earthly-regular-cell branches
have all11/all18 files preserved byte-identically in integrated commits
`164b071c` and `25b48b93`, respectively. Four index refs remain unmerged:
`index-iv-anchor-shadow` (4 unique commits),
`index-explicit-plan-shadow` (5),
`index-explicit-plan-production` (8), and
`index-broad-prose-placement-shadow` (14). Each has426 update-only
commits and no patch-equivalent history. They form an old-base
experimental chain with superseded reader/count/manuscript assumptions,
not changes imported into current shared-emission ownership.

## Question

- **Hypothesis or suspected problem (falsifiable):** the existing rule
  deletes short high linking vowels after light as well as heavy first
  syllables, contrary to independently attested retention contrasts.
  Its compound annotation dependency may also have been confused with
  historical loss of secondary stress.
- **What evidence would confirm it; what would refute it:** light-root
  retained i/u versus heavy-root loss, supported directly by the
  handbooks, confirms the missing weight restriction. Same-environment
  light-root loss with an independently established input and prosody
  would refute a categorical weight account; annotation stripping alone
  cannot establish its historical date.

## Current state (before any edits)

- **Existing historical characterization:** registry SC037:
  `active; historical_sound_change; oe; english_specific; confidence A;
  unadjudicated; runner_limited_or_technical`.
- **Existing executable behavior:**

  ```foma
  define OECompoundLinkingSyncope Ctx([
      [{*a}|{*i}|{*u}] -> 0
          || PGmcStarAcuteVowel OEAnyConsonant+ _ OEAnyConsonant+ PGmcStarGraveVowel
  ]);
  ```

  The fresh tracer labels it stage 44 of 109 transitions. This display
  position is not a historical date. It precedes technical SC038.
- **Selected-input assumptions:** one selected form per lexeme; the
  selected rainbow and earthly inputs independently carry compound
  stress. Their hyphens are gone before SC037; the grave survives.
  Neither selected firing demonstrates high-vowel deletion.
- **Existing verdicts/dossiers consulted:** registry-owned reader,
  grouped SC035–037 dossier, chronology card, accepted rainbow adoption,
  preserved rainbow/earthly secondary-stress literature and lexical
  work, and the completed SC035/SC036 decisions. None is reopened.

## Diagnosis

- **Complete firing census:** fresh official `SC037 --evidence` rebuild
  and production/sandbox equivalence over all 391 selected rows; two
  live, in-domain a-deletions. The original 380 identities are a subset,
  not another independent population.
- **Principal witness traces:**

  | Selected row | Immediately before | Immediately after |
  |---|---|---|
  | 2148 rainbow | `*r*é*g*n*a*b*ò*g*ô` | `*r*é*g*n*b*ò*g*ô` |
  | 2336 earthly | `*é*r*θ*a*k*ù*n*d*ǭ` | `*é*r*θ*k*ù*n*d*ǭ` |

  The candidate produces the identical two firings, identical pre-rule
  applications for all 391 rows, and identical unique composed finals.
- **Witness role classification:** rainbow and earthly are live
  nonhigh-vowel applications. Light-root i/u stage controls are
  counterexamples to the old unrestricted high-vowel clause; heavy
  short-root and long-vowel controls are positive mechanism controls.
  Removing the grave is a technical negative, not a historical witness.
  The light-root closed-link control does not independently establish
  closed-syllable protection: it is already protected by root weight.

## Literature

- **Existing CAPR dossiers checked:** current SC035–037 dossier and
  preserved compound-secondary-stress literature/lexical evidence;
  Barrack census, crosswalk and citation ledger.
- **Sources checked, with page numbers:** original held Campbell 1959
  pp. 34–35 §§87–92, 143 §341, 145–146 §§348–353, 148–149 §§356–359,
  153 §367 and 159 §§386–387; Hogg, held 2011 reissue of volume 1,
  pp. 49–50 §§2.89–2.91 and 220–223 §§6.14–6.19; Ringe–Taylor 2014
  pp. 266–267 and 303; Sievers–Brunner 1965 pp. 137–138 §§167–168;
  Barrack 1975 pp. 82–84, rules 333a/b and 335. Text was extracted
  directly from the held PDFs; Brunner p.137 and Barrack pp.82–83 were
  also visually inspected. PDF identities and inspected sheets are in
  the immutable experiment archive; original PDFs and images are not.
- **Source-supported historical phenomenon:** short nonhigh medial
  vowels undergo syncope without the high-vowel root-weight condition;
  high linking i/u are lost after heavy first syllables, with
  independently attested light-root retention, including
  Winifrið/Winefrið and duruweard, contrasted with dælnimend,
  flæscmaðu and handclāð. Open-syllable restrictions and source-critical
  name/compound qualifications remain relevant. Ringe–Taylor p.303
  warns that different first-stem histories complicate the apparent
  hild-/hilde- distribution; it is not an automatic second-member-weight
  rule or a new chronology edge.
  Campbell's obscured second-root shortening/modification, connecting
  vowel insertion and weak-vowel quality changes are distinct
  phenomena, not interchangeable evidence for linker deletion.
  Barrack 333a/b concerns weak-vowel fronting/quality; 335 concerns
  rounding. Their ordering schema does not date SC037.
- **CAPR modelling decisions:** retain the a-clause literally and
  restrict the high-vowel clause to the represented heavy patterns:
  long acute vowel plus consonant(s), or short acute vowel plus at
  least two consonants. Compose the clauses explicitly; do not share
  contexts through a comma group. Do not add lexical exclusions,
  paradigm records, a new stress architecture or a contraction ordering.

## Historical analysis

- **Historical stage:** retain `oe`, referring to the preliterary/Old
  English developments reconstructed by the cited grammars. This is
  not inferred from the executable prefix.
- **Historical scope:** retain `english_specific` for the Old English
  account; no exclusive English innovation or new common-ancestor
  assignment is demonstrated by this bounded investigation.
- **Regular phonological conditioning:** unstressed medial vowel
  between an independently primary-stressed first domain and a
  subordinate-stressed second domain; high-vowel loss additionally
  requires the relevant first-syllable weight. No grammatical class,
  lexical diffusion or compound-name exception conditions the rule.
- **Counterexamples and falsification:** old and candidate components
  both accept the stage shapes underlying the light-root i/u
  comparisons; the old component deletes, the candidate retains.
  Nine controls pass, including short-root a-loss, heavy i/u-loss,
  represented long-vowel loss and absence of a secondary-stress trigger.
  These are annotated stage/mechanism controls, not diplomatic source
  forms or independently established complete Proto-Germanic words.
  The three schematic raw input strings tested in the report are
  rejected by the canonical parser; they are not silently admitted.
  In particular the handclāð-inspired control has a schematic short
  second-root vowel, not its independently established long quantity.
- **Positive evidence for analogy:** none required for the demonstrated
  light/heavy contrast. Name variants and different inherited stem
  histories must not be reduced to an unsupported analogy claim.
- **Relationship between historical phenomenon and executable proxy:**
  the old high-vowel clause overgenerated after light roots. The
  adopted restriction repairs that concrete defect. It remains a
  bounded proxy: the acute/grave inventory does not encode all
  historical long vowels/diphthongs, and right-hand C+ is not a complete
  syllabification or closed-syllable detector. This is not certification
  of all historical compounds or the broad synthetic parser language.
- **Chronology evidence:** existing SC037→SC038 is
  `technical_computational`, neither `stage_entailed` nor
  `independently_demonstrated` historical chronology. The earlier
  bundled-stage runner limit is not a historical edge. The old SC049
  displacement card remains a historical experiment, not a newly
  remeasured or promoted relation. The accepted SC017 rainbow sequence
  and world/soul histories are unchanged; no new chronology edge is
  proposed.

## Verdict

- **Verdict:** RESTRICT executable high-vowel conditioning; retain
  nonhigh a-loss, historical stage/scope and executable position.
  Confidence B qualifies the represented proxy independently of stage.
- **Machine-readable line:**

Registry-verdict: SC037=RESTRICT

- **Justification:** direct handbook evidence independently requires
  the light/heavy distinction absent from the old high-vowel clause.
  The smallest correction preserves a-loss and all selected derivations
  while repairing the attested retention contrast at the represented
  stage. Barrack's quality rules are related discussion, not the same
  deletion law. No demonstrated fact requires a new sound-change
  identity or historical reordering.

## Propagation (only after verdict)

- **Affected files/registries:** FST; SC037 registry and inventory note;
  reader, current dossier section and chronology qualification; this
  memo; focused tests and the three cumulative preservation inventories.
  SC037's Barrack crosswalk/ledger is reconciled with this one decision.
  The separate research agenda reconciliation marks SC065/066/068/087
  complete and corrects narrow source-reading errors without adopting
  additional laws. Older agendas remain preserved at the base Git SHA.
- **Regression tests added/updated:** `test_sc037_adjudication.py`
  binds the current kernel to the actual immutable candidate, tests
  paired light/high and heavy/high outcomes and preserved a-loss, and
  checks the full selected comparison plus native component proofs.
  The historical cumulative inventories explicitly recognize this
  separately pinned change; their other protections are not relaxed.
- **Baseline/fingerprint effect:** none. Candidate FST SHA256
  `aff07d267ddb591d4b0d28ece6365b671f96751fa163c699496708550904c3ce`;
  prior FST SHA256
  `c51c3f440e48c320968dd7a12c3b9995c2b16f5e766ef075f16f7af8eba76d3d`.
  All 391 selected analyses/finals and all unchanged-stage histories
  conserve the certified result: 383 matches and eight inherited
  mismatches (buck, fire, fowl, rust, straw, tap, wolf, wool).
  Native `test functional` returns TRUE for both old and candidate
  components. No global full-cascade functionality/totality claim is
  made. The actual source-bound A/B/C certification and tested-tree
  binding belong to `sc037-experiments/certification.json`; adoption is
  not certified by an anticipated test result in this memo.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:** general closed-syllable protection, unrepresented
  long/grave and diphthongal stress patterns, and source-critical
  second-member/name variants remain explicitly outside this bounded
  executable correction. No independently supported selected derivation
  fails because of those limits. Comparison forms are not new selected
  publication targets. SC038 stays technical; earlier sound-change
  verdicts and all eight mismatches stay protected.
  The actual next sequential SC is SC039; SC040 is already adjudicated,
  followed by SC041 and SC042. The Barrack discrepancy queue remains
  separate, with overlap resolved by the owning SC decision.

## Lexical validation follow-up

The subsequent [bounded lexical assessment](sc037-lexical-validation.md)
preserves this adopted RESTRICT correction but makes no new admission.
The named comparison forms do not yet supply an independently dated
complete input discriminating the former and adopted high-vowel clauses.
In particular, Orel's *đura-warđaz* has a, not inherited linking u.
The source discussion and component controls must not be described as
selected whole-word lexical certification.

That assessment also qualifies the historical raw-probe rejection above:
the probes included a conventional initial reconstruction asterisk,
whereas the canonical parser takes normalized unstarred text. Their
rejection does not establish rejection of correctly encoded words.
The immutable assay itself is preserved.

The preceding Residue records the queue at this memo's original date.
SC039 has since received its bounded DEFER verdict. The actual sequential
queue now resumes at SC041, then SC042; the Barrack queue remains SC067,
then SC080. None is initiated by this lexical/publication follow-up.
