---
row_id: 2135
concept: need
counterpart: nīed
proto: *náudiz
protoform: *náudiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2135 need / nīed

## Current row state

- CONCEPT: `need`
- COUNTERPART: `nīed`
- PROTO: `*náudiz`
- PROTOFORM: `*náudiz`
- DERIVATION_CLASS: `regular`
- Live TSV row: OE row 2135 currently stands as `*náudiz -> nīed`, with no special warning note beyond duplicated Wiktionary etymology sourcing; the surrounding Dutch, English, and German rows all keep the same comparative proto headword `*náudiz` for the cognate set [Germanic/data/germanic-aligned-final.tsv:794-796].
- `oe_known_problems.tsv`: no row-specific entry or exception bucket is present for this lexeme, so the row is not currently being managed as an open OE problem case [Germanic/data/oe_known_problems.tsv:1-8].
- No row-local packet or research memo currently exists at `Germanic/docs/lexeme_reports/packets/2135-need-nīed.md` or `Germanic/docs/lexeme_reports/research_memos/2135-need-nīed.md`.
- Repo-local handbook/reference extracts support the inherited lexeme and the expected OE development even though they vary in spelling practice: Orel gives `*naudiz sb.f.` with OE `nid`; Campbell cites `nied` as the regular West-Saxon umlauted outcome of PGmc `au`; Ringe-Taylor write the explicit chain `*naudi > *néadi > WS *niedi > nied`, with Anglian `néd` beside it; Clark Hall cross-references `nēad` and `nid` to `nied` and lists broad variant spellings `(ē, ea, éo, i, ỹ)` under the noun [docs/references/orel_handbook_germanic_etymology.vision.txt:31783-31790; docs/references/campbell_old_english_grammar.txt:5823-5827; docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29386-29387,29743-29745].

## Development-note summary

No dedicated row-2135 DEV_NOTES subsection survives, and no row-local packet or memo currently preserves a bespoke argument for this lexeme. This slice therefore has to function as a replacement working note built from three things only: the live TSV state, shared DEV_NOTES fragments that explicitly mention `nied/nīed`, and handbook-style reference extracts that confirm the ordinary historical development [Germanic/data/germanic-aligned-final.tsv:796-796; Germanic/docs/DEV_NOTES.md:716-723,35039-35048; docs/references/campbell_old_english_grammar.txt:5823-5827; docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243].

The secure current conclusion is conservative and simple: the live row is presently defensible as a **regular OE reflex** of the inherited need/necessity lexeme, not as a special rescue case. The project-level `PROTO` and `PROTOFORM` fields both remain `*náudiz`, i.e. the comparative cognate-set headword used across the Germanic rows, while the OE-facing handbook chain runs through a West-Germanic/early-OE stem in `*naudi > *néadi > WS *niedi > nied` [Germanic/data/germanic-aligned-final.tsv:794-796; docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243; docs/references/orel_handbook_germanic_etymology.vision.txt:31783-31790]. The OE target `nīed` should therefore be read as the project's normalized OE citation form for the West-Saxon outcome represented in the handbooks as `nied`, not as evidence that the current row has a different etymon from the standard `*naudiz/*naudi-` family [Germanic/data/germanic-aligned-final.tsv:796-796; docs/references/campbell_old_english_grammar.txt:5823-5827; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29743-29745].

The most securely attachable DEV_NOTES authority is not row-specific argumentation but copied handbook framing. In the large `rēc` literature audit, DEV_NOTES quotes Campbell's rule that OE `éa` from primitive Germanic `au` “is subject to i-umlaut in all dialects” and includes `nied need` among the model lexemes. That is current and usable here because it states directly that the relevant vowel history is ordinary, not exceptional [Germanic/docs/DEV_NOTES.md:35039-35048; docs/references/campbell_old_english_grammar.txt:5823-5827]. Ringe-Taylor then make the same point more explicitly for this exact lexeme family by deriving `PWGmc *naudi ... > *néadi > WS *niedi > nied`, with Anglian `néd` alongside it [docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243].

The other genuinely useful DEV_NOTES fragment is the heavy-syllable syncope example `*néadiling -> OE nīedling`. That fragment is not row 2135 itself, but it matters because it shows the same lexical base already being handled in project spelling with `nīe-`, which helps explain why the live counterpart field is written `nīed` rather than the handbook-normalized `nied` [Germanic/docs/DEV_NOTES.md:716-723; docs/references/ringe_taylor_linguistic_history_vol2.txt:15364-15364]. This is orthographic/representational support, not a second independent etymology.

What does **not** survive is any securely current row-specific controversy. There is no DEV_NOTES fragment arguing that row 2135 should be retargeted, marked reconstructed-only, or moved into `oe_known_problems.tsv`. The only stray row-adjacent project history is a German diphthong-tokenization debug pass that included `naudiz` in a planned probe list; the follow-up note then reports that the duplicate parse problem actually affected `braudą` only. That material should be kept, if at all, only as transducer-debug chronology and not as evidence of an OE lexeme problem [Germanic/docs/DEV_NOTES.md:1914-1920,2216-2220].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-35039-35048

