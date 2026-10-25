# Corrective consolidation, 25 October 2026

Starting revision: `5515159665a20384db55baf500287895b7031ad5`.
This corrects library access, OCR selection and acquisition coverage only.
It makes no historical assessment of the acquired arguments.

## What changed

The first milestone left authoritative restricted texts in a disposable cache,
did not compare the difficult OCR methods, did not test clean-checkout access
or restoration, and treated absence from Downloads as the stopping point for
Wright--Wülcker II. The original [inventory](inventory.tsv) and
[610-sheet page map](page_map.tsv) remain unchanged historical records.
Their original PDFs still match their recorded hashes.

[holdings.tsv](holdings.tsv) is the current access manifest, not a competing
bibliography or scientific authority. It identifies 12 distinct PDF/text
representations: the original 11, plus Wright--Wülcker II. Gante's two
representations remain one contribution. Bibliographic authority remains
`docs/refs.bib`; no prior accepted evidence receipt is revised.

## Canonical access and restoration

| Material | Canonical location | Fresh public checkout |
| --- | --- | --- |
| Twelve original PDFs | `docs/references/<stem>.pdf` | Not included; locally retained, hashes in manifest |
| Van Helten complete text | `docs/references/van_helten_1891_grammatisches.vision.txt` | Included |
| Wright--Wülcker II complete text | `docs/references/anglosaxonoldeng02wriguoft.txt` | Included |
| Other ten complete texts | `docs/references/local/ga-prefix/<stem>.txt` | Not included; authorised local holding |
| Native/Tesseract/Vision comparison candidates | `docs/references/local/ga-prefix/ocr-comparison/` | Not included; in local restoration bundle |
| Checked short samples, scores, hashes and page maps | This acquisition directory | Included |
| Intermediate rendering, API JSON and extraction files | `.cache/ga-prefix/` | Disposable; not authoritative |

Restricted texts cover Bammesberger, Quinlin, Samuels, both Pheifer works,
Crouch, Minkova, Herren/Sauer and Gante's slides/handout. Each complete text
has bibliographic identification, source PDF checksum, preparation method,
page markers and significant limitations. The PDF witness remains authoritative
for disputed glyphs. No canonical holding depends on Downloads or `.cache/`.

The repository remains public. After the access discussion, the user explicitly
selected public Git with restricted texts in durable local holdings only.
No redistribution permission for these complete modern works was established;
OCR processing and noncommercial purpose alone were not treated as permission
to publish them. Only the public-domain original texts of 1884 and 1891 are
distributed in full. The new narrowly scoped ignore rule protects
`docs/references/local/`; no existing PDF/cache exclusion was relaxed.
Short, attributed comparison fragments are technical verification apparatus,
not substitute complete editions. The user authorised the controlled Vision
processing; this did not constitute a licence to publish complete results.

The local bundle is:

```text
docs/references/local/backups/ga-prefix-2026-10-25.tar.gz
docs/references/local/backups/ga-prefix-2026-10-25.tar.gz.sha256
```

It contains the twelve PDFs, ten restricted canonical texts, comparison
candidates and a frozen restoration manifest. It does not contain credentials.
Copy the bundle and checksum through an authorised private channel to restore
another working copy. From the project root of a matching checkout:

```bash
(cd /authorised/path && shasum -a 256 -c ga-prefix-2026-10-25.tar.gz.sha256)
tar -xzf /authorised/path/ga-prefix-2026-10-25.tar.gz -C .
python3 docs/references/ga_prefix_2026-10-25/verify_holdings.py \
  --require-local --check-ocr
```

The checksum is checked in the bundle directory. Restore only into a clean authorised
checkout; the archive uses project-relative paths. The public texts and
current manifest already come from Git.

This is a tested local recovery route, **not off-machine disaster recovery**.
No persistent remote controlled-access store was supplied or configured.
An agent with only a public clone cannot read the restricted complete works.
An ignored local PDF is not represented as automatically recoverable from
GitHub. The owner must retain/provide the bundle or arrange authorised access.

Wright--Wülcker II can also be reacquired independently of the local bundle:
the exact PDF URL and checksum are in the manifest, with the IA identifier
and input hashes in [wright_ii_acquisition.json](wright_ii_acquisition.json).
If IA replaces a derivative, a checksum mismatch is an acquisition change to
investigate, not permission to silently accept a new witness. Van Helten's
separately supplied PDF has no independently verified automatic download route;
its exact scan is restored from the local bundle, while its complete text
is already in Git.

