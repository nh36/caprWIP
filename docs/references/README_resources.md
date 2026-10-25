# OCRed reference resources (quick index)

This file lists OCRed reference texts in `docs/references/` with quick hints for searching.

## ga-/gi-/ge- intake (2026-10-25)

The [original acquisition record](ga_prefix_2026-10-25/README.md)
catalogues all 15 supplied PDFs, selection/exclusions, SHA256 identities,
edition qualifications and all 610 selected PDF sheets. The
[corrective consolidation record](ga_prefix_2026-10-25/corrections.md) and
[current holdings manifest](ga_prefix_2026-10-25/holdings.tsv) supersede its
initial cache locations and pending volume-II status. Ten contributions
(11 PDFs, including Gante's slides and handout) are newly registered:
`Quinlin1991`, `Bammesberger1981`, `Minkova2008`, `Crouch1995`,
`Pheifer1974`, `Samuels1949`, `Pheifer1987`, `HerrenSauer2016`,
`vanHelten1891` and `Gante2012`.

Original PDFs remain at their ignored `docs/references/*.pdf` paths.
Complete restricted searchable texts now have durable **local-only** paths
under `docs/references/local/ga-prefix/`, with a tested local restoration
bundle; they are not available from a public clone. Controlled page samples
selected Tesseract for Bammesberger, Vision for Quinlin and Samuels, and the
existing Vision text for van Helten. Other usable native extractions remain.
The public-domain `van_helten_1891_grammatisches.vision.txt` and newly acquired
`anglosaxonoldeng02wriguoft.txt` are committed; temporary OCR responses remain
in `.cache/`. No restricted complete transcript is committed.

The supplied Pheifer book is a netLibrary conversion of the 1998 reprint
of the 1974 edition, not a facsimile. Its own disclaimer explicitly removes
some diacritics; OCR cannot recover characters already absent from that PDF.
Roman labels are retained; p.lxxv, §63 is PDF sheet73. The entire supplied
edition, apparatus and both indices are searchable with this qualification.
Bennett1968 remains pending. Wright--Wülcker volumeII was subsequently acquired
from Internet Archive, title-verified and registered as `WrightWuelcker1884II`.
This intake does not revise any historical adjudication or reader analysis.

## Old English grammars and historical phonology

- `hogg_vol1.txt`  
  Hogg (ed.), *The Cambridge History of the English Language*, Vol. 1:
  *The Beginnings to 1066* (1992).
  Multi-author volume, not Hogg's separate grammar; cite the relevant
  chapter author. ~23,600 lines.

- `hogg_fulk_2011_grammar_old_english_vol1_phonology.txt`
  Hogg alone, *A Grammar of Old English*, Vol. 1: *Phonology*
  (1992; reissue 2011). The legacy filename's inclusion of Fulk is misleading:
  this is not the Hogg & Fulk morphology volume.
  Cite `HoggGrammar2011` for the held paperback's printed-page locators;
  `HoggGrammar1992` retains the original edition and its different pagination.
  The held title/copyright pages identify the sole author, the 2011 paperback
  and ISBN 978-1-4443-3933-8.

- `campbell_old_english_grammar.txt` and `campbell_old_english_grammar.pdf`
  Campbell, *Old English Grammar* (Clarendon Press, 1959).
  The original scan is retained locally alongside the searchable text;
  PDFs remain Git-ignored. Title/copyright are PDF sheets 7--8.
  Printed pp. 140--141 are sheets 158--159; pp. 153--155 are sheets 171--173.
  PDF SHA256: `fcb26efd5537a04ae3b202154e79a06b1b0c719e2f0ebabd261442e7449d3611`.
  The SC035 consistency closeout checked these page images; this is not a
  claim that the entire retained OCR has been corrected against the scan.

- `ringe_taylor_linguistic_history_vol2.txt`
  Ringe & Taylor, *A Linguistic History of English*, Vol. 2: *The Development of Old English* (2014).
  Primary reference for sound change chronology and PGmc→OE derivation. ~38,800 lines.
  Cite the printed running-head page, not the extract's `PAGE` sheet label:
  the stressed-ai discussion is printed pp. 170–171, under labels 185–186.
  The original `ringe_taylor_linguistic_history_vol2.pdf` is now retained
  locally (Git-ignored); printed pp. 334--335 are PDF sheets 349--350,
  checked as images in the SC035 consistency closeout.
  PDF SHA256: `278f94f6076a31278ecca75d8d0429f0822728e5efe0ec3011186a694cf8d6f2`.

- `ringe_vol1_pie_to_pgmc.txt`
  Ringe, *From Proto-Indo-European to Proto-Germanic*, second edition (2017).
  Both the retained PDF's title page and the searchable text identify the
  second edition; cite `Ringe2017` and its printed pages, not first-edition
  pagination under `Ringe2006`. The text preserves printed page headers.

- `luick_historische_grammatik_part1.vision.txt` and `luick_historische_grammatik_part2.vision.txt`
  Luick, *Historische Grammatik der englischen Sprache*, first volume,
  first division (held 1921 printing) and second division (1940, edited
  posthumously by Friedrich Wild and Herbert Koziol). Complete Google Vision
  texts with printed-page markers; use these holdings for verification.
  The older `luick_historische_grammatik.txt` is retained as a legacy extract,
  not the pagination or glyph authority for the new scans.

- `bulbring_altenglisches_elementarbuch.txt`  
  Bülbring, *Altenglisches Elementarbuch*, I: Lautlehre (1902).  
  Detailed OE phonology in German. ~15,690 lines.

- `kaluza_historische_grammatik_englisch.txt`  
  Kaluza, *Historische Grammatik der englischen Sprache* (1900–01).  
  Two-volume historical grammar of English (`Kaluza1900`).
  Both title pages identify Berlin, Emil Felber, 1900 and 1901:
  this holding must not be attributed to the later `Kaluza1906` record.
  OCR from page images (720 pages); first ~800 lines are frontmatter/OCR artefacts, real content starts ~line 794. ~29,575 lines.

- `fulk_comparative_grammar_early_germanic.vision.txt`
  Fulk, *A Comparative Grammar of the Early Germanic Languages* (2018).  
  Modern comparative grammar covering phonology, morphology of all early Germanic languages. Good for cross-branch comparisons. ~34,884 lines.
  Its `=== page NNN ===` markers count PDF sheets, not printed pages.
  Use the printed running heads for citations: §4.12 is printed pp. 72–73
  (sheet markers 089–090), not §5.2 or the marker numbers.

## Proto-Germanic and Germanic etymological dictionaries

- `etymological_dictionary_of_proto_germanic_kroonen.txt`  
  Kroonen, *Etymological Dictionary of Proto-Germanic* (2013).  
  Standard PGmc etymological dictionary. ~54,000 lines.

- `orel_handbook_germanic_etymology.txt`  
  Orel, *A Handbook of Germanic Etymology* (2003).  
  Alternative PGmc etymological dictionary. Useful for cross-referencing Kroonen. Includes extensive bibliography references per entry. ~70,353 lines.

- `kluge_seebold_2011_25th.txt` / `kluge_seebold_etymologisches_woerterbuch.pdf`
  Kluge (ed. Seebold), *Etymologisches Wörterbuch der deutschen Sprache*
  (25th ed., 2011; `KlugeSeebold2011`). The held PDF's title and edition
  history identify this printing. The new text is `pdftotext -layout`
  extraction of that PDF, retaining page breaks and printed running heads.
  Check load-bearing forms against the PDF.
  The older `kluge_seebold_etymologisches_woerterbuch.txt` identifies the
  **24th edition (2002)** and is retained as a separate legacy holding,
  catalogued as `KlugeSeebold2002`, not the text or pagination authority
  for `KlugeSeebold2011`. No matching older PDF or reliable printed-page
  map has been established; different editions are not independent votes.

- `mayrhofer_ewaia_A-DH.vision.txt`, `mayrhofer_ewaia_N-H.vision.txt`,
  `mayrhofer_ewaia_III.vision.txt` and their original PDFs
  Manfred Mayrhofer, *Etymologisches Wörterbuch des Altindoarischen*,
  volumes I (1992), II (1996) and III (2001).
  Volume III's scan appends F. B. J. Kuiper's *The New 'Mayrhofer'*,
  *Indo-Iranian Journal* 34 (1991), pp.105-120, on sheets998-1013
  (`Kuiper1991`). Attribute this article separately; it is not dictionary
  prose by Mayrhofer or a review of the completed three-volume work.

## Old English / Germanic lexica

- `aconciseanglosa01hallgoog.txt`  
  Hall, *A Concise Anglo-Saxon Dictionary* (2nd ed.).

- `bosworth_toller_anglo_saxon_dictionary.vision.txt` / `.pdf`
  T. Northcote Toller, *An Anglo-Saxon Dictionary: Supplement*
  (first edition 1921; held scan records reprints 1955 and 1966;
  `Toller1921`). The original title and preface identify the supplement,
  not the main dictionary or combined volumes. The plain `.txt` and
  `legacy/anglosaxondictio00tolluoft.txt` also identify the supplement.
  The former `BosworthToller1898` file association is withdrawn; old
  citations are not thereby reverified against either edition.

- `anglosaxonoldeng00wrig.txt`  
  Thomas Wright, *Anglo-Saxon and Old English Vocabularies*, second
  edition edited/collated by Richard Paul Wülcker, volume I
  (Trübner, 1884; `WrightWuelcker1884`).
  This is not Joseph and Elizabeth Mary Wright's *Old English Grammar*
  (`Wright1925`). The separate `anglosaxonoldeng02wriguoft.txt` holding
  is volume II: *Indices* (`WrightWuelcker1884II`), acquired from
  https://archive.org/details/anglosaxonoldeng02wriguoft. Its 498 sheets
  preserve pp.1--485 plus unnumbered material; see the corrective acquisition
  record for verified title, page mapping and the pp.53/73 reference caveat.

- `aneightcenturyl00librgoog.txt`  
  Hessels / early glossary material (Eighth-Century Latin-Anglo-Saxon Glossary).

## Old English primers and readers

### SC035 focused acquisitions (2026-10-25)

Final source-critical supplement: `HerrenEtAl2026`, revised online
*Épinal-Erfurt Glossary*. The project's editors page identifies Michael
W. Herren, Cameron Laird, David W. Porter, Hans Sauer and Gernot Wieland;
the short “Herren–Porter–Sauer” description is not its complete credit.
Landing page:
https://epinal-erfurt.artsci.utoronto.ca/index.php/new-revised-edition/.
Targeted PDFs are local-only ignored holdings named
`herren_et_al_epinal_erfurt_revised_{a,b,c,p,introduction}.pdf`.
No full copyrighted extraction or PDF is redistributed.
The site states copyright the editors; free access is not an open licence.
August2026 letter URLs use the base
`https://epinal-erfurt.artsci.utoronto.ca/wp-content/uploads/2026/08/`
and filenames `a_eperf_final.pdf`, `b_eperf_final.pdf`,
`c_eperf_final.pdf`, `p_eperf_final.pdf`.
Introduction:
https://epinal-erfurt.artsci.utoronto.ca/wp-content/uploads/2025/02/Introduction-to-Revised-Edition.pdf.
Original PDF SHA256 fingerprints:

| Holding | SHA256 |
|---|---|
| A | `583e3ad01f10373da249d74456f62bda4ae13911330ca355feea99ced1a811f3` |
| B | `be821d1c564f4ca356d696e8b8c66169525859cc60ff48593a2c5ac75f0765df` |
| C | `dc098032cb80d07806b4cf64d20fef019a51602c259d4d864c6487554b17952f` |
| P | `d12fc1178a2661ea2d8824b0e24b160f7667bf793b923e2d4e0e56a8277e6faf` |
| Introduction | `2c1baf45d25faac33e98de3eb4ecf97b131a574c90313729c70c8614efd0bdf4` |

Checked letter sheets A20, B4, C8–12/C21 and P3 distinguish actual
manuscript columns from reconstructed archetypes. The detailed SC035
collation apparatus records spacing, corrections, dictionary diacritics
and the genuine Corpus *saegeseotu* edition difference.
Seiler2017 is available through its registered open-access volume URL;
Seiler2019 was identified bibliographically but no reliable readable copy
was obtained. Do not cite the latter as an inspected argument.

These are source holdings, not generated manuscript text. Original PDFs follow
the existing local-only ignored-PDF policy; no copyrighted catalogue is
redistributed. Public-domain edition text extractions are navigation aids,
not certificates of every character. Significant forms were checked on images.

- `Sweet1885`: `sweet_1885_oldest_english_texts.{pdf,txt}`, complete688-sheet
  EETS83 edition, title1885; Internet Archive
  https://archive.org/download/oldestenglishtex83sweeuoft/oldestenglishtex83sweeuoft.pdf.
  IA metadata declares `NOT_IN_COPYRIGHT`. PDF SHA256
  `7f13fd3e587fa915b89fcbdce6908809619540fff594ceb8defeaf2fb236940a`.
  `pdftotext -layout` extraction; body printed page = PDF sheet minus14.
  EE p.48 is sheet62; Corpus p.51 is sheet65. Sweet's marginal references
  EE189→500/191→502 conflict with actual Corpus503/505; record actual entries.
- `Sweet1871`: `sweet_1871_pastoral_care.{pdf,txt}`,306-sheet partI,
  EETS45; original title sheet11 verifies year/editor/publisher.
  https://archive.org/download/kingalfredswests00greg/kingalfredswests00greg.pdf.
  Nineteenth-century public-domain edition, not a modern licensed translation.
  PDF SHA256 `ad5c16e2caefd04f7511702f790ce8ca335958c61130230bd0dad7b328dfded5`.
  `pdftotext -layout` extraction. Hatton p.3 is sheet15; preliminary notice
  explains additions, restorations and expansions. PartII not acquired.
- `Stevenson1840`: `stevenson_1840_durham_ritual.{pdf,txt}`, complete234-sheet
  Surtees10 edition; preliminary society title verifies1840.
  https://archive.org/download/ritualeecclesi00cathuoft/ritualeecclesi00cathuoft.pdf.
  IA metadata declares `NOT_IN_COPYRIGHT`. PDF SHA256
  `6645fd2946b425c12c9c2972a78c92cf17e45608db2e5de464c179c1821e3cf3`.
  `pdftotext -layout` extraction. Printed p.7 first occurs on sheet27;
  duplicated scan sheets mean there is no single global sheet offset.
- `LucasLucas2012`: `lucas_lucas_2012_epinal_72.pdf`, complete17-page
  description, ASM18,67–83. https://journals.lib.sfu.ca/index.php/asmmf/article/download/5810/5012.
  Authors PeterJ. and AngelaM. Lucas; citation metadata verifies2012, distinct
  from2023 digital posting/copyright. PDF SHA256
  `53153917589fabb10333bf201c00f2b0f262ab42cfd7eaa829ef1ee7d70914dc`.
  Public access is not a redistribution license; original retained locally,
  no full copyrighted extraction committed. Relevant p.67 distinguishes
  around/before700 copying and uncertain place/dialect.
- `Lucas2016`: `lucas_2016_corpus_144.pdf`, complete8-page description,
  ASM25,11–18. https://journals.lib.sfu.ca/index.php/asmmf/article/download/5964/5216.
  PeterJ. Lucas; citation metadata verifies2016, not2023 upload.
  PDF SHA256 `1f4941dd93037c9b13239c2eb27e3c4f23bf62121ac29d426b920273465774d4`.
  Same local-only copyright treatment. Relevant p.11 dates main hand to
  first half9c and distinguishes the expanded inherited compilation.
- `RuneSPforzen`: `runes_pforzen_201.xml`, complete unmodified LIDO
  descriptive metadata downloaded from https://www.runesdb.de/find/201?xml=true.
  SHA256 `0918264005b9a3a684e422c5f6199967adb74299ec4156e95bbd5377dd404d5c`.
  Attribution: Niedersächsische Akademie der Wissenschaften,
  *Runische Schriftlichkeit in den germanischen Sprachen* (RuneS),
  https://www.runesdb.de/find/201. Its object-description rights explicitly
  state CC BY-SA4.0, https://creativecommons.org/licenses/by-sa/4.0/.
  Creation event earliest/latest585/610 is distinct from excavation1991–1996.
  The record cites Düwel etal.2020:511,513 for external dating; that separate
  publication was not acquired or presented as directly read. This is the
  database's date assessment, not independent endorsement of its inscription
  interpretation.

Toller1921 p.284 (sheet296) was rechecked against the existing supplement and
https://bosworthtoller.com/46976. Pheifer1974/1987 full texts and direct modern
Erfurt palaeography remain unverified; the Toronto project and Bodleian
catalogue required human verification. No inaccessible primary reading is
silently promoted from a handbook or search summary.

- `crawford_1922_heptateuch.pdf`
  S. J. Crawford (ed.), *The Old English Version of the Heptateuch*
  (1922; `Crawford1922`), original scan retained locally.
  Title sheet9 verifies the year; sheets91/375 are printed pp.71/351.
  Those two pages were visually checked for infinitive *leornian* and
  singular imperative *leorna*. Navigation OCR is not a certified
  whole-volume text; see the SC015 adoption attestation record.

- `miller_1891_oe_bede_part1_2.pdf`
  Thomas Miller (ed.), *The Old English Version of Bede's Ecclesiastical
  History*, Part I, second half (1891; `Miller1891`), original scan retained
  locally. The preliminary publisher notice identifies the 1891 part;
  there is no conventional title page in this scan. Sheet180, printed
  p.380, lines26-27, was visually checked for third-singular *leornað*.
  Navigation OCR is not a certified whole-volume text.

- `sweet_anglo_saxon_primer.txt` / `.pdf`  
  Henry Sweet, *An Anglo-Saxon Primer* (seventh edition, Clarendon Press,
  1893; `Sweet1893`), as the held title identifies.
  This is not Norman Davis's ninth-edition 1953 revision (`Sweet1953`).
  Introductory grammar with notes and glossary. ~7,000 lines.

- `neri_review_ringe_pie_to_pgmc.txt` / `.pdf`
  Sergio Neri's review of Ringe's 2006 first edition, numbered1-12.
  The detached holding does not establish publication venue/date; the
  former Kratylos54(2009),156-160 association is unverified and withdrawn.
  The adjacent opening of a Casaretto review is not part of this review.

- `ringe_1984_germanic_e2_and_r.vision.txt` / `.pdf`
  Donald A. Ringe Jr., *Germanic 'e₂' and \*r*, catalogued as
  *Die Sprache*30(1984), pp.138-155, corroborated by the held Stiles
  bibliography. The14-sheet local scan ends at printed151, whose
  conclusion/author byline is visible; the remaining publication pages
  are not established as held. The former Linguistic Inquiry association
  was wrong. OCR corrupts vowel signs; consult the original.

- `bright_anglo_saxon_reader.txt` / `.pdf`  
  Bright, *An Anglo-Saxon Reader* (4th ed., 1917; held June 1926 printing,
  `Bright1917`).
  Reader with notes, complete glossary, chapter on versification, and outline of OE grammar. ~27,700 lines.
  The `.vision.txt` preserves the title/copyright evidence on sheets5-6.
  This is not Cassidy and Ringler's 1971 revision (`BrightCassidyRingler1971`).

## Articles and special studies

### SC035 prosody reconsideration (2026-10-23)

The following complete sources were acquired from their publishers or
institutional repository, not inferred from abstracts or search snippets.
The searchable holdings retain every PDF sheet with explicit sheet markers;
the extraction headers record original hashes, methods and glyph repairs.
Printed locators must be read from the retained page heads/folios, not
confused with PDF sheet numbers.

- `minkova_zhou_2022_functional_stress_shifts.{pdf,txt}`:
  Donka Minkova and **Z. L. Zhou**, *English Language & Linguistics* 26(3),
  **533–558**, DOI `10.1017/S1360674322000144` (`MinkovaZhou2022`).
  Publisher's published-version PDF obtained through its `citation_pdf_url`
  on 2026-10-23; original URL:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/59A438B9E1FFCC863DB66024C1FAECEE/S1360674322000144a.pdf/early-metrical-and-lexicographical-evidence-for-functional-stress-shifts.pdf.
  All 26 sheets correspond to printed pp.533–558. The first page explicitly
  licenses reuse under CC BY 4.0. Page images535–536 were checked for the
  root-stress, weak-prefix and verse-evidence claims. Incorrect alternative
  author expansions and pagination returned by web search were rejected
  against the actual publication.
- `riegger_bogel_walkden_2024_prosody_ge.{pdf,txt}`:
  Chiara Riegger, Tina Bögel and George Walkden, *Interspeech 2024*,
  pp.2065–2069, DOI `10.21437/Interspeech.2024-289`
  (`RieggerBogelWalkden2024`). Published five-sheet proceedings paper,
  obtained 2026-10-23 from
  https://www.isca-archive.org/interspeech_2024/riegger24_interspeech.pdf.
  Pages2065–2068 distinguish the three manuscript studies, their
  interpretation and the modern German production experiment.
  Full-text access is not itself a redistribution licence. On 2026-10-23
  the user supplied an author's permission after consultation with the
  publishers and co-authors: "I can grant you unrestricted permission
  to use our article in your project." The complete PDF and searchable
  extract may therefore be included here under that permission, not
  under an invented CC licence or a blanket ISCA redistribution policy.
- `berg_2014_old_english_unstressed_vowels.{pdf,txt}`:
  Joakim P. Berg, complete May2014 Oslo MA thesis (`Berg2014`),
  104 PDF sheets. The supplied CORE URL
  https://core.ac.uk/download/pdf/30829936.pdf returned403. The verified
  institutional record is https://hdl.handle.net/10852/39907, now
  https://nva.sikt.no/registration/019c8f22d9fe-877dde99-897e-4c4e-8e9c-ea68e4446b07.
  The public repository API's `filelink` for open artifact
  `1bfde0f0-cd8c-45d4-9b52-e255955b49f7` supplied the complete `Thesis.pdf`.
  The temporary signed download URL is not a persistent citation or
  credential to commit. Printed p.60 is PDF sheet72; that page was
  image-checked, including the analogy argument and Pforzen qualification.
  NVA labels this work with general copyright terms permitting private
  professional consultation, not unrestricted republication:
  https://nva.sikt.no/license/copyright-act/1.0.
  The user supplied explicit public-repository permission on 2026-10-23:
  "it is no problem to use this in your research including to put it in
  the public github repo." This permits the complete PDF and searchable
  extract in this repository; it is permission, not a CC licence.

Hogg's existing grammar holding was not duplicated. The 2011 reprint's
printed p.104 (PDF sheet117), §5.48 n.1, was image-checked: the relevant
palatal begins a stress foot, not necessarily a word; *sċeaft* and
*ġesċeaft* illustrate the contrast. Cite `HoggGrammar1992` by section and
identify the reprint explicitly when using its page number. This is not
the chapter cited as `HoggPhonology1992`. Merger evidence at §§6.50–6.54
has independent evidential force from that foot-conditioning claim.

### SC112 spatial-adverb source

- `hill_2017_west_germanic_lengthening.txt` / `.pdf`
  Hill, "West Germanic monosyllabic lengthening and Gothic breaking as
  partially Proto-Germanic developments: The evidence of pronominal place
  adverbs 'here', 'where' and 'there'" (*NOWELE* 70.2, 2017, 135–170;
  `Hill2017`, DOI 10.1075/nowele.70.2.02hil). All 36 PDF sheets are
  retained, with printed-page markers 135–170. Born-digital
  `pdftotext -layout` extraction; 36 spurious U+0008 controls before
  reconstruction asterisks are removed, with no normalization of linguistic
  signs. The extraction header records the PDF hash, page mapping and
  verification limits. Printed pp.149–158 were checked against rendered
  originals, including the close-vowel signs, quantities, tables and
  footnotes. This verifies the holding, not adoption of Hill's hypothesis.
  The original PDF is retained locally under the usual ignored-PDF policy.
  The copy in the `A-Ablaut` collection (`nowele.70.2.02hil.pdf`) is
  byte-identical to this holding and was not re-ingested.

