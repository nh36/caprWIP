# SC035: final source-critical audit

Follow-up to the published audit at `ca0b58f3`:
[the consistency closeout](sc035-consistency-closeout.md) records newly
available original Campbell and Ringe–Taylor PDFs and their exact sheet
maps. The pivotal source-check statuses below are updated accordingly;
uninspected pages remain qualified. Earlier experimental and publication
receipts are preserved, not retrospectively relabelled as image-verified.

## Identity

- **SC id:** SC035.
- **Executable identifier:** `OEPrefixAReduction`, not a historical-stage claim.
- **Date / branch / base commit:** 2026-10-25 / `update` /
  `976c1d07a9ba2703f19ef61e1fe89c2ebdf22cec`.
- This is the final source-critical and historical amendment to
  `sc035-literature-adjudication.md`, not a glossary census or OCR project.
  The initial narrow corrections were followed by the user's expanded
  adversarial review. RETAIN/B was tested, not assumed; the reasons for
  retaining it, and the limits of that judgment, are recorded below.

## Question

- **Hypothesis or suspected problem (falsifiable):** the alleged
  Sweet/Pheifer disagreement at EE76 is an earlier CAPR transcription
  error. Other load-bearing readings or attributions might similarly
  misrepresent the sources.
- **Confirmation/refutation:** compare actual edition images and selected
  original manuscript images; audit the reader's assertions against exact
  passages. A real source disagreement would refute the first hypothesis.
  A secure same-environment negative would require reopening the scientific
  assessment under the protocol, not silently changing a rule.

## Current state (before any edits)

- **Historical characterization:** registry stage `preoe`, scope
  `english_specific`, confidence `B`, verdict `RETAIN`; inventory
  "Pretonic front-vowel raising after a palatal fricative".
- **Executable behavior:**

  ```foma
  define OEPrefixAReduction SentenceCtx([
      {*æ} -> {*i} || .#. {*ᶠ} OEAnyConsonant* {*ʝ} _
  ]);
  ```

  The bounded positive-prosody context models one initial weak syllable.
  Position in the cascade is not an absolute date.
- **Selected input:** believe1944 supplies `*galáubijaną`, root stress
  already encoded; target *ġelīefan*. Nothing in a corrected spelling
  changes that selection.
- **Consulted decisions:** the current specialist memo, generality,
  prosody and model-comparison adjudications, their frozen assays, and
  `035-037-prefix-and-compound-adjustments.book-dossier.md`.

## Diagnosis

- **Complete firing census:** a fresh supported `SC035 --evidence`
  forced the container stage-bin rebuild and production/sandbox
  equivalence over all389 selected rows. Believe1944 is the sole live
  firing; the original380 population is its protected subset.
- **Principal witness trace:** the previous evidence receipt establishes
  weak ae immediately after the palatal trigger becoming i, subsequently
  lowered by SC076. No skip/displacement experiment is required for a
  transcription amendment. The expanded review additionally reruns the
  current cascade and phonological controls; historical counterfactual
  receipts are preserved rather than overwritten.
- **Roles:** believe1944 remains live application; preceding fronting and
  palatalization remain feeding requirements of the adopted model. EE76,
  EE228, EE728 and Corpus2152 are transmitted textual evidence, not newly
  selected execution witnesses. None becomes a secure early unraised
  same-environment negative simply by correcting a letter.

## Literature

### Explicit corrections and preservation

Statuses distinguish claim verification from agreement with CAPR:
`VERIFIED` means the stated passage/reading was checked;
`QUALIFIED` retains an explicit evidential limitation;
`INCORRECT` identifies the old claim being amended;
`UNVERIFIED` means the stated level of checking was not achieved.
An author's verified proposal need not be an established historical fact.

