---
row_id: 2088
concept: lade
counterpart: hladan
proto: *laθōjaną
protoform: *xláðaną
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2088 lade / hladan

## Current row state

- CONCEPT: `lade`
- COUNTERPART: `hladan`
- PROTO: `*laθōjaną`
- PROTOFORM: `*xláðaną`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: `Wiktionary: PGmc *hlaðaną (Verner) > OE hladan | Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1` [Germanic/data/germanic-aligned-final.tsv:613].
- Packet status: the live compact derivation is already successful and explicit about the OE-facing input. The packet starts from `PROTO: *xláðaną`, derives `*xlædaną` by Anglo-Frisian brightening, restores `a` in `*xladaną`, and surfaces exact `OUTPUTS: hladan`; it also records `_None_` for matching `oe_known_problems.tsv` entries [Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md:17-47].
- `oe_known_problems.tsv`: no row-specific entry survives for `2088`, `*laθōjaną`, `*xláðaną`, or `hladan`; the packet’s `_None_` line and the memo’s data-change recommendation both treat the row as currently solved rather than as an unmanaged exception [Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md:45-47; Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:95-101].
- Memo status: the row derives correctly, but the memo says the real documentation task is to preserve the split between cognate-set `PROTO = *laθōjaną` and OE-facing `PROTOFORM = *xláðaną`, i.e. conventional `*hlaðaną`. The OE row is intentionally not being derived directly from the weak cognate-set headword; it models the strong Verner-grade stem behind attested OE `hladan`, which is why `DERIVATION_CLASS = early_analogy` still fits [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:13-14,58-65,76-81,95-99].
- Current DEV_NOTES authority **does exist**, but only in a narrow March 2026 repair note. The usable row-specific authority is the `*xlaθaną` → `hladan` analysis that explains why OE `d` requires Verner-grade `*ð` and therefore a corrected OE-facing protoform; there is no later standalone lexeme dossier beyond that repair cluster, and older stray `hlaþan` verification lines are stale project history rather than live authority [Germanic/docs/DEV_NOTES.md:3151-3151,10225-10286; Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:17-28,76-81,99-101].

## Development-note summary

This row has to be written as a three-level case, not as a simple one-line inheritance chain. `PROTO = *laθōjaną` is the comparative/cognate-set headword shared by English `lade` and continental `laden`; `PROTOFORM = *xláðaną` is the OE-directed project input, effectively conventional `*hlaðaną`, with initial `h-`, Verner-grade `*ð`, and infinitival `-aną`; the OE target is the attested citation infinitive `hladan` [Germanic/data/germanic-aligned-final.tsv:611-614; Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:58-65]. The memo is explicit that the OE row is not being derived straight from the weak cognate-set proto. It is being documented as an early analogical/pre-selection choice in which the English row uses the strong verb stem as its OE-facing input while the wider cognate set keeps the weak headword for cross-language bookkeeping [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:64-65,76-81,95-99].

The row-specific DEV_NOTES authority is real but very narrow. The key March 2026 note begins from the stale metadata `PROTOFORM: *xlaθaną` and `NOTE: "Wiktionary: PGmc *hlaθaną > OE hladan"`, then states the actual philological problem plainly: “If PGmc had voiceless `*θ`, OE would have `þ`,” whereas “The OE form `hladan` with `d` shows Verner's Law applied” [Germanic/docs/DEV_NOTES.md:10227-10237]. The same note then gives the controlling repair: “**Fix:** Change protoform to `*xlaðaną` (with Verner's `*ð` → OE `d`)” and records that `hladan` now matches [Germanic/docs/DEV_NOTES.md:10239-10241]. That is the part of DEV_NOTES that still governs the row. What should not be carried forward as current metadata is the pre-fix spelling in the setup lines; the memo explicitly classifies those old `*xlaθaną` / `*hlaθaną` mentions as historical diagnostics only [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:25-29,76-79,99-101].

The strongest still-usable philological detail inside DEV_NOTES is the preserved paradigm statement from Kroonen: OE `hladan` is a class-VI strong verb with `hlōd`, `hlōdon`, and `hladen`, so the voiced dental is not an anomaly but the expected Verner-grade outcome for this strong verb family [Germanic/docs/DEV_NOTES.md:10235-10237]. The memo reaches the same conclusion from the wider repo bibliography: Ringe-Taylor, Kroonen, Bright, Clark Hall, and Bosworth-Toller all support attested OE `hladan` as an ordinary strong-verb infinitive meaning ‘load; draw water’, while comparator present cells such as `hlætst` / `hlet` are only paradigm background and do not justify changing the row target away from the infinitive [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:49-53,66-72,83-87].

