# Research memo — 2155 coat / rocc

## Starting point

- **ID / concept / counterpart:** 2155, **coat**, **rocc**.
- **TSV `PROTO`:** `*rúkkaz`.
- **TSV `PROTOFORM`:** `*rúkkaz`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** garment-word row: OE `rocc` 'tunic' etc., from PGmc `*rukkăz` as an a-stem; history says the earlier entry had conflated stone and garment etymologies.
- There is **no pilot lexeme report** for this row; coverage audit still lists it as needing report coverage because of `NOTE`.

The live row is therefore a note-bearing regular row whose main issue is not sound-law failure but lexical identification: which `rocc` is meant, and how the project's modelling form relates to the comparative etymological literature.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact derivation trace (`*rúkkaz -> rocc`); the current debug snapshots showing `EXPECTED: rocc`, `OUTPUTS: rocc`; and the row-specific `DEV_NOTES.md` section at 3001-3045 explaining that the project corrected an older conflation of three different etymologies.
- **Useful background:** the packet's coverage-style reminders that there is no `oe_known_problems.tsv` entry; the coverage audit showing why the row still needs a lexeme report; and the packet's quotations from `DEV_NOTES` identifying the garment lexeme as the intended one.
- **Stale or superseded:** the old project state where cognate set 379 was glossed as **rock** and paired with `*rukkiz`, German **Ruck**, Dutch **ruk**, and the stone sense. That history is useful only as diagnosis of the old mistake, not as present lexical evidence.
- **Irrelevant or misleading if taken at face value:** the packet's `old_english_wiktionary.tsv` hit (`rock -> rocc`, attested only in `stānrocc`) points to the **stone** lexeme, not the garment word now represented by row 2155. Also misleading is the packet's reuse of `DEV_NOTES` language attributing **Kroonen `*hrukkaz`** to this garment word; the repo-local Kroonen entry checked separately actually gives `*hrukka-`, not `*hrukkaz`, and adds a continental-loan caution for OE `roc`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 3001-3045.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md` and `...publish.md` — both show live `EXPECTED: rocc`, `OUTPUTS: rocc`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — row 2155 is still uncovered because of `NOTE`.
- `Germanic/data/oe_known_problems.tsv` — no entry for this lexeme.
- `Germanic/data/old_english_wiktionary.tsv` — only the stone-oriented `rock -> rocc` / `stānrocc` hit.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` and `...legacy/...txt` — `*rukkaz sb.m.` with OE `rocc` 'upper garment'.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `...legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — `*hrukka-` 'upper garment, robe', with initial `h` explicitly defended and OE `roc` possibly treated as a continental loanword.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `rocc m.` 'over-garment, rochet', plus compound `bisceoprocc`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — compound evidence such as `breóst-rocc` and `diácon-rocc`.

No full lexeme-specific dossier or analysis file was named in the packet or TSV note, and no prior pilot/full report for this lexeme was found.

## Reconstruction and early-stage forms

This row needs an explicit three-way distinction.

1. **Cognate-set proto / etymological headword:** the comparative sources checked in-repo do **not** speak with one voice. Orel gives a straightforward masculine a-stem `*rukkaz`, while Kroonen gives `*hrukka-` with initial `h`, argues that reconstruction without `h` is erroneous, and even notes that OE `roc` may be a continental loanword.
2. **Project input form:** TSV `PROTOFORM = *rúkkaz`, the form the current FST actually runs. The live trace shows the project using this as a regular input yielding `rocc` through NWGmc u-lowering and later OE orthography.
3. **OE target form represented by the row:** the garment noun `rocc`, not the separate stone word inferred from `stānrocc`.

So the current TSV is best read as a **project modelling choice**, not as a complete statement that all comparative philology agrees on a single PGmc shape. The future lexeme report should preserve that distinction instead of presenting `*rúkkaz` as unproblematic consensus.

## Old English philology

- **Attested vs. reconstructed:** the garment word is treated in repo-local dictionary material as an attested OE lexeme. Clark Hall has `rocc m.`, and Bosworth-Toller preserves garment compounds such as `breóst-rocc` and `diácon-rocc`. By contrast, the stone sense is only represented in the packet's background material through `stānrocc`, exactly as `DEV_NOTES` says.
- **Citation form vs. inflected/compound evidence:** the row target is a citation form for the garment noun, while most of the packet's explicit attestational reminders are compounds. That is enough to distinguish the garment lexeme from the stone compound evidence, but the final report should avoid overstating manuscript detail that was not checked here.
- **Headword/spelling issue:** repo-local sources split between normalized **OE `roc`** (Kroonen) and **OE `rocc`** (Orel, Clark Hall, current TSV). This looks like a headword/spelling normalization issue, not a reason to collapse the garment lexeme back into the stone entry.
- **Dialect/manuscript status:** no additional dossier here justifies a stronger dialect or manuscript claim. The safe philological statement is simply that the project row targets the attested garment lexeme and excludes the separate stone word.

## Project problem and solution

The project problem was a three-way conflation:

1. OE `rocc` 'garment/tunic';
2. a separate stone/rock word represented only in `stānrocc`;
3. German `Ruck` / Dutch `ruk` 'jerk, pull', from a different root.

The implemented solution in the live row is basically right: concept **coat**, OE target **rocc**, and a derivation that now produces the intended garment form. The remaining issue is not the FST output but the explanatory layer around it. The project should say clearly that row 2155 represents the garment noun only, while also acknowledging that the comparative proto citation is less settled than the current note implies.

## Paradigm probe

**No paradigm probe is required for this row.**

This is not a late-analogy or hidden-cell problem. The live issue is lexical separation (garment vs. stone vs. unrelated `Ruck`) plus proto/headword framing, and the current derivational path already lands on the intended OE target `rocc`.

If the supervisor later wants extra morphology checked, that would be a dictionary/paradigm documentation exercise for the noun, not a required probe for resolving the current row.

## Recommended final report

Recommend a concise final report saying that row 2155 now correctly represents the **garment** lexeme OE `rocc`, not the stone word in `stānrocc` and not the unrelated `Ruck/ruk` set; that the current project input `*rúkkaz` successfully derives the target; and that the report should briefly flag the comparative-source split between Orel's `*rukkaz` and Kroonen's `*hrukka-`, along with normalized `roc/rocc` variation on the OE side.

## Data-change recommendations

- **TSV `PROTO`:** no immediate change recommended. The current project-wide cognate-set form is usable, but the final report should not treat it as uncontested comparative consensus.
- **TSV `PROTOFORM`:** no change recommended. `*rúkkaz` is the live derivational input and currently produces the intended OE form.
- **TSV `COUNTERPART`:** no change recommended. `rocc` is a defensible OE target and matches the live trace, even though some sources normalize `roc`.
- **TSV `DERIVATION_CLASS`:** no change recommended. This is still a `regular` row with a note, not a paradigm-cell or unmodelled case.
- **TSV `NOTE`:** **change recommended.** The current note should be tightened so it says explicitly that the row is the garment lexeme only, and so it does not present `*rukkăz` as if it exhausted the comparative evidence.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** **change recommended** in `Germanic/docs/DEV_NOTES.md` (and thus any regenerated packet drawing from it). The present wording incorrectly cites Kroonen as `*hrukkaz`; the checked repo-local Kroonen entry is `*hrukka-` and also raises the continental-loan possibility for OE `roc`. No separate dossier cleanup is required because no dedicated row dossier was found.