| ID | Status of old claim | Earlier claim at the base commit | Checked correction and exact support |
|---|---|---|---|
| C01 | INCORRECT | Sweet prints *gibiodun*, unlike Pheifer's *gihiodum* | Sweet1885 p.40 EE76 (PDF54), p.27 (41), p.28 (42), p.622 s.v. *geēode* (636) all print *gihiodum*. Pheifer1974 p.6 (95) agrees. Épinal f.1v/94v column d confirms h and written final m. This is a CAPR OCR/transcription error, not an editorial disagreement. The exact earlier extraction mechanism is not established. |
| C02 | INCORRECT | Samuels p.110 has image-checked *gisiðe* | The actual article image, PDF49, prints *gisihðe*, Mark9.9. The omitted h was another CAPR transcription error. The stable evidence-row ID is retained. No Rushworth manuscript collation is claimed. |
| C03 | INCORRECT | Corpus *gibrec* means 'breaking' | Sweet1885 p.107 Corpus2152 (PDF121) prints *umecta : gibrec*; p.602 (616), s.v. *gebræc*, places it under 'phlegm'. Corpus144 f.64r corroborates the spelling and Latin lemma. Do not confuse the adjacent glossary entry for the preterite 'broke'. |
| C04 | INCORRECT | Sweet pp.39,50 support the EE76 transcription | EE76 is on p.40, not p.39; p.50 supports EE228. P.39 contains the Corpus comparison. The reader now cites the correct entry page. |
| C05 | QUALIFIED | Ringe/Taylor "explicitly propose" the regular raising account | P.335 says it is "conceivable", alongside possible influence from *bi-*. The reader now preserves that modal force. CAPR's preference is its own adjudication, not their exclusive conclusion. |
| C06 | INCORRECT | Versloot's volume30(1), pp.103–141 has issue year2025 | The issue is2026;2025 is online-first/copyright dating. `README_resources.md` already distinguishes these. `refs.bib` now records2026 and online-first2025 while preserving key `Versloot2025`. |
| C07 | QUALIFIED | Pheifer's Corpus *saegesetu* can stand for every edition | The revised online edition P sheet3 CpP599 prints *saegeseotu*, while its archetype P23 has *saegesetu*. This is a genuine edition difference, not the false disagreement in C01. Each source keeps its own reading. |

The 51-row `sc035-generality/attestations.tsv` is preserved byte-for-byte,
including its erroneous historical `EE76-Ep` row. SHA256:
`2a40862514f052edc7ffeb0b039d09205bddd304473d83c6f8a59975f1e998cf`.
Its contents must be interpreted through C01, not used to reconstruct a
disagreement between Sweet and Pheifer. The active specialist table's
`P74-EE76-Ep` caveat explicitly links C01 and the frozen row; its
`S49-Ru2-gisithe` row links C02 and the base commit. Earlier frozen
adjudications, aggregates and assay receipts are not rewritten.

### Selected manuscripts and editions

Épinal's separate foliation1–14 corresponds to bound foliation94–107
(Pheifer p.xxi §1; Lucas/Lucas p.67). Its six textual columns are a–f,
with interpretations in b/d/f (Pheifer p.xxii §2). Viewer page numbers
are neither folio numbers nor gloss numbers. The expanded
[collation apparatus](sc035-source-collation.md) counts EE76 at line37
of38 and records the h/b comparison, final nasal and modern edition.
Its coverage keys overlay all51 frozen IDs and the additional active
specialist observations, with originals explicitly unverified elsewhere.

| Entry | Manuscript location and direct image | Edition location | Result / layer |
|---|---|---|---|
| EE76 Épinal | MS72(2), f.1v =94v, c/d, interpretation d; Limédia viewer p7; image `B881606401_MS72_007_0192.jpg` | Sweet p.40; Pheifer p.6 | VERIFIED manuscript *gihiodum*, including h and written final m; edition transcriptions agree. Pheifer §72 n.6, p.lxxxiii (PDF81), interprets h as apparently a hiatus diacritic. That is interpretation, not another manuscript letter. |
| EE76 Erfurt | Amplonianus2°42, f.1v c/d, location from Pheifer's margin | Sweet p.40; Pheifer p.6 | VERIFIED edition *gaeadun*; original manuscript UNVERIFIED in this audit. |
| EE228 Épinal | f.4v =97v, c/d, interpretation d; viewer p13; image `B881606401_MS72_007_0198.jpg` | Sweet p.50; Pheifer pp.13,74 | VERIFIED *clabatum : gybyrdid*. Pheifer's 'striped(?)' is explicitly uncertain interpretation, not 'born'. The prefix y is a spelling, not an independently determined vowel quality. |
| EE228 Erfurt | f.4r a/b, location from edition margin | Sweet p.50; Pheifer pp.13,74 | VERIFIED edition *gebyrdid*; manuscript UNVERIFIED. |
| EE728 Épinal | f.9r =102r, e/f, interpretation f; viewer p22; image `B881606401_MS72_007_0207.jpg` | Pheifer pp.39,108 | VERIFIED manuscript *pro maritima : saegesetu*; commentary supplies 'maritime regions'. |
| EE728 Erfurt | f.9v c/d, location from edition margin | Pheifer pp.39,108 | VERIFIED edition *per maritima : saegaesetu*; manuscript UNVERIFIED. The medial *gae* is not an established early short unraised vowel after a palatal. |
| Corpus2152 | CCCC144 f.64r, right-hand Latin/gloss pair, gloss column; IIIF file `144_064_R_TC_46` | Sweet p.107; glossary p.602; Hessels1890 p.121 U246 used only as a locator | VERIFIED original *umecta : gibrec*. Sweet2152 and HesselsU246 are edition identifiers, not manuscript folios. |
| EE207 correction | Épinal f.4r =97r, e/f, interpretation f; viewer p12; image `B881606401_MS72_007_0197.jpg` | Sweet p.48 n.3; Pheifer p.13 | Current initial e is visible. Earlier i and the correction sequence are QUALIFIED edition reporting, not independently resolved palaeography here. No date of phonological lowering follows from that correction. |

