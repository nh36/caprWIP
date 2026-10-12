---
row_id: 2194
concept: six
counterpart: six
proto: *séxs
protoform: *séxs
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2194 six / six

## Current row state

- The live OE row is already a regular exact match: `CONCEPT = six`, `COUNTERPART = six`, `PROTO = *séxs`, `PROTOFORM = *séxs`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1023-1023].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so this row is **not** currently using a substitute OE-facing stem, a different paradigm cell, or an analogical repair input. The project has chosen one derivational input and one comparative label, both written `*séxs` [Germanic/data/germanic-aligned-final.tsv:1023-1023].
- The published derivation trace is an exact match and gives the current project chronology explicitly: `PROTO: *séxs`, `EXPECTED: six`, `OUTPUTS: six`, with OE-side stages `OE Breaking: *séoxs`, `OE Ws Palatal Umlaut: *sixs`, `OE Xs Merge: *siXS`, and surface `Outcome: six` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4306-4325].
- `oe_known_problems.tsv` has no row-specific entry for row `2194`, for `six`, or for `*séxs`; the file currently lists unrelated exception buckets only [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` classifies row `2194` as a regular row with no NOTE and no report requirement (`Requirement basis = none`), which makes this slice a replacement working note rather than the continuation of an existing required-report chain [Germanic/docs/lexeme_reports/coverage_audit.md:352-356].
- Comparative and OE reference support aligns with the current row but also shows the notation layers that must be kept separate. Kroonen cites the Proto-Germanic numeral as `*sehs`, Orel as `*sexs`, while the live TSV writes `*séxs`; for this row those are best treated as notation variants for the same lexical item, not as distinct chronological row policies or evidence for a different `PROTOFORM` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22368-22380; docs/references/orel_handbook_germanic_etymology.vision.txt:36041-36043; Germanic/data/germanic-aligned-final.tsv:1023-1023].
- The attested OE target also has its own layer. Clark Hall gives `siex (e, eo, i, y) 'six'`, Campbell gives early West Saxon `siex` and later `syx, six`, and Brunner likewise lists `ws. siex, später syx, seltener six` beside non-WS `sex`; the live row's `COUNTERPART = six` is therefore an attested OE spelling choice within a broader variant set, not a claim that all OE stages or dialects had surface `six` from the outset [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36313-36317; docs/references/campbell_old_english_grammar.txt:8763-8768,18850-18853; docs/references/brunner_1965_altenglische_grammatik.txt:12591-12593].

## Development-note summary

Row 2194 is currently a stable regular row, but the surviving DEV_NOTES evidence for it is mostly **guardrail material** rather than a standalone row dossier. The live trace already derives exact `six` from `*séxs` through three ordinary project stages—breaking, West-Saxon palatal umlaut, and final `xs` orthographic merge—and there is no surviving DEV_NOTES note that treats the row as a live mismatch or as a row needing a repaired `PROTOFORM` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4306-4325; Germanic/data/germanic-aligned-final.tsv:1023-1023].

The first distinction to keep explicit is **PROTO vs. PROTOFORM vs. attested OE target**. In the live TSV, `PROTO = PROTOFORM = *séxs`, so the row uses the same project-normalized form both as comparative label and as derivational input [Germanic/data/germanic-aligned-final.tsv:1023-1023]. That should not be confused with the reference-handbook spellings `*sehs` (Kroonen) and `*sexs` (Orel): those look like alternate notational conventions for the same Proto-Germanic numeral, not chronologically different row inputs [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22368-22380; docs/references/orel_handbook_germanic_etymology.vision.txt:36041-36043]. The OE target is a different layer again. The row targets attested OE `six`, but the handbook record also preserves `siex`, `syx`, and dialectal `sex`; those are attested output variants, not rival protoforms [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36313-36317; docs/references/campbell_old_english_grammar.txt:8763-8768,18850-18853; docs/references/brunner_1965_altenglische_grammatik.txt:12591-12593].

The second distinction is between the **cardinal** row and the much more frequently discussed **ordinal** material. DEV_NOTES repeatedly quotes handbook discussions of `North. sesta` and West-Saxon `syxta/siexta`, but those discussions belong to `sixth`, i.e. to `*sehsto-` or equivalent `*xs + C` environments, not to the cardinal `*séxs` row [Germanic/docs/DEV_NOTES.md:39023-39095,8148-8184]. That matters because the current DEV_NOTES material for row 2194 is mainly negative: it uses `six` as the example that must **not** be swept into the `*xs > s` loss rule that affects `*xsC` clusters. The strongest row-explicit current fragment says exactly that: row `2194 *séxs → six` sits in the `*xs` bucket where `*xs` is “mostly preserved as `x` orthographically, no loss,” and “Per Campbell §416, *xs survives as `x` (= ks) when no further consonant follows” [Germanic/docs/DEV_NOTES.md:39260-39276].

That guardrail is consistent with the handbooks and with the current trace. Campbell states that `xs` remained late enough in OE “to cause breaking,” and he includes `siex six` among the examples, which matches the project's trace step `*séxs -> *séoxs` [docs/references/campbell_old_english_grammar.txt:11015-11024; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4315-4320]. Ringe-Taylor make the same chronology even more explicit: `PGmc *sehs ‘six’ ... > OE *seohs > early WS siex, cf. ordinal siexta ~ sixta 'sixth'` [docs/references/ringe_taylor_linguistic_history_vol2.txt:19275-19276]. The project trace then carries the row one step further by applying West-Saxon palatal umlaut and surface-normalizing to `six` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4319-4325]. In other words, the live row is not being preserved by exception handling; it is being preserved because the current cascade treats cardinal `*séxs` as an ordinary `*xs` item and **reserves x-loss for different environments**.

The other current DEV_NOTES material that mentions `six` is similarly protective rather than exploratory. During the `*eo + o` contraction fix for `ten`, DEV_NOTES explicitly searched the `*[eé]x` cohort and recorded that `*séxs` is unaffected because it has `*x + C`, not `*x + V`; the only current lexeme in that audit needing the new contraction rule was `*téxun` [Germanic/docs/DEV_NOTES.md:42450-42455,42633-42638]. That is useful row history because it confirms that later sound-change work checked `six` for collateral damage and found none. But it is still not a row-specific philological analysis in the same sense as the large dossiers for `nine`, `fire`, or `tap`.

The safest dossier conclusion is therefore conservative. Row 2194 is a regular exact-match row whose live derivation is stable and philologically plausible; the surviving DEV_NOTES material mainly says what **not** to do to it. It does not preserve a row-specific mismatch narrative, and the current attachable evidence is mostly shared environment-control prose about `*xs` clusters, ordinal `sixth`, and collateral-risk audits for unrelated fixes [Germanic/docs/DEV_NOTES.md:39023-39095,39260-39276,42450-42455,42633-42638]. That makes the row well suited to a slice like this one, but a poor candidate for dense central indexing unless the project later decides to index negative guardrail fragments as such.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39260-39276

- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39276`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `xs_cluster`; `no_x_loss`; `row_policy`; `guardrail`
- Recommended next use: `cite_if_explaining_why_row_stays_regular`
- Shared with row IDs: `2017`; `2031`; `2146`; `2275`; `2276`

This is the strongest surviving row-explicit DEV_NOTES fragment. It lists row `2194 *séxs → six` under the `*xs` cohort and immediately glosses the whole bucket as “mostly preserved as `x` orthographically, no loss” [Germanic/docs/DEV_NOTES.md:39265-39270]. The follow-up sentence is the key policy statement: “Per Campbell §416, `*xs` survives as `x` (= ks) when no further consonant follows; the loss rule should not fire here” [Germanic/docs/DEV_NOTES.md:39273-39276].

For this row, that fragment does two useful jobs at once. First, it explicitly records that the project's current `*x`-loss research does **not** classify `six` as an item needing deletion of `x`. Second, it preserves the conditioning in a form that can be quoted later without re-litigating the entire `sixth / growth / axle / visit` cluster literature. If a final report ever needs a single DEV_NOTES anchor for row 2194, this is the best one.

### DEV_NOTES:line-39023-39095

- Source heading: `§17.40 research dossier — *x preconsonantal loss vs. j-gemination`
- Source line or section hint: `lines 39023-39095`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `xs_plus_c`; `ordinal_not_cardinal`; `conditioning`; `shared_background`
- Recommended next use: `cite_as_shared_background_only`
- Shared with row IDs: `2242`

This longer source canvass is not a six-row dossier, but it is the background that makes the row-specific guardrail intelligible. DEV_NOTES quotes Campbell, Brunner, Ringe-Taylor, and Bülbring on the loss of `x/h` in **preconsonantal** `*xsC` environments, with canonical examples such as `wæstm`, `sesta 'sixth'`, `þisl`, and `néosan` [Germanic/docs/DEV_NOTES.md:39027-39095]. The dossier repeatedly defines the change narrowly as `*xs → s / _ C`, i.e. `*xs` followed by an additional consonant.

For row 2194, the main importance of this fragment is negative delimitation. It explains why ordinal `sesta/siexta` material is relevant to the numeral family but **not** direct authority for the cardinal row `six`. The cardinal row has no additional following consonant after `*xs`, so the very dossier that discusses `sixth` ends up reinforcing the current treatment of `six` as outside the loss rule [Germanic/docs/DEV_NOTES.md:39027-39043,39077-39095; Germanic/docs/DEV_NOTES.md:39273-39276].

### DEV_NOTES:line-42450-42455 and line-42633-42638

- Source heading: `Risk audit` / `D. Risk audit (overgeneration)`
- Source line or section hint: `lines 42450-42455; 42633-42638`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `contraction_guardrail`; `collateral_check`; `x_plus_c`; `unaffected_row`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2010`; `2086`; `2242`

This pair of audit notes comes from the later `ten / tēon` contraction repair, not from a `six` investigation. Even so, the row is named twice in useful current form. DEV_NOTES says the audit searched all `*[eé]x` environments with back vowels and found that only `*téxun` creates the new `*eo + o` contraction environment; `*séxs`, alongside `*féxtaną`, `*wéxtiz`, and `*knéxtaz`, has `*x` followed by a consonant and is therefore outside the new rule's scope [Germanic/docs/DEV_NOTES.md:42450-42455,42633-42638].

This is worth preserving because it shows that later cascade repairs explicitly checked row 2194 for regressions. But it remains diagnostic project history rather than central row analysis. It is a “do not break six while fixing ten” note, not a primary explanation of why `*séxs` yields OE `six`.

## Superseded or diagnostic material

The most obviously misleading surviving DEV_NOTES material is not OE at all, but the Modern English sandbox work. In the English KIT sweeps, DEV_NOTES lists `six` among the remaining `{ɪ}` cases headed by `fish/give/six/will` [Germanic/docs/DEV_NOTES.md:2306-2324]. That material belongs to the Modern English pronunciation sandbox, not to the OE cascade, and it should not be cited as evidence that row 2194 was an OE mismatch or a live DEV_NOTES problem.

Less obviously, the repeated DEV_NOTES discussion of `sesta`, `siexta`, and `syxta` can also mislead if detached from context. Those forms are valuable for delimiting when `*xs > s` does and does not occur, but they are still ordinal evidence for `sixth`, not direct row policy for the cardinal `six` [Germanic/docs/DEV_NOTES.md:39023-39095,8148-8184]. Later writers should therefore avoid collapsing the two into one claim such as “DEV_NOTES says six loses x”; it does not.

The file also preserves no row-specific current mismatch dossier for 2194 analogous to the long notes for `nine`, `fowl`, or `fire`. That absence is itself part of the row history: the current project record treats `six` as a regular row that needed protection from overbroad rule changes, not as an active exception bucket item [Germanic/data/germanic-aligned-final.tsv:1023-1023; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4306-4325].

## Open questions for later work

- If a later final report wants a fuller philological note, decide whether the prose should normalize the proto citation explicitly as “project `*séxs` = handbook `*sehs/*sexs`,” since the row is stable but the notation difference is real and easy to misread as a stage difference [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22368-22380; docs/references/orel_handbook_germanic_etymology.vision.txt:36041-36043; Germanic/data/germanic-aligned-final.tsv:1023-1023].
- If later reporting wants to foreground attested OE variation, decide whether the row should continue to cite plain `six` alone or briefly mention the broader attested set `siex / syx / six / sex`; current evidence does not force a row change, but it does show that the target is one spelling choice within a larger OE variant field [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36313-36317; docs/references/campbell_old_english_grammar.txt:8763-8768,18850-18853; docs/references/brunner_1965_altenglische_grammatik.txt:12591-12593].
- If central index integration is attempted later, decide whether a negative guardrail fragment such as `39260-39276` is worth indexing at all. It is current and row-explicit, but it chiefly records that `six` is **unaffected** by the `*x`-loss discussion rather than preserving a positive row-specific derivation note.