The A-restoration point is secondary but still needs to remain explicit because it explains why the live row keeps full-vowel `-aną` in `PROTOFORM`. The packet’s current trace shows `*xláðaną` > `*xlædaną` > `*xladaną` > `hladan`, and the TSV note says directly that the full-vowel infinitival tail is there “for A-restoration” [Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md:17-43; Germanic/data/germanic-aligned-final.tsv:613]. DEV_NOTES’ broader A-restoration fix later confirms that infinitives were one of the weak-tail patterns deliberately added to the restoration environment: “A-restoration should still apply (infinitives, agent nouns, etc.)” [Germanic/docs/DEV_NOTES.md:1702-1704]. This is background on why the live derivation succeeds; it is not a separate argument for the lexeme split between `*laθōjaną` and `*xláðaną`.

The checked superseded history also has to stay visible so later writeups do not accidentally reactivate stale forms. DEV_NOTES earlier claimed that “All A-restoration-dependent forms [were] verified” including `hlaþan`, and the March 2026 progress log compressed the row to “Verner TSV fixes: lade, needle” [Germanic/docs/DEV_NOTES.md:3151-3151,10389-10391]. Both lines are useful only as workflow history. The first preserves an obsolete pre-Verner target spelling, and the second records repository change tracking rather than lexical authority. Later work should therefore cite the repair note and the live row metadata, not the stale `hlaþan` checkpoint and not the progress table [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:25-29,76-81,99-101].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10225-10241

- Source heading: `Analysis: *xlaθaną → hladan`
- Source line or section hint: `lines 10225-10241`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `verners_law`; `protoform_correction`; `strong_verb`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-specific DEV_NOTES fragment. Its setup lines preserve the stale pre-fix state—`PROTOFORM: *xlaθaną`, `COUNTERPART: hladan`, and note wording with `*hlaθaną`—but the actual argument remains current: “If PGmc had voiceless `*θ`, OE would have `þ`,” while “The OE form `hladan` with `d` shows Verner's Law applied” [Germanic/docs/DEV_NOTES.md:10227-10237]. The same note then gives the row-level repair in the exact form later documentation should inherit: “**Fix:** Change protoform to `*xlaðaną` (with Verner's `*ð` → OE `d`)” [Germanic/docs/DEV_NOTES.md:10239-10239]. The Kroonen summary embedded here—`hladan`, `hlōd`, `hlōdon`, `hladen`—is also still worth preserving because it ties the consonant correction to the ordinary class-VI strong-verb paradigm rather than to an ad hoc transducer workaround [Germanic/docs/DEV_NOTES.md:10235-10237].

### DEV_NOTES:line-10265-10286

