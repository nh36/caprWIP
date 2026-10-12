---
row_id: 2294
concept: wind
counterpart: windan
proto: *wíndaną
protoform: *wíndaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2294-wind-windan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2294-wind-windan.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2294 wind / windan

## Current row state

- The live OE row is a note-bearing regular row: `CONCEPT = wind`, `COUNTERPART = windan`, `PROTO = *wíndaną`, `PROTOFORM = *wíndaną`, `DERIVATION_CLASS = regular`, with the explicit row note `OE target: wind→windan (inf. of str.v. class III 'to wind, turn')` [Germanic/data/germanic-aligned-final.tsv:2294-2294].
- The published derivation trace is currently exact and uncomplicated: `# wind`, `PROTO: *wíndaną`, `EXPECTED: windan`, `OUTPUTS: windan`, with OE-side stages `OE Heavy Syllable Nasal Apocope: *wíndan`, `OE Secondary Nasalization: *wíndąn`, `OE Weak Tail Reduction: *wíndan`, and final `Outcome: windan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5965-5984].
- `coverage_audit.md` still classifies row `2294` as a row requiring note work (`| 2294 | wind | windan | regular | yes | - | - | - | NOTE |`), so this slice is not speculative extra commentary; it is the intended row-addressable replacement note layer for a row already flagged as needing documentation [Germanic/docs/lexeme_reports/coverage_audit.md:170-170].
- Row-specific support files do exist and should remain discoverable from here: the evidence packet and research memo both already treat the chief issues as (i) keeping the verb row separate from noun `wind` noise and (ii) keeping stale `*winþan-` / Verner speculation subordinate to later March 2026 conclusions [Germanic/docs/lexeme_reports/packets/2294-wind-windan.md:1-259; Germanic/docs/lexeme_reports/research_memos/2294-wind-windan.md:13-20,38-43].
- The distinction among the row fields still matters even though two of them coincide graphically. `PROTO = *wíndaną` is the comparative / cognate-set reconstruction used to label the row; `PROTOFORM = *wíndaną` is the actual OE-facing derivational input presently fed to the cascade; `COUNTERPART = windan` is the attested OE infinitive selected as the target output [Germanic/data/germanic-aligned-final.tsv:2294-2294; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5965-5984].
- Comparative lexical sources confirm that this row belongs to the **verb** family, not to the noun `wind` family. Kroonen has a distinct noun entry `*winda- m. 'wind'` and separately a verb entry `*windan- ... 'to wind'`; Seebold gives the OE principal parts `windan, wand, wundon, wunden`; Clark Hall separately records `wunden pp. of windan` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:1240-1242,29733-29736; docs/references/seebold_vergleichendes_woerterbuch.txt:47224-47225; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:50289-50289; @Kroonen2013; @ClarkHall1960].

## Development-note summary

The surviving `DEV_NOTES.md` material for row 2294 is real and useful, but it is mixed in genre. The most important current material is not a standalone `windan` dossier; it is a set of rule-scope and etymology-decision passages that use `windan` as a control form. Those passages are strong enough to preserve because they answer the only two live interpretive risks: whether `windan` is a Verner-style `*nþ/*nð` lexeme, and whether later `wi -> wu` work should have changed the infinitive to `*wundan`. On both questions the later notes are explicit and conservative [Germanic/docs/DEV_NOTES.md:7538-7556,7879-7882,43598-43624].

First, the later March 2026 `*nd` audit rejects the older `*winþan-` idea. The note now states: “`bindan, windan`: PIE roots `*bhendh-, *wendh-` with aspirated `*dh` → PGmc `*d`. No Grimm `*þ` ever existed” [Germanic/docs/DEV_NOTES.md:7555-7556; @Fulk2018, §3.6; @RingeTaylor2014, vol. 2, p. 157]. A second decision block restates the same point even more sharply: “Other `*nd` forms (bindan, windan, hund, etc.) have ORIGINAL `*d` from PIE `*dh` ... They were never `*þ` or `*ð` at any stage” [Germanic/docs/DEV_NOTES.md:7879-7882]. That is the current project position and should control future reuse of older notes.

Second, the later `wi -> wu` canvass uses `windan` as an anti-overgeneration check. The final rule discussion says that adding `*a` to the trigger set “would incorrectly fire on `*wíndaną → **wundan* (attested form is *windan*)`,” so the rule keeps a narrower `{*u, *o}` trigger set [Germanic/docs/DEV_NOTES.md:43598-43605]. The immediately following regression table then lists `| *wíndaną | w í n d a n ą | *n + *d (not *u/*o) | no | windan |`, making `windan` one of the explicit non-firing witnesses for the rule's final scope [Germanic/docs/DEV_NOTES.md:43613-43624]. The row therefore matters to project phonology not because it is problematic, but because it is one of the forms the project uses to prove that the newer umlaut rule has **not** over-fired. The related `widuwe-u-preservation` dossier says the same thing indirectly: forms like `*windan` “do NOT appear with *wu- attestations” and are therefore evidence for a conservative rule scope rather than for a repair target [Germanic/docs/dossiers/widuwe-u-preservation.md:1117-1126; @Campbell1959, §§218-219].

The remaining row-relevant `DEV_NOTES` material is thinner or more diagnostic. An early exploratory table had `wind | *winþan- | *đ (?) | windan`, but later notes supersede that table decisively [Germanic/docs/DEV_NOTES.md:7228-7233,7538-7556]. Another later discussion of `funden` cites Brunner's Epinal `awunden` from `awindan` as “the structurally closest parallel” for a class-III verb with nasal plus voiced stop and `u`-grade participial root [Germanic/docs/DEV_NOTES.md:25605-25616]. That passage is useful only as background for the wider verb family and for participial morphology; it is **not** a reason to reinterpret the row's target, because row 2294 still targets the simplex infinitive `windan`, not prefixed `awindan` and not past participial `wunden/awunden`.

The biggest practical caution is lexical noise. Because the concept label is modern English `wind`, generic search hits easily collapse the noun `wind` and the verb `windan`. DEV_NOTES itself contains such noise elsewhere, and comparative dictionaries do too unless the headword is checked carefully. Kroonen's separate noun `*winda- m. 'wind'` versus verb `*windan- 'to wind'` is therefore not an incidental lexicographic detail; it is the distinction future row work must keep explicit [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:1240-1242,29733-29736; @Kroonen2013]. The live TSV note is already doing this disambiguating work correctly by spelling out that the row is the infinitive of a class III strong verb [Germanic/data/germanic-aligned-final.tsv:2294-2294].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7538-7556 and line-7879-7882

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)` / `DECISION (2026-03-11): Option 2a Confirmed`
- Source line or section hint: `lines 7538-7556; 7879-7882`
- Fragment type: `lexeme_specific_shared_decision`
- Status: `current`
- Issue tags: `original_d_not_verner`; `nd_cluster`; `supersedes_winthan`; `etymology_control`
- Recommended next use: `cite_if_explaining_why_windan_is_not_a_nþ_nð_case`
- Shared with row IDs: `2192`; `2294`

This is the controlling current DEV_NOTES evidence for the row's consonant history. The audit table names `windan` explicitly and classifies it under “original *dh” rather than any `*þ/*ð` alternation: `| windan | *windăną | *wendh- "to turn" | original *dh | No |` [Germanic/docs/DEV_NOTES.md:7542-7546]. The prose conclusion then states: “`bindan, windan`: PIE roots `*bhendh-, *wendh-` with aspirated `*dh` → PGmc `*d`. No Grimm `*þ` ever existed” [Germanic/docs/DEV_NOTES.md:7553-7556]. The decision block at `7879-7882` is even stronger because it turns the same conclusion into explicit project policy: `windan` belongs with the `*nd` forms that had original `*d` all along and therefore “were never `*þ` or `*ð` at any stage” [Germanic/docs/DEV_NOTES.md:7879-7882; @Fulk2018, §3.6; @RingeTaylor2014, vol. 2, p. 157].

For later work, this fragment is what keeps the row from being dragged back into older Verner-style discussions. If a future report needs one sentence of current doctrine, it is this one: the row is a regular `*d` lexeme, not a hidden `*nþ/*nð` alternation case.

### DEV_NOTES:line-43598-43624

- Source heading: `Conditioning — handbook canvass and final scope` / `Cogset regression check (final rule, narrow C, broader-than-draft)`
- Source line or section hint: `lines 43598-43624`
- Fragment type: `lexeme_specific_rule_scope_guardrail`
- Status: `current`
- Issue tags: `wi_to_wu`; `overfire_guardrail`; `attested_windan`; `control_case`
- Recommended next use: `cite_if_explaining_why_the_row_must_not_shift_to_wundan`
- Shared with row IDs: `2282`; `2289`; `2294`

This fragment is current and row-explicit even though it belongs to a shared rule canvass rather than to a standalone `windan` memo. DEV_NOTES says that widening the trigger set to include `*a` “would incorrectly fire on `*wíndaną → **wundan* (attested form is *windan*)`,” so the final rule keeps the West-Saxon-conservative trigger set `{*u, *o}` [Germanic/docs/DEV_NOTES.md:43598-43605]. The regression table then names the row again as a non-firing witness: `| *wíndaną | w í n d a n ą | *n + *d (not *u/*o) | no | windan |` [Germanic/docs/DEV_NOTES.md:43615-43619].

The practical importance of this fragment is high. It preserves not just an outcome but a **negative constraint**: future phonological tinkering must continue to leave the infinitive as `windan`. Because the row's later past-participial family includes `u`-grade forms such as `wunden`, this guardrail is especially valuable; it prevents those paradigm shapes from being projected backward onto the infinitive without evidence [docs/references/seebold_vergleichendes_woerterbuch.txt:47224-47225; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:50289-50289; @ClarkHall1960].

### DEV_NOTES:line-7228-7233

- Source heading: `Similar Verbs to Check`
- Source line or section hint: `lines 7228-7233`
- Fragment type: `superseded_exploratory_history`
- Status: `superseded`
- Issue tags: `early_hypothesis`; `winthan`; `verner_probe`; `do_not_promote`
- Recommended next use: `retain_only_as_history_of_an_abandoned_guess`
- Shared with row IDs: `2192`; `2294`

This early table is worth preserving only because later packet generation can otherwise make it look more authoritative than it is. The table lists `wind | *winþan- | *đ (?) | windan` beside other verbs under a “Similar Verbs to Check” heading [Germanic/docs/DEV_NOTES.md:7228-7233]. Nothing in the later March 2026 decision blocks supports keeping that reconstruction alive. On the contrary, the later explicit statements that `windan` had original `*d` and “No Grimm `*þ` ever existed” directly supersede it [Germanic/docs/DEV_NOTES.md:7555-7556,7879-7882].

This fragment therefore belongs in the slice only as a warning label on project history. It is not a valid index anchor by itself unless it is paired with the later corrective material.

### DEV_NOTES:line-25605-25616

- Source heading: `Is fundan attested?`
- Source line or section hint: `lines 25605-25616`
- Fragment type: `diagnostic_paradigm_parallel`
- Status: `diagnostic`
- Issue tags: `awunden`; `awindan`; `past_participle_parallel`; `not_row_target`
- Recommended next use: `cite_only_if_explaining_why_u_grade_participles_do_not_change_the_infinitive_row`
- Shared with row IDs: `2192`; `2294`

This fragment does not diagnose row 2294 directly, but it is one of the few places where DEV_NOTES discusses a close morphological parallel. DEV_NOTES cites Brunner's Epinal `awunden` from `awindan` and calls it “the structurally closest parallel” because it is a class III verb with nasal plus voiced stop and `u`-grade participial root [Germanic/docs/DEV_NOTES.md:25608-25615]. That is useful for background because it shows the wider `windan` family behaving exactly as comparative dictionaries suggest: infinitive `windan`, past-participial `wunden`, prefixed participial `awunden` [docs/references/seebold_vergleichendes_woerterbuch.txt:47224-47225; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:9468-9473; @Campbell1959, §334].

But the fragment must remain secondary. It is about participial evidence in a different investigative context, not about the live row target. Row 2294 should not be rewritten as if it were a participle row or a prefixed-verb row merely because `awunden` is philologically relevant nearby.

## Superseded or diagnostic material

- The early `*winþan-` / `*đ (?)` table entry is superseded and should remain subordinate to the later 2026 `*nd`-cluster audit and decision blocks [Germanic/docs/DEV_NOTES.md:7228-7233,7538-7556,7879-7882].
- The `awunden` / `awindan` material is useful only as family-level background. It supports the ordinary strong-verb paradigm but does not alter `COUNTERPART = windan` for this row [Germanic/docs/DEV_NOTES.md:25605-25616; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:9468-9473].
- Search hits for the noun `wind` are not row evidence. Kroonen's noun `*winda- m. 'wind'` and verb `*windan- 'to wind'` are separate entries and must stay separate in later row notes [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:1240-1242,29733-29736; @Kroonen2013].
- The `widuwe-u-preservation` dossier is supportive but indirect. It is good negative evidence that `windan` does **not** show `wu-`, yet it remains a shared rule-scope dossier rather than a row-2294 file [Germanic/docs/dossiers/widuwe-u-preservation.md:1117-1126].

## Open questions for later work

- If a final report is ever drafted, keep the lexical disambiguation explicit at the start: this row is the verb `windan`, not the noun `wind`, and not a participial cell. That distinction is already justified by the TSV note, Kroonen's separate entries, and the principal-part evidence from Seebold [Germanic/data/germanic-aligned-final.tsv:2294-2294; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:1240-1242,29733-29736; docs/references/seebold_vergleichendes_woerterbuch.txt:47224-47225].
- If later documentation wants a compact paradigm note, the safest attachable forms are the standard principal parts `windan, wand, wundon, wunden`; these are directly relevant background but should remain clearly secondary to the infinitive row itself [docs/references/seebold_vergleichendes_woerterbuch.txt:47224-47225; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:50289-50289].
- If `index.tsv` is ever revisited, this row now looks indexable from current DEV_NOTES material. The strongest anchors are the March 2026 `*nd`-cluster audit / decision block (`7538-7556`, `7879-7882`) and the later `wi -> wu` guardrail passages (`43598-43624`), all of which are current and row-explicit enough to support indexing [Germanic/docs/DEV_NOTES.md:7538-7556,7879-7882,43598-43624].
