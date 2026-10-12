# SC032: quantity-distinct English diphthong realization

## Identity

- **SC id:** SC032.
- **Executable identifier:** `OEDiphthongLeveling`; the retained name is
  neither a phonological analysis nor a historical-stage argument.
- **Date / branch / base commit:** 2026-10-12, `workstream/sc032`,
  `7848f762`; isolated worktree `capr-sc032-workstream`.

## Question

- **Hypothesis or suspected problem (falsifiable):** the nine clauses
  conflate English realization of heavy inherited/secondary diphthongs,
  a later io/eo endpoint and short representation helpers. They do not
  constitute one West-Saxon-only smoothing or leveling law. The head
  displacement boundary may depend on a missing internal vowel symbol,
  rather than independently demonstrating the date of offglide change.
- **Confirmation / refutation:** literal clause populations, actual
  feeders, source quantity and dialect contrasts can confirm this.
  A source establishing one uniform WS event and a phonological head
  dependency independent of CAPR token membership would refute it.
  Equal final spellings alone cannot decide either question.

## Current state (before any edits)

- **Existing historical characterization:** registry
  `ws_oe / west_saxon`, confidence A, unadjudicated, “OE Diphthong
  Leveling”; staging note “West Saxon specific diphthong simplification
  chain; four SCs covered together; all are WS OE stage”.
- **Existing executable behavior:** position38 in the prepared executable
  model, immediately after SC110. Unconditional parallel replacements:
  atomic aeu/áeu → ēa; eu/éu/iu/íu → ēo; split e+u → eo,
  é+u → éo, i+u → eo. There is no split í+u clause. Atomic inputs
  are single symbols; split inputs contain two starred symbols.
  Atomic acute is discarded, whereas split é retains acute; acute is
  stress notation, not length or selected sentence stress.
- **Selected-input assumptions:** the live selected387 corpus and its
  adopted contexts are unchanged. Knee2085 selects *knéwai → cneowe,
  preserving citation *knéwą; hue2332 selects *xíwją → hīew.
  You2326 has independently selected weak-final context despite root
  acute. PROTO, selected PROTOFORM, whole-cell construction, target and
  author reconstruction are different records. No new witness or
  invented PGmc input is needed.
- **Existing verdicts/dossiers consulted:** CURRENT_STATE, protocol,
  registry/edges/notes, CONTROL_PLANE, canonical --next and SC032
  --prepare, 031–034 dossier (especially current §§16,18–19), SC031
  glide adjudication, SC033 and hue follow-up, SC029/030 and SC043
  dispositions, comparative synthesis and PGmc integration resumption.
  Historical sections/cards are retained as records, not revived.

## Diagnosis

### Runtime and complete firing census

Both existing backend containers bind the main worktree. Neither was used.
A separate compose project `capr-sc032` uses the existing backend image,
no published ports and explicit isolated backend/data/fsts/tools/docs mounts.
Container state, `/usr/app`, source/tool mounts and foma/flookup availability
were verified before canonical SC032 --evidence. Its forced rebuild proves
production/sandbox equivalence for all387 rows and validates the build
manifest. The first attempt stopped at an absent ignored held PDF after
rebuilding; restoring the existing local holdings into this worktree allowed
the complete canonical evidence command to finish. No main file was edited.

Source observations: FST SHA256
`f0c69af7233a17dc0e0d15c0c45b97054f6c071947fa85d3f66192596943a953`;
corpus SHA256
`67fb85b3f944afe6f0f3f0a99536f9bd70bf707246d968577b16fca5b17aece6`.
Fresh census: **32/387 rows**, with **32 clause applications**, no row
matching two clauses and no repeated clause application within a row.
The original380 identity subset contains31 of these (all except you);
the additional selected seven contain you only. This is a current subset
classification, not a re-execution or alteration of the immutable legacy
archive's old inputs.