Sweet p.28 explicitly lists *gihiodum* under m for n. Pheifer
p.xxiii §4 n.1 calls the nasal wrongly expanded. The manuscript image
does not license inventing an overbar or a modern Sweet/Pheifer
disagreement: distinguish visible written m, the proposed erroneous
expansion in transmission, and grammatical/emended n.

Original images and reproducibility:

- Limédia object:
  <https://galeries.limedia.fr/ark:/18128/d0s75hg5922r9k39/p7>;
  substitute the documented viewer pages above, not gloss numbers.
  Image filenames above resolve under
  `https://rgw.atolcd.com/swift/v1/sillon_container_prod/entrepot/`.
- Corpus manifest:
  <https://purl.stanford.edu/mz111xq7301/iiif/manifest>.
  The manifest has duplicate NC/TC captures; canvas labels are not folios.
  Checked image:
  <https://stacks.stanford.edu/image/iiif/mz111xq7301%2F144_064_R_TC_46/full/1800,/0/default.jpg>.
- Erfurt manuscript images were not located and checked in this bounded
  pass. Edition images do not substitute for a claimed manuscript
  collation. Nor were the Corpus counterparts C78/C1631 newly collated:
  these remain Pheifer apparatus comparisons.

| Downloaded image | SHA256 |
|---|---|
| Épinal0192 | `49ac1826c07338e7f391ad11122583885e42de08e73438f156cb3690779684b8` |
| Épinal0198 | `597e53b32079fb30ed15d0edfb925a8e63f3def9c7a352a1e4ca6af0e2f5190d` |
| Épinal0207 | `b9accc9b0773a99d0b8f93c0634b6b13b88fe0fe43f7eacdafb70503f8ad3ca2` |
| Épinal0197 | `68e25b7df51aed48275411b21688d903a7c1e97a27371d7d90e6c0faeaa6f966` |
| Corpus64r,1800px capture | `f57b25ca7335eeefb9920c5a00552f46ff45d887b0130b5e8b1508fae2579e52` |

### Reader assertion audit

This table covers the substantive assertions in reader order. PDF means
actual page image where stated; searchable-text-only checks are expressly
qualified. Scholarly citation and CAPR's own inference are separate.

