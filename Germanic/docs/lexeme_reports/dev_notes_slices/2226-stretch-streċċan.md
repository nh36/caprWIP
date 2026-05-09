---
row_id: 2226
concept: stretch
counterpart: streċċan
proto: *strákkijaną
protoform: *strákkijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2226 stretch / streċċan

## Current row state

- The live OE row is `2226`, `CONCEPT stretch`, `COUNTERPART streċċan`, `PROTO *strákkijaną`, `PROTOFORM *strákkijaną`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1149-1149].
- `PROTO` and `PROTOFORM` are currently identical in the live TSV; neither should be collapsed into the OE `COUNTERPART`. For this row, the comparator/input side is `*strákkijaną`, while the OE target side is `streċċan` [Germanic/data/germanic-aligned-final.tsv:1149-1149].
- `oe_known_problems.tsv` has no row-local entry for row `2226`, for `streċċan`, or for `*strákkijaną`; the current file lists unrelated exception and wontfix items only [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows row `2226` as `regular`, with no linked packet, research memo, or dossier and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:378-378].

## Detailed development-note summary

The surviving DEV_NOTES material for row `2226` is not a high-level etymology memo but a fairly concrete implementation-history note about a hidden overgeneration bug. The live row itself is straightforward: `PROTO = PROTOFORM = *strákkijaną`, `COUNTERPART = streċċan`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1149-1149]. The important project-history point is that DEV_NOTES once documented an apparent mismatch `*strákkijaną → strecċan`, where the FST allowed orthographic `cċ` instead of the expected `ċċ` [Germanic/docs/DEV_NOTES.md:37983-38083]. That bad output was never a rival OE target; it was an artefactual branch created inside `OEVelarPalatalization`.

DEV_NOTES is explicit that the lexical target remained `streċċan` throughout. The row note opens: “**Mismatch.** FST `*strákkijaną → strecċan` vs. attested `streċċan`,” and immediately frames the problem as one of palatalization of geminate `*kk` before `*j`, not one of lexical identity or target selection [Germanic/docs/DEV_NOTES.md:37985-37999]. The same fragment says standard reference forms have `ċċ`, not `cċ`, and it groups `streċċan` with synthetic class-III weak-verb comparators such as `lyċċan`, `weċċan`, `þeċċan`, and `leċċan` [Germanic/docs/DEV_NOTES.md:37987-37999; @BosworthToller1898; @ClarkHall1960]. That matters for later work: row `2226` is not a special lexical exception but a representative of a wider `*kk + *j` palatalization environment.

The most useful surviving project conclusion is the diagnosis of why the false branch existed. DEV_NOTES records that the cascade already contained the intended geminate clause

> ` {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j} ` [Germanic/docs/DEV_NOTES.md:38005-38007]

but that the same replacement block also still contained the singleton rule

> ` {*k} -> {*ʧ} || _ {*j} ` [Germanic/docs/DEV_NOTES.md:38013-38015]

so `*strákkijaną` admitted two analyses: one in which only the second `*k` palatalized and one in which the whole geminate did [Germanic/docs/DEV_NOTES.md:38017-38030]. That is the key row-specific development-note content worth preserving. The old bad output `strecċan` therefore reflects overlap between geminate and singleton `*k`-before-`*j` clauses, not missing palatalization altogether.

The same DEV_NOTES fragment also preserves the practical row verdict that later report writers would otherwise have to reconstruct from scratch. The mismatch report had already counted the row as solved because the good output `streċċan` survived among the candidates, but the bad output also still reached the surface; the real issue was hidden nondeterminism rather than a visible final-row mismatch [Germanic/docs/DEV_NOTES.md:38024-38030]. DEV_NOTES accordingly proposes a deterministic ordering fix: apply `*kk -> *ʧʧ || _ *j` before `*k -> *ʧ || _ *j`, and mirror the same ordering on the `*g` side as a preventive symmetry fix [Germanic/docs/DEV_NOTES.md:38034-38047]. For row `2226`, the important preserved conclusion is contrastive and explicit: regular target `streċċan`; superseded artefactual branch `strecċan`.

Two shared DEV_NOTES passages remain useful around that core note. First, the old heavy-stem table lists `streċċan` under the earlier post-Sievers-leveling notation `*strakkjăną`, which is now superseded but still explains why older notes may spell the comparator differently [Germanic/docs/DEV_NOTES.md:8731-8738]. Second, the later handbook digest on palatalization quotes Campbell's statement that an umlauted vowel may still be followed by a palatal consonant “even if a back vowel followed,” with `streċċan` named among the examples [Germanic/docs/DEV_NOTES.md:43229-43243; @Campbell1959, §429]. That shared source-context fragment is valuable because it confirms that `streċċan` with palatal `ċċ` is ordinary handbook phonology, not a project-internal normalization.

Taken together, the row should currently be read conservatively. The slice preserves a useful, explicit explanation of a now-resolved hidden overgeneration problem and of the shared handbook context for `streċċan`, but the support is still mostly one implementation-history note plus one shared phonological digest, not a full lexeme dossier. That is enough for a replacement working note and enough to keep `PROTO`, `PROTOFORM`, and `COUNTERPART` distinct, but probably not enough yet to justify indexing the row as if it carried a rich independent packet.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-37983-38083