| Clause | Literal input → output | Selected387 applications | Original380 |
|---|---|---:|---:|
| 1 | `{*aeu}` → `{*ēa}` | 0 | 0 |
| 2 | `{*áeu}` → `{*ēa}` | 20 | 20 |
| 3 | `{*eu}` → `{*ēo}` | 0 | 0 |
| 4 | `{*éu}` → `{*ēo}` | 10 | 10 |
| 5 | `{*iu}` → `{*ēo}` | 0 | 0 |
| 6 | `{*íu}` → `{*ēo}` | 2 | 1 |
| 7 | `{*e} {*u}` → `{*eo}` | 0 | 0 |
| 8 | `{*é} {*u}` → `{*éo}` | 0 | 0 |
| 9 | `{*i} {*u}` → `{*eo}` | 0 | 0 |

### Nine-component interpretation ledger

“Unmarked” below is literal CAPR notation, not a source-proven claim of
sentence stresslessness. Historical offglides are not equated with
independent syllabic u; neither atomic nor split spelling supplies a
complete phonemic analysis. The rule contains no conditioning context.

| Clause | Input value and quantity premise | Output / notation | Actual feeder and positive / negative control | Historical identity, scope and printed-page proof |
|---|---|---|---|---|
| 1 aeu | Unmarked atomic fronted-au, heavy diphthong tier; aeu is an encoding, not demonstrated phonetic triphthong | Long ēa | SC030's unmarked au branch is the potential producer; no live positive. Formal aeu→ēa; unfronted au remains unchanged | Same English fronted-au continuation as clause2, not a distinct unstressed event. Not all Northumbrian dialects unround. Ringe–Taylor p.172; Campbell pp.53–54,116–118 support the historical continuation, not this unused accent convention |
| 2 áeu | Acute atomic fronted-au; stress and length are separate | Long ēa, acute removed | SC030 on inherited au and products of SC029/031. Bread/head/dew/hew positive; singleton show/straw negative | Packages nucleus quantity and offglide realization, following fronting; neither smoothing nor leveling. English majority outcome, not WS-only; Ringe–Taylor pp.172–173; Campbell pp.53–54,116–118 |
| 3 eu | Unmarked atomic e-nucleus/u-offglide diphthong, heavy tier | Long ēo | Potential inherited atomic eu or SC031's unmarked eww; no live positive. Formal eu→ēo versus split e+u→short eo | English tensing/realization, broader than WS. Ringe–Taylor pp.173–175; Campbell pp.53–54,116–118. The unused notation branch is not independently dated |
| 4 éu | Acute atomic e-nucleus/u-offglide diphthong, inherited or created by early reanalysis | Long ēo, acute removed | Inherited breast/freeze etc.; SC031 on chew/four, with SC008 supplying four's ww. Split é+u is a short negative to long realization | Same English long eu history, with distinct input origins. Retained w is consonantal, not lengthening caused by SC032. Ringe–Taylor pp.41–42,65–66,173–175; Campbell pp.53–54,116–118 |
| 5 iu | Unmarked atomic high-front nucleus/u-offglide diphthong, heavy tier; early realization is long io, not initial eo | Long ēo endpoint | Potential inherited atomic iu or SC031 iww; no live positive. Formal iu→ēo; already-realized īo is negative | Bundles English realization and later selected io/eo endpoint. Northumbrian io and differing Mercian/WS convergence are controls on universal identity. Ringe–Taylor pp.174–175; Campbell pp.53–54,124–126 |
| 6 íu | Acute equivalent of clause5, with secondary origins actually selected | Long ēo, acute removed | SC009 contraction in friend; SC008/031/098 chain in you. Hue's already-realized īo and knee's singleton short e+w are negatives | Not one inherited-PGmc input class or a proven pre-mutation io merger. Ringe–Taylor pp.41–42,174–175; Campbell pp.124–126; separate hue account Ringe–Taylor p.250 |
| 7 e+u | Two-symbol short-tier helper; no demonstrated live origin. Not permission to contract arbitrary syllabic hiatus | Short eo | No actual selected feeder/positive; formal e+u→eo versus atomic eu→long ēo | Retained representation normalization. Campbell pp.116–118 supports short counterparts in breaking/back umlaut, not CAPR token boundaries or this exact historical domain |
| 8 é+u | Acute short-tier counterpart of clause7 | Short éo, stress retained | No actual selected feeder/positive; formal é+u→éo versus atomic éu→long ēo | Same compatibility status; stress retention is a notation choice, not an independent sound event. Campbell pp.116–118 supplies quantity contrast only |
| 9 i+u | Two-symbol short high-front/offglide helper; no selected feeder | Short eo, not long ēo | No actual selected positive; formal i+u→eo, while missing split í+u remains unchanged | Packages short realization and a selected io/eo endpoint, without licensing generic i+u hiatus treatment or an invented stressed counterpart. Campbell pp.116–118,124–126 distinguishes short diphthongs and later convergence, not the exact helper domain |

