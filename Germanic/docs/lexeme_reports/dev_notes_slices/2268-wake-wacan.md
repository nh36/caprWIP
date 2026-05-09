---
row_id: 2268
concept: wake
counterpart: wacan
proto: *wakēną
protoform: *wákaną
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2268-wake-wacan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2268-wake-wacan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md
current_status: current
needs_literature_agent: no
filename_basis: canonical_row_based_filename
---

# DEV_NOTES material — 2268 wake / wacan

## Current row state

- The live TSV row is already a split-lexeme row. In the actual TSV field layout, `PROTOFORM = *wákaną` (column 3), `COUNTERPART = wacan`, `DERIVATION_CLASS = early_analogy`, `CONCEPT = wake`, and the final `PROTO` column remains `*wakēną`; the live note explicitly says that OE `wacan` is the strong Class VI verb and that weak `*wakēną` belongs instead with OE `wacian` [Germanic/data/germanic-aligned-final.tsv:1-1,1311-1311].
- The derivation trace matches that OE-facing choice exactly. The published trace gives `PROTO: *wákaną`, `EXPECTED: wacan`, `OUTPUTS: wacan`, with `Anglo Frisian Brightening: *wækaną` followed by `OE A Restoration: *wakaną` before the normal tail rules [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6781-6800; @Campbell1959, §157].
- Row-local support files already exist and are worth retaining. The packet preserves the key DEV_NOTES hits and the compact `*wákaną -> wacan` derivation, while the research memo correctly foregrounds the strong/weak split and warns that Bosworth-Toller treats simplex `wacan` as a normalized headword rather than a directly cited infinitive [Germanic/docs/lexeme_reports/packets/2268-wake-wacan.md:15-18,48-128; Germanic/docs/lexeme_reports/research_memos/2268-wake-wacan.md:13-18,37-68].
- External lexical support is consistent but not flat. `old_english_wiktionary.tsv` gives the expected OE pairing `wake -> wacan`, Clark Hall separates `wacan` “to awake, arise, be born, originate” from `wacian` “to be awake, keep awake, watch,” and Kroonen's Proto-Germanic headword for the strong verb is `*wakan-`, not weak `*wakēn-` [Germanic/data/old_english_wiktionary.tsv:327-327; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46409-46418; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28826-28830; @ClarkHall1960; @Kroonen2013].
- No row-specific pilot file was found during slice preparation.

## Development-note summary

The surviving DEV_NOTES material for row 2268 is best read as a record of **lexeme disentanglement**, not as a simple sound-law repair. The core problem was that the cognate set for English *wake* had been allowed to carry weak Proto-Germanic `*wakēną` / `*wakē-` material straight into an Old English target that is actually the **strong Class VI** verb `wacan`. DEV_NOTES eventually states this plainly from Kroonen: “`*wakān-` s.v. (p.568): ‘Go. wakan s.v. "id.", OE wacan.’ This is a **strong verb** (Class VI), not weak at all. The proto `*wakēną` in the TSV is the wrong lexeme — it belongs to the Class III weak ‘to be awake, watch’ (→ OE `wacian`), not the strong ‘to wake up’ (→ `wacan`)” [Germanic/docs/DEV_NOTES.md:3891-3893; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28826-28830; @Kroonen2013].

That distinction now needs to be kept explicit in field terms. `PROTO` is the comparative/cognate-set label the row still shares with non-OE weak-verb continuations such as Dutch `waken` and German `wachen`; `PROTOFORM` is the OE-facing derivational input actually fed to the cascade; and `COUNTERPART` is the Old English lexeme the row intends to reach. For this row those three layers are **not interchangeable**: `PROTO = *wakēną` names the weak comparative set, `PROTOFORM = *wákaną` is the strong input that derives cleanly to OE `wacan`, and `COUNTERPART = wacan` is the OE strong-verb headword [Germanic/data/germanic-aligned-final.tsv:1310-1312; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6781-6800]. The row should therefore never be paraphrased as though `*wakēną`, `*wákaną`, `wacan`, and `wacian` were four spellings of one item.

The weak side of the split is also well documented and should remain visible in this slice because that is exactly where the row can be misread. Ringe-Taylor's class-III material gives the weak stative pathway: “`PGmce *wakai- ~ *wakja- (*waka-?) ‘be awake’ ... > ... OE (WS) wacian`,” with Northumbrian/Mercian relics such as `wecca(n)` / `weccan` before the verb is otherwise shifted into class II [docs/references/ringe_taylor_linguistic_history_vol2.txt:9447-9451; @RingeTaylor2014, §3.3.2]. Repo-local analysis files preserve the same weak pathway in project terms: `*wakōną -> *wækōjan -> wacian` and “`*wakōn` -> OE `wacian` ‘be awake’” [Germanic/docs/analysis/arestoration_r_l_research.md:337-343; Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:57-60]. Those are relevant here precisely because they support the **excluded** lexeme: they explain why weak `wacian` belongs nearby in discussion but not in the row's `COUNTERPART` field.

