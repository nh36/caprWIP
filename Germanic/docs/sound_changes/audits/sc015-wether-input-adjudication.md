# SC015 supplementary wether-input decision

## Identity

- SC id: SC015; executable identifier: `PNWGmcILowering`.
- Branch/base: `update`, `695609f33ebd039c46a1c53bad173699b7b7fcef`.
- This is the user's explicitly authorized lexical selection for Old English
  row 2283, not a historical adjudication of SC015. The existing registry
  remains unadjudicated, with empty verdict and memo fields. Its historical
  metadata, rule, conditions, order and chronology relations are unchanged.
- The standard strict input-adoption interface requires this SC-numbered memo
  path. That technical association does not confer a sound-law verdict.

## Question

Does the comparative evidence support masculine nominative singular PGmc
*weþruz, CAPR *wéθruz, instead of the selected *wíθrą? Gothic wiþrus,
masculine cognates and an explicitly attested reconstructed nominative would
support it; missing u-stem evidence or an incompatible complete derivation
would require reconsideration. Output convergence cannot choose between
the source-supported u- and a-stems.

## Current state (before any edits)

Both reconstructed fields of row 2283 were *wíθrą; target weþer and class
regular. The shared representations in cognate set 307 were identical for
German 1119, English 1120 and Dutch 1121. Those are shared etymological
fields, not permission to alter daughter-language forms or research their
runtime cascades. Weather 2280 is a different etymon and remains unchanged.

The selected corpus has 387 runnable rows, six additional research-only OE
rows, 379 matches and eight mismatches: 1973, 2013, 2030, 2162, 2224, 2240,
2298, 2300. There are no rejected or ambiguous selections.

The SC015 registry records `pnwgmc/pan_pnwgmc`, confidence A, unadjudicated.
The unchanged rule lowers first-syllable i/í before one or more permitted
coronals and a following non-high vowel, excluding preceding velars. Its
derived position is 17; executable position is not historical dating evidence.
The stressed clause is `{*í} -> {*é} || .#. EnglishStarNonVelarConsonant* _
EnglishStarCoronal+ EnglishStarNonHighVowel`; the unmarked i clause is parallel.
The existing Hill investigation and current reader supply the qualified
historical analysis; this lexical correction does not reopen it.

## Diagnosis

Fresh `SC015 --prepare` and `--evidence` established every pre-adoption live
application, not just the disputed noun:

| Row | Input | Immediately before → after SC015 | Final |
| --- | --- | --- | --- |
| 2124 meed | *mízdai | *m*í*z*d*ē → *m*é*z*d*ē | meorde |
| 2137 nest | *nístą | *n*í*s*t*ą → *n*é*s*t*ą | nest |
| 2283 wether | *wíθrą | *w*í*θ*r*ą → *w*é*θ*r*ą | weþer |
| 2302 world | *wír-àldu | *w*í*r*à*l*d*u → *w*é*r*à*l*d*u | weorold |

The first, second and fourth remain live applications. New wether is an
inherited-e negative, not an exemption added to the rule. World's existing
conditional SC015–SC036 relation is neither tested anew nor promoted here.

`wether-input-trials.py` and its deterministic gzip receipt record both
source-supported input-only alternatives against the exact pre-adoption
source and corpus hashes. Each protected isolated complete wrapper reproduces
all 387 canonical finals. All 107 named canonical checkpoints are compared
for every row, using provenance-checked snapshot bins: the laws are identical,
so recompiling every prefix is unnecessary. Every checkpoint of the other
386 selections is unchanged. Both alternatives retain the same eight
mismatches, without rejection, ambiguity or protected-artifact mutation.

| Checkpoint | Former input | Selected u-stem | Alternative a-stem |
| --- | --- | --- | --- |
| Input | *wíθrą | *wéθruz | *wéθraz |
| SC015 lowering | *wéθrą | *wéθruz, unchanged | *wéθraz, unchanged |
| SC020 final z loss | *wéθrą | *wéθru | *wéθra |
| SC041 bare a loss | *wéθrą | *wéθru, unchanged | *wéθr |
| SC047 nasal apocope | *wéθr | *wéθru, unchanged | *wéθr, unchanged |
| SC063 high-vowel loss | *wéθr, unchanged | *wéθr | *wéθr, unchanged |
| Epenthesis | *wéθer | *wéθer | *wéθer |
| Native orthography | weþer | weþer | weþer |

