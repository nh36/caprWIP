---
row_id: 2311
concept: "bore (iptv.2sg)"
counterpart: bora
proto: "*burōną"
protoform: "*búrô"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2311-bore-(iptv.2sg)-bora.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current_row_trace_with_shared_class_ii_background_and_superseded_bore_probe
needs_literature_agent: no
---

# DEV_NOTES material — 2311 bore (iptv.2sg) / bora

## Current row state

- The live OE row is `2311 | bore (iptv.2sg) | bora | PROTO *burōną | PROTOFORM *búrô | DERIVATION_CLASS late_analogy`, with the row note `Class II weak iptv. 2sg test. Trimoric *ō → OE -a.` [Germanic/data/germanic-aligned-final.tsv:1472-1472].
- This row is a **paradigm-cell companion**, not the lemma row. The lemma-level OE row remains `1956 | bore | borian | PROTO = PROTOFORM *búrōjaną | regular`, while the paired finite-cell companion `2312` keeps the same lexeme-level `PROTO *burōną` but uses `PROTOFORM *búrōθi` and target `boraþ` [Germanic/data/germanic-aligned-final.tsv:94-96; Germanic/data/germanic-aligned-final.tsv:1472-1473].
- The `PROTO` / `PROTOFORM` / OE target distinction is therefore essential here: `*burōną` is the project’s lexeme-level bore-family label for this non-lemma test row; `*búrô` is the selected imperative-cell input; `bora` is the OE counterpart for that selected cell, not a replacement lemma for `borian` [Germanic/data/germanic-aligned-final.tsv:1472-1472; Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:13-18,39-47].
- Current implementation evidence is positive and cell-specific: the published derivation snapshot gives `PROTO: *búrô`, `EXPECTED: bora`, `OUTPUTS: bora`, with the explicit path `NWGmc U Lowering: *bórô` followed by `OE Unstressed Long Vowel Shortening: *bóra`, `Outcome: bora` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7070-7089].
- Coverage infrastructure still treats this as an uncovered row needing slice/report material: `coverage_audit.md` lists row `2311` as `late_analogy` with `NOTE`, `report_manifest.tsv` still has no entry for it, and `oe_known_problems.tsv` has no row-local problem entry [Germanic/docs/lexeme_reports/coverage_audit.md:178-180; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- Repo-local evidence for `bora` is project-internal rather than dictionary-style. The research memo explicitly warns that it found “no separate lexical-table or dossier evidence directly attesting `bora` as a cited manuscript form,” so the row should be described as a project-selected imperative cell, not as a newly documented lemma or independently attested headword [Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:49-58].

## Development-note summary

Row `2311` has enough DEV_NOTES-related material to justify a replacement slice, but the support is **layered** and should not be oversold as a standalone `bora` dossier. The current row is best understood as a **selected regular paradigm cell** created to expose the non-`j` class-II pathway that the ordinary infinitive row cannot show directly. DEV_NOTES says of class-II weak verbs that the infinitive `*-ōja-` is a morphological innovation, while the “REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original `*-ō-` stem vowel … These are candidates for TSV encoding” [Germanic/docs/DEV_NOTES.md:2766-2778]. That rationale is **shared class-level / cell-level** support, not bore-specific evidence.

The most direct row-relevant DEV_NOTES material for `2311` is actually **superseded diagnostic history**. In the February class-II exploration results table, DEV_NOTES records `| burô | bura | bora | ✗ u-lowering |`, and the follow-up note says: “**Affected:** `*burô → bura (expected bora)` … **Issue:** `NWGmcULowering` should lower `*u → *o` before non-high vowels in a following syllable” [Germanic/docs/DEV_NOTES.md:2950-2956; Germanic/docs/DEV_NOTES.md:2967-2971]. That is genuinely about this imperative probe, but it is no longer the live analysis: the current published trace now gives `bora` directly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7070-7089].

The row also inherits **shared lexeme-level bore-family background** from the lemma row `1956 bore / borian`. Later DEV_NOTES accepts `búrōjaną → borian` as one of the class-III→II refashioned verbs whose OE-facing class-II shape can be used as a transponent and then derived “by regular sound change from this shape” [Germanic/docs/DEV_NOTES.md:37888-37898]. The existing `1956-bore-borian` slice already treats that as the controlling family-level background for the bore lexeme, while warning that older `*-ōja- > -ian` mismatch discussion and paradigm-cell workarounds belong to project history rather than a current `borian` problem state [Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md:32-38,74-88].

The safest replacement reading is therefore:

- **cell-level current evidence:** live TSV plus current derivation trace for `*búrô → bora` [Germanic/data/germanic-aligned-final.tsv:1472-1472; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7070-7089];
- **shared class-level current rationale:** class-II imperative / finite non-`j` cells are the regular probe forms, unlike the analogical infinitive [Germanic/docs/DEV_NOTES.md:2761-2778; Germanic/docs/DEV_NOTES.md:2905-2912];
- **bore-specific DEV_NOTES history:** the row once exposed a `u`-lowering failure (`bura`), now superseded [Germanic/docs/DEV_NOTES.md:2950-2971];
- **shared lexeme-level family background:** lemma `borian` remains the family citation row; `bora` inherits that background but does not replace it [Germanic/data/germanic-aligned-final.tsv:94-96,1472-1473; Germanic/docs/DEV_NOTES.md:37888-37898].