Complete live before/after population (stars delimit symbols, not spelling):

| Row | Concept | Before SC032 | After SC032 |
|---|---|---|---|
| 1944 | believe | `*g*a*l*áeu*b*i*j*a*n*ą` | `*g*a*l*ēa*b*i*j*a*n*ą` |
| 1961 | bow, verb | `*b*áeu*g*i*j*a*n*ą` | `*b*ēa*g*i*j*a*n*ą` |
| 1962 | bow, noun | `*b*áeu*g` | `*b*ēa*g` |
| 1966 | bread | `*b*r*áeu*d*ą` | `*b*r*ēa*d*ą` |
| 1968 | breast | `*b*r*éu*s*t*ą` | `*b*r*ēo*s*t*ą` |
| 1976 | chew | `*k*éu*w*a*n*ą` | `*k*ēo*w*a*n*ą` |
| 1988 | deer | `*d*éu*r*ą` | `*d*ēo*r*ą` |
| 1989 | dew | `*d*áeu*w*u` | `*d*ēa*w*u` |
| 1995 | dream | `*d*r*áeu*m*a` | `*d*r*ēa*m*a` |
| 2018 | flea | `*f*l*áeu*x` | `*f*l*ēa*x` |
| 2019 | flee | `*f*l*éu*x*a*n*ą` | `*f*l*ēo*x*a*n*ą` |
| 2022 | fly | `*f*l*éu*g*a*n*ą` | `*f*l*ēo*g*a*n*ą` |
| 2028 | forlorn | `*l*éu*s*a*n*ą` | `*l*ēo*s*a*n*ą` |
| 2029 | four | `*f*éu*w*a*r` | `*f*ēo*w*a*r` |
| 2032 | freeze | `*f*r*éu*s*a*n*ą` | `*f*r*ēo*s*a*n*ą` |
| 2033 | friend | `*f*r*íu*n*d` | `*f*r*ēo*n*d` |
| 2061 | hay | `*x*áeu*j*ą` | `*x*ēa*j*ą` |
| 2063 | head | `*x*áeu*b*u*d*ą` | `*x*ēa*b*u*d*ą` |
| 2074 | hew | `*x*áeu*w*a*n*ą` | `*x*ēa*w*a*n*ą` |
| 2094 | leaf | `*l*áeu*b*ą` | `*l*ēa*b*ą` |
| 2097 | leek | `*l*áeu*k*a` | `*l*ēa*k*a` |
| 2102 | light | `*l*éu*x*t*i*j*a*n*ą` | `*l*ēo*x*t*i*j*a*n*ą` |
| 2116 | lye | `*l*áeu*g*u` | `*l*ēa*g*u` |
| 2135 | need | `*n*áeu*d*i` | `*n*ēa*d*i` |
| 2151 | reek | `*r*áeu*k*a` | `*r*ēa*k*a` |
| 2170 | seam | `*s*áeu*m*a` | `*s*ēa*m*a` |
| 2184 | shove | `*s*k*áeu*b` | `*s*k*ēa*b` |
| 2225 | stream | `*s*t*r*áeu*m*a` | `*s*t*r*ēa*m*a` |
| 2227 | strew | `*s*t*r*áeu*j*a*n*ą` | `*s*t*r*ēa*j*a*n*ą` |
| 2241 | team | `*t*áeu*m*a` | `*t*ēa*m*a` |
| 2246 | thief | `*θ*éu*b*a` | `*θ*ēo*b*a` |
| 2326 | you | `*íu*w` | `*ēo*w` |

