---
row_id: 1943
concept: begin
counterpart: beġinnan
proto: *bigínnaną
protoform: *bigínnaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1943-begin-beġinnan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1943-begin-beġinnan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1943 begin / beġinnan

## Current row state

- CONCEPT: `begin`
- COUNTERPART: `beġinnan`
- PROTO: `*bigínnaną`
- PROTOFORM: `*bigínnaną`
- DERIVATION_CLASS: `regular`
- Live TSV note (abridged): `Palatalization of *g ... is regular; OE beġinnan confirmed.`

## Development-note summary

The live row is a regular prefixed infinitive: regular project comparator `*bigínnaną > beġinnan`, attested row target `beġinnan`, and the current FST output all coincide. The `ġ` is not an analogical rescue or a special spelling convention invented for this row; it is the regular OE palatal outcome for intervocalic `*g` in a front-vowel environment. The most useful handbook statement for this exact environment is Ringe and Taylor's rule that “Intervocalic *g was palatalized between any two front vowels” [@RingeTaylor2014, §6.4.1]. DEV_NOTES also preserves Campbell's direct lexical reminder that palatal `g` belongs in this verb family: “Examples of initial palatal sounds are: ... **gift** gift, **gifre** greedy, **ginnan** begin, **gefan** (W-S **giefan**) give...” [@Campbell1959, §427]. Dictionary headwords written with plain `g` therefore do not count against the row's normalized `ġ`; they are ordinary lemma spellings for the same verb [@BosworthToller1898, s.v. "be-ginnan"; @ClarkHall1960, s.v. "beginnan"].

The `be-` in this row must be kept separate from the palatalization claim. DEV_NOTES' later correction is explicit that `*biginnăną > beġinnan` does **not** instantiate the Fulk/Kock-style NWGmc medial `*i > e` problem. Instead it reflects a separate OE unstressed-prefix development: `bi- > be-`. The note preserves the handbook wording that matters most here — Ringe and Taylor's “So also bi- > be-, ni 'not' > ne.” [@RingeTaylor2014, p. 303] — and uses it to correct the earlier project tendency to treat this row as evidence about the broader medial-`*i` lowering debate. For later report work the contrast should stay explicit: regular comparator `bi-` prefix reduction plus regular palatalization yields `beġinnan`; attested/target outcome is likewise `beġinnan`; superseded detours such as `beġennan` came from project implementation mistakes, not from rival philological expectations.

DEV_NOTES keeps two distinct superseded debugging phases that later writers should not have to rediscover. The oldest row-local snapshot is the generic weak-tail stage `gennana`, shared with several other infinitives and useful only as pipeline history. The more important detour is the failed medial-lowering fix that produced `*biginnăną -> beġennan` by lowering the stressed root vowel as well as the prefix vowel. A temporary three-step `*ĭ`-marking system then restored `beġinnan`, but that mechanism is itself no longer current row policy. The later `*ĭ cleanup` note explicitly removes `OEUnstressedIMarking2` from the active composition and says that the prefix vowel is now handled independently by `OEPrefixIReduction`; the sentinel verification keeps `*bigínnaną -> beġinnan` unchanged through that cleanup. The current decision is therefore narrower and cleaner than the older notes: row 1943 remains `regular`, `ġ` comes from regular palatalization, `be-` comes from separate unstressed prefix reduction, and the abandoned `*ĭ`-marking workaround survives only as project chronology.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2422-2485