## Relevant DEV_NOTES fragments

### DEV_NOTES: class-II infinitives are morphological, non-`j` cells are the regular probes

- Source heading: `Implications for Class II Weak Verbs`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2759-2778`
- Fragment type: `current_shared_cell_rationale`
- Status: `current`
- Issue tags: `class_ii_weak_verbs`; `iptv_2sg`; `regular_probe_cell`; `not_bore_specific`
- Recommended next use: `cite when explaining why row 2311 exists at all`
- Shared-with rows if relevant: `2309`, `2310`, `2312`, `2313`, `2314`, `2315`, `2316`, `2317`, `2318`

This is the main current rationale for using a paradigm-cell row like `2311`. DEV_NOTES first states the class-wide problem: “The infinitive suffix `*-ōja-` is a **MORPHOLOGICAL** innovation … OE `-ian` does not derive by regular phonology from `*-ōjanan`” [Germanic/docs/DEV_NOTES.md:2766-2769]. It then gives the key positive claim for rows like `2311`: “The **REGULAR forms** (iptv. 2sg, 2sg, 3sg) preserve the original `*-ō-` stem vowel without the `*-ōja-` extension. These are candidates for TSV encoding” [Germanic/docs/DEV_NOTES.md:2777-2778].

For `2311`, this fragment is **shared cell-level methodology**, not direct `bora` attestation. It explains why an imperative-cell row is legitimate project evidence even though the bore-family lemma remains `borian` [Germanic/data/germanic-aligned-final.tsv:94-96,1472-1473].

> “The infinitive suffix `*-ōja-` is a **MORPHOLOGICAL** innovation … OE `-ian` does not derive by regular phonology from `*-ōjanan`.” [Germanic/docs/DEV_NOTES.md:2766-2769]

> “The **REGULAR forms** (iptv. 2sg, 2sg, 3sg) preserve the original `*-ō-` stem vowel without the `*-ōja-` extension. These are candidates for TSV encoding.” [Germanic/docs/DEV_NOTES.md:2777-2778]

### DEV_NOTES: the imperative 2sg probe was explicitly chosen as the clean test cell

- Source heading: `### Test forms: imperative 2sg and 3sg present indicative`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2905-2912`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `iptv_2sg`; `trimoric_o`; `class_ii_probe`; `shared_not_bore_specific`
- Recommended next use: `cite as direct support for the row’s chosen cell`
- Shared-with rows if relevant: `2309`, `2311`

DEV_NOTES explicitly chooses the imperative 2sg as a regular class-II test form: “**Imperative 2sg** (`*-ō`, trimoric): PGmc `*makō` → OE `maca`” [Germanic/docs/DEV_NOTES.md:2907-2912]. The example uses `make`, not `bore`, so the evidence is **shared** rather than row-local; but it exactly matches the modelling logic of row `2311`, where `PROTOFORM *búrô` likewise strips away the analogical infinitive suffix and tests the trimoric `*-ō` cell [Germanic/data/germanic-aligned-final.tsv:1472-1472].

This is stronger than a vague family resemblance: the row note itself repeats the same implementation claim, “Trimoric `*ō → OE -a`,” and the current trace confirms that the same pathway now works for `bore` [Germanic/data/germanic-aligned-final.tsv:1472-1472; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7077-7089].

> “**Imperative 2sg** (`*-ō`, trimoric): PGmc `*makō` → OE `maca`” [Germanic/docs/DEV_NOTES.md:2909-2912]

### DEV_NOTES: `burô → bura` was the row-specific diagnostic failure

- Source heading: `#### 4. Results summary` and `#### A. u-lowering (u → o before back vowel)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2948-2971`
- Fragment type: `bore_specific_diagnostic_history`
- Status: `superseded_as_live_state`
- Issue tags: `bore_probe`; `u_lowering`; `diagnostic`; `superseded_output`
- Recommended next use: `preserve only as project history`
- Shared-with rows if relevant: `2312` indirectly by family/root, but the exact `burô` line is row-2311-specific

This is the only clearly **bore-specific** DEV_NOTES fragment for the imperative cell, and it is diagnostic rather than current. DEV_NOTES records the failed row directly in the results table: `| burô | bura | bora | ✗ u-lowering |` [Germanic/docs/DEV_NOTES.md:2950-2955]. It then names the issue again in prose: “**Affected:** `*burô → bura (expected bora)` … `NWGmcULowering` should lower `*u → *o` before non-high vowels in a following syllable” [Germanic/docs/DEV_NOTES.md:2967-2971].

