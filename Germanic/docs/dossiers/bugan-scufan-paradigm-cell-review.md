# Paradigm-cell review for *būgan* and *sċūfan*

## §1. Question

The cogset (`Germanic/data/germanic-aligned-final.tsv`) currently
targets the **3 pl. pret.** of two Class II strong verbs:

| Row  | PROTOFORM  | OE COUNTERPART | Note (verbatim from TSV)                                                                                              |
|------|------------|----------------|-----------------------------------------------------------------------------------------------------------------------|
| 1962 | `*búgun`   | `bugon`        | "Past 3pl. Infinitive būgan has analogical ū (Campbell §740); past 3pl bugon is lautgesetzlich from *bugun."          |
| 2184 | `*skúbun`  | `sċufon`       | "Past 3pl. Infinitive sċūfan has analogical ū (Campbell §740); past 3pl sċufon is lautgesetzlich from *skubun."       |

Both rows were retargeted from the infinitive (`*beuganą / būgan`,
`*skeubaną / sċūfan`) to the 3 pl. pret. in the same session that
introduced the policy of picking a **Lautgesetzlich paradigm cell**
in preference to a known-analogical citation cell (session
checkpoints 064 and 065, dated 2026-04-06/-07; see §2 below).

The research outcome of §17.51.A1.3 in `DEV_NOTES.md` has now
established (via Appendix D of `widuwe-u-preservation.md` and
dossier `un-to-on-chronology.md`) that the OE-internal change
`*-un > -on` is **phonologically blocked** by stem-`u` harmony in
exactly the environment these two verbs occupy: stressed `*ú` +
single consonant + unstressed `*-un`. The lWS-attested forms
`bugon`/`sċufon` are therefore not a Lautgesetz outcome but an
**analogical levelling** on the dominant `-on` ending elsewhere in
the strong-verb paradigm. The FST output `bugun`/`sċufun` is the
phonologically correct early-OE / Mercian form, but is
**type-unattested for these two specific lexemes** (dossier
`bugun-scufun-attestation.md`).

This dossier asks whether — knowing now what we did not know in
checkpoint 065 — the **3 pl. pret. is still the right paradigm cell
to target**, and whether some other cell of the same paradigm would
be both Lautgesetzlich and attested for *būgan* and *sċūfan*
respectively. The question was prompted by the user's request:

> "We chose these forms precisely to be Lautgesetzlich. So we should
> also kind of review why is it we switched away from the infinitive
> to these forms, and kind of in retrospect, knowing what we know
> now, was it a mistake to choose these cells of the paradigm? Would
> there be a cell of these two paradigms that would have been more
> regular?"

The dossier treats *būgan* and *sċūfan* separately, surveys every
cell of each paradigm against (i) the regular Lautgesetzlich PGmc → OE
outcome and (ii) the attested OE form, and ends with a per-verb
recommendation.

## §2. Reconstruction of the original choice (checkpoints 064–065)

The decision to retarget rows 1962 and 2184 from the infinitive to
the 3 pl. pret. was made over two consecutive checkpoints in
April 2026.

**Checkpoint 064 ("class-ii-eu-paradigm-research.md")** records
the diagnosis that the OE infinitive is irregular:

> "OE būgan, sċūfan etc. are **analogical innovations**. Gothic
> biugan, OHG biogan preserve original *eu. … Since Gothic and OHG
> do not usually share innovations, it appears that most or all of
> the verbs with *ū must be innovative … The FST correctly produces
> *bēogan from *beugăną — the mismatch is expected."

The handbook basis is **Ringe-Taylor vol. 2 pp. 39–40** and
**Campbell §736(b)** (line 20300):

> "A few verbs are placed in Classes I–V because of the form of
> their past tenses and passive participles, but their presents
> diverge from those of most verbs of the classes in which they are
> placed. **A large group of verbs in Class II have ū (not éo) in
> the present system, e.g. OE brúcan enjoy, lúcan close.** The
> reason for the intrusion of ú into the present of this class is
> uncertain, but may be no more than analogy with Class I in Gmc.:
> after eu > iu, since verbs with ai in the past had í in the
> present system, those with au in the past might develop ú in the
> present system."

Checkpoint 064 ends with the question: "Is there a PGmc paradigm
cell that would yield OE ū by regular sound change?" — i.e. is there
a Lautgesetzlich path to *būgan*?

**Checkpoint 065 ("past-3pl-paradigm-cell-fixes-f.md")** records
the negative answer to that question, and the pragmatic substitution
that was made instead:

