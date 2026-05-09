---
row_id: 1948
concept: bid
counterpart: -
proto: *bídjaną
protoform: *bídjaną
derivation_class: ""
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 1948 bid / - (repo-local OE bid)

## Current row state

- The live OE row currently reads `CONCEPT = bid`, `COUNTERPART = -`, `PROTO = *bídjaną`, `PROTOFORM = *bídjaną`, with both `NOTE` and `DERIVATION_CLASS` blank; only the duplicated Wiktionary-derivation provenance survives in `HISTORY` [Germanic/data/germanic-aligned-final.tsv:63-63].
- Repo-local OE source data nevertheless preserves a specific intended OE form. `Germanic/data/old_english_wiktionary.tsv` gives `bid\t-\tder\ttemplate:der\tbid`, so the repo clearly remembers `bid` as the OE-side form associated with this row even though the live aligned row still keeps `COUNTERPART = -` [Germanic/data/old_english_wiktionary.tsv:16-16].
- On that basis, this slice uses the filename stem `bid` while keeping metadata distinctions honest: the filename reflects the repo-local intended OE stem, but the YAML metadata still records the live counterpart field as `-` [Germanic/data/germanic-aligned-final.tsv:63-63; Germanic/data/old_english_wiktionary.tsv:16-16].
- The attachable DEV_NOTES hit uses older March-2026 notation `*bidjăną` rather than the live row spelling `*bídjaną`. For present purposes that difference should be treated as a notation-layer mismatch inside the repo, not as evidence for a different lexeme or a different OE target, because the DEV_NOTES discussion is about Class I weak-verb stem weight and `-jăną` versus `-ijăną`, not about changing the row's lexical identity [Germanic/docs/DEV_NOTES.md:8991-9024; Germanic/data/germanic-aligned-final.tsv:63-63].
- No row-specific packet, research memo, or attached dossier/analysis file matching row `1948` or the OE stem `bid` was found during row-local repo inspection, so the link fields remain blank.

## Development-note summary

DEV_NOTES support for row `1948` is thin and narrowly scoped. No row-dedicated lexeme note for `bid`, `*bídjaną`, or the dashed OE counterpart survives in `Germanic/docs/DEV_NOTES.md`. The materially relevant in-repo discussion is instead the shared Sievers'-Law cleanup for Class I weak verbs, where the project decided which verbs should keep plain `-jăną` and which should be rewritten to heavy-stem `-ijăną` notation [Germanic/docs/DEV_NOTES.md:8989-9024,9035-9044].