## Controlled OCR comparison

Twelve original page images were examined: Bammesberger pp.377,382,389;
Quinlin pp.145,147,149; Samuels pp.65,96,110; van Helten pp.461,463,488.
The [64 manually checked fragments](ocr_reference_sample.tsv) comprise twelve
ordinary-prose fragments and 52 technical fragments. Image locations are
recorded separately from OCR text; no machine output was silently promoted
to a corrected reading. Ambiguous marks were enlarged before reference entry.

The comparison retains native extraction, the prior multilingual Tesseract
text, and Vision for each selected page. The new van Helten local candidate
used Tesseract 5.5.2, `deu+eng+grc+isl`, segmentation 3, 2400px longest edge.
Existing Bammesberger/Quinlin/Samuels local candidates used the previously
documented 3000px rendering and language sets.

The existing `Code/Vision/ocr.py` PDF runner processed nine sample sheets.
Hints: Bammesberger `de,en,el`; Quinlin `en,de`; Samuels default English.
For the default `["en"]` configuration the runner omits explicit
`image_context`, rather than forcing the service to recognise only English.
The existing 34-page van Helten Vision run supplied its comparison candidate;
no new complete run was performed for that source. Raw responses/renderings
are cache intermediates; retained candidate page texts and committed comparison
rows preserve the decision evidence without requiring another API call.

The reproducible score is minimum character-edit distance to the best matching
span on the same candidate page, after NFC and whitespace-only normalization.
It does not change spelling, accents, case, punctuation or hyphenation.
This is an **optimistic fragment-retrieval metric**, not whole-page character
error rate: short/repeated forms may match elsewhere on a page, and empty
best spans mean no recognisable matching fragment, not proven page omission.
The sample is deliberately difficult and small, not an estimate for every
page. [ocr_comparison.tsv](ocr_comparison.tsv) exposes the actual matched
strings and edit counts; `verify_holdings.py --check-ocr` reproduces all
192 comparisons using the authorised candidate holding.

| Source | Native technical edits / characters | Tesseract | Vision | Retained canonical method |
| --- | --- | --- | --- | --- |
| Bammesberger | 13/78 | 2/78 | 11/78 | Existing Tesseract |
| Quinlin | 7/110 | 6/110 | 1/110 | New complete Vision, 15/15 sheets |
| Samuels | 14/100 | 10/100 | 5/100 | New complete Vision, 55/55 sheets |
| van Helten | 6/67 | 6/67 | 1/67 | Existing Vision |

| Source | Native prose edits / characters | Tesseract | Vision |
| --- | --- | --- | --- |
| Bammesberger | 0/113 | 0/113 | 0/113 |
| Quinlin | 0/143 | 0/143 | 0/143 |
| Samuels | 0/152 | 1/152 | 2/152 |
| van Helten | 3/135 | 1/135 | 0/135 |

Concrete examples explain why fluent prose was not the deciding criterion:

- Bammesberger's Greek `τομός`/`τόμος` is searchable in the local Tesseract
  candidate but not recovered by the best-span native/Vision comparisons.
  Tesseract still reads Gothic `miþgatiuhan` with `d` for `þ` and `gá-`
  as `gd-`; neither engine is a diplomatic authority.
- Quinlin's Tesseract substitutes diaeresis for the acute accents in
  `*/kóm-dhugh-os/` and `*/hándugaz/`; Vision retains these sample accents.
  All candidates still mishandle the ogonek in `hǫndugr`. The bracketed
  stress expression, slashes and table content were included, but linear
  text does not reproduce the derivation table's geometry.
- Samuels's native `cyðnise` becomes `cyanise`, and `giðæhtung` becomes
  `giazehtung`. Vision retains those sampled forms, while still reading
  `gisihðe` as `gisihoe` and misreading some thorn/eth elsewhere.
  The sampled `spātan` is not silently normalized to another dialectal form.
- Van Helten's Vision sample retains `môdor`, `-ûn`, `-ôn` and `âgon`
  better than the other candidates; `tó niht` still loses its accent.
  The default English hint therefore did not justify an automatic rerun.