- Source heading: `PGmc→OE TODOs / OE evaluator snapshot / Ending diagnostics`
- Source line or section hint: `lines 2422-2485`
- Fragment type: `project_history`
- Status: `diagnostic_only`
- Issue tags: `weak_tail_cleanup`; `old_mismatch_snapshot`; `shared_infinitive_bug`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1934, 1967, 1971, 1972`

This early OE-wide snapshot preserves the oldest row-local failure: the project was still emitting `gennana` under the generic `-ana` weak-tail problem. The note groups begin with other infinitives such as `bacana`, `brecana`, `brengana`, and `brūcana`, so the fragment is useful only as chronology. It shows that the target `beġinnan` was not yet in doubt; the problem was unfinished weak-tail cleanup shared across several verbs.

### DEV_NOTES:line-6516-6521

- Source heading: `Attestation Evidence`
- Source line or section hint: `lines 6516-6521`
- Fragment type: `philological_background`
- Status: `current`
- Issue tags: `palatal_g`; `lemma_support`; `normalized_orthography`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is current as phonological and lexicographic background. DEV_NOTES preserves Campbell's quotation, “Examples of initial palatal sounds are: ... **gift** gift, **gifre** greedy, **ginnan** begin, **gefan** (W-S **giefan**) give...” [@Campbell1959, §427]. For row 1943 the point is not that the unprefixed lemma `ginnan` replaces the live row input, but that palatal `g` in the begin-family is handbook-normal; plain-dictionary `beginnan` spellings should therefore be read as orthographic/lexicographic equivalents rather than as evidence against normalized `beġinnan`.

### DEV_NOTES:line-6777-6875

- Source heading: `Implementation Attempt #1: Simple Parallel Rule (FAILED)` / `Implementation Attempt #3: Three-Step Marking (SUCCESSFUL)`
- Source line or section hint: `lines 6777-6875`
- Fragment type: `superseded_analysis`
- Status: `superseded`
- Issue tags: `overbroad_lowering`; `root_vowel_preservation`; `project_chronology`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is the indispensable record of the main abandoned detour. The first attempt at `OEMedUnstressedILowering` fixed `harvest` but regressed `begin`: `*biginnăną -> beġennan` because the rule lowered the stressed root vowel in `ginn-` as well as the prefix vowel. DEV_NOTES then introduced the three-step `*ĭ`-marking system and gives the row-specific trace explicitly: prefix `*i` marked, root `*i` accidentally marked too, root `*ĭ` restored, then lowering yields `beġinnan` again. That repair mattered historically because it restored the right output, but it is no longer the live explanation for row 1943 after the later cleanup moved the row onto `OEPrefixIReduction` instead.

### DEV_NOTES:line-17441-17452

- Source heading: `Fulk vs. Our Implementation of *i → *e (2026-04-12)`
- Source line or section hint: `lines 17441-17452`
- Fragment type: `row_policy`
- Status: `current`
- Issue tags: `prefix_lowering`; `not_nwgmc_i_lowering`; `source_quote`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling corrective fragment for the row. DEV_NOTES says plainly that `*biginnăną -> beġinnan` is **resolved** because the `be-` does not come from NWGmc medial `*i > e`, but from a separate OE unstressed-prefix rule. It then preserves the handbook wording that later reports should quote directly: “So also bi- > be-, ni 'not' > ne” [@RingeTaylor2014, p. 303]. Use this fragment whenever the report needs to prevent the row from being mis-cited as evidence about the wrong sound change.

### DEV_NOTES:line-38371-38387

- Source heading: `*ĭ cleanup sentinel verification for begin`
- Source line or section hint: `lines 38371-38387`
- Fragment type: `verification_snapshot`
- Status: `current`
- Issue tags: `sentinel_verification`; `prefix_root_protection`; `stable_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This sentinel table is current verification evidence rather than mere history. It lists `*bigínnaną -> beġinnan` under “bi-/ni- prefix root preservation,” which keeps the central row contrast concise: the prefix changes, the root vowel stays `i`. The fragment is especially useful because it shows the row surviving later cleanup work unchanged, not because it offers a new derivational theory by itself.

### DEV_NOTES:line-38419-38442

- Source heading: `current prefix-reduction mechanism after the *ĭ cleanup`
- Source line or section hint: `lines 38419-38442`
- Fragment type: `row_policy`
- Status: `current`
- Issue tags: `current_mechanism`; `prefix_reduction`; `ibreve_cleanup`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment states the current mechanism that supersedes the older three-step repair. DEV_NOTES explains that `OEUnstressedIMarking2`, the old `bi-/ni-` prefix-marking step, is no longer composed because the prefix vowel is “independently handled by `OEPrefixIReduction`,” which converts prefix `*i` to `*ĕ` and leaves the root untouched. The verification line is row-explicit: `*bigínnaną -> beġinnan` still works, and it works **via `OEPrefixIReduction`**. For later report prose this is the decisive “current, not superseded” implementation note.

## Superseded or diagnostic material

Two obsolete stories need to stay distinct. `gennana` is generic weak-tail pipeline history and says nothing special about the lexeme beyond its early participation in a shared OE infinitive bug. `beġennan`, by contrast, is the genuine row-local regression caused by an overbroad lowering rule. The three-step `*ĭ` repair solved that regression, but it too is now superseded as a mechanism; the current row explanation is the later `OEPrefixIReduction` cleanup plus regular palatalization.

## Open questions for later work

- If the final lexeme report cites dictionary support, keep the wording explicit that plain `beginnan`/`be-ginnan` spelling is lexicographic support for the same verb, not a rival non-palatal counterpart.
- If later report prose discusses `*i > e`, say directly that row 1943 is evidence for OE unstressed prefix reduction `bi- > be-`, not for NWGmc medial `*i > e` before non-high vowels.
- If any future note reuses the old `*biginnăną` or `*bĭ...` spellings, label them as internal staging/debug forms from superseded implementation history rather than as replacements for the live TSV `*bigínnaną`.
