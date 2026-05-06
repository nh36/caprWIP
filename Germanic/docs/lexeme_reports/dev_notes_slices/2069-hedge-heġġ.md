---
row_id: 2069
concept: hedge
counterpart: heġġ
proto: *xágjaz
protoform: *xágjaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2069-hedge-heġġ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2069 hedge / heġġ

## Current row state

- CONCEPT: `hedge`
- COUNTERPART: `heġġ`
- PROTO: `*xágjaz`
- PROTOFORM: `*xágjaz`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2069 currently keeps `PROTO = PROTOFORM = *xágjaz`, targets normalized OE `heġġ`, and carries the row note `Note: heċġ is the more standard spelling; using heġġ here` [Germanic/data/germanic-aligned-final.tsv:540-540].
- Packet status: the compact derivation already expects and outputs `heġġ`; the packet also records `_No manifest entry._`, `_None_` for matching `oe_known_problems.tsv` entries, and no high-confidence row-local DEV_NOTES discussion beyond the January cleanup history [Germanic/docs/lexeme_reports/packets/2069-hedge-heġġ.md:11-13,17-43,45-51].
- Memo status: the live row is a current engineering success case, but the memo warns that this only settles the project-normalized OE target and the `*-gj-*` derivational path. The memo explicitly separates three levels that later work must not collapse: current TSV comparative `PROTO` `*xágjaz`, current project derivational input `*xágjaz` / internal trace `*xagjăz`, and OE target `heġġ`; it also argues that standard OE lexical/headword evidence in repo sources is `heċġ` / `hecg`, while `heġġ` is the project's normalization, and that the deeper comparative stem-class question is not actually resolved by the existing DEV_NOTES material [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:35-55,57-66,72-82].

## Development-note summary

Current row-specific DEV_NOTES authority **does exist**, but it is narrow. It securely governs the January 2026 orthography-and-chronology cleanup that made the project output stay at normalized `heġġ` rather than oscillating between `hæġġ` and `hæċġ`, and it also preserves the specific implementation decision that `*xagjăz` should surface with stressed `e`, not with a later unstressed-`ag` rewrite [DEV_NOTES:line-1726-1729; DEV_NOTES:line-1750-1753; DEV_NOTES:line-3068-3074]. What DEV_NOTES does **not** securely provide is a current row-specific philological adjudication of the comparative reconstruction itself. The memo is therefore right to treat the engineering success and the comparative stem-class question as separate matters [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:21-22,33-45,57-66,75-82].

The current DEV_NOTES story is an implementation story, not a paradigm-cell story. First, the January orthography cleanup records that the project deliberately backed away from mapping `{ʤj}` to `{ċġ}` and instead kept OE output at `ġġ`, while simultaneously changing the aligned TSV row from `heċġ` to `heġġ` with the explicit caution that `heċġ` is the more standard spelling [DEV_NOTES:line-1726-1729]. Second, the immediately following `*-gj-*` chronology check says the implementation was aligned to the standard ordering “gemination before *j ... palatalization of velars by *j ... precedes i-mutation,” and reports the concrete result `*xagjăz → heġġ` [DEV_NOTES:line-1750-1753]. Third, the later `OELateUnstressedAgSuffix` note preserves an important guardrail: the medial unstressed `*a > e > i` machinery was explicitly restricted so it would not damage stressed-syllable forms, with `*xagjăz → heġġ` named as the control case “which should keep stressed *e” [DEV_NOTES:line-3068-3074]. For row 2069, then, live `PROTO` and live `PROTOFORM` are the same current project input, while OE `COUNTERPART` is the normalized engineering target `heġġ`; those facts are current row policy even if future philological review later changes the comparative headword.

The comparative/source-audit side has to be stated more cautiously than the current TSV row alone suggests. The packet is strong on current trace behavior but explicitly shows no substantive row-local DEV_NOTES or dossier discussion beyond the cleanup notes [Germanic/docs/lexeme_reports/packets/2069-hedge-heġġ.md:49-55,57-124]. The memo adds the missing caution: repo lexical/reference materials reportedly favor ordinary headword spellings `heċġ` / `hecg`, and comparative references reportedly point toward a feminine `*hagjō-` / WGmc `*hagjō(n)` type rather than the current TSV's masculine-looking `*xágjaz`; on that reading, the present row is a good normalized OE derivation built from a currently convenient project input, not a securely settled lexeme-level reconstruction [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:21-22,35-55,72-82]. Because no securely attachable current DEV_NOTES fragment settles that philological dispute, later reporting should say so directly rather than implying that successful output `heġġ` proves the comparative `PROTO` is already resolved.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1726-1729