> "User pushed back: the question was about ANY cell, not just long
> ū. Used FST inversion (`flookup -x`) to map OE forms back to
> proto-forms. Discovered: past 3pl `*bugun` → `bugon` ✓ and
> `*skubun` → `sċufon` ✓ are lautgesetzlich. **Zero-grade paradigm
> cells work; only infinitive has analogical ū.**"

And the verified table (checkpoint 065, "technical details"):

| PGmc       | FST output | Attested OE | Status                  |
|------------|------------|-------------|-------------------------|
| `*bugun`   | `bugon`    | `bugon`     | ✓ Match                 |
| `*buganăz` | `bogen`    | `bogen`     | ✓ Match                 |
| `*skubun`  | `sċufon`   | `sċufon`    | ✓ Match (after fix)     |
| `*beugăną` | `bēogan`   | `būgan`     | ✗ Analogical            |

Three crucial observations follow from this table:

1. **Both the past pl. (`-un`) and the past ptcp. (`-anaz`) cells
   were already known to map regularly to attested OE forms in
   April 2026.** The choice of past pl. over past ptcp. was made
   without explicit deliberation; the past ptcp. is recorded in the
   table as also passing the FST-inversion test, but no row was
   retargeted onto it.
2. **The "policy" claim — "use a finite cell when the infinitive is
   analogical" — does not appear in the codebase as a written
   policy.** It exists only as a one-shot pragmatic step in
   checkpoint 065. The widow row was retargeted under a different
   reasoning (TSV target chosen to match the WS-attested `wuduwe`
   directly, with the FST asked to derive it), and the widow case
   is morphological/lexical (a single noun stem), not paradigmatic
   in the strong-verb sense. So the *būgan*/*sċūfan* retargeting is
   not in fact downstream of a "widow precedent"; it is its own
   one-off decision.
3. **The verification at checkpoint 065 was that the FST as it
   stood at that time gave `bugon`/`sċufon`.** That FST did not yet
   have the stem-`u` harmony block on `OEMedUnstressedULowering`.
   Once the harmony block was reinstated for §17.51.A1 (commit
   `c017ae97`, the Path-1 + Path-2 final), the same input forms
   `*búgun`/`*skúbun` produce `bugun`/`sċufun` — i.e. the FST output
   for these two cells **changed under our feet** as a direct
   consequence of the widow research. That is the pivot that
   reopens the present question.

The decision recorded in checkpoint 065 was therefore epistemically
*correct given the FST as it stood in April 2026*, but the FST has
since been restored to a configuration in which the same cells no
longer produce the originally promised outputs. This is not a fault
of the original decision; it is a consequence of the deeper
phonological correction made by §17.51.A1.

## §3. The fault-line: `-un > -on` for stem-`u` verbs is analogical

The full handbook canvass is in `un-to-on-chronology.md` and is not
repeated here. The operative finding for this dossier is:

* **Brunner §44 Anm. 7** (line 2092) and **Luick §326.2** (line
  17291) agree that unstressed `*-u-` lowering in OE is **blocked
  when a stem-syllable `*u` precedes a single consonant**. This
  is the rule that produces `wuduwe`, `munuc`, `duguþ`, `iuguþ`.
* The pret. pl. ending `*-un` after stem `*u` + single C — i.e. cl.
  II `*bug-un`, `*sċuf-un`, `*lug-un`, `*flug-un` — meets the
  blocking condition exactly. The expected phonological output is
  therefore `-un`.
* Cross-Germanic confirms inheritance of `*-un`: Old Saxon shows
  `budun`, `dribun`, `wurdun` essentially exceptionlessly through
  the ninth century (Fulk *Comparative Grammar* §4.5; R&T §6.9.4).
* The earliest OE strata (Épinal, Vespasian Psalter) preserve `-un`
  for class-II verbs that survive in those texts (Campbell §735(e),
  Brunner §364.2 Anm. 4). For the two specific verbs we care about
  here, the early Anglian/Mercian witnesses simply do not contain
  a finite 3 pl. pret. token — the verb is unattested in those
  texts in that cell. See `bugun-scufun-attestation.md`.
* The lWS attested forms `bugon`, `sċufon`, `lugon`, `flugon` are
  therefore **paradigm-internal levellings** on the dominant `-on`
  ending of all other strong-verb classes (cl. I `ridon`, `drifon`;
  cl. III `bundon`, `holpon`; cl. IV `nāmon`, `bǣron`; cl. V
  `wǣron`, `sǣton`; cl. VI `sċōpon`; cl. VII `hēoldon`), reinforced
  by the productive weak pret.pl. `-don`. **None** of those models
  has a stem `*u`, so none was subject to harmony-blocking; their
  `-on` is Lautgesetzlich and dominant. Stem-`u` cl. II verbs were
  caught up in this levelling and lost their etymological `-un`.

The conclusion (DEV_NOTES §17.51.A1.3 verdict (b)): **the 3 pl.
pret. is precisely the cell most affected by the analogical
levelling** for stem-`u` cl. II strong verbs. It is the **least**
Lautgesetzlich finite cell available, not the most. The choice of
the 3 pl. as the "regular" cell in checkpoint 065 was made before
the harmony block was understood to be active in this environment;
once the block is in place (as it is in the FST per `c017ae97`),
the 3 pl. is structurally the worst finite candidate.

## §4. Cell-by-cell survey: *būgan*

The OE paradigm of *būgan* (with West Germanic *ū < earlier *eu by
the analogical Class-II innovation discussed by Campbell §736(b)
and R&T vol. 2 pp. 39–40):

| Cell                | OE attested form          | PGmc cell input (reg.)         | Regular FST output | Match? |
|---------------------|---------------------------|--------------------------------|--------------------|--------|
| infinitive          | `būgan` (analog.) ~ `bēogan` (cf. R¹) | `*beuganą`              | `bēogan`           | only nW-S/Angl.; lWS analog. ū |
| 1 sg pres. ind.     | `būge` ~ `bēoge`          | `*beugō`                       | `bēoge`            | analog. ū in lWS |
| 2 sg pres. ind.     | `bȳhst` (umlauted)        | `*biugizi`                     | `bȳhst`            | regular |
| 3 sg pres. ind.     | `bȳhþ` (umlauted)         | `*biugiþi`                     | `bȳhþ`             | regular |
| pres. pl.           | `būgaþ` ~ `bēogaþ`        | `*beuganþi`                    | `bēogaþ`           | analog. ū in lWS |
| imperative sg.      | `būh` ~ `bēog`            | `*beug`                        | `bēog`             | analog. ū in lWS |
| pres. ptcp.         | `būgende` ~ `bēogende`    | `*beugandi-`                   | `bēogende`         | analog. ū in lWS |
| **1/3 sg pret.**    | **`bēag`**                | **`*baug`**                    | **`bēag`**         | **regular ✓** |
| 2 sg pret.          | `buge`                    | `*bugi`                        | `buge`             | regular |
| **pret. pl.**       | **`bugon` (lWS)**         | **`*bugun`**                   | **`bugun`**        | **analog. -on ≠ Lautgesetz** |
| **past ptcp.**      | **`bogen`**               | **`*buganaz`**                 | **`bogen`**        | **regular ✓** (Gmc *u > *o by §115) |

### §4.1 Sources for the attested forms

* **Bosworth-Toller** s.v. `búgan` (lines 18013 ff.): principal
  parts paragraph implicitly underwriting `būgan, bēag, bugon,
  bogen`; pret.-sg. examples include
  > "Hē tō ðæm rīce **bēag**, Bd. 5, 19; S. 638, 17"
  > "**Bēag** þā ofer flōd, Beow. Th. 326; B. 163"
  > "Cot ūt **bēag**, Cd. Th. 64, 23; Gen. 1054"
  and many prefixed variants `ābēag`, `gebēag`, `onbēag`.
* **Clark Hall** s.v. `būgan` (line 4567): "**būgan, bēag, bugon,
  bogen** to turn back, flee. clǣne b. habban …" — i.e. `bēag` and
  `bogen` are the dictionary citation forms of the 1/3 sg. pret.
  and the past ptcp. Both are universal in lexicographic
  presentation.
* **Sweet's Anglo-Saxon Primer** (line 1891): "bugan (bow) bȳhþ
  **beag bugon bogen**" — same canonical paradigm.
* **Bright's Anglo-Saxon Reader** (line 16965): "būgan, **bēag**
  bugon **bogen**".
* **Campbell §740** (line 20668), Class II paradigm exemplar
  `béodan, **béad**, budon, **boden**` — and §736(b) names *būgan*
  among the verbs with analogical ū in the present system, with
  past sg. and past ptcp. fully regular.
* **Bēowulf** has `bēag` (line 2956 etc.); **Genesis A**, **Beowulf**,
  **Andreas**, **Christ**, **Elene** all attest `bēag` in 1/3 sg.
  pret.

### §4.2 Phonological assessment

* **`bēag` ← `*baug`** (1/3 sg. pret.): pure `*au > *ǣa > ēa` (the
  monophthongisation/breaking sequence in OE; Campbell §131,
  Brunner §38–39). No competing analogical pressure on this cell:
  it is the **morphological pivot** of the paradigm (the form that
  the analogical *ū* is built on), and is universally attested as
  `bēag`. The FST output is regular.
* **`bogen` ← `*buganaz`** (past ptcp.): regular Gmc *u > *o before
  non-high vowel in the next syllable (Streitberg's rule; Gmc *u-
  lowering / a-mutation; Campbell §115, Brunner §28, Hogg §3.5,
  R&T §3.2.4). Then `*-anaz > -en` by regular OE unstressed-vowel
  reduction. Universally attested as `bogen`. The FST output is
  regular.
* **`bȳhþ` / `bȳhst`** (3/2 sg. pres. ind.): would require
  i-umlaut of the *u* (or of the inherited *iu* > *í*-stage)
  followed by spirantisation/devoicing of the stem-final consonant
  (`*biug-iþi → *byg-iþi → bȳhþ`). The umlaut path is regular but
  the cluster-realisation is intricate and depends on the FST's
  current treatment of `*g + *þ`/`*t`. This cell is attested
  (Sweet's primer cites `bȳhþ`) but not a parsimonious target
  given the chain of cascade interactions involved.

### §4.3 Verdict for *būgan*

The 3 pl. pret. is no longer a Lautgesetzlich cell once the
stem-`u` harmony block is in place. **Two cells are unambiguously
both Lautgesetzlich and attested**:

1. **1/3 sg. pret. `*baug → bēag`.** Single sound change (`*au > ēa`),
   universal attestation, paradigmatic pivot.
2. **past ptcp. `*buganaz → bogen`.** Single sound change (Gmc *u
   > *o by a-mutation), universal attestation, dictionary headword.

Either is preferable to the current 3 pl. choice on
Lautgesetzlich-and-attested grounds.

## §5. Cell-by-cell survey: *sċūfan*

The OE paradigm of *sċūfan* (likewise with analogical *ū < *eu in
the present system per Campbell §736(b)). The conjugation closely
parallels *būgan* but with `*sk-` initial and `*b`-grade alternation
in the past; Verner's-Law alternation (`*b/f` ~ `*b`) operates
within the WGmc → OE transmission rather than as paradigmatic
ablaut, so the consonant skeleton is `sċūf-` ~ `sċēaf-` ~ `sċuf-` ~
`sċof-`.

| Cell                | OE attested form          | PGmc cell input (reg.)        | Regular FST output | Match? |
|---------------------|---------------------------|-------------------------------|--------------------|--------|
| infinitive          | `sċūfan` (lWS, analog.) ~ `sċēofan` (nW-S, Campbell §180) | `*skeubaną` | `sċēofan` | analog. ū in lWS |
| 1 sg pres. ind.     | `sċūfe` ~ `sċēofe`        | `*skeubō`                     | `sċēofe`           | analog. ū in lWS |
| 2 sg pres. ind.     | `sċȳfst`                  | `*skiubizi`                   | `sċȳfst`           | regular |
| 3 sg pres. ind.     | `sċȳfþ`                   | `*skiubiþi`                   | `sċȳfþ`            | regular |
| pres. pl.           | `sċūfaþ` ~ `sċēofaþ`      | `*skeubanþi`                  | `sċēofaþ`          | analog. ū in lWS |
| imperative sg.      | `sċūf` ~ `sċēof`          | `*skeub`                      | `sċēof`            | analog. ū in lWS |
| pres. ptcp.         | `sċūfende` ~ `sċēofende`  | `*skeubandi-`                 | `sċēofende`        | analog. ū in lWS |
| **1/3 sg pret.**    | **`sċēaf`**               | **`*skaub`**                  | **`sċēaf`**        | **regular ✓** |
| 2 sg pret.          | `sċufe`                   | `*skubi`                      | `sċufe`            | regular |
| **pret. pl.**       | **`sċufon` (lWS) ~ Northumb. `sċyufon`** | **`*skubun`**     | **`sċufun`**       | **analog. -on ≠ Lautgesetz** |
| **past ptcp.**      | **`sċofen`** (cf. North. `gesċyfen`, Campbell §740) | **`*skubanaz`** | **`sċofen`** | **regular ✓** |

### §5.1 Sources for the attested forms

* **Bosworth-Toller** s.v. `sċūfan`, `āscūfan`, `bescūfan`,
  `forscūfan`, `oðscūfan`, `tōscūfan`, `wiðscūfan`: pret.-sg.
  citations include
  > "Hé hit **āsceaf** fram his mūðe, Hml. Th. ii. 254, 17"
  > "**Sceaf** þā mid þām scylde, þæt se sceaft tōbærst, Byrhtnoth."
  > "Hē hī tō helle **sceaf** wælgrim wæter, Sat. 26."
  and past-ptcp. citations:
  > "**Tōsceofen** wæs sē apostol, Mart. H. 162, 30."
  > "**Sceofen** of his ġesetlum (ēsceofen Cot.), Bt. 3, 1."
* **Clark Hall** s.v. `sċūfan` (line 34723 ff.): "scūfan² … **sċēaf
  … sċofen**" — dictionary citation paradigm.
* **Campbell §740** explicitly discusses the consonant alternations
  in this verb's paradigm, citing North. **`sċyufon`** in *Durham
  Ritual* and Li. past ptcp. **`gesċyfen`** (with North. *yu* for
  WS *ū*); both forms confirm that the past pl. and past ptcp. are
  the corpus-attested cells where this verb appears, and that the
  underlying stem is `sċuf-` ~ `sċof-` for those cells.
* **Beowulf** 215: "Guman ūt **scufon**" (3 pl. pret. — but with
  the lWS / Late-OE `-on` ending).
* **Andreas** 1119: "Rinc mænig, gūðfrec guma, … **An. 1119**" —
  the same 3 pl. environment.
* The 1/3 sg. pret. `sċēaf` is well attested in the poetic and
  prose corpus (Beowulf, Maldon, Ælfric, etc.). The past ptcp.
  `sċofen` is attested in Boethius, Martyrology, Ælfric.

### §5.2 Phonological assessment

* **`sċēaf` ← `*skaub`** (1/3 sg. pret.): regular `*sk- > sċ-`
  before front-prosody (the *ǣa* triggers fronting of *sk-*;
  Campbell §427) and `*au > ēa`. Two regular sound changes, both
  centrally established and well-tested elsewhere in the cascade.
  Universal attestation. The FST already produces this form
  correctly for the cogset's other Class-II rows where the past sg.
  is targeted.
* **`sċofen` ← `*skubanaz`** (past ptcp.): regular palatalisation
  of `*sk-` (here before *o*, so the palatalisation depends on the
  cascade's WS-conservative treatment — the form is `sċofen` in WS
  but `scofen` outside it; Campbell §427). Then Gmc *u > *o by
  a-mutation, then *-anaz > -en. Universal attestation.
* **`sċȳfþ`** (3 sg. pres. ind.): would require i-umlaut + cluster
  realisation parallel to `bȳhþ`; possible but more cascade-
  dependent than the past sg.

### §5.3 Verdict for *sċūfan*

As for *būgan*, **two cells are unambiguously both Lautgesetzlich
and attested**:

1. **1/3 sg. pret. `*skaub → sċēaf`.** Two regular sound changes
   (`sk- > sċ-`, `*au > ēa`); universal attestation; paradigmatic
   pivot.
2. **past ptcp. `*skubanaz → sċofen`.** Regular Gmc *u-lowering;
   universal attestation; dictionary headword.

Either is preferable to the current 3 pl. choice on the same
grounds as for *būgan*.

## §6. Comparison with the widow precedent

The widow problem (`*wíduwōn → wuduwe`) was framed in
`widuwe-u-preservation.md` (and in DEV_NOTES §17.41) as a problem of
*reconstructing the WS surface form by a Lautgesetz from a
PGmc-faithful PROTOFORM*. There was never a question of switching
to a different lexical cell, because *widuwe / widwe / wuduwe* is a
single nominal n-stem with one citation form. The dossier's
"paradigm cell vs. infinitive" framing is therefore a metaphor in
the widow case, not a literal paradigm survey: the issue was
whether to encode the WS-specific *wi → wu* development as a
phonological rule (Option A, taken) or to set the PROTOFORM to
*wúduwōn directly (Option B, rejected).

The *būgan*/*sċūfan* problem is **structurally different**: there
*are* multiple paradigm cells, and they yield different
Lautgesetzlich outputs:

