# A-Ablaut literature: ingestion manifest

Source directory: `~/Downloads/A-Ablaut/` (seven PDFs, inventoried 2026-10-15).
Policy: `docs/references/README_resources.md` — original PDF retained under
the gitignored `docs/references/*.pdf` rule; committed searchable text with a
provenance header (PDF SHA256, extraction method, every deterministic repair,
sheet→printed-folio map) and `=== page NNN ===` markers carrying **printed**
folios. Registration in `docs/refs.bib` and `README_resources.md` (new
subsection "SC015 *i > e* packet (A-Ablaut collection)").

Ingestion verifies holdings; it does not adjudicate any author's hypothesis.

| # | Downloads file | Identification | Status | Bib key | Retained files (`docs/references/`) | Method / repairs | Page map and verification |
|---|---|---|---|---|---|---|---|
| 1 | `nowele.70.2.02hil.pdf` | Hill, *NOWELE* 70.2 (2017) 135–170 | **Duplicate** — SHA256 `73278c5e…0659e` identical to the held `hill_2017_west_germanic_lengthening.pdf` | `Hill2017` (existing) | unchanged | none | existing extraction already verified pp. 149–158 |
| 2 | `Cercignani_15Jun+Final+version_15h27.pdf` | Cercignani, "On the Germanic and Old High German distance assimilation changes", *Linguistik online* 116, 4/22 (2022) 41–59, DOI 10.13092/lo.116.8889 | **New** | `Cercignani2022` | `cercignani_2022_distance_assimilation.pdf` (sha `7149856e…`), `.txt` (sha `a3467f08…`) | born-digital, `pdftotext -layout`; 9× U+F02D (Symbol list dash) → U+2212 | folio = sheet + 40; 18/19 edge-confirmed (opening p. 41 anchored by first-page citation line) |
| 3 | `Howell 2024 What do we really know about Gothic breaking.pdf` | Howell, ch. 4 in Klein & Ratkus (eds), *Studies in Gothic* (OUP 2024) 75–91, DOI 10.1093/oso/9780198896692.003.0004 | **New** | `Howell2024` | `howell_2024_gothic_breaking.pdf` (sha `060ce5f8…`), `.txt` (sha `bf0311e4…`) | born-digital; 17 access-watermark lines removed; 192× U+2217 → `*` | folio = sheet + 74; 16/17 edge-confirmed (opening p. 75 anchored by chapter DOI block) |
| 4 | `jasanoff1973.pdf` | Jasanoff, "The Germanic Third Weak Class", *Language* 49.4 (1973) 850–870, DOI 10.2307/412065 | **New** — scan; embedded layer rejected | `Jasanoff1973` | `jasanoff_1973_germanic_third_weak_class.pdf` (sha `e2895c87…`), `.vision.txt` (sha `331dd22a…`) | JSTOR embedded OCR has 0 macrons (`habOn`, `hab&t`); Google Vision async PDF runner (`Code/Vision/ocr.py`, hint `en`) → 241 macrons, 107 thorns; NFC; JSTOR footers removed | sheet 1 = JSTOR cover (unnumbered); folio = sheet + 848 for sheets 2–22; 21/21 edge-confirmed; pp. 865 and 868 (*liznaiþ(i)*, *lirnên/lernên/lizniþ*) image-checked; residual þ→b/p misreads flagged in header |
| 5 | `s10828-025-09166-0.pdf` | Kostakis, "Coda nasals in early Germanic languages", *JCGL* 28:6 (2025), 32 pp., DOI 10.1007/s10828-025-09166-0 | **New** | `Kostakis2025` | `kostakis_2025_coda_nasals.pdf` (sha `f96c4696…`), `.txt` (sha `aa377afb…`) | born-digital; 242× U+22C6 → `*`; 149 fi/fl ligatures decomposed | article-number pagination, page = sheet; 32/32 confirmed via "Page N of 32" |
| 6 | `to-know-to-teach-and-to-learn-in-germanic.pdf` | Tarsi & Laker, "'to know', 'to teach', and 'to learn' in Germanic", *JGL* 38 (2026) 40–58, DOI 10.1017/S1470542726100178 | **New** | `TarsiLaker2026` | `tarsi_laker_2026_know_teach_learn.pdf` (sha `be6f8043…`), `.txt` (sha `43a16601…`) | born-digital; 19 CUP footers removed; 2× U+0001 → `+` (read from 150 dpi renders of pp. 43, 50) | folio = sheet + 39; 19/19 edge-confirmed |
| 7 | `Mubahis_02_Scheungraber.pdf` | Scheungraber, *Die Entwicklung der urindogermanischen Nasalpräsentien im Germanischen*, Magisterarbeit LMU München 2010; Mubahis Bd. 2 | **New** (grey literature; supervisor E. Hill) | `Scheungraber2010` | `scheungraber_2010_nasalpraesentien.pdf` (sha `2b7f4cda…`), `.txt` (sha `7cb526a0…`) | born-digital; PUA repairs U+E548→`i̯` (79), U+E40A→`ā́` (30), U+E535→`ī` (1), U+0001/U+0002→`•` (2+2); NFC | sheet 1 unnumbered cover, sheet 2 = p. 1; folio = sheet − 1; 245/246 edge-confirmed |

Glyph screen applied to every extraction: control characters, private-use
code points, U+FFFD, combining-mark counts, asterisk/macron/thorn counts.
Every residual non-ASCII symbol class was inspected in context before the
one-to-one repairs above were fixed. No linguistic normalization, no
correction of authors' notation.

## Not held

- **Hock 1973** (participles and *a*-umlaut), cited by Hill (2017: 150,
  154–155); not in the collection and not held. Requested by the brief;
  reported here at second hand only.
- Howell 1988a/b, 1991a/b, cited by Howell 2024; not held.

## Bibliography validation

`python3 Germanic/tools/check_bibliography_sanity.py` → passed (2 files);
105 entries, no duplicate keys.

Reproduction: `files/aablaut_ingest.py` in the session workspace (one-time
driver; rerunning it overwrites the six texts from the same PDFs and the
cached Vision output, deterministically).