- Source heading: `Pattern`
- Source line or section hint: `lines 10265-10286`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `verners_law`; `protoform_convention`; `shared_methodology`; `pgmc_stage`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2136`

This shared convention fragment matters because it states the project rule that row 2088 now exemplifies. DEV_NOTES says: “Our TSV convention should be: **use the post-Verner form in PROTOFORM** when the OE reflex shows Verner's Law applied,” and then explains why the repo writes `*ð`, not `*d`: `*ð` is the PGmc Verner outcome, with hardening to `d` happening later in PWGmc [Germanic/docs/DEV_NOTES.md:10267-10276]. The result table is explicit that the corrected input now gives the expected OE form: `*xlaðaną` → `hladan` ✓ [Germanic/docs/DEV_NOTES.md:10283-10284]. For row 2088 this fragment is not the place where the lexeme split itself is decided—that comes from the row-specific fix plus the memo—but it is the clearest shared statement of the protoform-writing convention that makes `*xláðaną` defensible for the OE row.

### DEV_NOTES:line-21738-21750

- Source heading: `A. Empirical probes (stems with root *á, Class VI strong verb infinitives)`
- Source line or section hint: `lines 21738-21750`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `a_restoration`; `class_vi_infinitives`; `protoform_encoding`; `shared_row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2046, 2266, 2268, 2272`

This shared fragment is the best compact current authority for the row’s `-aną` encoding. DEV_NOTES probes class-VI infinitives directly, shows that breve-marked `*bákăną` wrongly yields `bæcan` while plain-suffix `*bákaną` gives correct `bacan`, and then states the row-policy consequence in general form: “The current TSV has `*bákaną` with plain `a` for exactly this reason — the 10 Class VI strong verbs (`bákaną, grábaną, xláðaną, wádaną, wákaną, wáskaną, …`) rely on the plain `a` in the infinitival suffix to trigger OEARestoration” [Germanic/docs/DEV_NOTES.md:21742-21747]. Row 2088 is named inside that list, so this fragment should be kept as current shared policy support for why the OE-facing input is written with full-vowel `-aną` rather than a reduced or breve-marked tail.

## Superseded or diagnostic material

### DEV_NOTES:line-3151

- Source heading: `Water fix: PWGmc ō-shortening and A-restoration correction`
- Source line or section hint: `line 3151`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `stale_verification`; `pre_verner_form`; `a_restoration_history`; `search_residue`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This line should be preserved only so later searches do not mistake it for current authority. DEV_NOTES claimed that “All A-restoration-dependent forms [were] verified” and included `hlaþan` among the supposedly correct outputs [Germanic/docs/DEV_NOTES.md:3151-3151]. After the March Verner fix, that spelling is stale: the memo explicitly says older packet excerpts and notes quoting `*xlaθaną` or `hlaþan` are historical diagnostics only, because the live row now depends on voiced `*ð` and exact `hladan` [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:25-29,76-79,99-101]. This fragment therefore belongs only in the checked superseded history.

### DEV_NOTES:line-10391

- Source heading: `Mismatch Progress Log (2026-03-14)`
- Source line or section hint: `line 10391`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `progress_log`; `project_history`; `verner_fix`; `repository_chronology`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2136`

This progress-log entry is useful only as repository chronology. It compresses the change to “Verner TSV fixes: lade, needle” and records the mismatch drop from 72 to 70 [Germanic/docs/DEV_NOTES.md:10389-10391]. That line says nothing about why `hladan` needs a strong Verner-grade protoform, nothing about the PROTO/PROTOFORM split, and nothing about the OE infinitive’s A-restoration environment. It should therefore be cited only when reconstructing project workflow, never as row-level philological authority.

### Packet/DEV_NOTES search residue: stale `*xlaθaną` / `*hlaθaną` wording

- Source heading: `Packet-preserved pre-fix note wording`
- Source line or section hint: `packet lines 49-61; memo lines 25-29 and 99-101`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `packet_search_residue`; `old_protoform`; `source_hygiene`; `historical_note`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

The packet intentionally preserves the old DEV_NOTES hit that still opens with `PROTOFORM: *xlaθaną` and note text `PGmc *hlaθaną > OE hladan` [Germanic/docs/lexeme_reports/packets/2088-lade-hladan.md:49-61]. The memo is explicit that these are “historical diagnostics only” and must not be reused as current evidence once the row was corrected to a Verner-grade input [Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:25-29,99-101]. This residue is worth retaining only so later source audits can say the stale wording was checked and intentionally downgraded.

## Open questions for later work

- If the live TSV note is ever rewritten, make the main distinction explicit before the A-restoration detail: row 2088 keeps cognate-set `PROTO = *laθōjaną`, but the OE row uses strong Verner-grade `PROTOFORM = *xláðaną` / conventional `*hlaðaną`; the full-vowel `-aną` explanation should remain, but as support for the OE-facing input rather than as the whole note [Germanic/data/germanic-aligned-final.tsv:613; Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:58-65,95-99].
- If `dev_notes_slices/index.tsv` is updated later, record row 2088 as having one narrow current row-specific DEV_NOTES repair fragment (`10225-10241`), two current shared support fragments (`10265-10286` for Verner-aware protoform policy and `21738-21750` for class-VI `-aną` encoding), and only diagnostic/superseded history thereafter (`3151`, `10391`) [Germanic/docs/DEV_NOTES.md:3151-3151,10225-10286,10389-10391,21738-21750].
- If a later final lexeme report wants paradigm detail, keep the class-VI strong-verb mini-paradigm explicit—`hladan`, `hlōd`, `hlōdon`, `hladen`—and treat present-cell comparators such as `hlætst` / `hlet` as background philology only, not as reasons to retarget the row away from the infinitive [Germanic/docs/DEV_NOTES.md:10235-10237; Germanic/docs/lexeme_reports/research_memos/2088-lade-hladan.md:49-53,66-72,83-87].