- Source heading: `Campbell (1959), Old English Grammar — copied in the rēc handbook audit`
- Source line or section hint: `lines 35039-35048`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `au_plus_i_umlaut`; `handbook_example`; `ws_ie`; `regularity`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2151`

This is the clearest current DEV_NOTES fragment for row 2135 even though it was copied into DEV_NOTES while investigating another lexeme. DEV_NOTES reproduces Campbell's statement that “**éa the OE development of Prim. Gmc. au is subject to i-umlaut in all dialects**” and then gives the lexical list `biegan`, `hieran`, `liefan`, and crucially `nied need` [Germanic/docs/DEV_NOTES.md:35041-35048; docs/references/campbell_old_english_grammar.txt:5823-5827]. For this row, the fragment matters because it says exactly what later reporting needs to say: the vowel history behind OE `nied/nīed` is an ordinary `*au + i` development, not a special exception requiring a custom rescue story.

Used together with Ringe-Taylor's explicit derivation `PWGmc *naudi > *néadi > WS *niedi > nied`, this fragment is enough to defend the row's present `regular` status even though DEV_NOTES never opened a dedicated “need / nīed” subsection [docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243]. The safe formulation is therefore: current DEV_NOTES authority is shared rather than row-local, but it is still strong enough to support the live row.

### DEV_NOTES:line-716-723

- Source heading: `High vowel syncope applies only after heavy syllables`
- Source line or section hint: `lines 716-723`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `niedling`; `heavy_syllable`; `syncope`; `orthographic_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

DEV_NOTES' syncope overview includes the lexeme-family example `*néadiling -> OE nīedling 'slave'`, explicitly classed as syncopated after a heavy syllable because the base `nēad-` is heavy [Germanic/docs/DEV_NOTES.md:716-723]. This is not direct row-2135 authority in the narrow sense, but it is still highly usable context because it shows that the project already writes this OE stem as `nīed-` in a related derivative.

That makes the live counterpart spelling `nīed` easier to interpret correctly. The fragment does **not** prove a distinct protoform for row 2135; rather, it supports the house representation of the OE outcome once the regular `*naudi > *néadi > *niedi` development is accepted [docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243,15364-15364].

### DEV_NOTES:line-1914-1920-and-2216-2220

- Source heading: `German diphthong tokenization audit`
- Source line or section hint: `lines 1914-1920 and 2216-2220`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `transducer_debugging`; `diphthong_tokenization`; `naudiz_probe`; `not_row_specific`
- Recommended next use: `ignore_unless_debugging`
- Shared with row IDs:

This is the only place where DEV_NOTES mentions `naudiz` directly as a probe lexeme, but it is **not** good current row authority for the OE note itself. The first note proposed re-running tracer checks for several diphthong-bearing items, including `naudiz`, while investigating an ambiguity in proto tokenization [Germanic/docs/DEV_NOTES.md:1914-1920]. The follow-up note then reports that the duplicate `{*a}{*u}` vs. `{*au}` problem was logged for `braudą` only and that the fix cleaned up the relevant German proto path there [Germanic/docs/DEV_NOTES.md:2216-2220].

For row 2135 this material should therefore be treated as project-debug chronology only. It does not show that `*náudiz -> nīed` was disputed, broken, or philologically suspect; at most it shows that `naudiz` once sat in a generic diphthong-bearing regression set.

## Superseded or diagnostic material

- No securely current DEV_NOTES fragment argues against the live row. The slice's main limitation is absence of row-local prose, not presence of a rival analysis.
- The diphthong-tokenization audit is easy to overread because it mentions `naudiz`, but its actual finding concerned `braudą`, not `nīed`; use it only for transducer-debug history, if at all [Germanic/docs/DEV_NOTES.md:1914-1920,2216-2220].
- Orthographic variation in the reference extracts (`nid`, `nied`, `nēad`, etc.) is real and should stay visible, but it is not by itself evidence that row 2135 needs retargeting. Current repo references still support the same inherited lexeme and the regular West-Saxon umlauted development behind the row [docs/references/orel_handbook_germanic_etymology.vision.txt:31783-31790; docs/references/ringe_taylor_linguistic_history_vol2.txt:14240-14243; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29386-29387,29743-29745].

## Open questions for later work

- Decide whether later final-report prose should normalize the OE form as project `nīed` throughout, or whether it should use handbook `nied` in the main text and reserve `nīed` for row/TSV citation.
- If a packet or research memo is later created for row 2135, add direct dictionary-headword extracts for `nēad/nied/nid` so the orthographic range is documented in one place rather than inferred from scattered reference snippets.
- If the row is ever reconsidered as attested-versus-reconstructed OE, keep the distinction explicit: the comparative proto headword is `*náudiz`, the handbook OE development runs through `*naudi > *néadi > WS *niedi > nied`, and the current counterpart `nīed` is the project's normalized row target rather than a separately argued replacement protoform.