| ID | Assertion / exact support | Status and limit |
|---|---|---|
| A01 | Inherited prefix and comparative reflexes: Ringe/Taylor2014 p.206; *ġelīefan* derivation p.245, past p.267 | QUALIFIED: directly checked local searchable text; the newly held PDF's images at these locators were not checked in the bounded closeout. Comparative citations, not a new diplomatic continental collation. |
| A02 | Pforzen *gasokun*,585–610: RuneS find201 inscription/external dating; Berg2014 pp.60–61 | VERIFIED database record and local text. Excavation date is separate; neither establishes an English palatal trigger or English raising date. |
| A03 | Bammesberger's nominal accent:1981 pp.377–382,384 | VERIFIED, with p.384 image: genuine compounds with nominal second members, not every nominal formation. The reader now states that distinction. |
| A04 | Dental/Thurneysen argument: Bammesberger p.381 nn.9–10 | VERIFIED PDF5: voiced starting dental, Verner-based formation and Thurneysen devoicing are premises; Gothic þ is not direct observation of prefix accent. Notes qualify alternative derivations. |
| A05 | Quinlin's clitic/no-primary-stress analysis and criticism:1991 pp.150–157, especially155–157 | VERIFIED published discussion and images155–157 (PDF11–13). His inherited analysis is not an OE metrical measurement. |
| A06 | Alternative inherited dentals: Ringe2017 pp.305–306 | VERIFIED p.305 image (PDF316): inherited *gaburþi- ~ gaburdi-* alternatives and branch generalization undermine uniqueness of a voiced preform; no new dental rule is inferred. |
| A07 | Equipment word: Campbell1959 p.31 §74 n.5; p.149 §358 n.6 | QUALIFIED searchable text: accented-prefix account is accompanied by an explicit doubt about the relationship of associated forms. No fine typographic claim is represented as scan-verified. |
| A08 | Bammesberger's equipment analysis: p.384 n.17; Quinlin's alternative: pp.155–156 | VERIFIED images: prefixed account versus separate *ġeatwe/getāwe* and unprefixed *gatwō* proposal. The burial-related semantic bridge is Quinlin's hypothesis, not independent proof. |
| A09 | Orel2003 p.403, s.v. *tawō*; comparison with Orel p.128 and Kroonen2013 pp.170–171, *gata-*, *getan-*, *gatwōn-* | VERIFIED Orel403/128 and Kroonen170 images; dictionary families do not themselves identify equipment with road. Equipment remains of unknown origin in Orel; the reader does not cite Kroonen as proof of Quinlin's bridge. |
| A10 | Ordinary weak *ge/be*, stress and alliteration: Hogg's CHEL chapter1992 pp.99–100; Minkova2008 pp.22–23; Minkova/Zhou2022 pp.535–536 | VERIFIED local chapter text and published article passages. Hogg here is `HoggPhonology1992`, not the separate grammar. Their synchronic classifications do not prove the same prehistoric accent. |
| A11 | Initial-prefix counts40/13,31/34,11bi each; denominator caveat: Pheifer1974 p.lxxv §63 (PDF73) | VERIFIED image. The percentages are CAPR arithmetic; neither complete token membership nor every correction decision is enumerated. Other medial/final exclusions cannot be borrowed as prefix policy. |
| A12 | Nine related alignments and Corpus ge counterparts: Toller1921 p.284 s.v.ge-; Sweet1885 pp.48–49 and actual Corpus entries in the frozen ledger | VERIFIED edition comparison retained from the generality receipt; not nine independent manuscript censuses. The old EE76 transcription error is explicitly overridden by C01. |
| A13 | Exceptional Corpus gi and lexical gloss | INCORRECT at base; corrected by C03 and the original f.64r image. |
| A14 | Written i→e correction does not date lowering: Sweet p.48 n.3, EE207 | QUALIFIED: edition reports the alteration; current e checked on the manuscript, underlying i not independently resolved. The chronological non-inference is CAPR's methodological limit. |
| A15 | EE228 'striped(?)', not birth: Pheifer pp.13,74 | VERIFIED edition images and Épinal f.4v; historical meaning remains explicitly uncertain. |
| A16 | EE76 reading, nasal and hiatus: Sweet pp.27–28,40,622; Pheifer pp.xxiii §4 n.1,6,lxxxiii §72 n.6 | INCORRECT disagreement at base, corrected by C01/C04. Readings VERIFIED; h-as-hiatus and erroneous expansion remain source interpretations. |
| A17 | EE728 internal spelling and maritime interpretation: Pheifer pp.39,108; ablaut suggestion p.lxxv | VERIFIED Épinal manuscript and edition; Erfurt manuscript UNVERIFIED. Ablaut is proposed, not demonstrated. Early prosody/trigger/quantity remain open. |
| A18 | Copy dates and relationships: Lucas/Lucas2012 p.67; Lucas2016 p.11; Herren/Sauer2016 pp.129–132; Pheifer1974 p.xli §24; Pheifer1987 pp.34–37 | VERIFIED source passages: around700 Épinal, ninth-century Erfurt/Corpus, common material and intervening copying. Lucas and Herren/Sauer differ in precision for Corpus; the reader says ninth century. None dates every gloss's vowel. |
| A19 | Source-linked spelling heterogeneity: Seiler2017 pp.159–164,167–168 | VERIFIED argument, with p.164 image; QUALIFIED application to prefixes. Her wyn/thorn evidence reinforces transmission caution, not a new gi/ge recensus. |
| A20 | Early and late Northumbrian forms: Sweet1885 p.125, Sweet1871 p.3, Stevenson1840 p.7 collects2–3 | VERIFIED edition-image readings documented in the earlier generality receipt; no new collation of these manuscripts. They defeat a universal spelling calendar, not every relative phonological ordering. |
| A21 | Samuels's Lindisfarne/Rushworth comparison:1949 pp.109–111, especially110 (PDF49) | VERIFIED article image; C02 corrects *gisihðe*. Prefix presence/absence is his subject, not a gi/ge vowel-frequency experiment. |
| A22 | Confused spellings and late raised allophony: HoggGrammar2011 pp.238–239 §§6.53–6.54 | VERIFIED images PDF251–252. The source allows spelling uncertainty and a possible late raised realization, not one universal gi date. |
| A23 | Regular pretonic raising is a published possibility: Ringe/Taylor p.335 | VERIFIED original PDF350 in the consistency closeout: the modal claim and alternative bi influence agree with the retained text. C05 corrects overstatement; the preference among alternatives belongs to CAPR. |
| A24 | Ordinary unstressed fronting and later merger: Campbell pp.140–141 §§333–334; pp.153–155 §§369–370; Ringe/Taylor pp.334–335 | VERIFIED original images: Campbell PDF158–159/171–173 and Ringe/Taylor PDF349–350. Fronting has nasal/syllable qualifications; merger evidence includes early and late variation. Neither passage independently proves SC035's additional raising pathway. |
| A25 | Following-palatal allophony is not preceding-fricative proof: HoggGrammar §§6.51–6.54, held2011 pp.238–239 | VERIFIED images: posttonic retention/raising before palatals and possible late Northumbrian allophony have different environments from SC035. |
| A26 | bi influence/analogy: Ringe/Taylor p.335; Berg pp.60–61; Pheifer p.lxxv §63 | VERIFIED as attributed possibilities, including Ringe/Taylor original PDF350 in the closeout. No demonstrated replacement series is supplied. "No positive redistribution established" reports this bounded CAPR investigation, not a universal absence claim. |
| A27 | Stacked *mísgewìeld*, *geédnìwad*, *únforcùð*: Minkova2008 pp.38–41, especially39 | VERIFIED PDF19: winning parses and postlexical incorporation into the first prosodic word; weak outer ge and hiatus before ed; no alliterative test for the cited finite double-prefixed extension. Her analysis is not a PGmc accent reconstruction. |
| A28 | Written/prosodic units can differ: Riegger/Bögel/Walkden2024 pp.2065–2068 | VERIFIED published text: historical written grouping and restricted modern experimental results; not direct proof of every ancient foot boundary or of SC035 raising. |
| A29 | Internal *modgidanc*: Sweet1885 p.149; *saegaesetu*: Pheifer pp.lxxv,39 | VERIFIED edition reporting already separated from reconstruction. No independent early short-vowel/stress/trigger combination is established; these are unresolved domain candidates, not dismissed as irrelevant. |
| A30 | Printed rule, annotation, bounded initial domain, absence of independent non-ga positive/secure negative | VERIFIED against unchanged Foma and previous domain assay. These are CAPR implementation and bounded-search statements, not facts attributed to a handbook. |
| A31 | Stressed palatal diphthongization versus weak prefix: HoggGrammar §5.48 n.1, held2011 p.104; Ringe/Taylor p.335 | VERIFIED source-backed stress contrast from the existing prosody receipt and Ringe/Taylor original PDF350 in the closeout. Exact headed-foot implementation is CAPR's formalization, not Hogg's notation. Contested equipment etymology is not the sole diagnostic. |
| A32 | *believe*, fronting/palatal trigger, raising before merger and later lowering: Ringe/Taylor pp.245,267,335; HoggGrammar §§6.50–6.54, held2011 pp.237–239 | QUALIFIED: lexical developments and marginally later weak-i lowering are source-supported; exact SC107/052/035/073/076 dependencies are the adopted model's feeding requirements, not independently dated edges newly proved by these citations. |
| A33 | Retained staged account, qualified confidence and limited generality | VERIFIED as the registered CAPR decision and unchanged bounded evidence, not independent confirmation by a successful output. |
| A34 | Revised edition confirms h, distinguishes archetype and prints Corpus *saegeseotu*: `HerrenEtAl2026`, A sheet20 EpA192/Ef341.4/CpA217/archetypeA194; P sheet3 CpP599/archetypeP23 | VERIFIED on edition images. Spacing, corrections and dictionary forms are distinguished in the apparatus. The archetype is not independent manuscript evidence. |
| A35 | No obligatory phonemic high-vowel stage or cross-family lexical generality is demonstrated by spelling alone | QUALIFIED as CAPR's evidential conclusion, not a claim that a cited author disproves raising. The historical A–D comparison below states the shared uncertainties symmetrically. |

