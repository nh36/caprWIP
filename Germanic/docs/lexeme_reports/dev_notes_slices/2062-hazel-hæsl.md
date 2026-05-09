---
row_id: 2062
concept: hazel
counterpart: hæsl
proto: *xáslaz
protoform: *xáslaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2062 hazel / hæsl

## Current row state

- CONCEPT: `hazel`
- COUNTERPART: `hæsl`
- PROTO: `*xáslaz`
- PROTOFORM: `*xáslaz`
- DERIVATION_CLASS: `regular`
- Live TSV row is bare and regular: row 2062 keeps `PROTO = *xáslaz`, `PROTOFORM = *xáslaz`, `COUNTERPART = hæsl`, and no explanatory NOTE beyond inherited-source placeholders. There is no paradigm-cell substitution here; the comparative proto headword and the active FST input are the same form [Germanic/data/germanic-aligned-final.tsv:513-513].
- Coverage infrastructure is still empty for this row: `coverage_audit.md` lists row 2062 as `regular | no | - | - | - | none`, so this slice is being written without an existing packet, memo, or manifest-backed report to inherit from [Germanic/docs/lexeme_reports/coverage_audit.md:269-269].
- The current published derivation already lands on the live target with no repair logic: `*xáslaz` loses final `-z`, then final bare `-a`, undergoes Anglo-Frisian brightening to `*xæsl`, then OE velar-fricative palatalization to `*çæsl`, and surfaces orthographically as `hæsl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2137-2157; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6218-6271].
- Lexicographic background is mixed in exactly the way the DEV_NOTES class note implies. Bosworth-Toller keeps the entry under `hæsel` but records unbroken forms in the addendum — `"[H]aesil, haesl auellanus"` and `"Haesil, haes corylus"` — while Clark Hall gives `hæsel m. 'hazel' shrub` and immediately cross-references `hæsl=hæsel` [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:80430-80434; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20154-20162]. That is consistent with a row whose target is the unbroken form `hæsl` even though normalized dictionary presentation may also use `hæsel`.

## Development-note summary

No lexeme-specific `hazel` / `hæsl` DEV_NOTES block survives as an isolated dossier. The usable authority is instead a **shared-background-only** note at `§17.18` on OE parasitic vowels in final `-Cl/-Cn/-Cm#`, and that note explicitly includes row 2062 in its tables and later policy statements [Germanic/docs/DEV_NOTES.md:29881-29946,30067-30083].

That shared note is nevertheless strong enough to govern this row. Its current position is that `hæsl` belongs to the retained set of **unbroken nominative singular** targets: the current TSV/FST table lists `*xáslaz | hæsl | hæsl | ✓`, the attestation table says unbroken `hæsl` is attested ("mostly compounds") while broken forms also occur in late West Saxon/place-name material, and the later decision section says the dataset deliberately keeps these unbroken spellings where they are genuinely attested in earlier/poetic/Anglian usage [Germanic/docs/DEV_NOTES.md:29887-29915,29937-29946,30069-30083].

The conservative reading for row 2062 is therefore: `PROTO` and `PROTOFORM` stay `*xáslaz`; the live OE target remains `hæsl`; support is **shared-background-only but current**, not lexeme-local; and broken `hæsel` plus oblique `hæsles` belong in the record as considered comparators/related forms, not as the active row target [Germanic/docs/DEV_NOTES.md:29914-29915,29943-30000,30017-30030,30075-30083].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:29881-29946

- Source heading: `§17.18.2 Current TSV state (11 candidate words)` + `§17.18.3 Attestation findings`
- Source line hint: `lines 29881-29946`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `parasiting`; `-Cl-final`; `shared_class_policy`; `attestation_mix`; `row_target_retained`
- Recommended next use: `cite as the main current shared authority for why row 2062 remains hæsl`
- Shared-with rows if relevant: `the other retained unbroken -Cl/-Cn/-Cm# rows (bōsm, botm, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn)`

This fragment is **shared-background-only**, not a hazel-only note, but it is the main surviving DEV_NOTES authority because it explicitly names the row in both the implementation and attestation tables. First, the current-TSV table records `| 4 | *xáslaz | hæsl | hæsl | ✓ |`, so the row is not a live mismatch and not a speculative reconstruction patch [Germanic/docs/DEV_NOTES.md:29887-29903]. Second, the attestation table gives the row-specific summary `| 4 | hæsl | ✅ (mostly compounds) | ✅ (LWS, place-names) | **hæsl** (BT) / *hæsel* (CH) |`, which is the clearest project-level statement of how the unbroken and broken spellings coexist for this lexeme [Germanic/docs/DEV_NOTES.md:29909-29915].

