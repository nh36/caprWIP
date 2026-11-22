# Hay article source inventory, 22 November 2026

## Result

This report records the local source-inventory phase only. No phonological
experiment, lexical row, FST rule, book publication, or PR merge was changed.
PR #21 remains open and is still a draft; it was not merged. The work was
performed on the separate `research/hay-article` branch.

## Environment and scope

The current worktree is the main CAPR checkout. Existing worktrees were
listed and left intact. The `113101ac...` SC047 integration worktree remains
registered for PR #21.

The accessible candidate locations included:

- Downloads
- Downloads/Germanic
- Downloads/Germanic 2
- Downloads/New CAPR resources
- Downloads/New to OCR
- Downloads/New new to OCR
- Downloads/Books2
- Desktop/CAPR stuff
- the local August 2026 archive
- the canonical `docs/references/` library

Candidate counts: 733 PDF/DjVu/EPUB/image-like files under Downloads,
629 under `docs/references`, 174 under the local August archive. The machine
inventory and existing holdings audit remain more authoritative than filename
appearance for distinguishing duplicates and editions.

## Ingestion performed

Five newly relevant originals were byte-preserved and registered locally:

| Source | Canonical private/original path | SHA-256 | Extraction |
|---|---|---|---|
| Minkova 2014 | `docs/references/minkova_2014_historical_phonology_of_english.pdf` | `98fff07475818c69ad9b116aef62225a4d322350eb45c1f76759d025ac358009` | 456 pages; native layout text added |
| Jones 1989 | `docs/references/jones_1989_history_of_english_phonology.pdf` | `2f0cd1637b6f99722bfd1996b4fa55f517bc71254f9cabbbeb9dbea4b93b19c8` | 340 pages; native layout text added |
| Mokrowiecki 2015 | `docs/references/mokrowiecki_2015_vowel_quantity_old_english.pdf` | `22d81654f633e913f545d631a027d42ca64f09f3db01728eecd0dfb9903bbea1` | 30 pages; native layout text added |
| *Friesische Studien II* 1995 | `docs/references/friesische_studien_ii_1995_complete.pdf` | `c904e5c1a73df06fc344347d1f72e78e52a3a14d24326cc8b6a3ceeef5090269` | 234-page scan; native text unusable |
| Merged missing-pages scan | `docs/references/friesische_studien_ii_1995_merged_missing_pages_129-148.pdf` | `81ab75404400fc42ae4dfc9ca571fad237e386fbc2aea9150dd1dbf953dda320` | 214-page companion scan; distinct preservation copy |

The Stiles 1995 chapter was therefore located in the containing volume. It
occupies printed pages 177--220. The complete PDF supplies the chapter, while
the companion PDF preserves a separately assembled missing-pages variant. The
two PDFs are not byte-identical and are not silently merged.

The originals and complete text aids are ignored/private holdings. Public
metadata was reconciled in `docs/refs.bib` and the hay inventory TSV.

## Priority 1 checklist