### SC015 *i > e* packet (A-Ablaut collection)

Six sources collected for the SC015 (`PNWGmcILowering`) investigation.
Five are born-digital and extracted with `pdftotext -layout`; **one —
Jasanoff 1973 — is a JSTOR scan whose embedded layer destroys macrons**
(`habOn`, `hab&t` for *habēn*, *habēt*) and was sent through the
established Vision PDF runner instead, hence its `.vision.txt` suffix.
Every text opens with a header recording the PDF SHA256, the extraction
method, each deterministic glyph repair with its count, and the
sheet-to-printed-folio map; `=== page NNN ===` markers carry **printed
folios**. Two publisher fonts emit the reconstruction asterisk as a
mathematical operator (Howell U+2217, Kostakis U+22C6); these are mapped
to ASCII `*` for searchability, and the mapping is recorded in each header.
Unconfirmed edge folios are the chapter/article opening pages only.
Ingestion does not adjudicate any author's hypothesis.

- `cercignani_2022_distance_assimilation.txt` / `.pdf`
  Cercignani, "On the Germanic and Old High German distance assimilation
  changes", *Linguistik online* 116, 4/22 (2022), pp. 41–59
  (`Cercignani2022`, DOI 10.13092/lo.116.8889). 19 sheets, folio = sheet + 40;
  18/19 edge-confirmed. Nine Symbol-font list dashes (U+F02D) are restored
  as U+2212. Restates the 1979/1980 five-phoneme position; not an independent
  vote for it.