* infinitive *bēogan*/*sċēofan* — regular but not the lWS attested
  citation form;
* past sg. *bēag*/*sċēaf* — regular AND attested;
* past ptcp. *bogen*/*sċofen* — regular AND attested;
* past pl. *bugun*/*sċufun* (FST output) — regular but not
  attested for these specific lexemes; lWS *bugon*/*sċufon* is
  analogical.

The "policy" credited to the widow case in the user's prompt — "we
shouldn't always pick the infinitive — sometimes a finite cell
gives a cleaner Lautgesetzlich path" — is **not actually a widow
policy**; the widow row was retargeted on different grounds (Option
A of §17.51.4: encode the OE-internal *wi → wu rule and keep the
PROTOFORM as `*wíduwōn`). The retargeting of *būgan*/*sċūfan* to
the 3 pl. pret. in checkpoint 065 was its own one-off decision,
made without an explicit cross-paradigm survey, and based on an
FST that did not yet have the §17.51.A1 harmony block in place.

The widow precedent is therefore not relevant as a justification
for the 3 pl. choice. If anything, the **present** (post-§17.51.A1)
policy that the widow research consolidates is "stem-`u` + single
C blocks lowering of an unstressed `*u`" — and that policy points
*against* the 3 pl. cell for these two verbs, not for it.