For this slice, the right use is conservative. The fragment proves that row `2311` was once a real debugging probe and that the key obstacle was root-vowel lowering, not uncertainty about the imperative ending. But the row file should not present `bura` as a live alternative: the current published trace, packet, and memo all treat `bora` as the present outcome [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7070-7089; Germanic/docs/lexeme_reports/packets/2311-bore-(iptv.2sg)-bora.md:17-41; Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:45-47].

> “| burô | bura | bora | ✗ u-lowering |” [Germanic/docs/DEV_NOTES.md:2954-2954]

> “**Affected:** `*burô → bura (expected bora)` …” [Germanic/docs/DEV_NOTES.md:2967-2969]

### DEV_NOTES: shared bore-family background remains on the lemma row `borian`

- Source heading: `§17.32.7 The choice: very-early vs very-late analogy`
- Source line hint: `Germanic/docs/DEV_NOTES.md:37888-37898`
- Fragment type: `current_shared_lexeme_background`
- Status: `current`
- Issue tags: `borian`; `transponent_policy`; `family_alignment`; `not_imperative_specific`
- Recommended next use: `cite to keep row 2311 aligned with row 1956`
- Shared-with rows if relevant: `1956`, `2312`

Later DEV_NOTES does not return to `bora` specifically; instead it normalizes the **lemma-level** bore-family treatment. The transponent-policy note says that class-II shapes like `búrōjaną → borian` are acceptable OE-facing inputs that the FST derives “by regular sound change from this shape” [Germanic/docs/DEV_NOTES.md:37888-37898]. For row `2311`, this matters because it keeps the lexeme family anchored at `borian`, while the imperative row remains only a selected companion cell.

This is therefore **lexeme-level inherited support**, not cell-level proof for `bora`. It helps explain why `PROTO *burōną` in row `2311` sits beside lemma row `1956 bore / borian` rather than replacing it [Germanic/data/germanic-aligned-final.tsv:94-96,1472-1473; Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md:36-38,74-88].

> “The FST then produces `sparian` by regular sound change from this shape, exactly as it does for the other class-III→II refashioned verbs already in the TSV (`búrōjaną → borian`, `líznōjaną → liornian`, `xándlōjaną → handlian`, `súndrōjaną → sundrian`, etc.).” [Germanic/docs/DEV_NOTES.md:37894-37898]

## Superseded or diagnostic material

- The older class-II options discussion recommended imperative-cell substitution “for verbs where it works cleanly,” but that discussion was still working out global row policy and should not be read as a dedicated `bora` decision note [Germanic/docs/DEV_NOTES.md:2838-2861]. Its historical value is explaining why rows like `2311` were created, not proving independent attestation for `bora`.
- `bura` is superseded diagnostic output only. It belongs in this slice because it is the clearest row-specific DEV_NOTES history, but it should never be presented as a current OE comparator or alternate target [Germanic/docs/DEV_NOTES.md:2950-2971; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7070-7089].
- The packet is accurate but candid about the thinness of row-local DEV_NOTES authority: under “High-confidence evidence” it has `_None_` for DEV_NOTES hits, then relegates the `2954` / `2969` material to “Supporting/background evidence” [Germanic/docs/lexeme_reports/packets/2311-bore-(iptv.2sg)-bora.md:15-18,48-82]. That is a good warning against overstating the row as if DEV_NOTES contained a full bora-specific narrative block.
- The research memo’s no-attestation caution is still current and should remain explicit: absence of lexical-table or dossier hits for `bora` does not invalidate the row, but it means this slice should describe `bora` as a project-selected imperative form, not as a newly documented standalone lemma [Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:49-58,86-98].

## Open questions for later work

- Should `DERIVATION_CLASS = late_analogy` remain the best row label once the row’s own selected cell is fully regular in the current trace? The label still captures why this companion row exists inside an analogically remodelled lexeme family, but it can mislead if readers take it as a claim that `*búrô → bora` itself is still failing [Germanic/data/germanic-aligned-final.tsv:1472-1472; Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:60-65].
- If `index.tsv` is revisited later, does row `2311` deserve a full indexed DEV_NOTES entry, or is it still better treated as slice-only? Right now the strongest row-local DEV_NOTES evidence is one superseded diagnostic line plus shared class-II rationale, not a dedicated bora dossier [Germanic/docs/DEV_NOTES.md:2759-2778,2905-2912,2950-2971; Germanic/docs/lexeme_reports/packets/2311-bore-(iptv.2sg)-bora.md:48-82].
- The memo asks for a formal paradigm probe covering `*búrô`, `*búrōθi`, and the lemma/comparator forms. If that built-in probe is ever added, it should keep lexeme row `1956 bore / borian`, imperative row `2311 bora`, and 3sg row `2312 boraþ` explicitly separate so family-level and cell-level evidence do not collapse together again [Germanic/docs/lexeme_reports/research_memos/2311-bore-(iptv.2sg)-bora.md:66-84].