The u-stem differs from the former path at 71 named checkpoints, converging
at SC063. The a-stem differs at 55, converging at SC047. The complete receipt
retains every state, including unchanged ones. Only four application statuses
change for the adopted u-stem: SC015 −1, SC020 +1, SC047 −1, SC063 +1.
No other rule gains or loses a live application as a result of this selection.

The first attempt to compile all prefixes redundantly exceeded the existing
600-second compiler limit; it made no canonical change and is not a failed
historical prediction. The completed input-only assay instead uses the same
protected full-wrapper control plus all existing, provenance-checked prefixes.

## Literature

- Kroonen (2013, p. 584), original sheet 624: *weþru-; masculine Gothic
  wiþrus 'lamb, young ram', ON veðr 'ram', OE weðer, OS withar and OHG widar.
  The printed headword label “adv.” is anomalous and retained in diplomatic
  evidence, not silently corrected into a quotation. The connection with
  the PIE year root is expressly conditional; if correct, the original
  meaning was 'yearling, one-year-old animal'.
- Orel (2003, pp. 459–460), original sheets 498–499: explicitly
  *weþruz ~ *weþraz, masculine; Norse retains u-stem traces. The year
  etymology is asserted more affirmatively, with Hittite, Greek and Albanian
  year comparanda. The complete nominative is printed, not assembled from
  Kroonen's citation stem and an unacknowledged ending.
- Kluge–Seebold (2011, 25th edition, pp. 985–986), original sheets
  1056–1057, edition verified on sheets 4–5: masculine *weþru-, or a similar
  formation. The year connection is conditional, the Latin calf comparison
  phonologically difficult, and an alternative sheep-root account is noted.
  No noun-specific, settled OHG raising chronology is supplied.
- Bosworth–Toller (1898, main dictionary p. 1212), actual entry and printed
  facsimile at `https://bosworthtoller.com/35485`: weþer, es; m., 'a wether,
  a ram', hence genitive weþeres. The locally held PDF is the separately
  catalogued Supplement, not a verified original of this main-volume page.
- Fulk (2018, p. 59): Gothic short e/i merger; p. 69: continental
  u-conditioned raising with failures; pp. 91–92: final sonorant
  vocalization and high-vowel loss; p. 163: heavy u-stems and
  inflectional reclassification. The general continental development is
  not promoted into a completely demonstrated history of every wether cell.

The Gothic and Norse lexical forms were checked in the original comparative
dictionaries, not falsely attributed to independent newly consulted lexica.
Masculine Norse veðr 'ram' is separate from neuter veðr 'weather'.
The lexical source ledger records the full source and page provenance.
The existing reconstruction survey, its tranche-44 evidence and the frozen
SC015 report (especially its wether section) were consulted and reconciled.

## Historical analysis

Both selected reconstructed fields are the masculine nominative singular at
the Proto-Germanic stage. No exceptional entry-stage sidecar is needed because
PROTO and PROTOFORM agree. Confidence and historical stage remain independent.
Gothic wiþrus positively supports an older u-stem; its i does not establish
inherited i because Gothic raised short e. The West Germanic masculine
paradigm can reflect reclassification and does not require an inherited a-stem.

CAPR theta and acute stress are transcription conventions. The endpoint
derivation verifies the complete nominated cell, including loss of z and u
and subsequent epenthesis; its success is not the reason for preferring it.
The a-stem is legitimate but has less positive evidence for original
inflection here. Its exact remodelling date and the deeper year etymology
remain unresolved. No new historical edge, stage assignment or independence
claim about dialectal lowering is made.

## Verdict

ADOPT the authorized lexical reconstruction and selected nominative
*wéθruz; RETAIN every production law, context and order. This is not an SC015
historical verdict, so there is deliberately no machine-readable
`Registry-verdict:` declaration. SC015 remains unadjudicated in its existing
registry. The positive u-stem evidence, not a model score, chooses the input;
the alternative *wéθraz remains in the research record and book.

## Propagation (only after verdict)

Exactly PROTO and PROTOFORM change on rows 1119, 1120, 1121 and 2283; every
other corpus field, daughter target, class and sidecar is preserved. The new
regular-class `.model.md` is selected through the existing combined-book
class manifest and independently certified through `editorial_cases.tsv`
for the complete derivation report. It adds only wether, not a new assembly
route or unrelated entry. The book contains historical argument only.

Current survey coverage, comparison and commentary supersede the unsupported
selected-input conclusion without altering source-native forms, analyses,
consultation identities or original tranche-44 receipts. The old SC015
investigation and all its experimental receipts remain byte-identical
historical research; the current reader identifies three live applications.

