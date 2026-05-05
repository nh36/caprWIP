# Research memo — 2041 give / ġiefan

## Starting point

- **ID:** 2041
- **CONCEPT:** give
- **COUNTERPART:** ġiefan
- **PROTO:** *gébaną
- **PROTOFORM:** *gébaną
- **DERIVATION_CLASS:** regular
- **NOTE:** WS palatalized initial (R/T §6.4.1 rule 1: g before front vowel)
- **HISTORY:** `TSV: giefan → ġiefan;`
- `coverage_audit.md` flags this row as memo/report-relevant because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row and the current compact derivation trace agree that the project now targets **`ġiefan`**, with a regular derivation from `*gébaną` and no live mismatch.
- The packet's substantive support from `ws_vs_anglian_dialect_differences.md` is current and directly relevant: Campbell and Ringe/Taylor support WS `giefan/ġiefan` versus non-WS forms without WS palatal diphthongization [@Campbell1959; @RingeTaylor2014].

**Useful background:**
- `old_english_wiktionary.tsv` gives plain `giefan`; that is useful as a quick lexicographic checkpoint, though not as authority for dialect, normalization, or chronology.
- `DEV_NOTES.md` 6496-6504 and 11313-11316 are useful background because they explicitly contrast `*gebaną > giefan` with `*geftiz > gift`, showing that `giefan` keeps `e` long enough for WS palatal diphthongization while `gift` does not.

**Stale or superseded:**
- Older debug snapshots are now stale project history. In February traces the expected form was still plain `giefan`, and an older mismatch report even had `*gebăną -> ġeban (expected giefan)`; those predate the TSV history change to dotted `ġiefan` and the current successful derivation.

**Irrelevant or misleading if taken too literally:**
- Most of the packet's "possibly stale or diagnostic" concept-name hits are unrelated false positives (`widow`, `door`, KIT work, `lierna/leorna`, etc.) and should not be treated as lexical evidence for this row.
- The packet can also mislead if one collapses three different things into one: comparative **`*geban-`** as cognate-set background, project input **`*gébaną`**, and the OE target **WS `giefan` / project-normalized `ġiefan`**.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 6496-6504 and 11252-11357.
- `Germanic/docs/dossiers/g-palatalisation-conditioning.md`.
- `Germanic/data/oe_known_problems.tsv` (no entry for this row or lexeme).
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.

No pilot lexeme report for this item appears to exist yet.

## Reconstruction and early-stage forms

The **cognate-set proto/headword** in comparative lexicography is the verbal stem **`*geban-`** 'give' [@Kroonen2013]. The row's TSV `PROTO` and `PROTOFORM`, however, are both **`*gébaną`**, i.e. the specific infinitival input the project feeds into the derivation. That distinction should be stated in the final report even if the TSV fields stay unchanged.

For the OE derivation itself, the important chronology is regular:

- project input `*gébaną`;
- initial palatalization of `g` before front `e` [@RingeTaylor2014];
- WS palatal diphthongization of that `e` after the new palatal, yielding `ie` [@Campbell1959; @RingeTaylor2014; @Fulk2018];
- later weak-verb/infinitive reductions to OE `giefan`.

So the row is **not** a case of i-umlaut. The `ie` of WS `giefan` belongs to WS palatal diphthongization, whereas non-WS comparanda such as Merc. `for-geofan` and North. `geafa` reflect different later dialect histories, not a different cognate set [@RingeTaylor2014].

## Old English philology

The philological target for this row is the **WS infinitive** usually cited as plain **`giefan`**, not a manuscript-only claim about dotted **`ġiefan`**. Campbell gives `gefan (W-S giefan)` in his list of initial palatal examples [@Campbell1959]; Ringe/Taylor list the WS principal parts `giefan, geaf, géafon, giefen` and contrast them with Northumbrian `geafa` and Mercian `for-geofan` [@RingeTaylor2014]. Clark Hall likewise indexes the lexeme under plain `giefan`, with past forms such as `geaf` and `gafon/geafon` [@ClarkHall1960].

Accordingly:

- **attested/canonical handbook headword:** plain `giefan`;
- **project-normalized target:** `ġiefan`, with dotted `ġ-` making palatalization explicit;
- **citation form represented by the row:** the WS infinitive;
- **other paradigm cells:** present singular forms such as `gifst, gifþ` and preterites such as `geaf, géafon` are real OE evidence [@RingeTaylor2014], but they are not competing citation-form targets for this row.

The main philological caution is therefore representational: the memo should not let the project's dotted spelling look like a direct claim that manuscripts or dictionaries standardly headword the verb as `ġiefan`.

## Project problem and solution

The live project problem is no longer a derivational failure. The FST now reaches the row target, and the row rightly remains **regular**.

The real issue is explanatory precision:

1. the row represents the **WS** citation form, not OE in all dialects;
2. the dotted **`ġ-`** is a **project normalization**, not the ordinary lexicographic headword spelling;
3. the note should not imply that initial palatalization alone explains the whole form, because the crucial vowel shape `ie` depends on **WS palatal diphthongization** after that palatalization.

So the current project solution should be: keep the regular row and current target, but explain the normalization and the WS-specific vowel history clearly.

## Paradigm probe

No paradigm probe is required.

Reason: this row is not choosing among competing paradigm cells to justify the citation form. The issue is the interpretation of a regular WS infinitive plus project normalization, not a late-analogy or cell-selection problem. If a richer final report ever wanted a small paradigm table, the most informative cells would be infinitive `giefan`, 2/3 sg. present `gifst/gifþ`, pret. sg. `geaf`, pret. pl. `géafon`, and pp. `giefen`; but that is optional background, not a required probe for this memo.

## Recommended final report

Recommend a **short** final lexeme report that:

- distinguishes comparative `*geban-`, project input `*gébaną`, and OE target WS `giefan` / project `ġiefan`;
- explains that the row is regular and that `ie` comes from **WS palatal diphthongization after initial palatalization**, not from i-umlaut;
- notes the dialect contrast with Merc. `for-geofan` and North. `geafa`;
- states that dotted `ġ-` is the project's normalized spelling, while handbook/dictionary headwords usually give plain `giefan`;
- omits a paradigm-probe subsection.

## Data-change recommendations

- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change. `ġiefan` is defensible as the project's normalized target, provided the report explains that source headwords normally use plain `giefan`.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** **change recommended.** The current note is too narrow. It should mention that the row is the **WS** form, that dotted `ġ-` is a project normalization of source `giefan`, and that `ie` reflects **WS palatal diphthongization** after initial palatalization rather than merely "g before front vowel."
- **`oe_known_problems.tsv`:** no change.
- **`DEV_NOTES` text:** no change required.
- **dossier text:** no change required.
