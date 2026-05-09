---
row_id: 2248
concept: think
counterpart: þenċan
proto: *θánkijaną
protoform: *θánkijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2248-think-þenċan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md
linked_dossier_or_analysis_files: [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md, Germanic/docs/dossier-leek-2026.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2248 think / þenċan

## Current row state

- The live OE row is `2248`, `CONCEPT think`, `COUNTERPART þenċan`, `PROTO *θánkijaną`, `PROTOFORM *θánkijaną`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1233-1233].
- The live TSV note is: `Proto: *θankăz → *θankijăną (Kroonen *θankjan- 'to think'); OE þenċan (wk.v.)` [Germanic/data/germanic-aligned-final.tsv:1233-1233]. That note preserves useful etymological background, but it must not be read as if noun `*θankăz` were the row's direct OE derivational input.
- `PROTO` and `PROTOFORM` are the same here. The row is already using the fully encoded verbal input `*θánkijaną`; no substitute preform, oblique paradigm cell, or repaired protoform is in play [Germanic/data/germanic-aligned-final.tsv:1233-1233].
- The linked packet and the published derivation trace both show an exact match: `PROTO: *θánkijaną`, `EXPECTED: þenċan`, `OUTPUTS: þenċan` [Germanic/docs/lexeme_reports/packets/2248-think-þenċan.md:17-42; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5214-5217].
- `oe_known_problems.tsv` has no row-specific entry for `*θánkijaną`, `þenċan`, or row `2248`, so the current project is not treating this item as an unresolved OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Existing row infrastructure already supplies a reusable stem: packet `2248-think-þenċan.md` and research memo `2248-think-þenċan.md` both exist, so the slice uses that same stem [Germanic/docs/lexeme_reports/research_memo_index.tsv:111-111].

## Detailed development-note summary

The replacement working note for row `2248` should stay conservative because the live row is already clean. The core row-level claim is simply that OE `þenċan` is the regular outcome of the verbal input `*θánkijaną`, and the current implementation already derives that target exactly [Germanic/data/germanic-aligned-final.tsv:1233-1233; Germanic/docs/lexeme_reports/packets/2248-think-þenċan.md:17-42]. The main interpretive task is therefore documentary rather than phonological: keep the noun background `*þanka-/*þankaz`, Kroonen's dictionary-style verb lemma `*þankjan-`, and the row's actual `PROTO`/`PROTOFORM` `*θánkijaną` clearly distinct [Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md:32-40; @Kroonen2013, s.v. "*þankjan-"].

Kroonen's entry is useful precisely because it confirms the verbal lexeme without collapsing it into the noun. He gives `*þankjan- w.v. 'to think' ... OE þencan w.v. 'to think'` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:27213-27216; @Kroonen2013, s.v. "*þankjan-"]. Ringe and Taylor likewise list `PGmc *þankijaną 'to think' ... OE þenċan`, and elsewhere give the principal parts `*þankijaną, *þanhtē, *þanhtaz` with OE `þenċan, þōhte, þōht` [docs/references/ringe_vol1_pie_to_pgmc.txt:5400-5401,12303-12304; @RingeTaylor2014]. Those sources support the live row's verbal reconstruction directly. The noun `*þankaz` belongs here only as etymological background explaining the TSV note's noun-to-verb arrow, not as the operative row input.

The surviving DEV_NOTES material is thin and mostly negative/diagnostic, but it is still worth preserving because it prevents a predictable misreading. DEV_NOTES repeatedly uses `hycgan`, not `þenċan`, as the OE example of a residual weak class-III verb. One note states that “The 4 ‘Class III’ verbs in OE (habban, secgan, libban, hycgan) are NOT from *-ēn- at all — they are from *-jan- with j-gemination” [DEV_NOTES:line-3939-3944]. A later source survey says that Campbell's grammar lists `habban` among “the four verbs which preserve the clearest signs of belonging to **Class III**” and names `hycgan` alongside `secgan` and `libban`; Hogg is then quoted: “Four verbs in Old English preserve very clear signs of the Germanic weak class 3, namely **habban** 'have', libban 'live', secgan 'say' and hycgan 'think'” [DEV_NOTES:line-11578-11579,11696-11703]. For row `2248`, the practical consequence is simple: DEV_NOTES evidence about class-III `hycgan` is not positive evidence about row `2248` even though both gloss as “think.”

The only directly portable handbook point involving the `þencan` lexeme itself is Campbell's assibilation discussion, and even that is background rather than a row-level problem. Campbell says: “beside *þencan, þyncan, sécan, sengan* with assibilation, 3rd sg. pres. indic. would be *þencþ, þyncþ, sécþ, sengþ*” [Germanic/docs/dossier-leek-2026.md:269-273; @Campbell1959, §438]. That matters because it confirms that `þencan` is the ordinary lexeme Campbell discusses in the assibilation environment, but it does **not** require any change to the row's infinitival target `þenċan`. The row is about the citation form; it is not a finite-cell rescue note.