The surrounding “Critical findings” text matters just as much as the table. DEV_NOTES says, for this whole class, that “The broken NomSg is the late-WS prose norm” while “the unbroken NomSg is preserved as a poetic / earlier-prose variant,” and it separately says the oblique stem is uniformly unbroken across the set, explicitly including `hæsles` [Germanic/docs/DEV_NOTES.md:29937-29946]. For row 2062 that means the support is not “hazel uniquely demands `hæsl`,” but rather “hazel belongs to a class where the project intentionally accepts the older/unbroken nominative when it is actually attested.” That is current support, but it is class-level rather than lexeme-local.

### Germanic/docs/DEV_NOTES.md:30067-30083

- Source heading: `§17.18.7.1 Resolved policy`
- Source line hint: `lines 30067-30083`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `final_policy`; `retained_unbroken_targets`; `register_choice`; `thistle_exception_only`
- Recommended next use: `cite when explaining why hæsl was not moved to hæsel or hæsles`
- Shared-with rows if relevant: `same retained set as above; only þistel was moved away from NomSg`

This is the decisive later policy fragment. DEV_NOTES preserves the user ruling, `“If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them. Move ONLY thistle to another paradigm cell which is lautgesetzlich and attested.”`, and then applies that ruling to the whole retained set [Germanic/docs/DEV_NOTES.md:30069-30073]. The note immediately names `hæsl` inside “the dataset's existing unbroken NomSg targets (#2–#11: *bōsm, botm, hæsl, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn*)” and says these are “all directly attested manuscript spellings” that should be “retained unchanged” [Germanic/docs/DEV_NOTES.md:30075-30080].

For row 2062 this fragment is stronger than the earlier option tables because it is the settled policy rather than an exploratory recommendation. It also states that the FST's current behavior — “no parasiting in `-Cl/Cn/Cm#`” except the separate `-gl#` handling — “is correct for these ten lemmas,” since the dataset has chosen an early / poetic / Anglian register for them [Germanic/docs/DEV_NOTES.md:30080-30083]. So for `hæsl`, the absence of a parasitic vowel is not missing implementation; it is the intended output for the retained target register.

## Superseded or diagnostic material

- The option tables earlier in `§17.18` explicitly considered two alternatives that would have changed the hazel row away from the live target: Option 2 would have relemmatized the class to broken nominatives including `hæsel`, and Option 3 would have retargeted the class to oblique forms including `hæsles` [Germanic/docs/DEV_NOTES.md:29959-30000]. Those forms are therefore **superseded as live targets for row 2062**, but still useful diagnostically because they show that both the broken simplex and the unbroken oblique were seriously considered before the later retention policy won out.
- `§17.18.5` briefly recommends the paradigm-cell / GenSg strategy as the “lautgesetzlich-cleanest solution” for the whole class [Germanic/docs/DEV_NOTES.md:30015-30030]. For row 2062 that recommendation is **superseded** by the later `§17.18.7.1` decision to keep attested unbroken nominatives such as `hæsl` unchanged; do not quote the recommendation as current policy without also carrying forward the later override [Germanic/docs/DEV_NOTES.md:30067-30083].
- The current trace reports are **diagnostic rather than argumentative**. Their value is to confirm present implementation state — `*xáslaz -> hæsl` with no parasitic-vowel step — not to establish the philological policy that selected `hæsl` in the first place [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2137-2157; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6218-6271].
- The lexica are likewise **diagnostic support**, not superseding row policy. Bosworth-Toller and Clark Hall show the coexistence of `hæsel` and `hæsl`, but the project-level choice of which attested register to target for row 2062 comes from the shared DEV_NOTES class decision, not from any single dictionary line in isolation [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:80430-80434; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20154-20162; Germanic/docs/DEV_NOTES.md:30075-30083].

## Open questions for later work

- If later report prose needs a sharper statement about attestation, verify how much of the unbroken evidence for `hæsl` is simplex manuscript usage versus compounds/local names. The current DEV_NOTES table is explicit but compressed: unbroken `hæsl` is attested “mostly compounds,” while broken forms are also attested in “LWS, place-names” [Germanic/docs/DEV_NOTES.md:29914-29915].
- If the class-level `§17.18` material is ever split into row-local reports, decide whether row 2062 merits its own packet/memo or should continue to rely on shared-class policy plus live trace state. Right now the evidence bundle is enough for a conservative slice, but it is still shared-background-only rather than a dedicated hazel dossier [Germanic/docs/lexeme_reports/coverage_audit.md:269-269; Germanic/docs/DEV_NOTES.md:29881-29946].
- If a future editorial pass prefers dictionary-normalized headwords over retained early/poetic/Anglian targets, row 2062 would need an explicit policy decision rather than silent normalization, because the superseded alternatives `hæsel` and `hæsles` are both already documented in DEV_NOTES as rejected possibilities [Germanic/docs/DEV_NOTES.md:29959-30030,30067-30083].
