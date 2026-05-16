# Citation locator full-exhaustion 01 report

## Summary

This pass completed a **75-row first tranche** rather than all 161 remaining broad rows. The tranche combined the fully investigated difficult-source dossier, the explicit dictionary-dossier findings with row-level IDs, and a manually verified Campbell subset so that every counted row has an explicit recorded outcome.

- broad citations before: **161**
- broad citations after: **154**
- rows inspected: **75**
- locators added: **5**
- sentences split: **2**
- citations removed: **2**
- rows retained broad: **68**
- rows needing human review: **0**
- outputs regenerated: **yes**

## Method

This pass treated prior classifications as provisional, not final. Earlier `headword_not_found`, `source_quarantined`, and `source_preparation_needed` labels were challenged against the local primary-source witnesses again, source by source, using the difficult-source and dictionary dossiers plus direct spot-verification in the live prose targets.

Original PDFs/OCR were checked directly where the current tranche made changes or reclassifications. No proxy locators, OCR line numbers, file offsets, or guessed PDF image pages were accepted.

## Source-by-source results

The first tranche focused on sources with explicit row-level outcomes in hand.

| Source | Broad rows at start in tranche | Rows inspected | Locators added | Citations removed | Rows retained broad | Remaining blockers |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| Campbell1959 | 7 | 7 | 5 | 0 | 2 | Two mixed handbook sentences (`grave`, `fire`) still need cleaner claim isolation. |
| BosworthToller1898 | 16 | 16 | 0 | 1 | 15 | Remaining Bosworth rows outside this tranche still need their own pass. |
| ClarkHall1960 | 9 | 9 | 0 | 0 | 9 | Current local witness verifies entry content but does not give safe page markers for these broad background citations. |
| KlugeSeebold2011 | 14 | 14 | 0 | 0 | 14 | The source is no longer “quarantined”; the remaining issue is page-less witness structure, not entry recovery. |
| Kroonen2011 | 1 | 1 | 0 | 0 | 1 | Locator work is blocked only by source structure, not by missing content. |
| Kroonen2013 | 17 | 17 | 0 | 1 | 16 | Many rows now have verified page candidates but still need a source-specific application pass. |
| Orel2003 | 10 | 10 | 0 | 0 | 10 | Several rows have extractable pages but were deferred rather than half-applied here. |
| BrightCassidyRingler1971 | 1 | 1 | 0 | 0 | 1 | The finite-form evidence is valid; a later Bright-specific pass can still tighten it. |

## Successful recoveries

1. **CLMM01-0050 hedge / heġġ** — Campbell broad citation replaced with **`§407`** after isolating the j-gemination clause.
2. **CLMM01-0083 sheep / sċēap** — Campbell broad citation tightened to **`§185`** for West Saxon _scéap_.
3. **CLMM01-0190 lap / lappa** — Campbell broad citation tightened to **`§158`** for restored-_a_ _lappa_.
4. **CLMM01-0198 laugh / hliehhan** — sentence split; Campbell now cites only **`§407`** for j-gemination.
5. **CLMM01-0444 rust / rust** — Campbell broad citation tightened to **`§115`** for regular _u_ > _o_ lowering.
6. **CLMM01-0240 sieve / sife** — Kroonen citation removed because the cited nearby entry is the unrelated kinship lexeme _*sebjō-_.
7. **CLMM01-0430 knob / cnobba** — Bosworth-Toller citation removed after recheck failed to verify the cited _cnopp/cnoppa_ evidence.
8. **CLMM01-0235 sap / sæp** — Kluge-Seebold no longer treated as “source_quarantined”; the entry is recoverable in the page-less local witness and now carried as source-verified broad background.
9. **CLMM01-0023 fly / flēogan** — Bosworth-Toller no longer left in `source_preparation_needed`; the entry content is recoverable and now retained broad with an honest source-verified justification.
10. **CLMM01-0052 hedge / heġġ** — Clark Hall no longer left as `headword_not_found`; the lexical entry is recoverable in the legacy OCR and now carried as verified broad background.

## Retained broad citations

Representative retained-broad cases from this tranche:

