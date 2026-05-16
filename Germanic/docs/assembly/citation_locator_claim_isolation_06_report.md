# Citation locator claim-isolation 06 report

## Summary

- broad citations before: **219**
- broad citations after: **209**
- `claim_not_isolated` before: **68**
- `claim_not_isolated` after: **56**
- rows inspected in this pass: **68**
- locators added in this pass: **6**
- sentences split in this pass: **4**
- rows reclassified in this pass:
  - `page_markers_unreliable`: **2**
- unsupported citations removed after direct inspection: **1**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass stayed with the final easy wins only. The productive cases were entries
where one source-specific clause could be separated cleanly from a wider
comparative or paradigm discussion without distorting the prose. Once the
remaining rows tilted toward handbook synthesis or unsafe page anchoring, they
were left broad or reclassified rather than forced.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the headword-audit-01
baseline:

1. **10** rows were removed from the remaining-broad manifest after prose was
   safely split or narrowed.
2. **2** rows were reclassified in place from `claim_not_isolated` to
   `page_markers_unreliable`.
3. The rest of the inspected rows were left in place as genuine
   `claim_not_isolated` cases.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 56 |
| `general_background` | 59 |
| `headword_not_found` | 39 |
| `page_markers_unreliable` | 17 |
| `source_preparation_needed` | 15 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |

The localized rows also appear in the regenerated
`lexical_volume_regular_compact_alpha_01.md`, so the manifest and the current
reader-facing Markdown remain synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in
`citation_locator_primary_source_evidence.tsv`.

New evidence rows were added for:

- `CLMM01-0076`, `CLMM01-0078` — `RingeTaylor2014, 192`
- `CLMM01-0231` — `Kroonen2013, 420`
- `CLMM01-0243` — `Kroonen2013, 465`
- `CLMM01-0248` — `RingeTaylor2014, 193`
- `CLMM01-0293` — `RingeTaylor2014, 344`

All six were checked directly in the cited local source witnesses before being
inserted into prose.

## Sources worked through

This pass concentrated on the full remaining `claim_not_isolated` queue, with
the most productive direct verification coming from:

- `RingeTaylor2014`
- `Kroonen2013`
- `Campbell1959`

Additional inspection and reclassification work was carried out against:

- `ClarkHall1960`
- `Orel2003`
- `SieversBrunner1965`
- `Adamczyk2001`

## Successful split-and-localize fixes

| entry | source | locator | note |
| :--- | :--- | :--- | :--- |
| `nightmare / mare` | `RingeTaylor2014` | `192` | split the comparative-lemma sentence from the Orel clause and localized both the main sentence and the form note |
| `sap / sæp` | `Kroonen2013` | `420` | narrowed Kroonen from a broader stem-history paraphrase to the directly visible sap-family entry |
| `spare / sparian` | `Kroonen2013` | `465` | split Kroonen's inherited class-III line away from the still-unlocalized Orel clause |
| `staff / stæf` | `RingeTaylor2014` | `193` | isolated the singular/plural contrast `stæf, stafas` from the Luick sentence |
| `find / fundene` | `RingeTaylor2014` | `344` | separated the inherited infinitive citation from the later participial paradigm analysis |

## Reclassified rather than localized

Two rows turned out not to be claim-isolation problems after direct checking:

| entry | source | new status | reason |
| :--- | :--- | :--- | :--- |
| `spare / sparian` | `Orel2003` | `page_markers_unreliable` | the `*sparēnan ... OE sparian` entry was found, but the available local witnesses did not expose a stable printed page label for a new locator |
| `withy / wīþiġ` | `ClarkHall1960` | `page_markers_unreliable` | the `wiðig, wiði(g)e m.` entry was found, but the available local witnesses still did not expose a stable printed page label |

## Unsupported citation removed

- `withy / wīþiġ` — the broad `Adamczyk2001` support line was dropped from the
  sentence after direct reinspection, leaving the Campbell-based suffix claim
  stated more narrowly.

## Rows deliberately left broad

Examples inspected and left in `claim_not_isolated` because further splitting
would have become misleading or awkward:

| entry | source | reason |
| :--- | :--- | :--- |
| `find / fundene` | `Campbell1959`; `Luick1914`; `SieversBrunner1965` | the remaining sentence is still a three-source synthesis about analogical leveling, not one clause cleanly attributable to a single locator |
| `whine / hwīnan` | `SieversBrunner1965` | the available Brunner witness still behaves more like index-level classification support than a clean page-anchored prose claim |
| `wolf / wulf` | mixed handbook sources | the remaining prose still compresses exception handling and explanatory debate into broader argument rather than one safely localizable source sentence |

The remaining `claim_not_isolated` queue now skews more strongly toward this
kind of synthesis-heavy handbook prose than toward clean dictionary-style
sentence splitting.

## Support-package updates

All changed non-regular model entries had their paired support files updated:

- `.source_ledger.md`
- `.reviewer_checklist.md`
- `.model_implementation_report.md`

Each received a short claim-isolation-06 note recording the tightened locator or
the localized citation basis retained in the revised prose.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No locators were copied from earlier reports without direct rechecking in the
  local source witnesses.
- Every newly added locator has a matching primary-source evidence row.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- No generated TeX/PDF files were hand-edited.

## Recommendation

**C. address `page_markers_unreliable` / `source_preparation_needed`.**

This pass appears to have harvested the last clean claim-isolation easy wins.
The newly prioritized carryover rows showed the pattern clearly: once the prose
was narrowed, the remaining blocker was often not claim isolation but anchor
quality. The unresolved `claim_not_isolated` bucket is still numerically large,
but it now skews toward synthesis-heavy handbook argument rather than easily
splittable clauses.