- `howell_2024_gothic_breaking.txt` / `.pdf`
  Howell, "What do we really know about Gothic breaking? On the problem of
  consonantally conditioned vowel mutations in Germanic", ch. 4 of Klein &
  Ratkus (eds), *Studies in Gothic* (OUP, 2024), pp. 75–91 (`Howell2024`,
  DOI 10.1093/oso/9780198896692.003.0004). 17 sheets, folio = sheet + 74;
  16/17 edge-confirmed. Access watermarks removed. Phonetic account of
  rhotic- and glottal-conditioned lowering across Germanic (pp. 81–82, 85–88).

- `jasanoff_1973_germanic_third_weak_class.vision.txt` / `.pdf`
  Jasanoff, "The Germanic Third Weak Class", *Language* 49.4 (1973),
  pp. 850–870 (`Jasanoff1973`, DOI 10.2307/412065). Sheet 1 is the JSTOR
  cover; folio = sheet + 848 for sheets 2–22; 21/21 edge-confirmed. Vision
  text, NFC; þ is occasionally read as `b`/`p`. The *learn* passages (p. 865
  *liznaiþ(i)*; p. 868 "Upper German *lirnên* (for phonologically regular
  *lernên*) ... a lost 3sg. *lizniþ*") were checked against page renders.