That shared note is still important, because it is the only current DEV_NOTES passage that names this lexeme directly. DEV_NOTES states the criterion explicitly: “A heavy-stem Class I weak verb should have `-ijăną` (Sievers' Law),” then defines light stems as those with short vowel plus single consonant `(VC)` and lists `*bidjăną` under “Light-stem verbs (keep `-jăną`)” as `bid- (CVC) | light | ✓ correct` [Germanic/docs/DEV_NOTES.md:8991-8995,9020-9024]. The substance to preserve is therefore not a special phonological rescue for this row, but the opposite: as far as DEV_NOTES currently shows, the proto-side notation for this lexeme was reviewed and left unchanged because the stem was judged light. The older DEV_NOTES spelling `*bidjăną` versus live-row `*bídjaną` should be read as a notation mismatch, not as a competing row policy [Germanic/docs/DEV_NOTES.md:9020-9024; Germanic/data/germanic-aligned-final.tsv:63-63].

The later decision lines make that scope even clearer. DEV_NOTES says that “All heavy-stem Class I weak verbs have been updated to use `-ijăną` notation” and gives rationale framed entirely in terms of etymological correctness, PGmc input notation, and the existing `SieversLawSyncope` handling [Germanic/docs/DEV_NOTES.md:9035-9044]. For row `1948`, the implication is indirect but material: `*bídjaną` belongs to the class of items that were *not* supposed to move into `-ijăną`, so the surviving project note supports the current proto spelling but says nothing positive about why the OE side is still dashed.

That gap has to be stated plainly. The live row still does not adopt `bid` in `COUNTERPART`, and DEV_NOTES does not preserve any attachable explanation of whether that dash reflects unattestation policy, incomplete OE row migration, or a still-open derivational problem [Germanic/data/germanic-aligned-final.tsv:63-63; Germanic/docs/DEV_NOTES.md:8989-9024]. The row-local Wiktionary source file preserves `bid`, but the main aligned TSV does not; current replacement-note prose should therefore preserve the distinction rather than silently upgrading the repo-local OE form into settled row policy [Germanic/data/old_english_wiktionary.tsv:16-16; Germanic/data/germanic-aligned-final.tsv:63-63].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-8989-9024

- Source heading: `Analysis: Which Forms Are Etymologically Correct?`
- Source line or section hint: `lines 8989-9024`
- Fragment type: `shared_rule_discussion_with_row_explicit_hit`
- Status: `current`
- Issue tags: `Sievers_law`; `class_i_weak_verbs`; `light_stem`; `proto_notation`
- Recommended next use: `cite_if_explaining_why_proto_stays_jana`
- Shared with row IDs: other light-stem Class I weak verbs kept in `-jăną`

This is the core surviving DEV_NOTES support for row `1948`. DEV_NOTES first states the operative criterion — “A heavy-stem Class I weak verb should have `-ijăną` (Sievers' Law)” — and then defines the light/heavy distinction by stem weight, including “Short vowel + single consonant (VC) = light” [Germanic/docs/DEV_NOTES.md:8991-8995]. The lexeme then appears by name in the light-stem table: `*bidjăną | bid- (CVC) | light | ✓ correct` [Germanic/docs/DEV_NOTES.md:9020-9024].

For this slice, the fragment should be read narrowly but firmly. It preserves an explicit in-repo claim that the proto notation for this lexeme was reviewed and judged already correct as a light stem. It does **not** preserve any claim that the dashed OE counterpart is correct, any note on attestation, or any row-specific derivation from `*bídjaną` to OE `bid`.

### DEV_NOTES:line-9035-9044

- Source heading: `Decision: Update All Heavy-Stem Forms — COMPLETED`
- Source line or section hint: `lines 9035-9044`
- Fragment type: `shared_policy_followup`
- Status: `current`
- Issue tags: `notation_policy`; `heavy_stem_scope`; `SieversLawSyncope`
- Recommended next use: `use_as_shared_scope_control`
- Shared with row IDs: all Class I weak-verb rows reviewed in the March 2026 Sievers'-Law pass

This fragment is not lexeme-specific, but it explains why the preceding `*bidjăną` classification matters. DEV_NOTES says that “All heavy-stem Class I weak verbs have been updated to use `-ijăną` notation” and justifies that update by reference to Ringe–Taylor, Fulk, PGmc input notation, and the fact that `SieversLawSyncope` already handles the heavy-stem cases correctly [Germanic/docs/DEV_NOTES.md:9035-9044].

For row `1948`, the force of the fragment is supervisory rather than derivational. It shows that the March 2026 pass was about correcting *heavy-stem* notation, which is exactly why `*bidjăną` stayed outside the update. In other words, DEV_NOTES preserves a reason to leave the proto spelling alone, but still leaves the OE-side dash unexplained.

## Superseded or diagnostic material

- Current sandbox diagnostics should be kept, if at all, as diagnostic only. `old_english_sandbox_results_current.json` still shows the live-style OE row as `concept: "bid"`, `proto: "*bidjăną"`, `counterpart: "-"`, `outputs: []` [Germanic/tmp/old_english_sandbox_results_current.json:114-118]. That is evidence of present pipeline difficulty, not DEV_NOTES authority.
- The stage-trace JSON is even more obviously diagnostic. In the staged sandbox pass, the row begins from `*b*i*d*j*ă*n*ą`, then unexpectedly shows `ConsonantRules` output `*b*ind*ă*n*ą`, and later hits a `+?` placeholder at `ProtoRhoticFronting` before continuing the dump [Germanic/tmp/old_english_sandbox_results_with_stages.json:2139-2197]. This is useful for later debugging because it suggests the row is not simply a documentation placeholder; however, it is not a reviewed development note and should not be treated as settled explanation.
- The most important documentary caution is still the row-state split itself. Repo-local OE source data preserves `bid`, but the live aligned row keeps `COUNTERPART = -` and blank `DERIVATION_CLASS` [Germanic/data/old_english_wiktionary.tsv:16-16; Germanic/data/germanic-aligned-final.tsv:63-63]. Until a row-specific memo exists, later writers should not flatten that distinction away.

## Open questions for later work

- Decide whether row `1948` should continue to keep `COUNTERPART = -` or whether repo-local OE `bid` is strong enough to be promoted into the aligned row as an explicit intended/reconstructed target.
- Audit the current OE pipeline failure for `*bídjaną`, especially the diagnostic shift to `*bind-` and the empty-output result in the sandbox traces, to determine whether the dash is masking an unresolved derivational bug rather than a deliberate attestation policy [Germanic/tmp/old_english_sandbox_results_current.json:114-118; Germanic/tmp/old_english_sandbox_results_with_stages.json:2139-2197].
- If a later report or index proposal is prepared, it should probably wait for a row-specific memo or literature-backed note. On present evidence this slice is useful as a replacement working note, but the surviving DEV_NOTES support is too thin and too shared to be confidently index-worthy.
