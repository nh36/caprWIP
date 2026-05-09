---
row_id: 2220
concept: stone
counterpart: stān
proto: *stáinaz
protoform: *stáinaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md; Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2220 stone / stān

## Current row state

- The live OE row is `2220	stān	PROTO *stáinaz	COUNTERPART stān	DERIVATION_CLASS regular`, with `PROTO = PROTOFORM = *stáinaz` and no row-local warning note beyond the duplicated Wiktionary inheritance sourcing [Germanic/data/germanic-aligned-final.tsv:1126-1126].
- The current published OE derivation trace is a clean exact match: `PROTO: *stáinaz`, `EXPECTED: stān`, `OUTPUTS: stān`, with the compact historical path `PWGmc Ai Monophthongization: *stānaz`, `PGmc Final Z Deletion: *stāna`, `PWGmc Final Bare A Loss: *stān` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4726-4744]. The full trace shows the same thing in rule-by-rule form and confirms that nothing more exotic is happening in the OE branch [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:32136-32208].
- `oe_known_problems.tsv` currently has no entry for `*stáinaz`, `stān`, or row `2220`, so the row is not being tracked as an OE exception, wontfix item, or live mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Comparative and OE lexical references agree well with the live row, but they use ordinary handbook lemma formats rather than the project's accented row input. Kroonen gives `*staina- m. 'stone'` with `OE stān m. 'id.'`; Ringe–Taylor give both nominative-style `PGmc *stainaz 'stone' > OE stan` and an accusative/case-form illustration `*staing acc. sg. 'stone' > PWGmc *stain > OE stan`; Clark Hall has `stān m. (and n. in NG) 'stone,' rock`; Campbell uses `stains < *stainaz` as a regular final-`s(z)` example and lists `stan, stone ... stines ... stane` among the masculine a-nouns [@Kroonen2013, p. 472; @RingeTaylor2014, pp. 60, 185; @ClarkHall1960, s.v. "stān"; @Campbell1959, §§399, 570].
- No reusable packet or research-memo stem was found for this row during this pass, so the canonical row-based slice filename is the correct replacement working note.

## Detailed development-note summary

No dedicated stone dossier presently survives in `DEV_NOTES.md`. The row is nonetheless easy to stabilize because every live source agrees on the basic outcome: the OE target is ordinary `stān`, the live project comparator is ordinary `*stáinaz`, and the current OE trace already derives `stān` by regular sound change with no special repair logic [Germanic/data/germanic-aligned-final.tsv:1126-1126; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4726-4744; @Kroonen2013, p. 472; @RingeTaylor2014, p. 185; @ClarkHall1960, s.v. "stān"].

The most useful surviving **current** DEV_NOTES support is shared sound-change material about stressed `*ai`. The West Germanic monophthongisation note says the project inserted an `EnglishSandboxWestGermanic` stage so proto `{*ai}` first collapses to historical `{*ā}`, and that spot checks now expose “the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches” [Germanic/docs/DEV_NOTES.md:2259-2263]. A later verification note then states even more plainly: “No regression on stressed-*ai forms (e.g. `*stainaz` still → `stān` via `*ai → *ā`)” [Germanic/docs/DEV_NOTES.md:28123-28124]. For row `2220`, those notes are not stone-only philological dossiers, but they are still the clearest surviving current project prose supporting the live pathway `*stáinaz > *stānaz > stān`.

The main interpretive trap is that other DEV_NOTES stone examples do **not** use the live row's nominative-style `PROTO/PROTOFORM`. In the apocope chronology note, DEV_NOTES quotes Ringe–Taylor's ordering and says: “the final *a of nom.sg. *-az ... was *also* lost in the same PWGmc step, after *z-loss, leaving a bare stem,” then illustrates the point with `PGmc *stainą > PWGmc *stain > OE stān` [Germanic/docs/DEV_NOTES.md:21451-21458; @RingeTaylor2014, p. 60]. A later restatement gives the same shape as a bare apocope example: `*daga → *dag`; `*staina → *stain`; `*horna → *horn` [Germanic/docs/DEV_NOTES.md:23664-23669]. Those forms are useful because they explain why the live trace legitimately ends with `*stāna > *stān`. But they are **not** alternate live row states. For this slice, `PROTO` and `PROTOFORM` remain `*stáinaz`; the `*stainą/*staina` examples are case-form or rule-order illustrations carried over from shared phonological discussion.

That distinction matters because many plain-text `stān` or `*stānaz` hits in `DEV_NOTES.md` belong to the English sandbox rather than to the OE row. The 2025-12-07 core-vowel audit notes, for example, say `*stānaz` “still surfaces as `stānə`” and later “reaches `{təʊ/taɪ/teɪ}` options ahead of weak tails” [Germanic/docs/DEV_NOTES.md:1818-1819,1835-1835]. Those are useful only as cross-branch diagnostics about later English development toward `stone`; they should not be cited as if row `2220` itself were mismatching in the OE cascade. The live OE trace already succeeds, and the row's actual OE problem-state is therefore thin to nonexistent.

