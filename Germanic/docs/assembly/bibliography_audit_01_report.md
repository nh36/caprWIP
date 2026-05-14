# Bibliography audit 01 report

## Summary

- Inspected **55 targeted records**: 28 `@book` records, 26 `@article` records, and the single pre-audit `@incollection` record (`Kroonen2011`).
- Changed **30 BibTeX records** in `docs/refs.bib`.
- Completed all three priority records: `Bammesberger1997`, `Lloyd1966`, and `GermanicSlavicBaltic2025`.
- Audited book publication-place coverage across all `@book` records. Most already had verified `address` fields; for the cited books, publisher strings were normalized so the current citeproc style actually prints the place in the compact-alpha bibliography.
- Regenerated `lexical_volume_regular_compact_alpha_01.md`, `lexical_volume_regular_compact_alpha_01.tex`, and `lexical_volume_regular_compact_alpha_01.pdf`.

## Priority records

### Bammesberger1997

- **Original problem:** The record had corrected title and pages from the previous cleanup pass, but still rendered as a containerless article.
- **Verified metadata found:** `Anglia: Zeitschrift für englische Philologie` 115(2): 223--230, DOI `10.1515/angl.1997.115.2.223`.
- **Fields changed:** `journal`, `volume`, `number`, `doi`.
- **Source used:** Local PDF for title and pages; final journal/issue/DOI supplied by the user in-session.
- **Remaining uncertainty:** None.

### Lloyd1966

- **Original problem:** The record rendered as author-year-title only, with no journal, volume, issue, or pages, and the title in `refs.bib` did not match the local article PDF.
- **Verified metadata found:** `Language` 42(4): 738--745; stable JSTOR URL `http://www.jstor.org/stable/411829`; DOI `10.2307/411829`; title `Is There an a-Umlaut of *i in Germanic?`.
- **Fields changed:** `title`, `journal`, `volume`, `number`, `pages`, `month`, `doi`, `url`.
- **Source used:** Local JSTOR PDF title page; Crossref used as a secondary confirmation of DOI/container details.
- **Remaining uncertainty:** None.

### GermanicSlavicBaltic2025

- **Original problem:** The record was thin and bibliographically vague even after the earlier author-rendering repair.
- **Verified metadata found:** Unpublished manuscript, Geneva, 20 October 2025; circulating online as `full text (unfinished)`; author `Rémy Viredaz`.
- **Fields changed:** Entry type changed from `@misc`/working-paper style note handling to a `@misc` record with `howpublished` and `url` so the current citeproc style prints the manuscript status and location.
- **Source used:** Local PDF title page for author/title/date/place; web search for the Academia.edu URL.
- **Remaining uncertainty:** No journal or institutional repository publication could be verified in this pass; the public URL located is an Academia.edu copy.

## Article and chapter audit

- Found **23 incomplete non-book records** at the start of the pass: 22 article-style problems plus the mis-typed `Kroonen2011` monograph.
- Fixed **4 records** in this pass:
  - `Bammesberger1997`
  - `Lloyd1966`
  - `GermanicSlavicBaltic2025`
  - `Kroonen2011`
- Remaining incomplete article records after the pass: **21**.
- Remaining incomplete incollection records after the pass: **0**.
- The unresolved records are listed in `bibliography_audit_inventory.tsv`; they remain flagged with TODO comments in `docs/refs.bib` rather than being guessed into publication-ready form.

## Book address audit

- Checked all **28 `@book` records**.
- No cited book in the compact-alpha bibliography was missing an `address` field after audit.
- For the books cited in the current compact alpha, publisher strings were normalized to include place (for example `Oxford: Clarendon Press`, `Leiden and Boston: Brill`) because the present Pandoc/citeproc style suppresses `address` when left in a separate field.
- Left **`Kaluza1906`** unchanged because its existing TODO about publisher/edition remains unresolved; adding a surfaced place string there would have implied more certainty than the current evidence warrants.

## Output inspection

- The regenerated PDF bibliography now gives an adequate container for **Bammesberger 1997**: journal, volume, issue, pages, and DOI are present.
- The regenerated PDF bibliography now gives an adequate container for **Lloyd 1966**: journal, volume, issue, pages, and DOI/URL are present.
- **Viredaz 2025** now renders by author and states that the item is an unpublished Geneva manuscript, with the public online copy linked.
- Cited books now display publication places in the regenerated bibliography, including Oxford, Heidelberg, Toronto, Leiden and Boston, Amsterdam and Philadelphia, The Hague and Paris, Tübingen, and Berlin and Boston where verified.
- The references still begin on a fresh page with a visible heading.

## Remaining bibliography problems

The following records are still too thin for publication and remain flagged in `docs/refs.bib` and `bibliography_audit_inventory.tsv`:

- `Kaluza1906`
- `Erdmann1972`
- `Pierce1999`
- `Pierce2003`
- `Pierce2006`
- `Kroonen2006`
- `HowellSalmons1988`
- `Stiles2012`
- `Polome1967`
- `Polome1994`
- `Kylstra1983`
- `Hamp1990`
- `vanHelten1905`
- `Vine2019`
- `Mees2020`
- `Stiles2017`
- `NeriRingeReview`
- `Stiles1985`
- `Stiles1986a`
- `Stiles1986b`
- `Ringe1984`
- `Rice1994`

## Scope confirmation

- No TSV, FST, compact trace, model-entry prose, or citation-locator report files were edited.
- No generated TeX or PDF was hand-edited.
- Changes were limited to `docs/refs.bib`, regenerated compact-alpha outputs, `bibliography_audit_inventory.tsv`, and this report.

**Recommendation:** **B.** Bibliography is improved but specific listed records still need verification.
