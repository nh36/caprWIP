---
row_id: 2217
concept: still
counterpart: stillan
proto: *stéllijaną
protoform: *stéllijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2217-still-stillan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2217-still-stillan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2217 still / stillan

## Current row state

- The live OE row is `2217`, `CONCEPT still`, `COUNTERPART stillan`, `PROTO *stéllijaną`, `PROTOFORM *stéllijaną`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1114-1114].
- The live TSV note already states the lexical caution that matters most for this row: “OE stillan wv. 'to still, calm' matches verb form of Du. stillen, G stillen; stille is adj.” [Germanic/data/germanic-aligned-final.tsv:1114-1114].
- `oe_known_problems.tsv` has no row-local entry for row `2217`, for `stillan`, or for `*stéllijaną`; the project is not currently treating this row as an exception or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The linked packet and research memo already agree that the live row is a regular weak-verb derivation and that the main caution is lexical framing, not sound-change rescue: the row targets the verb `stillan`, while adjective `stille` is related background only [Germanic/docs/lexeme_reports/packets/2217-still-stillan.md:17-41; Germanic/docs/lexeme_reports/research_memos/2217-still-stillan.md:13-20,52-60; @ClarkHall1960; @BosworthToller1898].

## Detailed development-note summary

The live row is straightforward if the three row labels are kept distinct. `PROTO` and `PROTOFORM` are both the current project input `*stéllijaną`, while `COUNTERPART` is the OE weak verb `stillan` [Germanic/data/germanic-aligned-final.tsv:1114-1114]. The row note already warns against the main confusion: the wider lexical family also contains adjective `stille`, but this row is the **verb** row, aligned with Dutch `stillen` and German `stillen`, not an adjective row [Germanic/data/germanic-aligned-final.tsv:1114-1114].

The relevant DEV_NOTES material is thin and mostly shared with other heavy-stem Class I weak verbs. The earliest usable fragment is the old heavy-stem table at `DEV_NOTES:line-8719-8739`, where `stillan` appears as `*stelljăną | CVCC (heavy) | -jăną | stillan`. That fragment once argued that house notation for heavy stems should be post-Sievers-leveling `*-jăną`, not `*-ijăną` [Germanic/docs/DEV_NOTES.md:8719-8739]. For row `2217`, this remains useful only as project chronology. It does **not** match the live row state, because the live row now uses a PGmc-style `*-ijaną` input with acute-accented root vowel, `*stéllijaną`, rather than the older normalized post-syncope/post-leveling notation `*stelljăną` [Germanic/data/germanic-aligned-final.tsv:1114-1114].

DEV_NOTES itself then reverses that earlier notation policy. The transition note at `DEV_NOTES:line-8743-8759` explicitly labels the older `*-jăną` reasoning “SUPERSEDED,” and the current shared decision at `DEV_NOTES:line-8763-8836` says that heavy-stem Class I weak verbs must keep `*-ijăną` under PGmc input notation and then undergo a regular PWGmc syncope: “the sequence *-CijV- was syncopated to *-CjV-” [Germanic/docs/DEV_NOTES.md:8743-8759,8763-8836; @RingeTaylor2014, p. 157]. `stillan` is not singled out in the quoted handbook example there, but the row belongs to exactly that heavy-stem CVCC class. On current project logic, the older `*stelljăną` form is therefore a later derived stage or an obsolete house notation, not the stored row header.

The later implementation log gives the row its closest current DEV_NOTES anchor. At `DEV_NOTES:line-8911-8935`, the update table explicitly includes `*stelljăną → *stellijăną`, and it labels the change “by analogy (CVCC heavy)” [Germanic/docs/DEV_NOTES.md:8911-8935]. The follow-up heavy-stem inventory at `DEV_NOTES:line-8997-9018` again lists `*stellijăną` among the heavy verbs now treated with `*-ijăną` [Germanic/docs/DEV_NOTES.md:8997-9018]. These fragments are useful because they show that the row was intentionally brought under the shared PGmc `*-ij-` policy. But they are also the reason to stay conservative: the support is still a **shared notation table** and an **implementation log**, not a row-specific stillan dossier or a direct handbook citation for this exact lexeme.

The replacement working note for row `2217` should therefore preserve a narrow, explicit conclusion. Current row policy is: keep `PROTO *stéllijaną`; keep `PROTOFORM *stéllijaną`; keep `COUNTERPART stillan`; treat adjective `stille` as related but non-target background; and treat DEV_NOTES `*stelljăną` / `*stellijăną` spellings as project-history or normalization variants rather than rival live row states [Germanic/data/germanic-aligned-final.tsv:1114-1114; Germanic/docs/DEV_NOTES.md:8719-8739,8743-8759,8763-8836,8911-8935,8997-9018]. Because the surviving DEV_NOTES evidence is shared, partly superseded, and partly “by analogy,” this row is a good candidate to remain a no-index slice unless later work adds lexeme-specific stillan evidence.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-8719-8739

- Source heading: `Empirical Confirmation from Our TSV`
- Source line or section hint: `lines 8719-8739`
- Fragment type: `shared_notation_history`
- Status: `superseded`
- Issue tags: `heavy_stem_class_i`; `old_house_notation`; `sievers_law`; `row_2217_in_shared_table`
- Recommended next use: `use_as_project_history_only`

This fragment is worth preserving because it is the earliest direct DEV_NOTES place where row `2217` appears by reflex name. It lists `stillan` in the shared heavy-stem table as `*stelljăną`, then concludes that the TSV convention was “post-Sievers'-Law-leveling (= PWGmc or later)” and therefore should prefer `*-jăną` for heavy stems [Germanic/docs/DEV_NOTES.md:8719-8739].