### Seiler and Versloot: disposition

Seiler2017, "Untangling the strands", pp.153–174, was read in the
specified open-access volume (PDF162–183). Her concentration of wyn/thorn
spellings in source-linked material and argument for inherited orthographic
systems (pp.159–164) materially strengthen the warning against treating
Pheifer's totals as a homogeneous spoken sample. Her assignment to
particular batches remains tentative (pp.167–168); not all Isidore/Orosius
glosses carry the runic spellings. A short, explicitly limited qualification
is therefore added to the reader. No prefix token is reassigned.
Chapter DOI `10.1515/9783110516340-010`; volume PDF SHA256
`7db850d673f2c21f2f5987639acedf1cdb7f4de15f5d7cac41f930b182e04fd4`.
The linked open-access source is bibliographically registered, not made
into another local OCR/ingestion pipeline.

Versloot2026, "Reconstructing the historical phonology of Old English",
pp.103–141, DOI `10.1017/S1360674324000674`, was already held under stable
key `Versloot2025`. P.107 (PDF5, image checked) explicitly restricts the
PGmc a investigation to stressed syllables and defers palatalization.
P.133 (PDF31) does mention unstressed function words 'and/then/when' in
the nasal comparison: it would be inaccurate to say the paper never
mentions an unstressed environment. But that comparison does not treat
weak ga- after a palatal fricative or supply a replacement pretonic
fronting chronology. Its conclusion again specifies stressed syllables.
Status QUALIFIED for applicability to SC035; no material rule change or
reader digression is warranted. The bibliographic issue year is corrected
without renaming the key or acquiring another copy.