The strong OE target also needs one philological caution that DEV_NOTES only partly internalized. Bosworth-Toller says of simplex `wacan`: “This infinitive form does not occur, its place seems taken by `wæcnan`” [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:119992-119993]. That does **not** collapse the strong verb into the weak one; Clark Hall still lists `wacan`, along with strong-family material such as `āwacan`, `onwacan`, and preterite `wōc` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:4349-4351,31779-31780,46409-46418,49379-49379; @ClarkHall1960]. But it does mean the row's `COUNTERPART = wacan` should be understood conservatively as a normalized strong headword, not overclaimed as a directly quoted simplex infinitive. That caution is compatible with the live row, but it should stay attached to the documentation.

Finally, the current row state is more nuanced than one influential DEV_NOTES sentence suggests. DEV_NOTES line 3966 says, “The TSV proto `*wakēną` was wrong — corrected to `*wakaną`. Now matches” [Germanic/docs/DEV_NOTES.md:3965-3966]. As lexeme diagnosis, that is substantially right. As description of the **current** TSV fields, it is stale: the live solution is not to replace every row label with strong `*wakaną`, but to preserve the cognate-set `PROTO = *wakēną` while setting the OE-facing `PROTOFORM = *wákaną` and documenting the split in the note field [Germanic/data/germanic-aligned-final.tsv:1311-1311]. This slice should therefore preserve line 3965-3966 as part of the resolution history, but not treat its field wording as fully current metadata.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-3891-3893

- Source heading: `What Kroonen reconstructs`
- Source line or section hint: `lines 3891-3893`
- Status: `current_primary_lexeme_distinction`
- Issue tags: `strong_vs_weak_split`; `proto_selection`; `wacan_vs_wacian`
- Recommended next use: `primary_index_anchor`

This is the strongest surviving row-local DEV_NOTES anchor. It gives the essential quotation from Kroonen and spells out the lexical split in exactly the terms later work still needs: strong `*wakān-` / OE `wacan` versus weak `*wakēną` / OE `wacian` [Germanic/docs/DEV_NOTES.md:3891-3893; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28826-28830; @Kroonen2013]. The fragment is also stronger than the surrounding table at line 3873, because line 3873 still preserves the earlier mistaken setup that put row 2268 inside a weak-verb mismatch table with pipeline output `wacon` [Germanic/docs/DEV_NOTES.md:3866-3877]. For future work, line 3891-3893 should be treated as the philological core, while line 3873 remains diagnostic history only.

The key documentary value here is not merely that the row is “strong.” It is that DEV_NOTES explicitly names the **other** OE target (`wacian`) and says that the old TSV proto “belongs” there instead. That makes this fragment lexeme-addressable in a way many shared technical notes are not. If any DEV_NOTES anchor is strong enough to justify indexing, this is the first candidate.

### DEV_NOTES:line-3965-3966

- Source heading: `The individual verbs`
- Source line or section hint: `lines 3965-3966`
- Status: `current_core_with_stale_field_wording`
- Issue tags: `row_resolution`; `strong_class_vi`; `metadata_drift`
- Recommended next use: `cite_for_resolution_with_caveat`

This short row-specific resolution notice remains valuable because it marks the row as settled: “`wacan (ID 2268): RESOLVED. This was a strong verb (Class VI), not weak Class III`” [Germanic/docs/DEV_NOTES.md:3965-3965]. That sentence is still accurate and should be preserved. The immediately following sentence is only partly current: “The TSV proto `*wakēną` was wrong — corrected to `*wakaną`. Now matches” [Germanic/docs/DEV_NOTES.md:3966-3966]. The live row no longer expresses the solution exactly that way, since the present TSV keeps `PROTO = *wakēną` but moves the strong form into `PROTOFORM = *wákaną` [Germanic/data/germanic-aligned-final.tsv:1311-1311].

Accordingly, this fragment is best used as a **resolution summary with metadata caveat**. It confirms that the project rejected the old weak-verb reading, but a later writer should not quote it as though the present TSV simply replaced the weak form wholesale. The live state is more precise than that.

### DEV_NOTES:line-21729-21749