- Source heading: `*strákkijaną / streċċan (row 2226): *kk geminate palatalization before *j`
- Source line or section hint: `lines 37983-38083`
- Fragment type: `row_specific_diagnostic_and_fix_note`
- Status: `current`
- Issue tags: `oe_velar_palatalization`; `geminate_kk_before_j`; `hidden_overgeneration`; `determinism_fix`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-local DEV_NOTES fragment. It identifies the exact contrast that matters for the slice: attested OE `streċċan` versus bad FST branch `strecċan` [Germanic/docs/DEV_NOTES.md:37985-37999]. It also preserves the most important implementation insight: the problem was not absence of a geminate rule, but overlap between the geminate rule and the singleton `*k / _ *j` rule in the same block [Germanic/docs/DEV_NOTES.md:38001-38030].

> `The mismatch report treated the row as solved because the good output (`streċċan`) was among the final candidates, but the bad output (`strecċan`) still survived all the way to OldEnglishSurface.` [Germanic/docs/DEV_NOTES.md:38024-38026]

> `So the real bug is not "missing geminate clause" but overlap between the geminate and singleton *k-before-*j clauses inside the same palatalization block.` [Germanic/docs/DEV_NOTES.md:38028-38030]

For later row work, this fragment should be used to preserve the contrastive formula plainly: live row comparator/input `*strákkijaną`; attested OE target `streċċan`; superseded implementation artefact `strecċan`. Its proposed fix also matters historically because it shows the row as the only live OE TSV exposure of the `*kk + *j` nondeterminism, while noting the same ordering risk on the `*g` side [Germanic/docs/DEV_NOTES.md:38034-38058; @RingeTaylor2014, §3.2.2].

### DEV_NOTES:line-43229-43252

- Source heading: `handbook digest on medial and preconsonantal palatalization`
- Source line or section hint: `lines 43229-43252`
- Fragment type: `shared_handbook_context_for_lexeme`
- Status: `current`
- Issue tags: `campbell_palatalization`; `umlaut_override`; `shared_sound_change_context`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This shared fragment is useful because it preserves a direct handbook quotation in which `streċċan` itself appears as an example. DEV_NOTES summarizes Campbell's palatalization discussion and then quotes the crucial override explicitly:

> `an umlauted vowel is followed by a palatal consonant, even if a back vowel followed, e.g. fēġan, drenċan, streċċan, liċġan.` [Germanic/docs/DEV_NOTES.md:43241-43243; @Campbell1959, §429]

For row `2226`, that quotation is more valuable than a bare paraphrase. It shows that palatal `ċċ` in `streċċan` belongs to ordinary OE descriptive phonology as presented in Campbell, not to a one-off project preference [@Campbell1959, §429]. DEV_NOTES also places the row in a wider rule discussion alongside Ringe & Taylor's summary of preconsonantal and word-final palatalization constraints [Germanic/docs/DEV_NOTES.md:43245-43252; @RingeTaylor2014, §6.4.1].

### DEV_NOTES:line-10425-10425

- Source heading: `Mismatch Progress Log (2026-04-26)`
- Source line or section hint: `line 10425`
- Fragment type: `project_chronology_log_entry`
- Status: `diagnostic_only`
- Issue tags: `mismatch_log`; `project_history`; `row_2226`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This single-line log entry — `streċċan: OEVelarPalatalization *kk before *j (§17.34)` — is useful only as chronology [Germanic/docs/DEV_NOTES.md:10425-10425]. It shows when row `2226` entered the mismatch work queue, but it adds no independent lexical or philological evidence beyond pointing forward to the fuller note.

## Superseded or diagnostic material

- The old heavy-stem table entry

  > `| *strakkjăną | CVCC (heavy) | -jăną | streċċan |` [Germanic/docs/DEV_NOTES.md:8731-8731]

  belongs to the earlier post-Sievers-leveling notation policy and should now be treated as superseded shared notation history, not as the live row header [Germanic/docs/DEV_NOTES.md:8731-8738]. For current row work, the live TSV remains authoritative: `PROTO = PROTOFORM = *strákkijaną`, not `*strakkjăną` [Germanic/data/germanic-aligned-final.tsv:1149-1149].
- The mismatch-log line at `DEV_NOTES:line-10425-10425` is useful only to date the investigation. It should not be indexed or cited as if it were substantive row analysis [Germanic/docs/DEV_NOTES.md:10425-10425].
- The central §17.34 note is current as project history, but even there the bad form `strecċan` is diagnostic only. It is an overgenerated branch that DEV_NOTES explicitly aims to eliminate; it is not a competing OE counterpart and should never be allowed to blur the row's current `COUNTERPART streċċan` [Germanic/docs/DEV_NOTES.md:38024-38030].

## Open questions for later work

- If a later final report is written, decide whether to quote only Campbell's `streċċan` example or also to add direct dictionary quotations for `streċċan`, `lyċċan`, `weċċan`, and `þeċċan`, since DEV_NOTES currently names those comparators but does not preserve their full dictionary wording [Germanic/docs/DEV_NOTES.md:37987-37999,43229-43243; @Campbell1959, §429; @BosworthToller1898; @ClarkHall1960].
- If the row is ever indexed, keep the one-line summary strictly contrastive: live `PROTO/PROTOFORM *strákkijaną`, live `COUNTERPART streċċan`, superseded artefactual branch `strecċan`, underlying issue `*kk + *j` palatalization overlap [Germanic/data/germanic-aligned-final.tsv:1149-1149; Germanic/docs/DEV_NOTES.md:37983-38083].
- The surviving support is still thin outside §17.34 itself. If later work wants this row to become confidently indexable, the missing ingredient is not another shared sound-change digest but a genuinely row-specific packet or memo that preserves direct lexicographic support for `streċċan` and the parallel `*kk + *j` verb class.