All32 are in-domain English long-tier realization applications under the
adopted reconstruction/cell accounts. Strew's selected WS endpoint is
reconstructed, not an attested spelling; the census's generic “attested”
label is not an evidential upgrade. The zero populations establish no
historical positive witness. In particular the FST's “from palatal glide”
comment does not identify a current feeder: SC016 is later orthographic
handling and emits atomic eo directly, not split e+u before SC032.

### Principal traces and witness roles

- **Inherited au:** bread, head and the other inherited atomic-au rows
  receive áeu from SC030; all are live applications and first-element/
  offglide feeding examples. Dew/hew additionally receive áu+w from
  inherited SC031 reanalysis. Hay/strew receive áu+j from settled SC029.
  The following w or j is not deleted by SC032.
- **Inherited eu:** breast/deer/flee/fly/forlorn/freeze/light/thief
  retain their selected atomic diphthong to clause4. Chew and four
  receive éu+w from SC031; four is first supplied ww by SC008.
  Deer retains its already modeled paradigm treatment; SC032 does not
  adjudicate its endingless/levelled r.
- **Secondary iu:** friend receives íu+nd from SC009 contraction of
  selected í+j+ō+nd+z. You receives íu+w+i from SC008→SC031, loses
  final i through adopted SC020/SC098 context, then receives ēo+w.
  Their secondary inputs do not date all inherited eu/iu origins alike.
- **Hue negative:** `*x*í*w*w*j*ą` → SC033
  `*x*íu*w*j*ą` → SC110 `*x*īo*w*j*ą`; SC032 leaves it unchanged,
  SC055 later gives īe. SC110 preempts the ordinary atomic iu matcher:
  executable bleeding, not an independently proved universal historical
  order. Knee's short `*k*n*é*w*ē` is also unchanged here; SC044
  supplies short éo. These settled controls are not reopened.
- **SC034 negatives:** show2186, straw2224 and show2317/2318 are singleton
  a+w paths, not current SC032 applications. No old dew/hew SC034
  boundary is reinstated.
- **Head:** SC032 gives `*x*ēa*b*u*d*ą`; later SC040 changes
  `*ç*ēa*β*u*d` → `*ç*ēa*β*o*d`. Before realization, atomic áeu
  is absent from `PGmcStarVocalic`/`EnglishStarVocalic`. SC040's
  left-context therefore cannot recognize that vowel at all. The old
  hēafud displacement is a **model-local recognition dependency**,
  not proof that a rounded diphthong historically blocked medial lowering.
- No live out-of-domain firing, counterfeeding or counterbleeding witness
  was found for SC032. You's loss of the mutation trigger is a SC098
  bleeding control, not a new SC032 edge. No additional private
  counterfactual is warranted: literal membership and source contrasts
  resolve this question without manipulating a corpus input.

## Literature

- **Existing CAPR dossiers checked:** the current chain dossier,
  comparative synthesis and source-local contrasts, SC029/030,
  SC031, SC033/hue and the integration resumption cited above. The
  completed thirteen-source AF survey is not repeated or replaced.
- **Direct sources checked, printed pages:** Ringe–Taylor2014
  pp.170–175 (§6.1.2); Campbell1959 pp.52–54 (§§132–138),
  pp.116–118 (§§275–278), pp.124–126 (§§293–297),
  pp.155–156 (§373), and pp.95–96 (§§225–227) to check the old
  opening's misplaced smoothing citation. Page headings, not PDF/OCR sheet counts, determine
  these locators. Existing adopted source accounts supply the early
  feeders (Ringe–Taylor pp.41–42,65–66), awwj (p.173),
  and separately palatalized hue (p.250).