- Source heading: `§17.10.11 — Phase 1d (Role 1) research findings: breve is NOT an engineering tag; rescope`
- Source line or section hint: `lines 21729-21749`
- Status: `current_shared_technical_policy`
- Issue tags: `protoform_shape`; `a_restoration`; `class_vi_infinitives`
- Recommended next use: `secondary_index_anchor`
- Shared with row IDs: `1934`; `2046`; `2266`; `2272`; `2292`

This is not a `wake`-only note, but it is the strongest current explanation for why the live `PROTOFORM` must remain plain `*wákaną` rather than a breve-marked debugging surrogate. DEV_NOTES says the earlier migration assumption was “wrong,” then names the affected class explicitly: the current TSV keeps plain `a` because the Class VI infinitives, including `wákaną`, “rely on the plain `a` in the infinitival suffix to trigger OEARestoration” and the trigger set includes `{*a}` but not `{*ă}` [Germanic/docs/DEV_NOTES.md:21731-21749; @Campbell1959, §157].

For row 2268 this shared fragment matters because the live trace visibly depends on that policy: `*wækaną` is restored to `*wakaną` before the normal OE tail steps, producing exact `wacan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6790-6800]. The fragment should therefore be cited when the question is “why is the strong OE-facing input spelled `*wákaną` in the live row?” It is less useful for the strong/weak lexeme split itself.

### DEV_NOTES:line-9501-9511

- Source heading: `Empirical Validation (Dry Run 2026-03-13)`
- Source line or section hint: `lines 9501-9511`
- Status: `superseded_debugging_history`
- Issue tags: `wakăną_workaround`; `wæcen_bug`; `project_history`
- Recommended next use: `retain_only_as_superseded_history`
- Shared with row IDs: `1934`; `2046`; `2266`; `2272`; `2292`

This fragment preserves an important but superseded debugging phase. DEV_NOTES temporarily rewrote the strong verb as ``*wakaną` -> `*wakăną``` and then recorded the targeted success `wakăną -> wacan ✓ (was wæcen)` [Germanic/docs/DEV_NOTES.md:9501-9511]. That history explains why older packet material and trace discussion can look as though breve `ă` was the fix for `wake`.

It is no longer current row policy. The later §17.10.11 note explicitly restores plain `a` as the correct encoding for Class VI infinitives, including `wákaną` [Germanic/docs/DEV_NOTES.md:21729-21749]. For this row, the March `*wakăną` stage should be preserved only as implementation archaeology, not as lexical evidence.

## Superseded or diagnostic material

- The weak-verb mismatch table entry at `Germanic/docs/DEV_NOTES.md:3873-3877` is diagnostically useful because it shows exactly how row 2268 was once being misrouted (`*wakēną -> wacon`), but it is not current row policy. The lexical correction comes immediately afterward in lines 3891-3893.
- The terse resolution line at `Germanic/docs/DEV_NOTES.md:3965-3966` is half current and half stale: current in saying the row is strong Class VI, stale in implying that the live TSV simply replaced weak `PROTO` with strong `*wakaną`. The live row now keeps a field split instead [Germanic/docs/DEV_NOTES.md:3965-3966; Germanic/data/germanic-aligned-final.tsv:1311-1311].
- Bosworth-Toller's warning about simplex `wacan` should be retained as a philological caution, not as an argument to rewrite the row to weak `wacian`. The caution affects how strongly one claims direct infinitive attestation, not the strong-versus-weak lexeme identity [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:119992-120001].
- Shared weak-verb analysis for `wacian` is relevant background but must stay labeled as background. It clarifies what `PROTO = *wakēną` means in the comparative set, but it does not override the row's OE target [Germanic/docs/analysis/arestoration_r_l_research.md:337-343; Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:57-60; @RingeTaylor2014, §3.3.2].

## Open questions for later work

- If a final lexeme report is written, it should say explicitly that `COUNTERPART = wacan` is a normalized strong headword and should cite Bosworth-Toller's “This infinitive form does not occur” warning, so that future readers do not mistake the row for a claim about a directly quoted simplex infinitive [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:119992-119993].
- If indexing is reconsidered later, the safest anchors are still the lexeme-split note at `DEV_NOTES:line-3891-3893` and the row-resolution notice at `DEV_NOTES:line-3965-3966`, with `DEV_NOTES:line-21729-21749` available as shared technical support for the current `PROTOFORM` shape. The March `*wakăną` block should not be used as an index anchor.
- Future row prose should keep the nomenclature rigid: weak comparative `PROTO = *wakēną`; strong OE-facing `PROTOFORM = *wákaną`; OE strong headword `COUNTERPART = wacan`; excluded weak OE comparator `wacian`. This row becomes misleading very quickly if those labels are flattened.