- Source heading: `Hedge (2026-01-20)`
- Source line or section hint: `lines 1726-1729`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `orthography_normalization`; `counterpart_selection`; `current_output`; `project_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current row-specific DEV_NOTES authority. It records three still-live decisions in one place: the project “Reverted the orthographic `{ʤj} -> {ċġ}` mapping,” removed `{ċġ}` from `OldEnglishSurfaceConsonant`, updated the aligned TSV row “(OE heċġ → heġġ),” and preserved the caution that `heċġ` is “the more standard spelling” [DEV_NOTES:line-1726-1729]. For row 2069 this fragment therefore settles the current engineering target exactly: `COUNTERPART = heġġ` is not an accidental spelling drift but an intentional project normalization, and the note itself already warns that dictionary/headword OE is more standard as `heċġ`, exactly as the live TSV note and the memo continue to say [Germanic/data/germanic-aligned-final.tsv:540-540; Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:46-55].

### DEV_NOTES:line-1750-1753

- Source heading: `OE *-gj- chronology check (2026-01-22)`
- Source line or section hint: `lines 1750-1753`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `gj_chronology`; `gemination`; `palatalization`; `i_umlaut`; `row_derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1961`

This fragment is the current derivational warrant for why the row now works. DEV_NOTES says standard accounts place WGmc gemination before `*j`, then palatalization of velars by `*j`, and then i-mutation; implementation was changed so palatalized consonants still count as intervening material for i-umlaut, and the note gives the direct result: `*xagjăz → heġġ` [DEV_NOTES:line-1750-1753]. For row 2069 that matters more than a generic statement about palatalization, because it is the surviving note that actually attaches the successful chain to this lexeme. It also helps keep levels distinct: the cited form here is the project's derivational input `*xagjăz`, not an argument that comparative `PROTO = *xágjaz` is philologically beyond dispute, and the output is normalized OE `heġġ`, not a claim that lexicographic headwords ordinarily print `ġġ` rather than `ċġ` [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:35-55].

### DEV_NOTES:line-3068-3074

- Source heading: `OELateUnstressedAgSuffix — Implementation`
- Source line or section hint: `lines 3068-3074`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `stressed_e`; `ag_suffix_scope`; `no_regression_guardrail`; `shared_implementation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This note is not a full hedge discussion, but it is still useful current background because it names row 2069 as a control case when later unstressed `*ag` handling was tightened. DEV_NOTES says the three-step `OELateUnstressedAgSuffix` sequence was restricted to medial, non-initial position “to prevent regressions on stressed-syllable forms (e.g. `*xagjăz → heġġ`, which should keep stressed `*e`)” [DEV_NOTES:line-3068-3074]. That sentence is worth preserving because it shows that later pipeline work treated the hedge row as already solved and as something that must not be rebroken by suffix-cleanup logic. It is therefore background/current implementation context for the row, not a separate philological argument about the lexeme itself.

### DEV_NOTES:line-2630-2645

- Source heading: `OE orthography cleanup + reports (2026-01-18)` and `Foma CLI gotchas (2026-01-18)`
- Source line or section hint: `lines 2630-2645`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `nondeterminism`; `hæġġ_vs_hæċġ`; `pre_orthography_cleanup`; `debug_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is the checked superseded history that later writers should keep, but only as history. DEV_NOTES reports that the 2026-01-18 trace still gave hedge as both `hæġġ` and `hæċġ`, calls that nondeterminism an open issue, and says pre-orthography cleanup was needed so `*dʒ + *j` would coalesce to `{ʤj}` before orthography; the paired one-off `foma` test output `"ç*æʤj"` confirms the merge rule on the hedge pre-orthography form [DEV_NOTES:line-2630-2645]. For row 2069 this material should be carried forward only as superseded debugging context, because the later 2026-01-20 and 2026-01-22 notes replace it with the stable policy/output `heġġ` [DEV_NOTES:line-1726-1729; DEV_NOTES:line-1750-1753].

## Superseded or diagnostic material

- The only securely attachable row-specific DEV_NOTES controversy is the old orthography nondeterminism `hæġġ` / `hæċġ`; that problem is superseded. Later notes explicitly normalize the row to `heġġ` and treat it as matching expected output [DEV_NOTES:line-2637-2645; DEV_NOTES:line-1726-1729].
- No current row-specific DEV_NOTES fragment securely adjudicates the memo's larger philological warning about comparative `*xágjaz` versus a likely feminine `*hagjō-` / `*hagjō(n)` type. That issue therefore remains outside current DEV_NOTES authority and should be described as a checked open source-audit question rather than as solved row policy [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:21-22,35-45,75-82].
- The packet's background hits at `DEV_NOTES:line-1728-1729`, `1753`, and `3074` remain useful only when read with their status distinctions intact: the first two are current engineering policy, the third is shared guardrail/background, and none of them by itself proves the comparative lexeme reconstruction [Germanic/docs/lexeme_reports/packets/2069-hedge-heġġ.md:61-107].
- `oe_known_problems.tsv` has no entry for this row, so row 2069 is not currently treated as an unresolved FST exception bucket. The remaining uncertainty is documentary/philological, not a live pipeline failure [Germanic/docs/lexeme_reports/packets/2069-hedge-heġġ.md:45-47; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a final lexeme report goes beyond current engineering state, decide whether to adopt the memo's source-audit warning that comparative `PROTO`/`PROTOFORM` may need review toward a feminine `*hagjō-` / `*hagjō(n)`-type reconstruction; current DEV_NOTES does not settle that question [Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:21-22,35-45,75-82].
- Decide how explicitly later report prose should frame `heġġ` as project normalization versus standard dictionary/headword `heċġ` / `hecg`. The January DEV_NOTES wording “heċġ is the more standard spelling” is strong enough that later prose should probably quote or paraphrase it rather than softening the distinction [DEV_NOTES:line-1728-1728; Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:46-55].
- If the row is ever re-audited for comparative reconstruction, keep the three-way distinction explicit: live comparative field `PROTO`, live derivational input `PROTOFORM`, and OE target `COUNTERPART` are currently aligned in the TSV, but the memo argues that only the OE derivation/output side is securely settled by present repo notes [Germanic/data/germanic-aligned-final.tsv:540-540; Germanic/docs/lexeme_reports/research_memos/2069-hedge-heġġ.md:35-45,57-66].