Accordingly, the present row should remain documented as a regular exact-match derivation with a small lexical caution attached. `PROTO` = `PROTOFORM` = `*θánkijaną`; `COUNTERPART` = `þenċan`; noun `*θankăz` is background only; and class-III `hycgan` passages are concept-name collisions, not row evidence [Germanic/data/germanic-aligned-final.tsv:1233-1233; Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md:49-57]. That is enough for a replacement working note, but probably not enough for indexable row-local DEV_NOTES coverage.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-3939-3944

- Source heading: `Weak verb class history / *-ēn- vs *-jan-`
- Source line or section hint: `lines 3939-3944`
- Fragment type: `diagnostic_gloss_collision_fragment`
- Status: `diagnostic_only`
- Issue tags: `hycgan_not_þencan`; `class_iii`; `project_history`
- Recommended next use: `use_as_negative_control_only`

This fragment is relevant to row `2248` only because it draws a boundary that later writers could otherwise blur. DEV_NOTES says that the four OE class-III verbs are `habban`, `secgan`, `libban`, and `hycgan`, and explicitly says these are `*-jan-` verbs with j-gemination rather than reflexes of `*-ēn-` [DEV_NOTES:line-3939-3944]. Since `þenċan` is not named in that list, the fragment should be carried forward as negative control evidence: it warns against importing `hycgan`-type class-III discussion into the `þenċan` row just because both verbs can be glossed “think.”

> “The 4 ‘Class III’ verbs in OE (habban, secgan, libban, hycgan) are NOT from *-ēn- at all — they are from *-jan- with j-gemination.” [Germanic/docs/DEV_NOTES.md:3943-3944]

### DEV_NOTES:line-11578-11579,11696-11703

- Source heading: `Campbell/Hogg source survey on OE weak class III`
- Source line or section hint: `lines 11578-11579, 11696-11703`
- Fragment type: `diagnostic_gloss_collision_fragment`
- Status: `diagnostic_only`
- Issue tags: `hycgan_not_þencan`; `source_survey`; `class_iii_background`
- Recommended next use: `use_as_negative_control_only`

This later source survey repeats the same lexical warning with explicit handbook phrasing. DEV_NOTES first says that Campbell's grammar lists `habban` among the four verbs that preserve the clearest class-III signs, “alongside `secgan`, `libban`, `hycgan`” [DEV_NOTES:line-11578-11579]. It then quotes Hogg: “Four verbs in Old English preserve very clear signs of the Germanic weak class 3, namely **habban** 'have', libban 'live', secgan 'say' and hycgan 'think'” [DEV_NOTES:line-11696-11703]. For row `2248`, this fragment is again diagnostic only. Its value is to show that the weak-class-III “think” verb in the handbooks is `hycgan`, not `þenċan`, so the project should keep that evidence in a separate lexical bucket.

## Superseded or diagnostic material

- No surviving DEV_NOTES fragment argues that row `2248` needs a different current `PROTO`, `PROTOFORM`, `COUNTERPART`, or derivation class. The live row, packet, and trace all agree on the regular derivation `*θánkijaną -> þenċan` [Germanic/data/germanic-aligned-final.tsv:1233-1233; Germanic/docs/lexeme_reports/packets/2248-think-þenċan.md:17-42; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5214-5217].
- The noun-to-verb sequence in the TSV note, `*θankăz → *θankijăną`, should be treated as etymological background only. It is useful because it preserves the derivational relationship, but it is superseded as a row-internal derivation if anyone reads it as though the noun were the FST input. The actual row input is already the verbal form `*θánkijaną` [Germanic/data/germanic-aligned-final.tsv:1233-1233; Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md:35-40].
- Campbell §438 is relevant background, not a row problem. The `þencan` / `þencþ` contrast belongs to assibilation and de-assibilation within the paradigm, whereas the live row targets the infinitive/citation form `þenċan` and already derives it correctly [Germanic/docs/dossier-leek-2026.md:269-273; @Campbell1959, §438].
- The DEV_NOTES fragments attached here are therefore best classified as `diagnostic_only` rather than as current row-local explanatory prose. They help keep `hycgan` evidence out of the row, but they do not provide a positive lexeme-specific development history for `þenċan`.

## Open questions for later work

- If a later final report is written, decide whether the TSV note should eventually be rewritten to mark `*θankăz` explicitly as etymological background while keeping `*θánkijaną` as the operative row input; the slice records that distinction, but the TSV itself has not been changed here.
- If later report work wants a paradigm aside, Campbell §438 is the right place to cite `þencan` / expected `þencþ`; that should remain optional background, not the main argument of the row report [@Campbell1959, §438].
- If future indexing work requires stronger row-local DEV_NOTES support, this row will probably need either a fuller lexeme report or a shared index entry that explicitly records the “hycgan is a gloss collision, not the same lexeme” warning. The current attachable DEV_NOTES material is real but thin.
