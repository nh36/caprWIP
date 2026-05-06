---
row_id: 2049
concept: guest
counterpart: ġiest
proto: *gástiz
protoform: *gástiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2049 guest / ġiest

## Current row state

- CONCEPT: `guest`
- COUNTERPART: `ġiest`
- PROTO: `*gástiz`
- PROTOFORM: `*gástiz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T vol.2 3857: PGmc *gastiz > WS OE giest`, with no live split between cognate-set proto and OE-facing protoform for this row [Germanic/data/germanic-aligned-final.tsv:462].
- Packet status is clean and fully regular: the compact derivation trace already lands on `ġiest`, with Anglo-Frisian Brightening, OE Velar Palatalization, OE I Umlaut, WS palatal diphthongization, and high-vowel apocope all shown as ordinary steps rather than rescue devices [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:17-43].
- Memo status matches the packet's regular reading but adds the philological caution that `ġiest` is a normalized West Saxon target inside a wider OE spelling and dialect set, not the only attested OE surface spelling; the row still does not need a paradigm-cell substitution, special protoform, or exception label [Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:13-32,65-90,111-123].
- `oe_known_problems.tsv` has no entry for row `2049`, `*gástiz`, or `ġiest`, which is consistent with the row's current solved/regular status rather than a live modelling failure [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:45-47].
- `report_manifest.tsv` currently has no row-specific manifest entry for 2049, so this slice needs to stand on its own as the replacement working note rather than pointing to a completed report [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:11-13; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Development-note summary

No dedicated row-specific DEV_NOTES mismatch note survives for row 2049. The live row is regular, and the securely attachable DEV_NOTES material is therefore comparator/background material rather than a self-contained repair dossier. That absence should be stated explicitly so later workflow does not go hunting for a missing controversy that is not actually there [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:49-52; Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:23-38].

The one clearly reusable current DEV_NOTES line cluster is the comparison bullet in the `sæp` investigation. It preserves the compact derivational chain "`*gastiz` → AFB → `*gæstiz` → i-umlaut → `*giestiz` → ... → `ġiest` ✓ (i-stem, BUT has initial palatal which triggers WS palatal diphthongization first)`" [DEV_NOTES:line-12010-12012]. For replacement-note purposes, that sentence matters because it says almost everything a later report writer needs in one place: the lexeme is an i-stem; Anglo-Frisian Brightening gives the fronted pre-umlaut vowel; i-umlaut is part of the history; and the specifically West Saxon `ie` is attributed to palatal-triggered diphthongization, not to some special row-only workaround [DEV_NOTES:line-12010-12012].

That comparator use also explains how this row should be narrated. The central row issue is not whether `*gástiz` can yield OE `ġiest`—the project already treats that as a successful regular derivation—but what kind of OE form `ġiest` represents. The memo's most durable clarification is that the row chooses normalized West Saxon `ġiest`, while Anglian material and dictionary headwording preserve forms such as `gest`, `gyst`, and `gist`; those variants are philological background, not evidence that the live TSV row is mis-specified [Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:57-63,80-90,111-121]. DEV_NOTES:line-12010-12012 is consistent with exactly that reading because it uses `ġiest` as the West Saxon-style positive control, not as a disputed reconstruction.

Two additional DEV_NOTES mentions are worth preserving, but only with explicit limits. First, a later `wyrm` note says that Campbell §602 lists `wyrm` as an i-stem in the category "`like *giest*`" [DEV_NOTES:line-8413-8422]. That is not a row-specific analysis of `guest`, but it is useful background because it shows that within the repo's handbook framing `giest` functions as a model short-root i-stem noun. Second, a much later paradigm regression table includes the heavy i-stem dative/instrumental plural probe ``*gastimiz`` → `ġiestum` [DEV_NOTES:line-39696-39710]. That is valuable only if a later report wants to say something about inherited i-stem inflectional behavior; it is not authority for the citation form `ġiest` itself.

The main thing later writers should *not* do is inflate unrelated diagnostic material into row authority. The Old Saxon example `gast < *gastiz` appears in a completely different note about **rēk** and is used there only as a generic example of early Old Saxon i-stem nominative singular behavior [DEV_NOTES:line-35373-35378]. It helps explain why `guest` can surface as a generic stem-class comparator elsewhere in the repo, but it is not a DEV_NOTES argument about row 2049 and should remain a checked false positive. The replacement working note for this row is therefore simple but explicit: keep the live row regular, use the `*gastiz ... ġiest` comparator line as the main DEV_NOTES authority, preserve the West Saxon-vs.-Anglian nuance from the memo, and mark the rest as background or diagnostic only.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-12010-12012

- Source heading: `Compare working forms` inside the `sæp` investigation
- Source line or section hint: `lines 12010-12012`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `i_stem`; `anglo_frisian_brightening`; `i_umlaut`; `ws_palatal_diphthongization`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the only clearly row-relevant DEV_NOTES fragment that directly walks through the derivation. It should be carried almost verbatim because the wording is already dense and accurate: "`*gastiz` → AFB → `*gæstiz` → i-umlaut → `*giestiz` → ... → `ġiest` ✓ (i-stem, BUT has initial palatal which triggers WS palatal diphthongization first)`" [DEV_NOTES:line-12010-12012]. The fragment is not a mismatch repair note; it is a comparator bullet inside another lexeme's discussion. Even so, it is current and securely attachable because it states the specific derivational logic the live row still assumes.

### DEV_NOTES:line-8413-8422

- Source heading: `wyrm` note citing Campbell's i-stem category `like giest`
- Source line or section hint: `lines 8413-8422`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `i_stem`; `campbell_classification`; `model_lexeme`; `comparative_background`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment belongs primarily to the `wyrm` investigation, but it is still worth indexing in the slice because it shows how `giest` functions in the repo's handbook framing. DEV_NOTES says Ringe & Taylor use `*wurmiz` as an i-stem and then adds: "`Campbell §602 lists wyrm as an i-stem noun in the 'like *giest*' category (short root syllable i-stems)`" [DEV_NOTES:line-8413-8422]. For row 2049 this is background confirmation of noun class, not direct evidence for the surface derivation.

### DEV_NOTES:line-39696-39710

- Source heading: `paradigm probes` regression table with heavy i-stem dat./inst.pl.
- Source line or section hint: `lines 39696-39710`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `i_stem`; `paradigm_probe`; `dative_plural`; `regression_suite`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This late DEV_NOTES table is not citation-form evidence, but it is still a useful diagnostic record that the project treated `guest` as a heavy i-stem in paradigm probing. The relevant line is `P8 | i-stem dat./inst.pl. (heavy) | *gastimiz | ġiestum` [DEV_NOTES:line-39703-39703]. If later report work needs a compact inflectional aside, this line shows the expected plural oblique behavior; otherwise it should stay secondary to the main citation-form fragment at DEV_NOTES:line-12010-12012.

## Superseded or diagnostic material

- No securely attachable row-specific DEV_NOTES repair dossier survives beyond the comparator/background material listed above. That is a real outcome, not a gap to be silently patched over [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:49-52; Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:23-38].
- The Old Saxon note at `DEV_NOTES:line-35373-35378` is a checked false positive. It says early Old Saxon i-stem masculines typically show nominative singular `-i`, giving OS `gast < *gastiz` as an example, but the actual discussion is about OS **rēk** and stem-class diagnosis there, not about OE `ġiest` [DEV_NOTES:line-35373-35378]. Keep it only as project-history evidence that `gast` was used generically as an i-stem comparator.
- The packet's supporting/background section is useful, but its top-level DEV_NOTES status line says `_None_`; later users should therefore rely on the explicit line-based fragment refs in this slice rather than assuming the packet itself already sorted DEV_NOTES evidence at the right granularity [Germanic/docs/lexeme_reports/packets/2049-guest-ġiest.md:49-71].
- The memo correctly rejects two tempting distractions that should stay out of row authority: the irrelevant lexical-table hit `guest -> appear`, and the OS `gast` aside discussed above [Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:29-37,94-104,123-124].

## Open questions for later work

- If a final lexeme report is written, decide how explicitly it should separate normalized West Saxon target `ġiest` from the wider OE spelling and dialect set (`gest`, `giest`, `gyst`, `gist`) without obscuring that the live row itself remains regular [Germanic/docs/lexeme_reports/research_memos/2049-guest-ġiest.md:80-90,111-121].
- Decide whether the final report should quote the comparator bullet from DEV_NOTES:line-12010-12012 verbatim, since it is already the most concise project statement of the derivational chain.
- If later noun-paradigm work expands beyond citation forms, decide whether the diagnostic probe `*gastimiz -> ġiestum` deserves a short appendix note or should remain internal regression history only [DEV_NOTES:line-39696-39710].