- `kostakis_2025_coda_nasals.txt` / `.pdf`
  Kostakis, "Coda nasals in early Germanic languages", *JCGL* 28:6 (2025),
  32 pp. (`Kostakis2025`, DOI 10.1007/s10828-025-09166-0; Open Access).
  Article-number pagination: cite "28:6, p. N"; article page = sheet;
  32/32 confirmed via "Page N of 32". fi/fl ligatures decomposed.

- `tarsi_laker_2026_know_teach_learn.txt` / `.pdf`
  Tarsi & Laker, "'to know', 'to teach', and 'to learn' in Germanic",
  *Journal of Germanic Linguistics* 38 (2026), pp. 40–58 (`TarsiLaker2026`,
  DOI 10.1017/S1470542726100178). 19 sheets, folio = sheet + 39; 19/19
  edge-confirmed. Two math-font `+` signs emitted as U+0001 restored from
  page renders (p. 43 n. 6, p. 50). CUP footers removed. Treats PGmc
  *\*lais-/liz-* and the *learn* verb's morphology.

- `scheungraber_2010_nasalpraesentien.txt` / `.pdf`
  Scheungraber, *Die Entwicklung der urindogermanischen Nasalpräsentien im
  Germanischen*, Magisterarbeit LMU München, 2010; Mubahis Bd. 2
  (`Scheungraber2010`). 247 sheets: sheet 1 unnumbered series cover, sheet 2
  = p. 1 (title), folio = sheet − 1; 245/246 edge-confirmed. Five PUA/control
  code points (`i̯`, `ā́`, `ī`, two list bullets) repaired from context and
  listed in the header. §2.2.2.4 (p. 74) treats WGmc *\*liznō/ē-*. A
  Magisterarbeit (supervisor E. Hill), cited as such.