| Work | Status | Next milestone |
|---|---|---|
| Ringe and Taylor 2014 | Located, preserved, extracted; not hay passage checked | Search and visually verify load-bearing hay/length pages |
| Hogg 1992/2011 Volume 1 | Located, preserved, extracted; native symbols require image checking | Verify quantity/glide/hiatus discussion |
| Campbell 1959 | Located, preserved, extracted | Verify inflection and orthographic passages |
| Jones 1989 | Newly ingested | Locate *heig*/*heg* discussion and check image pages |
| Minkova 2014 | Newly ingested | Locate hay/way, vowel length and glide vocalization passages |
| Mokrowiecki 2015 | Newly ingested | Visually verify orthographic quantity marks |
| Versloot 2025 | Located and preserved; acquisition variant retained | Assess the hay chronology against this account |
| Goering 2025 | Missing | Acquire DOI 10.1017/S1360674325000164 |
| Ritt 2000 | Missing from searched roots | Acquire the Lindisfarne Gospel accent study |

## Priority 2 and existing holdings

- Dahl 1938, Adamczyk 2018 and Hogg 1979 analogy are already held privately
  with targeted consultation records.
- Hollifield 1980 has both parts privately held with per-sheet OCR.
- Hogg/Fulk 2011 morphology, Boutkan 1995, and the Anglo-Frisian comparative
  holdings are already registered.
- Stiles 1995 is now closed as an acquisition gap. The complete text is not
  verified; source pages remain the authority.
- Bennett 1968 is held in the Sehrt festschrift.
- Dal 1934 is ILL requested and awaiting delivery.
- *Approaches to Old Frisian Philology* 1998 remains incomplete as an edition,
  but Fulk 1998 and the complete Fulk chapter are already held.

## Extraction and consultation limits

Native `pdftotext -layout` was used for born-digital PDFs. Native text for
Stiles/Mokrowiecki is not diplomatic transcription and requires source-image
checking. The Stiles volume is an image-only scan; a bounded local Tesseract
attempt did not recover a usable text aid. The page showing the beginning of
section 7 was visually confirmed, establishing that the scan contains the
chapter and that page-to-image navigation is possible.

No source should be described as “consulted” merely because text was
extracted. At present, these are acquired, preserved and searchable only to
the extent stated above.

## Outstanding ranked acquisitions

1. Goering 2025 DOI 10.1017/S1360674325000164
2. Ritt 2000 Lindisfarne Gospel accent marks
3. Bennett 1968 Gothic ga- accentuation
4. Dal 1934 in the nominal-levelling gap
5. Complete missing tail/printed page set for the 1998 Old Frisian volume,
   where needed beyond the complete Fulk chapter

## Recommended next task

Begin a bounded hay reading pass on Minkova 2014 and Jones 1989, with the
Mokrowiecki 2015 and Stiles 1995 pages as cross-controls. Visually verify only
the central passages concerning *hay*, *way*, glide vocalization, length,
gemination chronology and Anglo-Frisian controls. Do not alter the
phonological models until that evidence is documented.

## 22 November 2026 continuation

The priority inventory now contains 106 sources in Downloads/Germanic and
Downloads/Germanic 2. Exact hashes match 92 of them to canonical holdings;
14 remain unregistered candidates or variant scans. Thirteen document-like
items or PDFs had modification times on 22 November 2026; eight exact-byte
matches resolve to existing holdings and five have no existing canonical match.
The modification-time field is uncertain as a download-date field and is not
used as proof of acquisition time.

Newly registered or ingested sources include Nelson Goering's 2025/2026
article, the revised 2018 standalone Stiles extraction, Wright's Old English
grammar, Rask's Anglo-Saxon grammar, and the Sehrt festschrift containing
Bennett's 1968 Gothic *ga-* chapter. The Rask and Wright scans are
general historical grammars rather than hay-specific acquisitions.

The Stiles chapter has two distinct holdings: the complete image scan in
*Friesische Studien II* and a born-digital 38-sheet revised standalone
extraction. The standalone text is usable for comparative reading but is not
substituted for printed 1995 pp. 177--220.

Bennett 1968 is no longer missing: the Sehrt 274-sheet volume supplies printed
pp. 53--60. The exact chapter scan is mapped to PDF sheets 64--71. Sheet 65
was visually verified as printed p. 54. Load-bearing transcription remains.

Goering 2025 is acquired and native-text searchable. Ritt 2000 and Dal 1934
are ILL requested and awaiting delivery; no further local acquisition search
is needed for them.

The initial source-critical reading identifies Jones's Lindisfarne
`heig`/`heg` diphthongization discussion and Minkova's objection to
contrastive diphthongal length in *hæg* ‘hay’/*weg* ‘way’ as the strongest
immediate hay passages. These bounded page checks have now been completed.

## Completion reconciliation

The previous 14-candidate list has been resolved. Dresher's EPUB was
preserved and extracted. Erdmann 1972 and Sievers 1892 were preserved with
native text. The Sehrt and Goetz scans were preserved as incomplete, distinct
holdings. The valid Boutkan PDF is an exact duplicate of the canonical copy;
the extra zero-byte file is defective. The valid Hogg/Fulk -1 PDF is the
canonical morphology holding; the extra 114-byte file is a download-limit
message. CAPR manuscript, notes and the Secondary Stress working document
are excluded from the external scholarship inventory.

The Stiles 1995 printed chapter was OCRed for PDF sheets 186--229 and a
sidecar was retained at
`docs/references/local/stiles/stiles_1995_pp177-220.txt`.
The Bennett 1968 chapter was OCRed for PDF sheets 64--71 and retained at
`docs/references/local/bennett/bennett_1968_pp53-60.txt`.

All four Goetz tranches were preserved and OCRed. Pages 51--68, 69--87,
88--107 and 108--126 are available; printed p. 121 is missing from the final
tranche. The Sehrt volume variants preserve the complete Bennett chapter but
the volumes themselves omit pp. 33--34 and 255. These omissions are explicit
and do not invalidate pp. 53--60.

The 185-page PDF originally found in Downloads and later moved to Trash was
recovered into the project as `Inscriptions of Burma, Portfolio IV`.
It is unrelated to Germanic historical linguistics and is excluded from the
hay/Germanic inventory.
