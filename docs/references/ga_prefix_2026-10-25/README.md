# ga-/gi-/ge- source acquisition, 25 October 2026

This is a reference-library acquisition record and neutral navigation aid,
not an SC035 adjudication or a replacement for any earlier evidence receipt.
The starting revision is `0bfd8f9507050f06588884bc4b76ef88a4c0840e`.
The supplied directory is actually `~/Downloads/ga-prefix/`, not `GA Prefix`.
All 15 supplied PDFs are identified in [inventory.tsv](inventory.tsv),
including their original filenames, SHA256 hashes, extent, text-layer status,
selection, related copies, relevance, rights and local destination.

## Selection and ownership

Eleven PDFs representing ten contributions were selected. All five supplied
core works and four supplied supporting works are included. Gante's conference
slides and handout are additionally selected because they explicitly discuss
phonology and inherited nominal formations; they share one bibliography key,
not two independent evidential identities. No exact supplied-PDF hash matches
an existing `docs/references/*.pdf` holding.

The full 1891 journal scan contains van Helten's article at sheets463--496,
printed pp.455--488. The separately supplied article has clearer page images
and is the canonical searchable holding. Title/year, article opening and
ending, final addenda, and the next article boundary were checked against
the complete volume. The volume is a duplicate container, not a second
publication or a second complete OCR job.

Pilch1953, McFadden2015 and Martín Arista2012 were reviewed for selection
using their openings, abstracts where supplied, and searchable text. They
remain unselected because their principal questions are preverb semantics,
aspect, productivity and grammaticalization. No concrete phonological
exception was selected for ingestion. Their originals remain in the intake
directory; no bibliography keys or new project holdings were created.

`docs/refs.bib` remains the bibliographic SOURCE. This record, inventory and
page map are acquisition metadata, not new scientific or executable authority.
They neither amend frozen adjudications nor introduce the acquired authors
into the reader or its printed bibliography.

## Availability and rights

Selected original PDFs are retained, byte-for-byte, under `docs/references/`
with the stems below. Existing ignore rules exclude all these PDFs.
Complete restricted texts are retained under `.cache/ga-prefix/holdings/`
with the same stems and `.txt` suffix. This existing ignored-cache convention
avoids redistributing either copyrighted PDFs or their complete transcripts.
Native extracts and initial OCR comparisons are also retained there.

Only `docs/references/van_helten_1891_grammatisches.vision.txt` is publicly
redistributed: it transcribes the public-domain 1891 article, not a modern
translation or scholarly edition. Its original PDF remains ignored.
No redistribution license was verified for the other nine contributions,
including the conference materials; they are conservatively local-only.
No copyrighted source was uploaded to an external OCR service.

A public clone contains metadata, navigation, hashes and the van Helten text,
**not** the complete restricted research library. These local PDFs/texts are
complete supplied copies, not publicly redistributable project holdings or
purportedly licensed extracts. No ignore rule was changed or bypassed.

## Holdings and navigation

In this table, a stem resolves to `docs/references/<stem>.pdf` and, except
van Helten, `.cache/ga-prefix/holdings/<stem>.txt`. The latter is the
page-marked searchable holding, not a committed file.

| Citation key | Holding stem | Neutral navigation |
| --- | --- | --- |
| `Quinlin1991` | `quinlin_1991_accentuation_ga` | pp.145--146: word/syntactic accent and clitic question; pp.147--150: derivations and disputed etymologies; pp.151--157: competing accentuation accounts and nominal formations. |
| `Bammesberger1981` | `bammesberger_1981_nominale_ga_komposita` | pp.377--391: nominal *ga-* compounds; opening §§1.1--1.2 introduces accentuation; compare the nominal analyses throughout with Quinlin separately. |
| `Minkova2008` | `minkova_2008_prefixation_stress` | pp.22--23: verse evidence; pp.28--29, §4.4: phonological integrity and syllabification; pp.38--41, §7: stacked prefixes and prosodic structure. |
| `Crouch1995` | `crouch_1995_morphological_status_ge` | pp.165--168: proposed clitic status; pp.173--176: clitic diagnostics, accent and prosodic grouping, especially §§3.2.1--3.2.2 on p.175. |
| `Pheifer1974` | `pheifer_1974_epinal_erfurt_1998_reprint` | Introduction pp.xxi--xci; §63, p.lxxv: unstressed-vowel counts; §71: palatalization; §§88--90: date/dialect. Text pp.1--58, notes pp.59--135, lemmata index pp.136--152, interpretations index pp.153--166. |
| `Samuels1949` | `samuels_1949_ge_lindisfarne` | pp.62--63: contents, abbreviations and source conventions; p.67: parallel passages; pp.105--112: nonverbal material and comparison; p.110: explicit Rushworth *gi-* forms. |
| `Pheifer1987` | `pheifer_1987_early_glossaries_canterbury` | pp.17--44: early glossary relationships, sources and transmission; opening manuscript/item-reference conventions and the closing discussion on p.44. |
| `HerrenSauer2016` | `herren_sauer_2016_epinal_erfurt_sample` | pp.125--198: editorial principles, witness readings, proposed archetypes, sample edition and commentary; start with the preface on p.125. |
| `vanHelten1891` | `van_helten_1891_grammatisches` | pp.455--488, including addenda on p.488; pp.461--463 provide navigation into back-vowel material. Broader SC021/SC040 reference, not an SC035 reassessment. |
| `Gante2012` | `gante_2012_ga_revisited_handout`, `gante_2012_ga_revisited_slides` | Six numbered handout pages, especially pp.2--4 for etymology/phonology and formations; slides retain animation builds and displayed slide numbers1--12. One 2012 Copenhagen conference contribution, not a verified proceedings paper. |