> `| *stelljăną | CVCC (heavy) | -jăną | stillan |` [Germanic/docs/DEV_NOTES.md:8730-8730]

For current row work, this fragment is no longer live authority. It matters because it explains why older packeted material may still mention `*stelljăną`, but the line should now be read as superseded notation history, not as the row's current `PROTO` or `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:1114-1114].

### DEV_NOTES:line-8743-8759

- Source heading: `Final Resolution`
- Source line or section hint: `lines 8743-8759`
- Fragment type: `superseding_transition_note`
- Status: `superseded_but_explanatory`
- Issue tags: `explicit_reversal`; `notation_policy_change`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`

This fragment is the explicit reversal notice that keeps the older table from being misread as current. DEV_NOTES says the previous `*-jăną` argument is “SUPERSEDED,” explains that PGmc input notation is now being adopted instead, and states that heavy-stem forms retain `*-ijăną` [Germanic/docs/DEV_NOTES.md:8743-8759].

> `**SUPERSEDED** — See "DECISION UPDATE" section below. We are adopting PGmc input notation, which means heavy-stem Class I weak verbs retain *-ijăną.` [Germanic/docs/DEV_NOTES.md:8745-8747]

For row `2217`, this fragment does not itself prove the exact live spelling `*stéllijaną`, but it does show that the old `*stelljăną` table must no longer control row policy.

### DEV_NOTES:line-8763-8836

- Source heading: `DECISION UPDATE (2026-03-13): Adopting PGmc Input Notation`
- Source line or section hint: `lines 8763-8836`
- Fragment type: `current_shared_policy`
- Status: `current`
- Issue tags: `pgmc_input_notation`; `heavy_stem_class_i`; `sievers_law_syncope`; `proto_vs_later_stage`
- Recommended next use: `cite_if_indexed_later`

This is the controlling current DEV_NOTES policy fragment for the row, even though it is shared rather than stillan-specific. It states that heavy-stem Class I weak verbs “need `*-ijăną`, not `*-jăną`,” and it gives the handbook rule that “the sequence *-CijV- was syncopated to *-CjV-” in PWGmc [Germanic/docs/DEV_NOTES.md:8767-8773,8795-8836; @RingeTaylor2014, p. 157].

> `Heavy-stem Class I weak verbs need *-ijăną, not *-jăną` [Germanic/docs/DEV_NOTES.md:8770-8770]

> `"the sequence *-CijV- was syncopated to *-CjV-"` [Germanic/docs/DEV_NOTES.md:8797-8799; @RingeTaylor2014, p. 157]

For row `2217`, this fragment justifies treating live `*stéllijaną` as the PGmc-level row header while understanding older `*stelljăną` as the later syncopated shape. It is current and important, but still only shared policy support.

### DEV_NOTES:line-8911-8935

- Source heading: `Sievers' Law Implementation Status (2026-03-13)`
- Source line or section hint: `lines 8911-8935`
- Fragment type: `implementation_log_with_row_mention`
- Status: `background`
- Issue tags: `old_to_new_form_log`; `shared_table`; `by_analogy_support`
- Recommended next use: `cite_if_project_history_needed`

This fragment is the closest thing DEV_NOTES has to a row-local implementation record. It says that heavy-stem verbs were updated to `*-ijăną` notation and explicitly includes the row's older/newer normalized pair: `*stelljăną → *stellijăną` [Germanic/docs/DEV_NOTES.md:8911-8935].

> `| *stelljăną | *stellijăną | by analogy (CVCC heavy) |` [Germanic/docs/DEV_NOTES.md:8932-8932]

Its limitation is exactly what later report writers need to remember: the support here is not a lexeme-specific philological argument but a shared heavy-stem implementation sweep, and the source column says “by analogy,” not a direct stillan citation from a handbook or dictionary.

## Superseded or diagnostic material

- The old heavy-stem table at `DEV_NOTES:line-8719-8739` should not be silently normalized away. It explains why older notes may still use `*stelljăną`, but its `*-jăną` policy is explicitly overturned by `DEV_NOTES:line-8743-8759` and `DEV_NOTES:line-8763-8836` [Germanic/docs/DEV_NOTES.md:8719-8759].
- The implementation log's `*stellijăną` is useful but not identical in notation to the live row's `*stéllijaną`. The consonantal/suffixal point is the same — heavy stem plus `*-ij-` — but later work should keep the live TSV spelling authoritative rather than treating DEV_NOTES normalization variants as interchangeable row headers [Germanic/docs/DEV_NOTES.md:8911-8935; Germanic/data/germanic-aligned-final.tsv:1114-1114].
- The packet's lexical-table hit for adjective `stille` is diagnostic background only. It does not compete with the row's verbal `COUNTERPART stillan`, and the live TSV note already warns that adjective and verb must be kept separate [Germanic/docs/lexeme_reports/packets/2217-still-stillan.md:76-86; Germanic/data/germanic-aligned-final.tsv:1114-1114].

## Open questions for later work

- If `index.tsv` is revised later, only index this row once there is a reason to index a **shared-policy** fragment for a lexeme with no row-specific DEV_NOTES dossier. On present evidence, the slice is probably better kept as no-index working infrastructure.
- If a final lexeme report is later needed, the report should state the hierarchy in one sentence: cognate-set `PROTO *stéllijaną`; row-level `PROTOFORM *stéllijaną`; OE target `COUNTERPART stillan`; adjective `stille` only as related background [Germanic/data/germanic-aligned-final.tsv:1114-1114].
- If later philological work wants this row to become indexable, the missing ingredient is not more shared Sievers-law policy but a genuinely stillan-specific lexical citation or discussion that directly addresses the verb/adjective split and the verbal target.