- **Source-supported phenomenon:** Ringe–Taylor p.175 explicitly
  identifies tensing/lengthening of diphthong nuclei as a common change
  preceding breaking, followed by subsequent offglide developments.
  P.172 separates fronting/tensing of au from later offglide
  unrounding/lowering, with Northumbrian non-unrounding; pp.173–175
  distinguish eu, iu, inherited ww products and contraction-created
  inputs. Campbell pp.53–54 likewise includes secondary WGmc
  diphthongs, while pp.116–118 distinguishes long inherited and short
  breaking/back-umlaut histories. Campbell pp.124–126 distinguishes
  retained Northumbrian io, Mercian convergence and WS io/eo overlap.
  Thus direct iu→ēo packages an earlier io realization and a subsequent
  selected dialectal endpoint; it is not the initial English eu law.
  Campbell pp.155–156 documents both hēafud and hēafod, not a strict
  diphthong-offglide condition on the lowering.
  His pp.95–96 instead discuss conditioned smoothing of ea/eo to
  monophthongs, prominently in Anglian; that passage does not prove
  these au/eu/iu-to-diphthong realization clauses.
- **CAPR modelling decisions (not source claims):** atomic symbols
  carry the heavy/long tier; aeu is a transient spelling for fronted
  au, not a phonetic transcription of a newly proved three-vowel
  sequence. Single ēa packages quantity and final spelling even though
  its phonetic nucleus is fronted and historical spellings vary.
  Ordinary iu→ēo is an endpoint proxy in the pre-mutation cascade:
  its position does not date the io/eo merger before mutation.
  Split e+u/é+u/i+u produce short eo, with the last also packaging
  an io→eo endpoint. The sources do not specify CAPR token boundaries,
  prove the unused clauses' exact historical conditioners, supply an
  absent stressed-i clause, or prove their alleged palatal-glide origin.

## Historical analysis

- **Historical stage:** multiple English developments, from pre-OE
  nucleus tensing/offglide realization to OE dialectal io/eo convergence.
  Registry `oe` is an umbrella for this retained bundle, not one
  uniformly dated event. The early common tensing belongs before
  breaking in Ringe–Taylor's account (p.175); the complete nine-clause
  network cannot inherit that whole-event order merely by association.
- **Historical scope:** English realization, not an exclusively WS
  innovation. Au→ēa excludes Northumbrian varieties preserving the
  rounded offglide; eu realization is broader; io→eo supplies the
  chosen WS endpoint with non-WS parallels and Northumbrian negatives
  (Ringe–Taylor pp.172–175; Campbell pp.116–118,124–126).
  This does not reopen the synthesis's competing AF stem assignments.
- **Proxy versus phenomenon:** retain a quantity-distinct compound
  realization network, not a newly named smoothing law. Nucleus
  tensing, offglide change and dialectal convergence are historically
  distinguishable; they are documented separately without inventing
  new executable identities or a speculative sequence of atomic tiers.
  Confidence A concerns established long English outcomes, not proof
  of one law, exact timing of all subevents, or unused helper domains.
- **Chronology:** SC030→SC032 is **independently demonstrated feeding
  for the fronted-au component**, anchored by Ringe–Taylor p.172,
  not by the archived18 no-output failures. The reciprocal card row
  SC032→SC030 describes the same earlier-boundary observation,
  not a reverse historical order. SC031→SC032 is independently
  supported feeding for inherited/coronal-created a/e/i+ww products
  (Ringe–Taylor pp.41–42,65–66,172–175); uww is not included.
  SC009 feeds friend by contraction (p.175); its ancestral origin
  precedes English realization, without dating the later io merger.
  SC032→SC040 is demoted to **technical**, with its frozen measurement
  retained. SC033→SC110 preempts hue's ordinary iu consumption;
  this is model-local serialization. SC032 output permits later
  SC055 mutation and other English consumers, but this is not proof
  that every subevent preceded them. No new strict whole-bundle
  breaking edge, counterfeeding, counterbleeding or universal
  pre-mutation io-merger edge is adopted.

## Verdict

- **Verdict:** REFORMULATE identity, scope and chronology metadata;
  RETAIN all nine executable clauses, identifier, quantity distinction,
  serialization, selected inputs/contexts/targets and final outputs.

Registry-verdict: SC032=REFORMULATE

The long applications have source-supported English histories, but
“WS diphthong leveling/smoothing” misidentifies both their event structure
and distribution. The retained network realizes several endpoints and
unwitnessed short encoding paths; common spelling does not unify their
quantity or chronology. Source-supported au feeding remains authoritative,
while head's token-recognition boundary does not. Physical decomposition
or a new early io tier is not justified merely to make terminology tidier.