Not in the collection and still not held directly: **Hock 1973** (on the
strong-verb participles and *a*-umlaut), cited by Hill (2017: 150, 154–155) and discussed in the earlier SC015 report.

- `luehr_article.txt` / `.pdf`
  Lühr, "Zur Semantifizierung von Zahlwörtern: Das Wort 'Tausend' —
  eine germanisch-baltoslavische Isoglosse?" (*Linguistica* 33, 1993,
  117–136; `Luehr1993`). The local article preserves all twenty printed
  pages; its author/title and range match the bibliography in the held
  Viredaz study. This is not Lühr's distinct 1998 EWA *dûsunt* entry.
  The text layer corrupts reconstructed glyphs; verify forms against
  the local PDF before diplomatic transcription.

- `vine_2019_greek_stomylos.txt`  
  Vine, "Greek στωμύλος 'chatty': An anomalous ō-grade" (*Indo-European Linguistics* 7, 2019, 222–240).  
  Discusses the PIE \*stom-/\*stem- root ('mouth') with detailed treatment of ablaut grades and derivatives. Directly relevant to the stefn/stemn problem (see DEV_NOTES §Case 3 and notable_findings §5). ~826 lines.

- `polome_1967_reflexes_ie_ms.txt`  
  Polomé, "Notes on the Reflexes of IE /ms/ in Germanic" (*Revue belge de philologie et d'histoire* 45.3, 1967, 800–826).  
  Discusses IE nasal + s clusters in Germanic, with treatment of the \*stemn-/\*stibna problem. Directly relevant to the stefn/stemn problem. ~1,282 lines.

- `thorhallsdottir_1993_intervocalic_j.vision.txt`  
  Þórhallsdóttir, *The Development of Intervocalic \*j in Proto-Germanic* (Ph.D. dissertation, Cornell University, 1993; UMI 9410504). 293 scanned pages, no text layer; Google Vision OCR over 300 dpi renderings.  
  Page markers are the dissertation's own **printed** folios (printed N = PDF sheet N + 11; front matter as roman iii–ix). The specialist source for the hiatus-breaking consonants of the *verba pura*: Ch. 5 (pp. 114–137) is the direct authority for CAPR SC102, giving the phonological insertion of \*w before \*u (pp. 120, 126–127) and its analogical generalization through the Anglo-Frisian paradigm (pp. 130, 134, 136). Heavy diacritic load — verify any quoted form against the page image. ~293 pages.

- `lid_1952_nordiske_nominativ_an_stammer.vision.txt`  
  Lid, "Den nordiske nominativ singularis av maskuline an-stammer" (*Norsk Tidsskrift for Sprogvidenskap* 16, 1952, 237–240). Norwegian Nynorsk; 2-up scan, split on the detected gutter, Google Vision OCR.  
  Cited in CAPR for p. 238, where the Sámi loanword evidence (Sámi *mānno* etc.) is used to argue that Germanic \*ē (cf. Gothic *mēna*) had already become *ā* before the borrowing. Replaces the former indirect citation via Stiles 2017: 4. One OCR character (*å* for printed *ā*) was corrected against the page image and the correction is documented in the file header. ~258 lines.

## Anglo-Frisian / North Sea Germanic specialist literature

The original nine-source Anglo-Frisian chronology packet: **seven** of the nine
were extracted with `pdftotext -layout` from born-digital text layers.
**One — Campbell 1939 — required the Google Vision OCR route** and carries the
`.vision.txt` suffix. **One — Laker 2007 — required a deterministic
font-aware rebuild** and keeps the plain `.txt` suffix, since it is not OCR.
Four of the seven `pdftotext` sources still needed character repairs before
they were usable; three were usable as extracted.

An initial screen that measured only characters-per-page passed all eight of
the original sources; that screen was wrong, because it measured volume rather
than accuracy. A second screen on diacritic integrity caught both failures:

- **Campbell 1939** yields zero ae-ligatures, zero macrons and zero thorn
  across thirty pages of Old Frisian vowel history. Its text layer is itself
  machine-generated from the 1939 letterpress page and destroys exactly the
  characters that carry the content.
- **Laker 2007** is born-digital, but three of its fonts carry WordPerfect
  legacy encodings with *wrong* ToUnicode maps. The palatal dot of `ċ` is
  mapped to `k`, so both `pdftotext` and PyMuPDF render the article's central
  diagnostic `ċeapian` as `keapian` — an unpalatalized form, in a paper
  arguing that the form *is* palatalized. That is an active falsification, not
  merely a loss, and it is the clearest case in this library of why a text
  layer's existence is not evidence of its reliability.

  Vision was not the right fix here either: it reads the dot only about
  two-thirds of the time and misreads `æ` as `oe`/`a`. Instead the text was
  rebuilt **from the PDF's own glyph stream with its font labels**, applying
  each affected font's fixed substitution table. That is deterministic and is
  not OCR, so the file keeps the plain `.txt` suffix. Characters in the Times
  fonts are untouched, which is why genuine `k` (Luick, Laker, kontinentalen)
  survives correctly. Each substitution was established three ways: by font
  membership; by token-by-token alignment against an independent Vision OCR of
  the same pages; and, where doubt remained, by rendering the line at 500 dpi
  and reading it off the page. The restored forms also supply a lexical
  plausibility check, with expected palatal spellings (`eċġ`, `seċġ`,
  `hryċġ`, `dīċ`, `rīċe`, `wīċ`, `ċeorl`, `wreċċa`, `styċċe`, `wiċċe`,
  `mēċe`, `fliċċe`). That agreement is corroboration, not a substitute for
  checking the printed glyphs.

Three further files (Bremmer, Kortlandt, Repanšek) had a *recoverable*
defect: the John Benjamins house font emits combining macrons as a trailing
`U+00A4`, with `\` for schwa and dotless `ı` for `i` in Kortlandt. That
mapping is one-to-one and context-free, so it was repaired deterministically
(`mo¤na` → `mōna`, `æ¤` → `ǣ`, `*e¤\` → `*ēə`) and the repair was verified
against forms whose value is fixed by the surrounding prose. No judgement
call was involved and no OCR was needed.

Every file in this group uses the `=== page NNN ===` marker convention with
**printed folio numbers**, so memos can cite exact printed pages. Each file
opens with a header recording the citation, the extraction method, the
mechanically verified pdf-sheet-to-printed-folio offset, and an itemised
account of every sheet that did not self-confirm its folio (opening pages
with drop titles, full-page figures, blanks). The nine-source packet comprises
245 printed pages. An independent PDF-edge check confirmed 241 folios; the
four exceptions are Campbell p. 78 and Laker p. 165 (opening pages),
and Versloot 2021 pp. 352 (full-page figure) and 374 (blank).

Research use of these sources is organised in
`Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/`, whose
synthesis dossier is the single authority for the comparative English/Frisian
chronology.

- `campbell_1939_some_old_frisian_sound_changes.vision.txt`
  Campbell, "Some Old Frisian Sound-Changes", TPS 38.1 (1939), pp. 78-107.
  A classic argument against inherited short-*a* fronting in a unitary
  Anglo-Frisian period, using competing English and Frisian diphthong
  chronologies (pp. 90-91). 30 printed pages.

- `bremmer_2008_north_sea_germanic_at_the_cross_roads.txt`
  Bremmer, "North-Sea Germanic at the Cross-Roads: The Emergence of Frisian
  and Hollandish", NOWELE 54/55 (2008), pp. 279-308.
  Includes a substantial locally available report of Stiles 1995, which CAPR
  does not hold directly. 30 printed pages.

- `kortlandt_2008_anglo_frisian.txt`
  Kortlandt, "Anglo-Frisian", NOWELE 54/55 (2008), pp. 265-278.
  Explicit numbered relative chronologies. 14 printed pages.

- `laker_2007_palatalization_of_velars.txt`
  Laker, "Palatalization of Velars: A Major Link of Old English and Old
  Frisian", ABaeG 64 (2007), pp. 165-184.
  The hinge of the shared-versus-independent palatalization question.
  20 printed pages. Rebuilt font-aware from the glyph stream (see above);
  palatal `ċ`/`ġ` are correct. Laker prints `kapia` and `ċeapian` without
  macrons; that is faithful to the printed page, not an extraction loss.

- `repansek_2012_anglo_frisian_vowel_system.txt`
  Repansek, "Remarks on the Development of the 'Anglo-Frisian' Vowel System",
  NOWELE 64/65 (2012), pp. 77-90. 14 printed pages.

- `versloot_2017_proto_germanic_ai_in_north_and_west_germanic.txt`
  Versloot, "Proto-Germanic *ai in North and West Germanic", Folia
  Linguistica Historica 38 (2017), pp. 281-324. 44 printed pages.

- `versloot_2021_traces_of_a_north_sea_germanic_idiom.txt`
  Versloot, "Traces of a North Sea Germanic Idiom in the Fifth-Seventh
  Centuries AD", in Hines & IJssennagger-van der Pluijm (eds), *Frisians of
  the Early Middle Ages* (2021), pp. 339-374. Printed p. 352 is a full-page
  figure and p. 374 is blank. 36 printed pages.

- `waxenberger_2019_absolute_chronology_pre_oe_runic.txt`
  Waxenberger, "Absolute Chronology of Early Sound Changes Reflected in
  Pre-Old English Runic Inscriptions", NOWELE 72.1 (2019), pp. 60-77.
  Absolute, archaeologically anchored dates; to be kept methodologically
  distinct from handbook relative chronologies. 18 printed pages.

- `versloot_2025_reconstructing_historical_phonology_of_oe.txt`
  Versloot, "Reconstructing the Historical Phonology of Old English",
  English Language and Linguistics 30.1 (2026; first published 2025),
  pp. 103-141. Open Access; bibliography key `Versloot2025`.
  39 printed pages, 39 of 39 folio-verified. Added to the pass after the
  first eight. Argues against the "Standard Theory" chronology, replacing
  the eight traditional sound laws targeting PGmc *a with a smaller set
  having claimed Frisian parallels, tested against the Epinal and Erfurt
  glossaries.

  The text layer passes the diacritic screen, but the IPA font maps three
  SMALL CAPITAL letters into the Unicode private use area: U+F769, U+F76C
  and U+F772, on the systematic pattern 0xF700 plus the base letter's ASCII
  code. Each was confirmed by rendering its line at 520 dpi and reading it,
  and repaired to small capital I, L and R respectively. These are
  Versloot's notation for the velarized resonants conditioning breaking, so
  dropping them would have deleted the conditioning environment from a paper
  about breaking. Ligatures and the non-breaking hyphen were also normalized
  so that "different" and the environment "-rC" are searchable.

  One quirk to know about: on pp. 110-119 `pdftotext` kerns the running-head
  folio apart, so p. 113 appears in the body as "11 3". The page markers are
  unaffected; do not cite from the running head.

### Additional specialist sources: Google Vision PDF OCR

These two requested works are now held as local, ignored PDFs and searchable
Vision texts. Both are scans with unreliable old embedded OCR, not born digital.
Their embedded layers were rejected rather than published as reference texts.

| Committed reference text | Bibliographic identity | Printed-page preservation |
|---|---|---|
| `hogg_1979_old_english_palatalization.vision.txt` | Richard M. Hogg, "Old English Palatalization", TPS 77.1 (1979); key `Hogg1979`; DOI 10.1111/j.1467-968X.1979.tb00855.x | 89–113, 25 sheets; printed folio = sheet + 88; 24 numbered running heads confirmed; opening p. 89 anchored by the publication range and following p. 90 |
| `goblirsch_1991_germanic_ai_and_au_in_anglo_frisian.vision.txt` | Kurt Gustav Goblirsch, "Germanic ai and au in Anglo-Frisian", ABaG 33 (1991); key `Goblirsch1991`; DOI 10.1163/18756719-033-01-90000004 | 17–23, 7 sheets; printed folio = sheet + 16; six numbered running heads confirmed; opening p. 17 anchored by the publication range and following p. 18 |

The established runner at `Code/Vision/ocr.py` successfully processed both
original PDFs with `asyncBatchAnnotateFiles` / `DOCUMENT_TEXT_DETECTION`
and its existing staging-bucket configuration. Earlier synchronous image
requests failed with resource-exhaustion errors, but the normal PDF runner
worked without changing billing or credentials. No Google account repair
was needed.

The new texts use `=== page NNN ===` printed-folio markers throughout.
Raw JSON, 300 dpi comparison images, independent Tesseract output and the
old embedded OCR are retained in the ignored cache. Mean per-page plain-letter
skeleton agreement with Tesseract is 96.9% for Hogg and 95.4% for Goblirsch;
this does not establish diacritic accuracy. Image-verified repairs and residual
linguistic-symbol cautions are documented in each text's header. The original
nine texts plus these additions cover **277 printed pages**; **271** folios
are confirmed at page edges, with six explicitly recorded exceptions.
Acquisition and OCR do not themselves adjudicate either author's chronology.

### Further acquisitions: Bremmer 2009 and Nielsen 2001

| Committed reference text | Identification and method | Page preservation |
|---|---|---|
| `bremmer_2009_introduction_old_frisian.vision.txt` | Bremmer, *An Introduction to Old Frisian: History, Grammar, Reader, Glossary* (2009); the supplied ebook is the **corrected 2011 reprint**, identified on its copyright page. Seventeen born-digital exports have materially wrong special-font mappings, so all parts were sent through the established asynchronous Vision PDF runner rather than publishing the corrupted layer. | Complete 250-sheet sequence: i–xii, then 1–238. Roman frontmatter remains roman. All 228 displayed running-head folios independently checked; 22 suppressed opening/blank folios explicitly recorded, including five PDF-confirmed blank pages. |
| `nielsen_2001_frisian_and_grouping_older_germanic_languages.vision.txt` | Hans Frede Nielsen, chapter 48, "Frisian and the Grouping of the Older Germanic Languages", in Munske (ed.), *Handbuch des Friesischen / Handbook of Frisian Studies* (2001). Scanned article; processed through the same Vision PDF runner. | Twelve consecutive printed pages, 512–523; every folio independently checked against the page images. The adjacent chapter 49 opening on p. 523 is excluded, not attributed to Nielsen. |

The PDFs are retained locally as
`bremmer_2009_introduction_old_frisian_part_01.pdf` through
`bremmer_2009_introduction_old_frisian_part_17.pdf`, and
`nielsen_2001_frisian_and_grouping_older_germanic_languages.pdf`.
They remain ignored, as do raw OCR JSON and comparison images. Each text
records PDF hashes and exact sheet-to-folio mappings. Bremmer's repeated
ebook-access watermarks are excluded by their coordinates, without truncating
body text when Vision reads a footer before it. Special notation, diagrams and
tables still require image checks for load-bearing quotations.

Hogg's fricative misread as digit `3` is now transcribed as `ȝ` / `ȝ'`,
preserving his explicitly non-IPA notation (p. 103; p. 111, note 1).
The text header explains the modern IPA equivalents `[ɣ]` / `[ʝ]`;
lost palatal primes were restored from the images, not guessed.

## Other references

- `oe_sound_change_index.md`  
  Quick index of frequently cited sound-change passages + exact `rg`/`sed` commands.

- `knob_email_2026-01-22.txt` / `README_knob.md`  
  Project-specific correspondence/notes.


## Missing direct sources (Anglo-Frisian pass)

These works are load-bearing in the literature ingested above but are **not**
held locally in any form. They are recorded here so that no memo silently
turns one author's report of another into that other author's evidence. The
full audit, including what each one blocks, is in
`Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/missing-direct-sources.md`.

- **Stiles 1995**, "Remarks on the 'Anglo-Frisian' Thesis". *Highest
  priority.* Bremmer, Laker, Kortlandt and Repansek all engage his
  chronological argument; CAPR currently knows it only at second hand.
- **Fulk 1998**, "The Chronology of Anglo-Frisian Sound Changes". Directly on
  the question at issue. (Fulk 2018, *A Comparative Grammar of the Early
  Germanic Languages*, is held, but is not a substitute.)
- **Nielsen's other treatments**, where specifically load-bearing; the
  requested 2001 chapter is now held, but does not substitute for his monographs.
- **Siebs**, cited by Laker as a proponent of shared palatalization.

Hogg 1979, Goblirsch 1991, Bremmer 2009 and Nielsen 2001 are now held as
PDFs and page-preserving Vision texts. Their direct-source research review
is separate from ingestion. Stiles 1995 and Fulk 1998 are the two remaining
priority acquisitions.

### Luick: complete scans and printed-page verification

Both downloaded scans were processed successfully by the established
asynchronous Google Vision PDF runner, using its configured English hint.
All 1,212 sheets have ordered raw responses and page-marked reference text;
no job or page-error response occurred. The ignored PDFs retain their
original hashes; raw responses are cached under `.cache/anglo-frisian/luick/`.
The text headers record the hashes, method and exceptional folios.

| Holding | PDF sheets | Printed-page map |
| --- | --- | --- |
| First division, 1921 | 568 | Sheets 17–564 = pp. 1–548 (sheet − 16) |
| Second division, 1940 | 644 | Sheets 23–270 = pp. 549–796 (sheet + 526); 279–414 = pp. 797–932 (sheet + 518); 423–639 = pp. 933–1149 (sheet + 510) |

Inserted editorial matter, frontmatter and terminal sheets retain explicit
unnumbered-sheet labels. Do not apply a single offset to the second division.
Eighteen no-text sheets were visually checked as blank/cover sheets; the
first division's sheet 110 is the blank verso at numbered position p. 94.
Seventeen numbered positions lack a matching edge token in Vision OCR.
Their image audit distinguishes five displayed folios missed by the edge
check, one clipped running head (p. 733), and eleven suppressed folios
anchored by neighboring printed pages. No body sheet was omitted.

Printed pp. 130–133 (first division, sheets 146–149) were visually checked
for §§118–123. Section 637 is now directly located and visually read at
pp. 835–841 (second division, sheets 317–323), including the chronology
in note 8 on p. 841 and its transition to §638. These checks replace the
previous “§637 unlocated” limitation; they do not adjudicate Luick's
historical premises. Follow-on images verify p. 129 (§117), pp. 157–163
(§§168–176, with the start of §177), and pp. 842–848 (§§638–639).
The §639 continuation ends on p. 848; §640 starts on p. 849.
The enlarged p. 133 conjectural chain reads æe > æə > æa > ā:
its middle offglide is schwa, not the digit 3. The g-shaped letter in
consonant discussions is not a licence to replace OCR `3` by one IPA
symbol throughout the texts.

Relevant errata were visually checked in first-division sheet 15 and
second-division pp. 1142 and 1145. The corrections to pp. 132 and 162
are grammatical, not retractions of the chronological argument.
The addition of “, altfriesisch” to p. 832 is recorded but does not
independently adjudicate common-stem event identity. These are bounded
checks of relevant passages, not an exhaustive errata incorporation.
OCR remains unreliable for specialist glyphs elsewhere.
Use the original page images, not a guessed normalization, for exact
phonetic quotations; the complete text remains an explicitly uncorrected
OCR witness rather than a diplomatic edition.

## Not yet OCRed

- **Lloyd & Springer**, *Etymologisches Wörterbuch des Althochdeutschen*, Bd. 1 (1998).  
  Source PDF is a scan with no text layer; would need OCR. DJVU version also available.  
  Located in Downloads, not yet incorporated.