The strict `approved_wether_input_migration.json` and exact original380
mapping authorize only row 2283's three baseline input fields. All 387 final
outputs and match flags stay identical. Before migration, the input-sensitive
fingerprint consequences were calculated explicitly:

| Projection | Authorized new SHA256 |
| --- | --- |
| Evaluator input plus output | `3caa0d07ba4f63c7ba512a22e48a7be86f975e573ae01d7cbea830eb08d4b1e0` |
| Lexical input plus output | `32d551ca5bc6317a6e528f00259159915599c6e08d265af170e2be7341edb522` |
| Active original380 | `3a676cc3d591bb2d7ae34784c30b07e62b1f9ff880b40292b5e6e020dcde247f` |

Adoption uses `SC015 --adopt-cell-baseline --approval
approved_wether_input_migration.json`. The named `*_pre_sc015_wether_input.*`
archive preserves the previous active baseline separately from rust, straw,
hue, knee, context and gift archives. Immutable legacy380 remains
`fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.
Canonical propagation uses `adjudicate.py --refresh`, not SC015 finalization.
Focused tests protect the exact fields, both full-corpus trials, all
checkpoints, unchanged laws/registry/history, strict transition failures,
archive idempotence and the historical-only certified book note.

The strict adopter completed successfully and independently reproduced all
three predicted fingerprints. Canonical refresh reports CONTROL PLANE CLEAN.
The current coverage census has exactly the four predicted deltas:
SC015 4 -> 3, SC020 112 -> 113, SC047 159 -> 158, SC063 63 -> 64.
The actual full trace, not merely the private receipt, preserves every state
of the other 386 lexical entries. The 80-file immutable preparation audit
finds only seven declared changed files: the corpus, approved migration map,
active baseline and summary, and generated equivalence report, coverage
census and annotations. All 73 other protected hashes and all 18 pre-existing
baseline archives/approval files are unchanged.

The complete Germanic run recorded 1,386 passing tests, five failures and
8,555 passing subtests. The failures exposed historical migration fixtures
incorrectly including the later wether
mapping, or the undeclared publication fingerprint delta. Those historical
fixtures now retain their exact earlier migration scope and all old hash
assertions. The exact semantic additions/removal are declared in
`index_semantic_fingerprint_allowlist.tsv`, with negative controls proving
that each remains necessary. The combined final coupled run passes all
189 tests and 1,221 subtests, including all five corrections, the new
all-entry full-trace check and the exact four application deltas. No production
validation rule or scientific invariant was relaxed.

After publication, the coupled adoption, archive, index and editorial checks
passed 116 tests and 1,113 subtests. A fresh official `SC015 --evidence`
rebuild again confirmed all 387 selections and exactly the three current
lowering applications. Final nonmutating artifact-graph verification reports
CONTROL PLANE CLEAN. The SC-specific adjudication check is not a completion
gate for this lexical-only decision: it requires an adjudicated registry
record, which this task deliberately does not create.

The standard, unbypassed combined-book build completed. Its semantic,
predicted-form, paragraph-gloss, bibliography, citation-locator, reference,
heading-wrap, index-emission/parity, print-readiness and 18 index negative
checks pass. The combined PDF has 318 pages; wether is section 6.77,
printed pp. 188–189. The three-row SC015 census and inherited-e wether
paragraph are on p. 17. Native and reconstruction index entries are on
pp. 313 and 315 and point to the wether heading on p. 188. The standalone
lexical PDF has 154 pages. Actual rendered prose, quantities, dental signs,
citations, ending trace and both index entries were visually inspected.
The final note has approximately 415 words (416 whitespace tokens including
lexical-span attributes). Sanskrit uses the existing explicit lexical-span
markup so the assembly cannot consume its stem-final emphasis delimiter;
the historical wording and calf gloss are unchanged.

The inspected combined PDF SHA256 is
`d3ed19d1702f51ab493ddebd3e5d025a4215444d96b7ca8ec7aec280dc015fd8`.
The render still prints unrelated existing missing-character warnings for
angle brackets/control characters elsewhere in the volume; none occurs in
the inspected wether passage. They did not bypass or fail a publication gate.

## Residue

The a-stem's date and relation to the u-stem, precise continental vocalism
history and ultimate year connection remain qualified. These do not prevent
the positively supported masculine u-stem selection. The broader SC015
formulation, historical verdict and chronology are expressly outside this
decision. The lexical correction and its publication are complete; they do
not select a new SC015 formulation or settle the remaining historical questions.