The safest replacement working conclusion is conservative. Row `2220` is a regular, stable OE row with good comparative support and a clean current trace, but its surviving DEV_NOTES evidence is mostly shared phonological background plus one general apocope chronology note rather than a stone-specific lexical audit. That is enough for a careful replacement note, but it is still a **no-index-leaning** evidentiary shape unless later packet or memo work creates a genuinely row-local discussion.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2259-2263

- Source heading: `WG monophthongisation stage`
- Source line or section hint: `lines 2259-2263`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `wg_monophthongisation`; `stressed_ai`; `regular_pathway`; `intermediate_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1954`; `2144`

This is the strongest current DEV_NOTES fragment that still bears positively on row `2220`. DEV_NOTES says the project added a West Germanic stage where proto `{*ai}` collapses to `{*ā}` before later English/OE handling, and the crucial direct wording is that spot checks now surface “the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches” [Germanic/docs/DEV_NOTES.md:2261-2263]. For `stone / stān`, that matters because it preserves the project's current understanding of the lexeme as a regular stressed-`*ai` outcome, not as an exception bucket item.

The fragment must still be used with proper scope. It is shared sound-change background, not a dedicated stone memo. Its value is that it explains why the current OE trace legitimately contains `*stānaz` as an intermediate form on the way from `*stáinaz` to `stān` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4735-4739].

### DEV_NOTES:line-28123-28124

- Source heading: `§17.12.4 Verification`
- Source line or section hint: `lines 28123-28124`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `stressed_ai`; `regular_outcome`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1954`

This short verification note is the cleanest surviving present-tense sentence that names the exact stone-type pathway. DEV_NOTES says: “No regression on stressed-*ai forms (e.g. `*stainaz` still → `stān` via `*ai → *ā`)” [Germanic/docs/DEV_NOTES.md:28123-28124]. For row `2220`, that is valuable because it matches the live row's actual comparator and target much more closely than the apocope examples using `*stainą` or `*staina`.

Even so, the fragment remains shared verification, not a full lexical argument. It should support a final report's statement that the row is presently regular, but it is not by itself enough to make the row richly indexable.

### DEV_NOTES:line-21441-21461

- Source heading: `Ringe–Taylor chronology for final *-z and final *-a loss`
- Source line or section hint: `lines 21441-21461`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `z_loss`; `final_a_loss`; `apocope_chronology`; `oblique_example`; `proto_vs_protoform`
- Recommended next use: `cite_if_explaining_rule_order`
- Shared with row IDs: `2082`; `2146`

This fragment is current and useful, but only if the row-level distinctions stay explicit. DEV_NOTES summarizes Ringe–Taylor's chronology, then states: “the final *a of nom.sg. *-az ... was *also* lost in the same PWGmc step, after *z-loss, leaving a bare stem,” with the example `PGmc *stainą > PWGmc *stain > OE stān` [Germanic/docs/DEV_NOTES.md:21451-21458]. The practical value for row `2220` is that it explains why the live trace's final steps `*stāna > *stān` are historically intended rather than ad hoc [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4737-4739].

What the fragment should **not** be made to say is that the live row's `PROTO` or `PROTOFORM` is `*stainą`. The row's current comparator remains nominative-style `*stáinaz`; the DEV_NOTES example is a shared rule-order illustration using a different paradigm form. That difference is exactly the sort of thing later report writers should keep explicit instead of silently normalizing away.

## Superseded or diagnostic material

- The main diagnostic boundary is between OE and later English. DEV_NOTES lines `1818-1819` and `1835` discuss `*stānaz` in the English sandbox, where it still surfaced as `stānə` or later branched toward `{təʊ/taɪ/teɪ}` on the way to Modern English `stone` [Germanic/docs/DEV_NOTES.md:1818-1819,1835-1835]. Those notes are not row-`2220` mismatch evidence and should not be cited as if OE `stān` were failing.
- The apocope examples `*stainą > *stain > stān` and `*staina > *stain` are not superseded, but they are easy to misuse if detached from the row. They are current rule-order background, not alternate live row inputs [Germanic/docs/DEV_NOTES.md:21451-21458,23664-23669].
- Because no packet, memo, or row-dedicated source audit currently survives for this lexeme, later work should resist overstating the DEV_NOTES base. The row is well supported as a regular OE outcome; what is thin is the row-specific DEV_NOTES prose, not the philology.

## Open questions for later work

- If a packet or research memo is ever created for row `2220`, decide whether it should foreground the simple live derivation `*stáinaz > *stānaz > *stāna > stān` or begin with the handbook-format distinction `*staina-` / `*stainaz` versus the row's accented project input `*stáinaz`.
- If later report prose uses the Ringe–Taylor apocope note, label `*stainą` or `*staina` explicitly as rule-order examples rather than silently replacing the live row's `PROTOFORM` with them [Germanic/docs/DEV_NOTES.md:21451-21458,23664-23669].
- If `dev_notes_slices/index.tsv` is revisited later, the likely candidate fragments are the shared current monophthongisation and verification notes (`DEV_NOTES:line-2259-2263`, `DEV_NOTES:line-28123-28124`), but on present evidence the row still looks better kept as a no-index slice unless a genuinely stone-specific note is added.