The inspected evidence includes reconstructed asterisks, ga-/gi-/ge-,
Greek accent placement, Gothic forms in Roman transliteration, Old English
þ/ð/æ, macrons/circumflexes, brackets/slashes, German typography, footnotes,
section/page references and a tabular comparison. The sample does not
contain Gothic Unicode script or a verified `gæ-` instance; those are not
claimed as tested. Superscripts on the source images become baseline digits
or lose attachment in plain extraction. Their vertical position is not a
Unicode-text accuracy score, and remains an image/layout limitation.
No global character substitution or invented restoration was applied.

## Pheifer and missing sources

The complete supplied Pheifer edition remains available under its new local
canonical text path, including Roman frontmatter, apparatus and both indices.
§63, p.lxxv is still sheet73 and directly searchable. The conversion's explicit
loss of non-Latin-1 diacritics is preserved in its header and manifest.
Arguments depending on vowel length/accent or a removed mark require an
independent printed-page witness; OCR of the damaged conversion cannot supply
one. The legitimate IA catalogue
<https://archive.org/details/oldenglishglosse0000phei> identifies a 1974
Clarendon scan (scandate 2021-11-22), with `access-restricted-item=true`
and the ordinary PDF marked private. This is a potential authorised image
witness, not an acquired facsimile or a verified reading of p.lxxv.
No access controls were bypassed, and no verified original-print facsimile
was acquired in this correction.
No marks were fabricated or inferred from historical expectations.

Bennett1968 remains **Pending source acquisition — no full text supplied**.
It was not reconstructed from Quinlin and has not been represented as read.
The three peripheral exclusions remain unchanged.

## Wright--Wülcker II

IA item `anglosaxonoldeng02wriguoft` supplied the complete 498-sheet PDF,
DjVu XML OCR and `scandata.zip`. The advertised individual scandata URL was
absent (HTTP404); the archive's actual ZIP supplied the mapping successfully.
The title image on sheet3 explicitly identifies Thomas Wright, second edition,
edited/collated by Richard Paul Wülcker, volume II: *Indices*, London,
Trübner, 1884. This is not the existing volume-I holding.

The canonical text retains XML line/word reading order and sheet boundaries.
[wright_ii_page_map.tsv](wright_ii_page_map.tsv) records every included leaf:
sheets7--491 = printed pp.1--485; frontmatter, advertisements and covers
remain unnumbered rather than receiving guessed folios. The 502 scan leaves
include four excluded colour/white calibration cards; the 498 access-format
leaves match both the PDF and OCR objects.

The related key `WrightWuelcker1884II` explicitly identifies volume II.
`WrightWuelcker1884` retains its volume-I identity and original file pointer;
reciprocal `related` fields join the two without changing existing citations.

Images of printed pp.53 and73 (sheets59 and79) were checked. They are
Latin-index pages, beginning with `comparantur` and `diafragma` respectively;
neither supplies a literal *gi-mynd* entry. Printed p.303 (sheet309) has
nearby `gemyndelican`, `gemyndelice`, `gemyndleas` and `gemynte` index
entries, not a verified replacement for the requested locator.
The Toller reference's precise edition/page/line interpretation remains
unresolved. Acquisition is verified; the requested attestation is not.

## Acceptance checks

The clean staged Git-tree export contained exactly the two public-domain
canonical complete texts and none of the twelve original PDFs or ten
restricted complete texts. The default verifier reported that limitation;
`--require-local` failed explicitly before restoration.

Restoring the 59-file checksummed bundle into that clean tree then passed
all twelve PDF/text checksums, all 1,108 sheet markers and all 192 OCR
sample/method comparisons, without Downloads or `.cache/` present.
A deliberate text alteration failed its checksum check. These are actual
local restoration results, not a claim of remote restricted-source access.

All eleven distinct contribution/volume keys resolve through citeproc.
Existing bibliography sanity checks and focused repository/citation-range
regressions passed: 14 tests and 1,098 subtests. The supported
`adjudicate.py --refresh` and `artifact_graph.py --check` reported
`CONTROL PLANE CLEAN`; only the bibliography checksum changed in generated
survey provenance.

Combined, sound-change and lexical manuscript citeproc output is unchanged
from the starting bibliography. Original intake inventory/page-map bytes,
scientific sources, executable rules, chronology, lexical selections,
reader prose and protected outputs are unchanged. No Foma revalidation
or historical adjudication was undertaken.