## Propagation (only after verdict)

- **Affected files/registries:** SC032 registry row, human inventory note,
  component-scoped chronology notes/technical head boundary and sourced
  SC031 feeder, this memo, SC032 reader, current continuation of the
  031–034 dossier and comparative synthesis; new regression/control
  tests and canonical finalize-generated projections.
- **Regression tests:** all-clause formal quantity/stress controls,
  corpus census including overlaps and original380 membership, source
  metadata/chronology, head's actual vowel membership, paired hue/knee/
  SC034 negatives and adopted feeders. Unwitnessed formal strings
  are component fixtures, not invented lexemes or admitted PGmc forms.
  Existing frozen recipes are preserved unchanged.
- **Baseline/fingerprint effect:** none authorized or expected. No FST
  source edit, corpus field change, context change, migration or refreeze.
  Selected387 remains
  `47a901e9e4a7cd663b8eb574b87fe737382e8fc1b4f1bc8afc38701af0c96872`;
  original380 remains
  `70bdaba537d8f6b6bb7d872d00eefbef75127d2d77689af7ba01b35a79ebce39`.
  Knee/hue/gift/context receipts and immutable archives remain protected.
  All seven established mismatch identities remain unchanged.
- **Lexical implications:** explain dew/hew as SC031→SC030→SC032,
  chew/four as SC031→SC032, friend as SC009→SC032 and you as
  SC008→SC031→SC098→SC032. Do not relabel their endpoint as evidence
  for one WS-only law. Hue and knee remain separate negative controls;
  head's lowering needs no new input. Stream2 owns lexical SOURCE
  entries; this stream changes none of them and communicates these
  implications rather than editing them concurrently.

## Residue

- Unused unaccented atomic and all split clauses lack selected-corpus
  positive witnesses. Their formal behavior is retained, not certified
  as independently established historical events. A future source-backed
  domain extension, new witness or input migration requires its own gate.
- The strict io/eo phonemic chronology, nucleus dating, author-level
  analyses and full AF ancestral inventory are not uniquely resolved by
  these32 applications. Existing source-local commitments remain distinct.
- No author-choice or baseline gate is crossed by this metadata-only
  verdict. SC034 remains the next pending historical identity; it is not
  investigated or adopted here.

## Completed verification and publication

- Canonical isolated SC032 --evidence completes with32 applications;
  production/sandbox equivalence covers all387 selected rows. Final
  SC032 --finalize reports CONTROL PLANE CLEAN and passes propagation.
  The bin synchronization check confirms107 fresh expected bins.
- The unchanged released `post-hue-controls` assay passes68 component,
  13 staged and14 corpus fixtures. The separate `sc032-controls`
  recipe passes all16 literal checks: nine positive clauses and seven
  paired representation/quantity negatives. Both independently prove
  full-wrapper identity across387 rows, unchanged selected inputs and
  finals, the same seven mismatch IDs
  (1973,2013,2030,2162,2240,2298,2300), no rejection/ambiguity and
  unchanged bytes for all131 protected artifacts. The new recipe makes
  no intervention and preserves all four released source/context pins;
  its formal checks do not admit any new word. The reused historical
  fixture file selects no additional named corpus fixtures for this new
  recipe; the all-row comparison and committed census tests are separate.
