# Research memo — 2311 bore (iptv.2sg) / bora

## Starting point

- **ID:** 2311
- **CONCEPT:** bore (iptv.2sg)
- **COUNTERPART:** `bora`
- **PROTO:** `*burōną`
- **PROTOFORM:** `*búrô`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Class II weak iptv. 2sg test. Trimoric *ō → OE -a.`

The live row already makes the crucial distinction in outline: `*burōną` is the lexeme-level source used for this class-II weak-verb test set, while `*búrô` is the selected paradigm-cell input and `bora` is the OE target for that specific cell.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*búrô -> bora`; and the current paired 3sg row 2312 `*búrōθi -> boraþ`, which confirms the same class-II `-a-` treatment in the non-`j` present system.
- **Useful background:** the packet’s DEV_NOTES carry-over on the earlier `burô -> bura` u-lowering bug, because it explains why this lexeme family appeared in debugging at all.
- **Stale or superseded:** the packet’s background DEV_NOTES hits at 2954/2969 are diagnostic only now, not current lexical evidence, because the live compact trace already outputs `bora`. More importantly, older DEV_NOTES sections from the class-II exploration phase still claim regular 3sg `-eþ`; those are superseded by later `§15.1–15.5`, which establish regular class-II `-aþ` for the non-`j` cells.
- **Irrelevant or misleading:** the absence of dossier, analysis, or lexical-table hits for `bora` does **not** prove direct attestation. For this row, lack of hits mainly means the packet is about a project-selected paradigm cell, not a well-documented dictionary headword.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the trimoric-`*ō` discussion (`Class II weak iptv. 2sg *salbō -> ... -> OE sealfa`), the February class-II exploration section, and the later April corrections on weak class-II `-aþ`
- `Germanic/data/germanic-aligned-final.tsv` for rows 1956 (`bore / borian`), 2311, and 2312
- `Germanic/data/old_english_wiktionary.tsv` for supplementary lemma evidence (`bore -> borian`)
- `Germanic/tools/oe_paradigm_probe.py`
- Manual current-bin probe checks via `oe_full_trace_report.apply_down`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/non_firing_rules_analysis.md` as older project history on the class-II infinitive problem
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry)

No separate full dossier, analysis memo, or pilot lexeme report exists for this row in the repo at present.

## Reconstruction and early-stage forms

Three levels need to stay separate:

1. **Cognate-set / project lexeme level:** `*burōną`, the class-II weak verb behind the OE bore-family test rows.
2. **Project input form for this row:** `*búrô`, the imperative singular cell chosen because it preserves the inherited non-`j` stem vowel and gives a regular sound-law path.
3. **OE target form:** `bora`, the expected OE reflex of that selected imperative cell.

The important project-history complication is that the broader class-II citation-form discussion also uses `*búrōjaną -> borian` for the analogical infinitive row 1956. That citation-form pathway is relevant background, but it is **not** the same thing as row 2311. Row 2311 is deliberately about the non-`j` paradigm cell, not the analogical infinitive.

For the row itself, the current trace is straightforward: `*búrô` undergoes NWGmc `u`-lowering to `*bórô`, then late unstressed long-vowel shortening gives OE `bora`. The older `bura` development cited in background DEV_NOTES is therefore superseded project history, not the current analysis.

## Old English philology

Repo-local philology supports a clear citation-form vs. inflected-form distinction:

- **Citation lemma / dictionary headword:** `borian`, supported in `old_english_wiktionary.tsv` and in row 1956.
- **Row 2311 target:** `bora`, an inflected imperative singular form, not a dictionary headword.

Within the repo, I found no separate lexical-table or dossier evidence directly attesting `bora` as a cited manuscript form. So this memo should treat `bora` as a project-selected OE paradigm form whose shape is philologically motivated by the regular class-II ending, but not as independently attested on the current repo evidence.

Likewise, there is no repo-local support for any dialect or manuscript claim about `bora` specifically. The only dialect note in the nearby material concerns 3sg `-eþ` variants, and that belongs to row 2312 rather than to this imperative row.

## Project problem and solution

The project problem is the same one seen across the class-II weak verbs: the ordinary OE citation form in `-ian` is morphologically remodeled and therefore not a clean neogrammarian test of the inherited suffixal vowel. For this lexeme family, the project solved that by creating special paradigm-cell rows for forms that keep the regular non-`j` ending.

Row 2311 is therefore not trying to replace the lemma `borian`. It is a controlled test row for the regular imperative singular cell `*búrô -> bora`. The `late_analogy` label still makes sense because the lexeme family is only being handled this way precisely because the ordinary citation paradigm is analogically remodeled; the selected row itself is the regular workaround.

## Paradigm probe

A paradigm probe **is required** here, and the packet is right that the formal project probe is still missing: `oe_paradigm_probe.py` has no built-in spec for row 2311.

Manual current-bin checks are already useful:

- `*búrô -> bora`
- `*búrōθi -> boraþ`
- `*búrōsi -> +?`
- `*búrōną -> boren`
- `*búrōjaną -> borian`

So the missing formal probe should at minimum cover these cells/comparators:

- **iptv.2sg.** `*búrô` (the live row)
- **2sg pres. indic.** `*búrōsi` (to see whether the regular `-as` cell is modelled yet)
- **3sg pres. indic.** `*búrōθi` (paired row 2312)
- **infinitive comparator** `*búrōjaną` (analogical citation-form row 1956)
- **non-`j` infinitive comparator** `*búrōną` if the project wants to keep testing the underlying class-II morphology directly

## Recommended final report

Recommend a final report that says: `bora` is not the lemma of OE “bore,” but a project-selected imperative singular cell from the class-II weak verb, chosen because it gives the regular non-`j` outcome `*búrô -> bora`; the report should contrast this with the citation lemma `borian` and treat older `bura` / `boreþ` project history as superseded diagnostics only.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** minor cleanup recommended. The current note is basically right, but it should say more explicitly that this is a selected regular class-II imperative cell used in place of the analogical citation-form pathway; adding the same source-style support used in row 2309 would also help.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** `DEV_NOTES` cleanup is recommended. The older February and early-April class-II sections that still present regular 3sg `-eþ` or otherwise blur the older `-ōja-` exploration with the later non-`j` solution should be marked more explicitly as superseded by `§15.1–15.5`. No separate dossier text needs change because no row-specific dossier exists.