## §7. Recommendations

### §7.1 *būgan* (row 1962)

**Recommend: retarget to the 1/3 sg. pret. cell.**

* New PROTOFORM: **`*báug`** (PGmc 1/3 sg. pret.; cf. Goth. baug,
  ON baug, OS bōg, OHG boug).
* New COUNTERPART: **`bēag`**.
* Attestation: universal (Beowulf, Cynewulfian poems, prose). The
  form is the morphological pivot on which the analogical *būgan*
  infinitive itself is built (Campbell §736(b)).
* Cascade clean-ness: requires only the regular `*au > ēa`
  monophthongisation/breaking sequence. No interaction with
  unstressed-vowel lowering, no interaction with stem-`u` harmony,
  no interaction with `-un > -on` analogy.
* Trade-off: the cogset already contains a different `bow` lexeme
  in row 1963 (`*búgô / boga`, the noun 'bow (curve)'), and a
  Class-I weak causative in row 1961 (`*báugijaną / bīeġan` 'to
  make bend'); adding a fourth cell here would mean the cogset
  represents three distinct PGmc reflexes of the root. That is
  consonant with how the cogset already handles other verbs with
  noun derivatives (e.g. *béodan/bod*).

**Alternative: retarget to the past ptcp. cell.**

* New PROTOFORM: **`*búganaz`** (PGmc strong past ptcp.).
* New COUNTERPART: **`bogen`**.
* Attestation: universal as the dictionary citation form (Clark
  Hall, Sweet, Bright); also corpus-attested (Bosworth-Toller).
* Cascade clean-ness: requires Gmc *u > *o by a-mutation
  (Campbell §115, Brunner §28); cleanly tested elsewhere in the
  cogset (e.g. PGmc *budanaz → boden in cl. II, *holpanaz →
  holpen in cl. III, etc.).
* Trade-off: this is the **same change** that the widow research
  is keying off of (medial *u in `*wúduwōn` is the bleeding
  environment for the harmony rule that this dossier is in
  consequence of). Targeting the past ptcp. would re-test the
  Gmc *u-lowering rule, which is good defensively but slightly
  redundant with existing `*budanaz → boden`-type rows.

**Hybrid (most defensive): keep the 3 pl. row AND add a 1/3 sg.
pret. row.**

* Retain row 1962 `*búgun / bugon` as is, but tag in
  `oe_known_problems.tsv` with kind `analogical_paradigm_levelling`
  (the path the parallel agent is already implementing), citing
  Brunner §44 Anm. 7, Luick §326.2, dossier
  `un-to-on-chronology.md`, Appendix D of
  `widuwe-u-preservation.md`.
* Add a new row `*báug / bēag` at the same cogset_id (255) so the
  cogset retains a fully Lautgesetzlich and attested instance of
  the *bow* (verb) entry.

The hybrid path preserves the corpus-faithfulness of `bugon` and
adds the Lautgesetzlich anchor `bēag`. It increases row count by
one and is the most conservative choice if the project's present
policy is "do not lose data already in the TSV".

### §7.2 *sċūfan* (row 2184)

**Recommend: retarget to the 1/3 sg. pret. cell.**

* New PROTOFORM: **`*skáub`** (PGmc 1/3 sg. pret.; cf. Goth.
  *(ga)skáuf*, OHG sciob, OS skōf).
* New COUNTERPART: **`sċēaf`**.
* Attestation: universal (Beowulf, Maldon, Ælfric, Wright's
  Vocabulary).
* Cascade clean-ness: requires regular `*sk- > sċ-` (palatal
  sibilantisation; Campbell §427) and `*au > ēa`. Both rules are
  well-tested in the cogset and produce the right output for
  related Class-II verbs.

**Alternative: retarget to the past ptcp. cell.**

* New PROTOFORM: **`*skúbanaz`** (PGmc strong past ptcp.).
* New COUNTERPART: **`sċofen`**.
* Attestation: dictionary citation form (Clark Hall, Campbell
  §740); corpus-attested (Boethius, Ælfric, Martyrology).
* Cascade clean-ness: requires `*sk- > sċ-` + Gmc *u > *o (a-
  mutation). The *u-lowering rule is what the entire widuwe /
  un-to-on chain of dossiers is *about*; retargeting onto this
  cell would re-test that machinery on a second lexeme — a useful
  defensive cross-check.

**Hybrid: as for *būgan*, keep the 3 pl. row tagged as analogical
in `oe_known_problems.tsv` and add a new `*skáub / sċēaf` row.**

### §7.3 Cross-verb summary

The two verbs are structurally identical (both Class II, both with
the analogical *ū-presents diagnosed by Campbell §736(b), both with
stem-`u` harmony blocking the `-un > -on` lowering in the past
pl.). The recommendation is therefore the same for both:

| Verb     | Current row                 | Recommended retarget         | Alternative retarget        |
|----------|------------------------------|------------------------------|-----------------------------|
| *būgan*  | `*búgun / bugon` (3 pl. pret., analogical -on) | `*báug / bēag` (1/3 sg. pret.) | `*búganaz / bogen` (past ptcp.) |
| *sċūfan* | `*skúbun / sċufon` (3 pl. pret., analogical -on) | `*skáub / sċēaf` (1/3 sg. pret.) | `*skúbanaz / sċofen` (past ptcp.) |

The 1/3 sg. pret. is preferred over the past ptcp. on the grounds
that:

1. It is the **morphological pivot** on which the analogical *ū-
   present is built, so it is the form that the rest of the
   paradigm is most clearly secondary to.
2. It requires the smallest number of cascade rules: only `*au >
   ēa` (and, for *sċūfan*, `*sk- > sċ-`), with no interaction with
   the unstressed-vowel and harmony machinery whose conditioning
   is the entire focus of §17.51.A1 and the parent widow research.
3. It is **independently attested** (in Beowulf for both verbs);
   the past ptcp. is attested but largely as a dictionary
   headword + scattered prose tokens, while `bēag` and `sċēaf`
   appear in canonical poetic loci.

If both 1/3 sg. pret. and past ptcp. are equally appealing on
philological grounds, then the **hybrid path** is the most
defensible: retain the 3 pl. row as the lWS-attested lemma (with
an analogical-overlay tag in `oe_known_problems.tsv`, a path the
parallel agent is already implementing) AND add a 1/3 sg. pret.
row as the Lautgesetzlich anchor. This reflects the fact that the
attested paradigm has *both* analogical and regular forms in
different cells, and the cogset can mirror that.

## §8. Caveats

1. **No FST or TSV change is proposed by this dossier.** The
   recommendations above are research output for the user to
   adjudicate. The TSV change would be a separate, deliberate
   commit, made after the parallel `oe_known_problems.tsv` work
   has landed.
2. **The 1/3 sg. pret. recommendation is contingent on the FST
   currently producing `bēag` and `sċēaf` from `*báug` and
   `*skáub`.** Checkpoint 065 verified this for the FST as it
   stood in April 2026; the same verification needs to be repeated
   on the post-`c017ae97` FST before any retargeting is done. The
   relevant rules (`*au > ēa`, `*sk- > sċ-`) have not changed
   between those two FST states, so the result is expected to
   hold, but it should be checked.
3. **The past ptcp. recommendation is contingent on the FST
   currently producing `bogen` and `sċofen`.** Same caveat as
   above; `*buganaz → bogen` was verified at checkpoint 065 and
   the relevant rule (Gmc *u > *o by a-mutation) has not been
   touched by §17.51.A1.
4. **The "policy" question — should the project always prefer a
   1/3 sg. pret. cell when the infinitive of a Class-II *ū-stem
   verb is analogical? — is out of scope here.** The
   *būgan*/*sċūfan* problem is the only instance of this in the
   cogset (the other Class-II *ū-stem verbs — *brūcan*, *lūcan*,
   *strūdan*, *sūcan* — are not represented in the cogset in any
   strong-verb cell at present). A general policy statement should
   wait until further verbs in the same shape are added.

## §9. Sources

### Primary handbooks

* **Campbell**, *Old English Grammar*, 1959 (Reprinted, with
  corrections, 1977). §115, §131, §180, §181, §218, §369, §373,
  §427, §735(e), §736(a–h), §740. Local copy
  `docs/references/campbell_old_english_grammar.txt`.
* **Brunner**, *Altenglische Grammatik nach der angelsächsischen
  Grammatik von Eduard Sievers* (3., neubearb. Aufl., 1965).
  §38–39, §44 Anm. 7, §114b–c, §357, §364.2 Anm. 4, §367.
  `docs/references/brunner_1965_altenglische_grammatik.vision.txt`.
* **Bülbring**, *Altenglisches Elementarbuch*, 1902. §264, §302,
  §364, §§386–410.
  `docs/references/bulbring_altenglisches_elementarbuch.txt`.
* **Luick**, *Historische Grammatik der englischen Sprache*, 1914–40.
  §221 Anm. 1, §221, §326, §326 Anm. 2.
  `docs/references/luick_historische_grammatik.txt`.
* **Hogg**, *Grammar of Old English*, vol. 1: Phonology, 1992.
  §3.3.1.3, §3.3.3.2, §3.5.
* **Ringe & Taylor**, *The Development of Old English* (= *A
  Linguistic History of English*, vol. 2), 2014. §3.2.4, §3.2.10,
  §6.9.4, §6.9.6; pp. 39–40 on the Class-II *ū-innovation.
* **Sievers-Brunner**, *Abriß der altenglischen Grammatik*. §366–369.
* **Fulk**, *A Comparative Grammar of the Early Germanic
  Languages*, 2018. §4.5, §4.8, §5.6.

### PGmc / PIE handbooks

* **Ringe**, *From Proto-Indo-European to Proto-Germanic* (= vol. 1
  of *A Linguistic History of English*), 2nd ed. 2017. §3.2.7
  (Class II ablaut), §3.4.3 (a-mutation / Gmc *u > *o).
* **Kroonen**, *Etymological Dictionary of Proto-Germanic*, 2013.
  s.v. `*beugan-` ~ `*būgan-` (notes the variant ablaut grades);
  s.v. `*skeuban-` ~ `*skūban-` (idem).
* **Orel**, *A Handbook of Germanic Etymology*, 2003. s.v.
  `*beuganan`, `*skeu̯ban`.
* **Bammesberger**, *Die Morphologie des urgermanischen Nomens*,
  1990 (relevant only for the noun *boga* in row 1963;
  cross-reference).
* **Seebold**, *Vergleichendes und etymologisches Wörterbuch der
  germanischen starken Verben*, 1970. s.v. `beug-a-`, `skeub-a-`.

### Lexicographic / corpus

* **Bosworth & Toller**, *An Anglo-Saxon Dictionary*, 1898 + Supp.
  1921. s.vv. `būgan`, `ābūgan`, `bebūgan`, `forbūgan`, `gebūgan`,
  `onbūgan`, `tōbūgan`; `sċūfan`, `āscūfan`, `bescūfan`,
  `forscūfan`, `oðscūfan`, `tōscūfan`, `wiðscūfan`.
* **Toller**, *Supplement* (1921). s.v. `bugan. Add:`.
* **Clark Hall**, *A Concise Anglo-Saxon Dictionary*, 4th ed.
  1960. s.v. `būgan`, `sċūfan`.
* **Sweet**, *Anglo-Saxon Primer*, 9th ed. 1953. Class II strong
  verb paradigm (line 1891 in our local copy).
* **Bright**, *Anglo-Saxon Reader*, 1917. Glossary, s.v. `būgan`.

### Internal cross-references

* `Germanic/docs/dossiers/widuwe-u-preservation.md`, esp.
  Appendix D.
* `Germanic/docs/dossiers/un-to-on-chronology.md`.
* `Germanic/docs/dossiers/bugun-scufun-attestation.md`.
* `Germanic/docs/DEV_NOTES.md` §17.41, §17.51, §17.51.4,
  §17.51.A1, §17.51.A1.1, §17.51.A1.2, §17.51.A1.3, §17.51.A1.4
  (open).
* Session checkpoints 064, 065, 192 at
  `~/.copilot/session-state/22756d70-…/checkpoints/`.