- **CLMM01-0042 gold / gold** — retained broad as a genuine **multi-page discussion** about the _*gulþa-_ / _*gulda-_ alternation, not a single isolated claim.
- **CLMM01-0086 shilling / sċilling** — retained broad because the current sentence summarizes a wider suffixal and stem-family discussion rather than one page-bound fact.
- **CLMM01-0153 breast / brēost** — retained broad because the current wording compresses competing Proto-Germanic formations into one comparative summary.
- **CLMM01-0425 show (3sg) / sċēawaþ** — retained broad after direct recheck confirmed that Bright really does give _geond-scēawian_ with 3 sg. _-sceawað_; the citation is valid, but this pass did not yet convert it into a page-specific locator.
- **CLMM01-0345 meed / meorde** — retained broad with a verified Bosworth witness; the remaining issue is interpretive policy, not source recovery.

## Source-preparation failures

No inspected row in this tranche remained blocked solely by source preparation after direct recheck. The former `source_quarantined` Kluge-Seebold rows and the former Bosworth/Clark “not found” rows were all recoverable at the content level.

The remaining blockers inside the inspected tranche are **claim-isolation** blockers, not witness-quality blockers:

- **CLMM01-0044 grave / grafan**
- **CLMM01-0435 fire / fȳre**

## Human-review cases

No row in this tranche required a new human-review classification in order to decide citation validity. The older lexeme-policy questions around **meed / meorde** and **knob / cnobba** remain real philological/editorial questions, but they did not block the citation actions taken here.

## Safety checks

- no OCR line numbers were used as locators
- no file offsets were used as locators
- no search-result positions were used as locators
- no unverified PDF page indexes were used as locators
- no invented page ranges were introduced
- every new locator added in this pass has a primary-source evidence row
- the remaining-master manifest was updated in step with the seven citations removed from the live broad inventory in this tranche

## Files changed

- `Germanic/docs/assembly/book_prose/regular_all_01/2069-hedge-heġġ.book.md` — split and tightened the Campbell clause to `§407`
- `Germanic/docs/assembly/book_prose/regular_all_01/2179-sheep-sċēap.book.md` — tightened Campbell to `§185`
- `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.model.md` — tightened Campbell to `§158`
- `Germanic/docs/lexeme_reports/model_entries/2092-laugh-hliehhan.model.md` — split the Campbell clause to `§407`
- `Germanic/docs/lexeme_reports/model_entries/2162-rust-rust.model.md` — tightened Campbell to `§115`
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md` — removed unsupported Bosworth-Toller citation
- `Germanic/docs/lexeme_reports/model_entries/2189-sieve-sife.model.md` — removed wrong Kroonen citation
- matching support files for `2087-knob-cnobba`, `2090-lap-lappa`, `2092-laugh-hliehhan`, `2162-rust-rust`, and `2189-sieve-sife` — added full-exhaustion review notes
- `Germanic/docs/assembly/citation_locator_remaining_master.tsv` — removed seven no-longer-broad rows and reclassified the inspected broad tranche
- `Germanic/docs/assembly/citation_locator_primary_source_evidence.tsv` — added five new Campbell evidence rows
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md` — regenerated
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.tex` — regenerated
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.pdf` — regenerated
- `Germanic/docs/assembly/citation_locator_full_exhaustion_01_inventory.tsv` — created
- `Germanic/docs/assembly/citation_locator_full_exhaustion_01_report.md` — created

## Remaining issues

- **Kroonen2013 / Orel2003 page-candidate rows** — need a dedicated follow-up application pass that actually inserts the now-verified pages into the live prose.
- **grave / grafan** and **fire / fȳre** — need targeted sentence rewrites before another handbook-localization attempt.
- **uninspected remainder of the 161-row queue** — still needs the same row-by-row treatment used here.

Recommended follow-up types:

- **table-layout work:** no action needed from this citation pass.
- **source preparation:** no action needed for the inspected tranche.
- **human review:** only the pre-existing meed / knob policy questions.
- **prose revision:** needed for `grave` and `fire` before further handbook localization.
- **no action:** rows reclassified as honest broad general background unless later prose splitting makes a tighter locator worthwhile.

## Recommendation

**A. Do another full-exhaustion pass.** The first 75-row tranche materially reduced the live broad count and converted stale “not found/quarantined” labels into explicit source-verified outcomes, but it also surfaced a substantial second-wave queue of Kroonen/Orel page candidates that should be applied in a focused follow-up pass.