- Fresh native assay outputs were also compared by stable ID directly
  with every frozen selected387 record: zero assembled-input, output or
  multiplicity differences. Recomputed evaluator387 is
  `47a901e9e4a7cd663b8eb574b87fe737382e8fc1b4f1bc8afc38701af0c96872`;
  lexical387 is
  `90789094b8d8889bb478dd6077de75e1d8e1cb66b7b6d347b63e73a83d039c47`;
  the approved original380 projection is
  `70bdaba537d8f6b6bb7d872d00eefbef75127d2d77689af7ba01b35a79ebce39`.
  The unchanged immutable original380 archive recomputes to
  `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.
  These are measured observations, not hashes obtained by altering or
  adopting a baseline.
- The full Germanic suite was executed inside the isolated container,
  never using host foma. It reports1258 passed,7340 passing subtests,
  17 skips and9 failures. Two directly related failures were corrected:
  the next-SC assertion now expects SC034, and canonical finalization
  closes the reader projection briefly made stale during the layout
  inspection. The completed affected retest passes53 tests and5 subtests,
  including SC032, all memo/registry agreement, queue, protocol and census
  guards.
- **Seven pre-existing suite failures remain, not hidden or repaired
  under this scope:** five index-variety assertions and two infrastructure
  graph-authority assertions. Unmodified base7848f762 already contains
  2453 production occurrences and2365 print-main occurrences, whereas
  those tests pin2456/2368; the cud variety audit also points at obsolete
  source locations. The unmodified graph already has the PGmc survey and
  lexical-integration nodes omitted from the two infrastructure tests.
  These are baseline test/audit reconciliation issues, not SC032 output
  regressions. They were communicated to the other publication streams
  and coordinator; lexical SOURCE entries and those unrelated assertions
  are untouched.
- The normal unbypassed reader-section20 Docker build passes style,
  citations, Foma width, section order, generated-prose, cross-reference,
  chronology-evidence and heading gates. The actual121-page PDF was
  inspected: SC032's source/quantity discussion and complete nine-clause
  block are on printed p.70, and its selected endpoint, au feeding and
  technical head dependency continue on p.71. The first render left the
  closing bracket alone on p.71; moving the unchanged block immediately
  after its labelled heading fixes that layout without a semantic change.
  Long/short signs, acute, reconstructed stars, selected-cell contrasts
  and page-numbered citations were checked in the final rendered output.
  PDF SHA256:
  `629c2f420712ecc2b59c675e4ce16b9a93675fa47061c5e8060a1ef47b36a535`.
  Existing missing angle-bracket glyph warnings elsewhere in the reader
  remain disclosed; no affected SC032 glyph is missing. No full combined
  book rebuild is claimed or required for this reader-only change.
- **Mechanical hygiene:** canonical refresh also reconciles two stale
  Fulk accountability hashes in the generated reconstruction-survey
  provenance; their SOURCE files are unchanged. Other regenerated
  registry/graph/reader/index/draft outputs propagate the SC032 verdict
  and prose. A final git comparison confirms unchanged FST/data/context,
  complete cascade-baseline authorities, frozen chronology cards, released
  recipes and lexical model-entry SOURCE bytes. No baseline is refrozen,
  no protected receipt is repinned and no corpus admission is made.

### Coordinated prose-errata integration

After the initial SC032 release `9faa93ab8d88e9067180bd634f28f3b88e271efb`,
the coordinator authorized merging the completed prose-only errata release
`b74e3ce3f60f05c8843555eb409b35020386dcf0`. The normal merge was conflict-free;
canonical SC032 finalization then regenerated the combined projections and
passed propagation checks with **CONTROL PLANE CLEAN**. No scientific runtime
rebuild or protected-baseline adoption was needed. The isolated worktree's
107 runtime bins remained fresh, and the queue still returns **SC034**.

The two graph-authority failures were reproduced using the exact committed
`7848f762` test and graph module sources, loaded in memory: **two tests,
two failures, zero errors**. Both sources are byte-identical to the current
files. The omitted pre-existing nodes are `pgmc_reconstruction_survey` and
`pgmc_lexical_integration`; neither assertion was changed. The five separate
index failures are independently reproduced against that same committed
base in the merged integration errata receipt. Thus the full-suite account
remains **nine initial failures, two SC032-related failures resolved, seven
proved baseline failures remaining**, not a globally green suite.

The post-merge focused SC032, registry, protocol and census guards pass
**53 tests and five subtests**. A comparison against the initial SC032 release
confirms unchanged FST/data, cascade-baseline authorities, registry SOURCE,
Anglo-Frisian synthesis and recipes, and the SC032/queue tests. The lexical
model prose and navigation changes in this merge are exactly the coordinated
errata work, not new lexical or sound-change scientific decisions.