These pointers identify where to begin reading. They do not endorse one
accentuation theory, settle an etymology or change a chronology claim.
The sources have been acquired and checked for identity, navigation and
technical usability; their historical arguments await separate assessment.

### Edition and metadata checks

Titles, authors, opening/closing pages and selected difficult passages were
checked on rendered images. Publisher DOI metadata corroborates Quinlin,
Bammesberger, Crouch, Minkova, Samuels and van Helten. Pheifer1987 supplies
its DOI and publication metadata on the download cover; 2008 is its online
posting date, not its 1987 publication. Herren/Sauer supplies year, journal,
extent and DOI in the first-page imprint. Gante's title/handout specifies
the 17--22 September 2012 conference; no journal metadata was invented.

The legacy PBB DOI deposits encode year-like values as `volume` and actual
volumes as `issue`. The bibliography uses the historical volumes103 and15,
not fictitious volumes1981 and1891. Bammesberger's volume/page information
is also present in Quinlin's bibliography, checked on p.157.

Pheifer's supplied copyright page says Oxford University Press1974,
special edition for Sandpiper Books1998, ISBN0-19-811164-9. `Pheifer1974`
describes the original edition with an explicit consulted-reprint/conversion
note; no second bibliographic identity is created for a new scan.

## Extraction, OCR and page boundaries

All 610 selected sheets have one row in [page_map.tsv](page_map.tsv), including
covers, animation builds and blank sheets. Each prepared text retains ordered
form-feed boundaries and explicit `PDF sheet NNN; page ...` labels. Mapping
bases distinguish extracted edge folios, sequence-based assignments and
the supplied ebook's own labels; a marker is not itself an independent
printed-page verification. No global numerical offset is imposed on Roman
frontmatter or repeated slide labels.

| Holding | Sheets and mapping | Preparation |
| --- | --- | --- |
| Bammesberger | 15; sheet +376 = pp.377--391; first folio suppressed | Existing OCR drops the title's *ga-* and Greek. Local Tesseract `deu+eng+grc`, rendered longest edge3000px. |
| Quinlin | 15; sheet +144 = pp.145--159 | Existing OCR repeatedly turns `*/ga-/` into `7ga-/`. Local Tesseract `eng+deu+isl+grc`; native extract retained for comparison. |
| Minkova | 32; sheet +20 = pp.21--52; first page has no displayed folio21 | Native `pdftotext -layout`; no external OCR. |
| Crouch | 14; sheet +164 = pp.165--178 | Usable embedded OCR extracted with `pdftotext -layout`; scan remains glyph authority. |
| Pheifer book | 257; nonuniform Roman frontmatter, then sheet90 = p.1 through sheet255 = p.166; sheets256--257 are reprint advertisements labelled167--168 | Native electronic text; retain every supplied sheet. See the substantial qualification below. |
| Samuels | 55; sheet +61 = pp.62--116; first folio suppressed | Defective embedded OCR replaced for navigation by local Tesseract `eng+enm+isl`; native extract retained. |
| Pheifer1987 | 29; sheet1 download cover; sheets2--29 = pp.17--44 | Usable embedded OCR, native extraction. Some folios are OCR-corrupted; sequence and page images distinguish them from actual page jumps. |
| Herren/Sauer | 74; sheet +124 = pp.125--198 | Native electronic extraction. |
| van Helten | 34; sheet +454 = pp.455--488; first folio suppressed | Established `Code/Vision/ocr.py` asynchronous PDF runner, default English hint; 34/34 text responses, no failed page. Only this public-domain article went to Google. Raw JSON is ignored under `.cache/ga-prefix/`. |
| Gante slides | 77; title followed by repeated displayed slide labels1--12 | Native extraction; animation builds remain in supplied order, not deduplicated into invented pages. |
| Gante handout | 8; pp.1--6 then two blank sheets | Native extraction; preserve the blanks and distinguish extent from six numbered content pages. |

