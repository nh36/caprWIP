# Editorial cleanup report

## Corrections made

| Problem | File and location | Correction made | Evidence or authority | Verification | Substantive question remains for Fable |
|---|---|---|---|---|---|
| Mark 6:39 cited under the Luke edition key | `DRAFT.md`, §3 witness paragraph | Changed `@Skeat1874` to `@Skeat1871` | Skeat 1871 is the Cambridge Mark edition; the 1874 entry is the Luke edition | Key resolved; edition kept distinct | No |
| 1891 Miller edition used for p. 28 | `DRAFT.md`, §3 witness paragraph | Changed `@Miller1891` to `@Miller1890` | Bede p. 28 is in Miller's 1890 Part I, EETS OS 95; Miller 1891 is the second half | Catalog and held-partitioned edition records agree | No |
| Ritt entry was placeholder/incollection | `article_refs.bib`, `Ritt2000` | Replaced with article: 2000, *Sprachwissenschaft* 25(4), 497–512 | Supplied journal/article identity | BibTeX syntax and key check pass | ILL status remains awaiting delivery |
| Dal page range incomplete | `article_refs.bib`, `Dal1934` | Changed `243ff.` to `243--252` | Historical journal identity supplied for this cleanup | BibTeX syntax and key check pass | Original Dal text remains unconsulted; ILL pending |
| Corrupt Hogg–Fulk forms `se8e`/`se78` | `DRAFT.md` §2.1; `LITERATURE_MATRIX.md` §5 | Quarantined custom-font readings replaced by `*sege` and `*secg` | Held Hogg–Fulk Vol. 2, printed p. 20, PDF sheet 34, original page image | Search-free image check: page prints `sege` and `secg` | No direct phonological conclusion changed |
| Corrupt gap record in research memo | `RESEARCH_MEMO.md` §8 | Replaced `se8e` gap wording with `secg/sege` | Same Hogg–Fulk p. 20 image | Corrupt strings absent | No |
| Jones hay passage cited to p. 162 | `hay-source-critical-reading-2026-11-22.md`, Jones opening | Changed hay discussion to pp. 149 and 152; preserved p. 162 as non-hay pre-nasal matter | Earlier image verification and `PASSAGES.tsv` | PASSAGES.tsv already carries p. 152/sheet 166 and p. 162/sheet 176 distinctions | Lindisfarne locus itself remains unverified |
| Minkova final assessment still said `hæg` | Critical-reading report, initial assessment | Changed superseded form to `hēġ`; dated 400-dpi supersession notice retained | Minkova p. 178, PDF sheet 198, held page image | Page prints italic `hēġ` | No |
| Unqualified absence claims | `DRAFT.md`, `PARADIGM.md`, `LITERATURE_MATRIX.md`, `QUANTITY_EVIDENCE.md`, `RESEARCH_MEMO.md` | Qualified absence wording to “sources examined” or “overtly inflected form identified” | Sources examined have bounded ledger/edition scope | Wording now reflects search boundaries; Paris Psalter *hege* ×3 is acknowledged | Fable should assess whether these late datives bear on donor timing |
| Concordance Mark/Bede edition identities | `CONCORDANCE.tsv` rows 20–23 | Preserved `Miller1890` and `Skeat1871`; unverified Lindisfarne row remains id 26 | Existing concordance and edition records | 26 unique identifiers; 14-column structure parse passes | Lindisfarne secondary report remains unverified |

## Bibliography integrity

- `docs/refs.bib` remains unchanged.
- `article_refs.bib` now supplies `Skeat1871`, `Miller1890`, the corrected
  `Dal1934`, and the identified `Ritt2000` article.
- No new duplicate key is introduced.
- The Ritt and Dal entries explicitly state that ILL delivery or direct
  consultation has not occurred. They cite Dahl or Hogg–Fulk only for
  historical bibliographic/reporting purposes where appropriate.
- No DOI or URL was invented.

## Validation

- `python3 -m pytest Germanic/tests/test_hay_source_closeout.py -q`: 9
  tests passed.
- Combined-bibliography duplicate-key check: none.
- Combined-bibliography citation resolution: no missing keys.
- Concordance parse: 26 rows, 26 unique identifiers, 14 fields per row.
- Pandoc Markdown/citation parse: 2,617 words rendered successfully.
- PR #21 worktree and frozen SC047 capture were unchanged.

## Readings that could not be verified

- The 1871 Skeat Mark title page and the 1890 Miller first-half title page
  were verified from catalog metadata and the repository/edition record;
  the Mark 1871 original is not held at the identified local source path,
  and the Miller 1891 held PDF is not the 1890 first-half edition.
- Ritt 2000 and Dal 1934 remain unavailable through ILL and were not
  directly inspected.
- The Lindisfarne `heig/heg` locus cited in Jones remains to be verified
  against a held manuscript or facsimile.

## Questions reserved for research cycle 2

- Whether Dahl's no-gemination analysis is viable.
- Whether the Lindisfarne `heig/heg` evidence is genuine.
- Whether the `glīg/glēo` doublet supplies independent phonological controls.
- Whether the claims about vowel quantity and West Saxon vocalism need further qualification.
- Whether the late Paris Psalter datives inform availability of an oblique donor before i-umlaut.
- Whether the final derivational and evidential-symmetry claims should be revised after primary-source criticism.
