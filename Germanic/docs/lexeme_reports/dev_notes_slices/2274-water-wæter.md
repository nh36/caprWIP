---
row_id: 2274
concept: water
counterpart: wæter
proto: *wátną
protoform: *wátōr
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2274-water-wæter.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2274-water-wæter.md
linked_dossier_or_analysis_files: [Germanic/docs/analysis/unstressed_e_o_before_r.md, Germanic/docs/analysis/notable_findings.md, Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2274 water / wæter

## Current row state

- CONCEPT: `water`
- COUNTERPART: `wæter`
- PROTO: `*wátną`
- PROTOFORM: `*wátōr`
- DERIVATION_CLASS: `early_analogy`
- Live TSV storage order matters here. In `Germanic/data/germanic-aligned-final.tsv`, the third-column `PROTOFORM` is `*wátōr`, while the final `PROTO` column is `*wátną`; the row note then glosses the intended interpretation more precisely as `Kroonen *watar-/*watan- r/n-stem, nom.sg. *watōr; R/T §3.1.4 *ō→*a before final *r in PWGmc.` [Germanic/data/germanic-aligned-final.tsv:1335-1335].
- Existing row-specific support files are present and usable: a packet and a research memo both already isolate the water material, and both agree that the main issue is the heteroclitic r/n-stem morphology plus the need to distinguish generalized headword from derivational input [Germanic/docs/lexeme_reports/packets/2274-water-wæter.md:1-311; Germanic/docs/lexeme_reports/research_memos/2274-water-wæter.md:1-109].
- No pilot lexeme report was located for this row, and `coverage_audit.md` still treats row 2274 as a note-bearing `early_analogy` item awaiting slice/report treatment rather than as a completed indexed case [Germanic/docs/lexeme_reports/coverage_audit.md:163-163].
- No `oe_known_problems.tsv` ledger entry is attached to row 2274. In current repo practice that usually means the row is considered solved enough for normal derivation, even if its representation still compresses a more complicated paradigm than the one-line TSV schema can express.

## Development-note summary

Row 2274 is one of the clearest places where the project must keep **COUNTERPART**, **PROTOFORM**, and **PROTO** sharply distinct. `COUNTERPART = wæter` is the Old English target actually attested in repo-local lexical material and in the handbooks' paradigm tables [Germanic/data/germanic-aligned-final.tsv:1335-1335; docs/references/bright_anglo_saxon_reader.vision.txt:945-965,26975-26978]. `PROTOFORM = *wátōr` is the row's active derivational input, i.e. the nominative/accusative singular form that the FST can carry to `wæter` once the relevant PWGmc and OE rules are in place [Germanic/data/germanic-aligned-final.tsv:1335-1335; Germanic/docs/DEV_NOTES.md:3122-3147]. `PROTO = *wátną`, by contrast, is only the TSV's compressed lexeme-level label; it should not be mistaken for the best source-faithful citation form, because Kroonen does **not** present the lexeme as a simple one-shape n-stem lemma. He gives heteroclitic `*watar-~*watan-` and adds that “the Proto-Germanic material straightforwardly points to `*watōr, *watenaz`” [@Kroonen2013, p. 616; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29174-29185].

That distinction is why the current `early_analogy` label should be read cautiously. Nothing in the surviving DEV_NOTES suggests that OE `wæter` itself is a late analogical surface oddity. The phonological route from the selected singular input is explicitly treated as regular once the right prehistory is chosen. What is “early” and somewhat non-trivial is the row's reliance on a paradigmatically specific inherited form (`*wátōr`) rather than on the TSV's generalized shorthand (`*wátną`) [Germanic/docs/lexeme_reports/research_memos/2274-water-wæter.md:37-53,71-79]. This slice should therefore resist any wording that makes `wæter` sound like a target-side exception. The irregularity, such as it is, lies in representation and paradigm compression, not in the final OE output.

The strongest current DEV_NOTES authority is the dedicated water-fix section at lines 3120-3147. That section states the problem in exactly the terms still needed for future work: `PGmc *watōr (r/n-stem nom.sg.; Kroonen *watar-/*watan-) needed to produce OE wæter. Two issues:` first, PWGmc pre-final-`r` shortening/lowering; second, false A-restoration after Anglo-Frisian Brightening [Germanic/docs/DEV_NOTES.md:3120-3128]. DEV_NOTES preserves the decisive Ringe-Taylor quotation: `"Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a."` That is the rule that licenses `*watōr -> *watar` [Germanic/docs/DEV_NOTES.md:3125-3125; @RingeTaylor2014, §3.1.4]. The same section then records the implementation correction that made the row work for the right reason: unstressed `*æ` must **not** count as an A-restoration trigger, because the relevant trigger set is limited to genuine back vowels [Germanic/docs/DEV_NOTES.md:3129-3143; @RingeTaylor2014, §6.3.2].

Once those two points are kept together, the derivation is straightforward and should stay explicit in this slice: `*watōr -> *watar -> *wætær -> wæter` [Germanic/docs/DEV_NOTES.md:3146-3147]. DEV_NOTES itself labels the earlier false output `"water"` as an artefact of over-application, not as a genuine philological option for Old English `wæter` [Germanic/docs/DEV_NOTES.md:3127-3138]. The related analysis file `notable_findings.md` preserves the same lesson in a more reusable analytic form: when the FST fronted both vowels in `*watar` and then treated unstressed `*æ` as “underlyingly back,” it restored the stressed vowel and generated the wrong answer; the `*dagas -> dæges` comparator shows why that trigger logic is wrong [Germanic/docs/analysis/notable_findings.md:648-665].

The second surviving DEV_NOTES cluster worth preserving is the later comparison between inherited `*-ōr` and gen.sg. `*-ōz`. This material is partly shared, but it is still genuinely relevant to row 2274 because it answers a question that future report writers are likely to raise: why does inherited final `-r` survive in `wæter` when case endings in `*-ōz` lose their final consonant and end up as `-e`? DEV_NOTES now gives a clean answer: final `*-z` was lost before rhotacism, so inherited `*-r` and rhotacized `*-r < *-z` never merged [Germanic/docs/DEV_NOTES.md:3479-3495]. The trace table then puts `*watōr` and `*rastōz` side by side and shows that their shared vowel history is regular; only the final consonant history differs because the input phonemes differ [Germanic/docs/DEV_NOTES.md:3516-3527]. For this row, that matters because it removes an older worry that `wæter` needed some grammatically conditioned protection of final `-r`.

The older project history at lines 16608-16706 should also be kept, but only with a diagnostic label. That section preserves the evolution of the project's own row handling: `Original: *watną (n-stem) — didn't work; Changed to: *watrą (r-stem base) — worked via epenthesis; Current: *watōr (nominative singular) — works via *ō → *a rule` [Germanic/docs/DEV_NOTES.md:16615-16618]. This history is useful because it explains why older packets or mental models may still reach for `*watrą`, but DEV_NOTES is explicit that `*watrą` was a workaround route and that `*watōr` is “the etymologically correct reconstruction” for the row's active singular comparator [Germanic/docs/DEV_NOTES.md:16640-16648,16703-16706]. Future work should therefore preserve `*watrą` only as superseded project history, not as a coequal modern analysis.

Primary-source background outside DEV_NOTES supports the current row without needing to overclaim certainty. Kroonen's heteroclitic entry is the main morphological anchor: `*watar-~*watan- n. 'water' ... OE wæter` and the explicit remark that the material points to `*watōr, *watenaz` [@Kroonen2013, p. 616; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29174-29185]. Ringe and Taylor independently give `PGmc *wator nom.-acc. sg. 'water' ... > *watar ... > OE weeter, OF weter`, which matches the project's use of a singular `*watōr/*wator`-type input rather than a generalized `*watną` derivation [docs/references/ringe_taylor_linguistic_history_vol2.txt:4050-4052; @RingeTaylor2014, §3.1.4]. Their later paradigmatic and dialect material is also useful background: West Saxon `weeter` versus Mercian `weter`, and `*watar, *wataras, *wataré > OE weter, wetres, wetre — weeteres, weetere`, show that the row's `wæter` belongs to a real OE paradigm rather than to an isolated reconstructed form [docs/references/ringe_taylor_linguistic_history_vol2.txt:12619-12623,15333-15335]. Bright's paradigm table confirms the same lexical target inside the repo: `wæter, wæteres, wætere, wæter(-u), wætera, wæterum`, with explicit note that the medial vowel is retained after a short radical syllable as in `wæteres` [docs/references/bright_anglo_saxon_reader.vision.txt:945-969,26975-26978].

The practical upshot is conservative. This row now has a sound current DEV_NOTES argument, but it is narrower than a full lexeme dossier. The trustworthy claim is not that every aspect of Proto-Germanic `water` morphology has been encoded perfectly in the one-line TSV schema. The trustworthy claim is that the project has a stable and source-backed explanation for why the OE target should be derived from singular `*wátōr/*wator` and why that input yields `wæter` without special pleading. Any future full report should keep that exact scope: strong on the selected singular derivation, cautious about the inadequacy of one-form labels for an r/n-stem lexeme.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3120-3147

- Source heading: `Water fix: PWGmc ō-shortening and A-restoration correction (3a45a8b)`
- Source line or section hint: `lines 3120-3147`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `rn_stem`; `protoform_selection`; `pre_final_r_shortening`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core current anchor for the row and is strong enough to carry future index use if the row is ever indexed. DEV_NOTES names the lexeme directly, distinguishes the heteroclitic stem notation from the selected nominative singular, and states both technical failures that had to be fixed: missing `*ō -> *a` before final `*r`, and over-broad A-restoration [Germanic/docs/DEV_NOTES.md:3120-3143]. Its derivation line remains current and should be preserved nearly verbatim: `*watōr → (PWGmc ō-shortening) *watar → (AFB) *wætær → (A-restoration: NO trigger, *æ is not back) *wætær → (§6.9.6 unstressed merger) wæter` [Germanic/docs/DEV_NOTES.md:3146-3147]. The section is especially valuable because it preserves direct project wording that still matches the primary literature: the Ringe-Taylor rule about bimoric `ō` before word-final `r` and the `*dagas -> dæges` reasoning for the A-restoration trigger set [@RingeTaylor2014, §§3.1.4, 6.3.2].

### DEV_NOTES:line-3479-3527

- Source heading: `Why this resolves the exceptionlessness concern`; `Pipeline trace comparison: inherited *-ōr vs. gen.sg. *-ōz`
- Source line or section hint: `lines 3479-3527`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `final_r`; `z_loss`; `rhotacism`; `exceptionlessness`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2152; 2274`

This fragment is shared rather than purely row-local, but it is still a real support file for `wæter` because it directly uses `*watōr -> wæter` as the comparator against `*-ōz` material [Germanic/docs/DEV_NOTES.md:3481-3527]. Its main value is methodological: it blocks an easy but misleading objection that final `-r` survival in `wæter` must be protected by grammatical conditioning. DEV_NOTES now states instead that final `*-z` was deleted before rhotacism and therefore never merged with inherited `*-r`; the table `*watōr ... > wæter` versus `*rastōz ... > ræste` is meant to show exactly that [Germanic/docs/DEV_NOTES.md:3483-3495,3518-3527]. If a later report needs one concise explanation for why `wæter` is not an “exceptionless-phonology problem,” this is the best current project-language anchor after the main water-fix note.

### DEV_NOTES:line-16608-16706

- Source heading: `*watōr → wæter was already working before the rule was added?`
- Source line or section hint: `lines 16608-16706`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic`
- Issue tags: `project_history`; `watrą_workaround`; `epenthesis`; `correct_reconstruction`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This section is worth preserving because it records the row's own project-history chronology in one place, but it must stay carefully labeled. It distinguishes three stages of TSV handling — `*watną`, then workaround `*watrą`, then current `*watōr` — and explicitly contrasts the two routes to `wæter` [Germanic/docs/DEV_NOTES.md:16615-16634]. The fragment remains useful because it ends with the statement future writers most need: `*watōr` is the “etymologically correct reconstruction,” whereas the `*watrą` path depends on epenthesis and belongs to an earlier workaround phase [Germanic/docs/DEV_NOTES.md:16640-16648,16693-16706]. It is therefore good diagnostic support, but not the fragment to lead with when establishing the row's current analysis.

## Superseded or diagnostic material

- The older `*watrą` route should be preserved only as labeled project history. DEV_NOTES shows why it once seemed attractive — it could reach `wæter` through epenthesis — but it is no longer the row's preferred analysis now that the project explicitly models `*ō -> *a` before final `*r` and keeps `*watōr` as the active singular input [Germanic/docs/DEV_NOTES.md:16629-16634,16640-16648].
- The generalized `PROTO = *wátną` field is also somewhat diagnostic rather than philologically complete. Kroonen's actual entry is heteroclitic `*watar-~*watan-`, not a simple isolated `*watną` lemma, so later report writing should avoid treating the bare TSV `PROTO` as if it were already a full source-faithful reconstruction [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29174-29185].
- The packet's string-match hit in `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md` is not row evidence; it only happens to contain the word `wæter` inside an unrelated quotation [Germanic/docs/lexeme_reports/packets/2274-water-wæter.md:184-193]. It should not be promoted into the row's citation chain.
- Dialectal `weter/weeter` material is supporting background, not a reason to retarget the counterpart. Ringe-Taylor's tables and Bright's inflectional examples show that `wæter` belongs to a real OE paradigm while also reminding us that manuscript/dialect representation is not perfectly uniform [docs/references/ringe_taylor_linguistic_history_vol2.txt:12619-12623,15333-15335; docs/references/bright_anglo_saxon_reader.vision.txt:945-969].

## Open questions for later work

- If the TSV schema ever permits richer proto labels, replace bare `*wátną` with an explicit heteroclitic notation (`*watar-~*watan-`) or otherwise document more transparently that the row's actual singular derivational input is `*wátōr`, not a simple n-stem lemma.
- If a later final report is written, keep the role distinction explicit in one sentence near the top: `COUNTERPART` is attested OE `wæter`; `PROTOFORM` is the selected nom./acc.sg. `*wátōr`; `PROTO` is only the dataset's generalized lexeme label. This row becomes misleading very quickly when any two of those layers are collapsed.
- For indexing, the row now has one genuinely strong lexeme-local DEV_NOTES anchor (`line-3120-3147`) and one strong but shared supporting anchor (`line-3479-3527`). The older history note (`line-16608-16706`) is useful, but probably too diagnostic to serve as the main index hook by itself.