Local OCR used `pdftoppm`, Tesseract 5.5.2, automatic page segmentation3 and
at most two concurrent pages. The initial English-only Samuels pass lost
Old English letters; the retained `eng+enm+isl` pass restores searchable
æ/þ/ð in many places. That is not a guarantee of every accent or glyph.
Quinlin's reconstructed forms, Bammesberger's Greek/accents, Samuels's vowel
length, footnote markers and interlinear/tabular alignment still require
image checks. No uncertain glyph was globally normalized or silently supplied.

Image checks included titles/endings; Quinlin pp.145--149,157,159;
Bammesberger pp.377,391 and its opening Greek footnote; Crouch pp.174--175;
Minkova pp.28,40; Samuels pp.65,110,116; Pheifer1987 pp.21,30,44;
van Helten pp.461,463,488; and Gante's handout boundaries/comparative table.
These are bounded usability checks, not a diplomatic proofread.

### Pheifer: important limitation

The PDF is a netLibrary electronic conversion, **not a scan of the printed
critical edition**. Pageiv explicitly warns that diacritics outside
ISO8859-1 have been removed. This damage is already visible in the PDF:
another OCR pass cannot reconstruct the missing marks. It must not become
the sole authority for disputed accented/length-marked forms.

The complete supplied introduction, text, notes and both indices were retained.
Roman labelsiii--vii andix--xci remain Roman; labelsi,ii,viii are not supplied
and were not fabricated. Sheet1 is blank. §63/p.lxxv is sheet73, visually
checked against the supplied PDF, including the displayed *gi-* counts
40i:13e for Épinal and34e:31i for Erfurt, and11 *bi-* examples in each.
This verifies transcription/navigation in this supplied conversion, **not**
the manuscript readings, the statistical method or the historical inference.
No new attestation ledger or verdict was generated from it.

Title/copyright, text opening, notes opening, both index openings, index end
and appended advertisements were also checked. An original-print facsimile
or physical-copy check remains needed for load-bearing non-Latin-1 notation.

## Pending and excluded acquisitions

- **Bennett1968**, “The Accentuation of Gothic ga-”, in *Germanic Studies
  in Honor of Edward Henry Sehrt*, pp.53--60:
  **Pending source acquisition — no full text supplied.**
  Not read, ingested or reconstructed from another author's citations.
  No new bibliography key implying a verified holding was added.
- **Wright--Wülcker1884, volumeII: Indices**:
  **Pending source acquisition — no full text supplied.**
  Existing `WrightWuelcker1884` continues to identify the volumeI holding
  `docs/references/anglosaxonoldeng00wrig.txt`. The requested volumeII
  *gi-mynd* references cannot be checked from these 15 files.
- **Pheifer original-print facsimile**: the complete supplied electronic
  conversion is available, but its missing diacritics remain an access/quality
  gap rather than permission to guess the printed forms.
- **Pilch1953, McFadden2015, Martín Arista2012**: reviewed for relevance,
  not selected; see inventory rows12,13,5. No peripheral bibliography expansion.

## Delivery validation

- All 15 intake hashes were rechecked against untouched originals. The 11
  selected local PDFs match those hashes and their recorded sheet counts.
  All 610 prepared-text markers agree with the acquisition page map.
- All ten new keys are unique, resolve through Pandoc citeproc, and appear
  consistently in both reference indexes and this navigation record.
  Local holding paths and relative navigation links resolve.
- Existing bibliography sanity checks and the focused repository-cleanup
  and citation-range regressions passed: 14 tests and 1,098 subtests.
- The supported `adjudicate.py --refresh` workflow and subsequent
  `artifact_graph.py --check` report `CONTROL PLANE CLEAN`. The sole generated
  tracked change is the bibliography hash in survey provenance.
- Citeproc comparisons against the starting bibliography produce identical
  rendered content for the combined, sound-change and lexical manuscripts.
  The new uncited entries do not expand their printed bibliographies.
- Selected PDFs and restricted complete texts remain ignored and untracked.
  No ignore rules, existing evidence receipts, scientific inputs, executable
  rules, lexical selections, chronology, reader prose or protected scientific
  outputs changed. Pre-existing scratch files remain outside this delivery.

No new Foma experiment or phonological adjudication was performed.