## Historical analysis

### Chain of decisions and competing historical hypotheses

The full chain was reread: original closure, model-comparison, prosody,
generality and specialist-literature adjudications, with their frozen
evidence and the grouped dossier. The original confidence A concerned
the existence of a weak reflex, not a demonstrated discrete raising stage.
The model-comparison experiment's A/B/C meant compressed/fronting-merger/
staged-raising; **those labels do not name the historical hypotheses A–D
below**. Identical selected final outputs in those experiments cannot
choose a history. The later prosodic reformulation repaired the old gaCV
proxy and made the current staged interpretation explicit.

| Historical account | Direct support and assumptions | Independent prediction / difficulty | Assessment |
|---|---|---|---|
| A: regular raising, then lowering | Genuine early gi in the prefix family; ordinary fronting and palatalization; Ringe/Taylor p.335's conceivable raising after a palatal fricative. Requires reconstructed short weak ae, trigger and later lowering. | Other independently reconstructed short weak ae after the same trigger should raise. No independent non-ga positive or secure negative is established. Manuscript i does not by itself prove an obligatory phonemic i stage. | Best economical regular working reconstruction for covered cases, not a cross-lexical demonstration or directly observed phonetic mechanism. |
| B: conditioned raised realization without obligatory separate phonemic stage | The same gi evidence; spelling can represent height without diagnosing contrast. Hogg2011 pp.238–239 §§6.51–6.54 shows relevant allophonic possibilities, but partly opposite trigger direction or late Northumbrian. | Requires early conditioned phonetic height in the relevant environment, not merely a later allophone. A and B may have indistinguishable written outcomes. | Genuine unresolved alternative about phonetic/phonemic interpretation. CAPR's symbols discretize a reconstruction; they cannot establish its phonemic status. |
| C: fronting/merger with no obligatory raised realization | Independently established weak-vowel fronting/merger yields ordinary late ge. Inherited spelling systems and dialect/copying variation could transmit early gi without a single homogeneous phonology. | Must account for the origin and repeated use of i, not just label it “orthographic”. Seiler's source heterogeneity does not demonstrate that this particular prefix's i is nonphonetic. | Possible, but no positive prefix-specific orthographic/source allocation currently makes it a better evidenced account. |
| D: influence/replacement associated with bi | Ringe/Taylor p.335 and Berg pp.60–61 discuss it; Pheifer p.lxxv reports uniform bi beside variable gi/ge. | A demonstrated distribution or replacement mechanism should distinguish affected environments/texts. These unlike lexical/stress populations supply no migration series. | Published possibility, neither demonstrated nor refuted by absence of an observed replacement event. Samuels's prefix-presence data do not supply that missing evidence. |

