---
row_id: 2308
concept: youth
counterpart: ġeoguþ
proto: "*júgunθiz"
protoform: "*júgunθ"
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2308-youth-ġeoguþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2308-youth-ġeoguþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/widuwe-u-preservation.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: "Current row keeps a lexically specified g-bearing proto label and a pre-apocopated OE-facing PROTOFORM; later shared notes replace older u-lowering heuristics with stem-u harmony."
needs_literature_agent: false
---

# DEV_NOTES material — 2308 youth / ġeoguþ

## Current row state

- The live OE row is `2308 | youth | ġeoguþ | PROTO *júgunθiz | PROTOFORM *júgunθ | DERIVATION_CLASS early_analogy`. The row note already distinguishes the comparative proto label from the OE-facing derivational input: `PROTOFORM *jugunθ (without -iz)` is justified by early i-apocope in `*-unþi-`, while medial `u` is said to remain preserved in `ġeoguþ` rather than lowering [Germanic/data/germanic-aligned-final.tsv:1468-1468].
- That three-way distinction should remain explicit. `PROTO = *júgunθiz` is the row’s project-level cognate-set label; `PROTOFORM = *júgunθ` is the stage actually fed into the OE cascade; `COUNTERPART = ġeoguþ` is the attested OE target represented by the row [Germanic/data/germanic-aligned-final.tsv:1468-1468].
- `coverage_audit.md` classifies row `2308` as a required report row because it has both `NOTE` content and non-regular `DERIVATION_CLASS = early_analogy`, but there is still no manifest-backed report entry; `report_manifest.tsv` contains no row-2308 path, and `oe_known_problems.tsv` does not list this row or proto as an open OE exception bucket [Germanic/docs/lexeme_reports/coverage_audit.md:177-177; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match for the live `PROTOFORM`: `*júgunθ` → `*jéugunθ` (`OE Ws Palatal Glide`) → `*jéugūnθ` (`NWGmc Nasal Spirant Lengthening`) → `*jéugūθ` (`NWGmc Nasal Spirant Loss`) → `*jéogūθ` (`OE Diphthong Leveling`) → `*jéoguθ` (`OE Unstressed Long Vowel Shortening`) → orthographic `ġeoguþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6904-6924].

## Development-note summary

The row has substantial surviving DEV_NOTES support, but that support is layered. The durable row-local core is the April 2026 `ġeoguþ` dossier: it argues that the OE row must **not** feed the full `*-i(z)` form into the OE umlaut stage, because doing so yields the wrong over-umlauted output. DEV_NOTES preserves the key scholarly chain in direct quotation: “PWGmc `*jugunþi` 'youth' (OHG `jugund`) > `*juguþ` > OE `geoguþ` ~ `iuguþ`”, and it pairs that with Campbell’s statement that Ingvaeonic nasal loss in unstressed syllables gives “`duguþ` chivalry < `*dugunþ-`, and so `geoguþ` youth” [Germanic/docs/DEV_NOTES.md:18858-18860,18877-18903]. Those quotations are the main reason the live row keeps `PROTOFORM = *júgunθ` while still retaining `PROTO = *júgunθiz` as the broader proto label [Germanic/data/germanic-aligned-final.tsv:1468-1468].

DEV_NOTES then makes the project-policy consequence explicit. The row is handled by a transponent input, not by letting the full comparative headword run unchanged through the OE cascade. The notes say the system pre-applies the early loss of final `-i` and therefore uses `*jugunþ` as the derivational input because otherwise i-umlaut would wrongly remain active; the worked example contrasts the bad path `*júgunθiz ... → *jéogȳθ → †ġeogȳþ` with the accepted path `*júgunθiz → *júgunθi → *júgunθ ... → ġeoguþ ✓ (no i-umlaut trigger)` [Germanic/docs/DEV_NOTES.md:19012-19028,19115-19123]. For row 2308, this is current row-local authority, not mere historical debugging.

The second half of the row’s explanation is more mixed. The older row-local sections correctly recognized that `ġeoguþ` must keep medial `u`, but some of their first formulations were provisional. Mid-April DEV_NOTES framed the issue partly as a “final syllable exception” and then as an open research question comparing `*júgunθ → ġeoguþ` with `*búgun → bugon` [Germanic/docs/DEV_NOTES.md:18464-18517,19127-19169]. Later shared repo work superseded that narrower framing. DEV_NOTES now states that Bugge-style productive `*w > *g` should **not** be added to the cascade and instead recommends lexical specification of `*-g-` for the small attested set `*nigon, *geoguð, *sugu` [Germanic/docs/DEV_NOTES.md:43092-43115]. Likewise, the later u-lowering resolution says the handbooks treat `wuduwe`/`munuc`/`duguþ` as **progressive stem-`u` harmony**, and the companion dossier supplies the verbatim Brunner/Luick evidence that this blocking applies before a single consonant when the stem syllable contains `u`, citing `duguþ` and `iuguþ` explicitly [Germanic/docs/DEV_NOTES.md:43869-43879; Germanic/docs/dossiers/widuwe-u-preservation.md:1722-1758,1917-1930].

The safest current characterization is therefore: row `2308` is an `early_analogy` item because the OE cascade is deliberately fed the pre-apocopated `PROTOFORM *júgunθ`, but once that staging choice is made, the remaining OE derivation to attested `ġeoguþ` is regular and already exact in the published trace [Germanic/data/germanic-aligned-final.tsv:1468-1468; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6904-6924]. The row-local DEV_NOTES block remains authoritative for the early-i-apocope decision; later shared notes and dossier work are needed to state the current consensus on medial-`u` preservation and on lexical rather than productive g-specification [Germanic/docs/DEV_NOTES.md:18865-19036,43092-43115,43869-43879].

## Relevant DEV_NOTES fragments

### DEV_NOTES: `§14.9` core row-local analysis (`18822-19036`)

- Status: current for the row’s staging decision; partly superseded only in some sub-arguments about how to formulate `u`-preservation.
- Fragment type: row-local primary authority.
- Best use: cite for the distinction between `PROTO *júgunθiz`, reconstructed intermediate `*jugunþi > *juguþ`, and OE-facing `PROTOFORM *júgunθ`.

This is the most important surviving lexeme block. It preserves both the philological setup and the project decision. The key quotations are still usable as-is:

> “The Ingvaeonic loss of nasal consonants before voiceless spirants with compensatory lengthening of the vowel... occurs in unaccented syllables also... `duguþ` chivalry < `*dugunþ-`, and so `geoguþ` youth.” [Germanic/docs/DEV_NOTES.md:18858-18860]

> “PWGmc `*jugunþi` 'youth' (OHG `jugund`) > `*juguþ` > OE `geoguþ` ~ `iuguþ`” [Germanic/docs/DEV_NOTES.md:18879-18884]

The section then draws the project conclusion directly: final `-i` is already gone before OE i-umlaut would apply, so the system should treat `*jugunþ` as the OE-input stage and not expect `*u > y` here [Germanic/docs/DEV_NOTES.md:18877-18903,19004-19028]. For replacement-note purposes, this fragment is genuinely row-local and should remain the anchor for explaining why `PROTOFORM` is shorter than `PROTO` [Germanic/data/germanic-aligned-final.tsv:1468-1468].

### DEV_NOTES: worked verification example (`19115-19123`)

- Status: current.
- Fragment type: row-local verification.
- Best use: quote when a later report needs the exact “wrong if `-i` stays / right if `-i` drops” contrast in one compact place.

The short worked example is the clearest single proof of the row policy. DEV_NOTES explicitly contrasts the rejected derivation with the accepted one:

> “Without early i-apocope (wrong): … `*jéogȳθ` (i-umlaut) → †`ġeogȳþ` ✗” [Germanic/docs/DEV_NOTES.md:19117-19119]

> “With early i-apocope (correct): `*júgunθiz → *júgunθi (z-loss) → *júgunθ (early i-apocope) → *jéogunθ (u-lowering) → *jéogūθ (NSL) → ġeoguþ ✓ (no i-umlaut trigger)`” [Germanic/docs/DEV_NOTES.md:19121-19123]

This fragment is more operational than philological, but it is extremely valuable because it states the row’s accepted chronology in one place and matches the live trace’s exact-match outcome [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6904-6924].

### DEV_NOTES: palatal-glide and spelling background (`15687-15835`)

- Status: current shared background, not row-local closure.
- Fragment type: shared lexical-background support.
- Best use: cite for OE spelling variation and why `geoguþ/iuguþ` belongs with the initial-`j` glide-spelling cohort.

This section was written primarily for `ġeoc`/`ġeong`-type spelling behavior, but it contains directly relevant evidence for `ġeoguþ` too. Campbell’s quotation is still useful:

> “In W-S the glide is written with considerable regularity… initial `*jū` we find iū (gū), giū, geū … e.g. iung, giong, **geong** young, iuguð, gioguð, **geoguð** youth…” [Germanic/docs/DEV_NOTES.md:15729-15734]

For row 2308 this is background rather than closure. It supports the OE-side spelling facts (`ġeoguþ` alongside `iuguþ/iugoþ`-type variation), but it does not decide the PROTO/PROTOFORM split by itself [Germanic/docs/DEV_NOTES.md:15724-15734,18879-18884].

### DEV_NOTES: later lexical-specification and harmony follow-up (`43092-43115`, `43869-43879`)

- Status: current shared follow-up.
- Fragment type: shared project-policy support.
- Best use: cite when explaining why the row keeps a g-bearing project input and why later repo consensus prefers stem-`u` harmony over older ad hoc heuristics.

The later Bugge-velarization review says plainly:

> “Do not implement Bugge's velarization as a productive cascade rule.” [Germanic/docs/DEV_NOTES.md:43092-43098]

> “Lexical / morphological route (Fulk-style): treat `*nigon, *geoguð, *sugu` as items where the `*-g-` is morphologically-introduced or analogical… encode the post-velarization form in the TSV PROTOFORM and let the cascade derive only the regular OE-internal residue.” [Germanic/docs/DEV_NOTES.md:43100-43105]

Separately, the later u-lowering resolution states that the handbook-backed account is progressive stem-`u` harmony rather than the earlier narrower guesses: handbooks frame `wuduwe`/`munuc`/`duguþ` as harmony cases, and the FST exclusion after stem `u/*ú` is said to reflect that consensus [Germanic/docs/DEV_NOTES.md:43869-43879]. For row 2308 these are **shared** notes, not row-local lexeme essays, but they materially affect how the current row should be described.

## Superseded or diagnostic material

- The earliest direct row hit is the old mismatch note `*jugunθiz → expected ġeoguþ, output ġūgyþ`, from the December 2025 umlaut-debug sweep. This is useful as historical evidence of the old failure mode, but it is not current row policy now that the row derives exactly with `PROTOFORM *júgunθ` [Germanic/docs/DEV_NOTES.md:2581-2585; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6904-6924].
- The “final syllable exception” account in `§14.8.1` should be treated as superseded. It correctly noticed that `ġeoguþ` should not come out as `*ġeogoþ`, but its explanation in terms of final closed-syllable protection is later displaced by the Brunner/Luick-style stem-`u` harmony analysis preserved in later DEV_NOTES and the widow dossier [Germanic/docs/DEV_NOTES.md:18464-18517,43869-43879; Germanic/docs/dossiers/widuwe-u-preservation.md:1722-1758,1917-1930].
- The April 14 “open questions” comparing `*júgunθ → ġeoguþ` with `*búgun → bugon` are diagnostic, not final. They preserve the exact research problem, but later DEV_NOTES resolves the broader conditioning in favor of harmony plus lexical/project policy rather than leaving the row in an unresolved bug bucket [Germanic/docs/DEV_NOTES.md:19127-19169,43864-43925].
- Some philological reconstruction language inside the row-local block is older or inconsistent in detail and should not be copied uncritically. In particular, row prose should prefer the later, stable chain `*jugunþi > *juguþ > OE geoguþ ~ iuguþ` over stray earlier wording such as `*jugiþ`; the former is the repeated and better-supported formulation inside the same DEV_NOTES cluster [Germanic/docs/DEV_NOTES.md:18426-18429,18879-18884].

## Open questions for later work

- The live TSV note still points mainly to `§14.9`. If row `2308` is revisited, the note could be tightened so that the current harmony consensus and the later anti-Bugge lexical-specification policy are named explicitly, not left implicit in later shared notes [Germanic/data/germanic-aligned-final.tsv:1468-1468; Germanic/docs/DEV_NOTES.md:43092-43115,43869-43879].
- If a fuller production report is later written, it should keep four stages visibly separate at the top: scholarly etymological headword `*ju(w)unþi-`, project cognate-set `PROTO *júgunθiz`, OE-facing `PROTOFORM *júgunθ`, and attested OE `COUNTERPART ġeoguþ`. Collapsing those layers would blur the actual reason the row is classed `early_analogy` [Germanic/docs/DEV_NOTES.md:18827-18845,19012-19028; Germanic/data/germanic-aligned-final.tsv:1468-1468].
- The row appears stable enough that it does not belong in `oe_known_problems.tsv`, but it is still important enough for indexing because it combines a true row-local DEV_NOTES block with later shared follow-up that changes how the row should be summarized. Any future index entry should therefore point to both the row-local apocope block and the later shared harmony / lexical-specification follow-up, not to `§14.9` alone [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/DEV_NOTES.md:18822-19036,43092-43115,43869-43879].