All four accounts reconstruct something unobserved: A's early vowel
pathway, B's relevant phonetic realization, C's particular orthographic
transmission or D's redistribution. Lack of observed analogy is not
positive proof of A, just as the logical availability of copying or
analogy is not positive proof of C or D. The protocol's explanatory
priority for regular phonology selects a working reconstruction where
fit is otherwise comparable; it does not convert that preference into
independent evidence. The strongest warranted statement is a **qualified
regular reconstruction of one prefix family's history**, expressed by a
phonological, non-morphemic rule, with generality still testable.

### Independent controls: bounded search and actual exclusions

The investigation revisited handbook weak vowels, palatalization and
prosody (Campbell §§333–334,358,369–370; Hogg §§5.48,6.50–6.54;
Ringe/Taylor pp.334–335), the local Orel/Kroonen dictionaries, and Fulk's
comparative grammar. Searches covered non-ga j/g-initial function words
as well as the existing nominal/compound candidates; spellings resembling
gi were not automatically counted as the required fricative-plus-short-ae
environment. The following records state what was actually found:

| Candidate | Source and exclusion / unresolved property |
|---|---|
| *gif* 'if' | Orel2003 p.204 (PDF243, image checked), s.v. *jabā ~ jabōi*, compares Gothic *jabai*, OE *gif*, and explicitly says the individual languages' root vocalism does not match. Fulk2018 p.241 §11.6 also compares them through a pronominal j-stem. Neither supplies the independently established early palatal fricative, short ae and following accented head needed here. Inherited j is not automatically the rule's ʝ. This is a serious non-ga candidate but not an admissible positive or negative, and no synthetic accented input was constructed. |
| *giet/andgiet* and ordinary stressed palatal-vowel examples | Ringe/Taylor p.216 compares poetic *gieta* and the possibly allegro-shortened prose *giet*; Campbell p.69 §185 groups *giet*, *ondgiet* and the associated verbal roots under palatal diphthongization. These are head-vowel comparisons, not independently weak short pretonic ae controls. Orthographic gi or a diphthong alone does not establish the environment. |
| *gie/gé* 'you', *ġēa* 'yes' | Ringe/Taylor p.216 distinguishes inherited *jiz* for the pronoun from *ja* for 'yes'. The former does not supply inherited ae; the latter lacks an independently specified following accented head and early weak domain here. Campbell p.69 §185's unaccented *ge* beside *gie* is not proof of the required earlier vowel/trigger combination. Neither is manufactured into an isolated assay input. |
| *bi-* | Pheifer p.lxxv supplies a genuinely different inherited family but no preceding palatal fricative; it tests proposed influence, not SC035's conditioning directly. |
| *ġeatwe*, *ġebyrd* | Accent/etymology is itself disputed; the dental and equipment arguments were rechecked in the passages A03–A09. Neither disputed input nor EE228 'striped(?)' is fabricated into a non-ga control. |
| Internal/hiatus forms | *modgidanc*, *saegaesetu*, *geédnìwad* and *mísgewìeld* establish limits of word/foot equivalence, not a newly verified prehistoric same-environment negative. They remain historically relevant and outside the automatic parser's domain. |

No independent positive emerged from this bounded search. That is an
evidential gap, not an exhaustive claim about all Old English. The
formal345-case assay cannot fill it. Confidence B is retained because
early high-vowel spellings and the weak/stressed contrast are real,
while exact mechanism and generality remain qualified; A would overstate
the evidence, whereas C would understate the directly attested
phenomenon and the source-backed regular possibility.

### Executable hypothesis and chronology

The rule replaces only short plain ae immediately after ʝ. Its left
boundary also requires the pre-existing positive foot annotation.
`OEPretonicInput` inserts that annotation only for one initial plain
short vowel followed across one or more consonants by an explicitly
accented vowel; `SentenceCtx` preserves sentence context. Thus the
rule's consonant-star before ʝ does not license an arbitrary earlier
syllable: the separate annotation constrains the whole input.
Unmarked stress, secondary stress alone, long weak vowels, hiatus,
multiple pretonics and internal weak vowels do not get this automatic
analysis. The immediate trigger is ʝ, not every palatal or every written g.
This accurately implements the stated **bounded** hypothesis, not all
weak-prefix histories or a general prosodic parser.

SC107 fronting and SC052 palatalization feed its ae/ʝ input; SC056's
headed-foot diphthongization leaves the weak vowel alone; SC073 merges
unraised weak ae but preserves raised i; SC076 subsequently lowers i
and removes the annotation. The selected believe trace and isolated
climb/creation/shaft controls test these distinctions. Only believe is
a selected live firing. Synthetic controls are specifications, not
attestations; isolated historical examples are not new corpus entries.
The old skip/displacement comparisons remain traceable historical
receipts, not newly rerun experiments or historical dates.

- **Stage:** retain `preoe`; corrections do not supply an absolute date.
- **Scope:** retain `english_specific`; continental similarities do not
  prove one shared event.
- **Conditioning:** retain short weak pretonic ae immediately after a
  palatal fricative, with independently reconstructed stress. Neither a
  grammatical label nor the corrupted *gibiodun* conditions the law.
- **Counterexamples/falsification:** *gaeadun* and internal *saegaesetu*
  retain the unresolved prosody, quantity and transmission qualifications.
  No secure same-environment unraised negative or independent non-ga
  positive is created by this audit.
- **Positive analogy evidence:** none newly established. Published
  suggestions remain suggestions.
- **Phenomenon/proxy:** unchanged bounded initial implementation, not a
  complete historical parser for internal weak syllables.
- **Chronology:** no edge added, removed or promoted. Existing
  SC107→SC035 and SC052→SC035 feeding requirements, SC035 before SC073,
  and subsequent SC076 lowering remain adopted model dependencies.
  This audit does not relabel them `independently_demonstrated`; nor does
  it derive `stage_entailed` historical order from an identifier or convert
  a manuscript correction into a chronological witness.

## Verdict

- **Verdict:** RETAIN executable, historical assessment, stage, scope,
  chronology, selected vocabulary and confidence B; CORRECT documentary
  readings, locators and attribution strength.
- **Machine-readable line:**

  `Registry-verdict: SC035=RETAIN`

- **Justification:** the demonstrated defects concern CAPR transcription
  and source representation, not a failure of the accepted phonological
  account. The original manuscript confirms the crucial h and exceptional
  Corpus gi. Seiler strengthens transmission caution; Versloot does not
  adjudicate the relevant weak pretonic environment.

## Propagation (only after verdict)

- **Affected sources:** current reader, active specialist reading table
  and explicitly amended memo, dossier navigation, references index,
  bibliography and documentary tests. Generated publication projections
  are rebuilt only through the artifact graph.
- **Controls:** corrected positive readings plus rejection of the old
  false reader disagreement/gloss; frozen-ledger hash check; unchanged
  scientific SOURCE and earlier evidence bytes against the base commit.
- **Baseline effect:** none. FST SHA256
  `421e7ae9c0a705f910e081e20242f8f7b3a42731b9dc908124217d32826a9d77`;
  corpus SHA256
  `d40b6e65280d4cbe8acb08271803ef8acc64b3ff8e6b2656d416951aebdfa0a0`.
  Fresh runtime, documentary and publication results, exact commands,
  invariants and visual inspection are recorded separately in
  `sc035-final-validation.md`; successful checks are not historical proof.

## Residue

Erfurt originals, the underlying correction at Épinal EE207, and the
original Rushworth spelling were not independently collated here.
Campbell and Ringe/Taylor remain searchable-text-only holdings. Pheifer's
converted reprint loses some original diacritics; visible image text is
not a restoration of that lost type. Equipment etymology, prefix-count
denominator policy and early internal prosodic domains remain qualified
as before. None is silently resolved by OCR or by a successful PDF build.
The apparatus explicitly records the inaccessible Seiler2019 argument
and uncollated older facsimiles. These are bounded, non-decisive limits,
not evidence secretly supplied by an OCR transcription.
