---
row_id: 2284
concept: whale
counterpart: hwæl
proto: *wálaz
protoform: *xwálaz
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2284 whale / hwæl

## Current row state

- The live OE row reads `CONCEPT = whale`, `COUNTERPART = hwæl`, `PROTO = *wálaz`, `PROTOFORM = *xwálaz`, `DERIVATION_CLASS = early_analogy` [Germanic/data/germanic-aligned-final.tsv:2284-2284].
- The live row note is already partly corrective but still over-compressed: `Kroonen *hwalaz with initial *hw-; OE hwæl.` The source-note history also preserves the project-side repair `TSV fix: proto *walăz → *xwalăz` [Germanic/data/germanic-aligned-final.tsv:2284-2284].
- Required support-file checking found a row-specific packet and research memo, but no pilot file and no row-specific DEV_NOTES excerpt. The packet explicitly records `_None_` for direct DEV_NOTES hits, and the memo likewise says, `I found no dedicated dossier, no DEV_NOTES discussion for this row, and no pilot report already written for this lexeme` [Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md:49-61,87-103; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:35-46].
- Because dedicated DEV_NOTES material is absent, this slice has to preserve the row’s working-note logic from the live TSV, the packet/memo, and the reference extracts, without pretending that a row-specific DEV_NOTES mini-dossier survives.

## Development-note summary

The main documentation burden for row 2284 is **not** to rescue a broken derivation. The packet already shows that the current cascade takes `PROTOFORM = *xwálaz` to `hwæl`, and the memo correctly says the live question is instead how to explain that input choice and how to describe its relationship to comparative sources [Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md:17-43; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:13-19]. Since there is no lexeme-addressable DEV_NOTES section to quote, future editors should treat this file as a replacement working note rather than as a digest of a lost row dossier.

The three-way distinction among `PROTO`, `PROTOFORM`, and `COUNTERPART` has to stay explicit. `PROTO = *wálaz` is the aligned cognate-set headword now sitting in the TSV. It is useful for cross-row alignment, but it is **not** identical to the form the OE cascade actually consumes on this row [Germanic/data/germanic-aligned-final.tsv:2284-2284; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:48-56]. `PROTOFORM = *xwálaz` is the project’s row-level derivational input, i.e. the form needed to reach OE `hwæl` under the present modelling assumptions [Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md:19-43]. `COUNTERPART = hwæl` is the Old English target/headword represented by the row, and it is attested rather than reconstructed [Germanic/data/old_english_wiktionary.tsv:196-196; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:23684-23684].

The initial `*hw-` / `*xw-` correction should be kept **separate** from the question of exact comparative stem shape. The older project state had `*walăz`, and the history note `proto *walăz → *xwalăz` marks a real modelling repair: without initial `xw-/hw-`, the row could not transparently explain OE initial `hw-` [Germanic/data/germanic-aligned-final.tsv:2284-2284]. That much is solid project history. But the surviving note then overreaches by saying `Kroonen *hwalaz`. The repo’s Orel OCR actually supports the a-stem-like input directly: `*xwalaz sb.m.: ON hvalr 'whale' ... OE hwal id.` [docs/references/orel_handbook_germanic_etymology.vision.txt:22839-22841; @Orel2003]. By contrast, the repo’s Kroonen OCR gives `*hwali- m. 'whale' ... OE hwæl m. 'id.'`, which supports inherited initial `hw-` but not the exact cited form `*hwalaz` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:14445-14446; @Kroonen2013]. The safe replacement wording is therefore: the project corrected the row to an initial `*xw-` input, but Kroonen should not be quoted as the source of exact `*hwalaz`.

The OE side is much firmer than the comparative note. Clark Hall has `hwal I. (usu, hwal- in obl. cases) m.'whale,'`, confirming the ordinary dictionary headword, even if the OCR spells the lemma without the modernized ligature [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:23684-23684; @ClarkHall1960]. Bosworth-Toller likewise preserves the noun and explicitly gives a plural citation: `God gesceóp þa micelan hwalas` [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:92628-92631]. Bright’s reader also has the contrastive plural in context: `Se hwsel biS micle l^ssa ... o^re hwalas` [docs/references/bright_anglo_saxon_reader.txt:5764-5764]. These sources are enough for the conservative claim that the row’s `COUNTERPART = hwæl` is an attested OE citation form and that plural `hwalas` is also ordinary OE evidence, even if the slice does not attempt a full paradigm reconstruction.

That singular/plural contrast matters because it explains why the row can use `PROTOFORM = *xwálaz` and still sit in an `early_analogy` bucket without looking arbitrary. The row-specific useful analysis file is not a whale dossier but `arestoration_r_l_research.md`, which cites `hwalas` among forms showing `*\*hwalaz, \*hwalōz → \*hwæl, \*hwalas → hwæl, hwalas` and then lists row 2284 diagnostically as `monosyllabic; no surviving back trigger` [Germanic/docs/analysis/arestoration_r_l_research.md:377-377,720-720]. In other words, the slice should not imply that every paradigm cell had `æ`; singular `hwæl` and plural `hwalas` are precisely the contrast that makes the current project framing intelligible. The memo is right that the project’s a-stem-like input aligns better with Orel and with the OE plural evidence than with a literal reading of Kroonen’s `*hwali-` entry [Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:56-71].

Because DEV_NOTES support is missing, confidence should stay modest. What can be said confidently is limited but useful: (1) the row now deliberately distinguishes cognate-set `PROTO` from derivational `PROTOFORM`; (2) the initial `*xw-` repair is a genuine project correction and should remain explicit; (3) the exact attribution `Kroonen *hwalaz` is inaccurate as phrased in the current row note; and (4) OE `hwæl` plus plural `hwalas` gives enough philological support for the present row to remain documented as a resolved input-choice issue rather than as an outstanding sound-law defect [Germanic/data/germanic-aligned-final.tsv:2284-2284; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:64-91].

## Relevant DEV_NOTES fragments

### No dedicated DEV_NOTES anchor survives for row 2284

- Fragment type: `absent_row_specific_dev_notes`
- Status: `current`
- Issue tags: `no_direct_dev_notes`; `support_files_required`; `do_not_overindex`
- Recommended next use: `cite_absence_explicitly`
- Shared with row IDs:

The required searches and the row-specific packet agree that there is **no** dedicated DEV_NOTES discussion for this lexeme. The packet records `_None_` both for direct DEV_NOTES hits and for supporting/background DEV_NOTES hits, while the memo states that no dedicated DEV_NOTES discussion was found [Germanic/docs/lexeme_reports/packets/2284-whale-hwæl.md:49-61,87-91; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:35-46]. Future work should therefore avoid fabricating a line anchor in `index.tsv` or describing this row as if it had a surviving DEV_NOTES section comparable to stronger slices.

## Superseded or diagnostic material

- The older project state with `*walăz` should be retained only as **project-history diagnostics**. It is useful because it explains why the later `*xw-` correction was necessary, but it is not the live lexical analysis anymore [Germanic/data/germanic-aligned-final.tsv:2284-2284; Germanic/docs/lexeme_reports/research_memos/2284-whale-hwæl.md:27-33,66-71].
- The wording `Kroonen *hwalaz with initial *hw-` is also diagnostic/superseded. The initial `*hw-` point is directionally right, but the exact form is not what the repo’s Kroonen file says; it says `*hwali-` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:14445-14446; @Kroonen2013].
- The diagnostic line in `arestoration_r_l_research.md` (`monosyllabic; no surviving back trigger`) is useful for rule-scope explanation, but it should not be promoted into a stronger etymological claim than it makes. It explains why row 2284 is not an active a-restoration problem; it does not by itself decide between `*xwalaz` and `*hwali-` as comparative dictionary lemmata [Germanic/docs/analysis/arestoration_r_l_research.md:720-720].

## Open questions for later work

- If the TSV note is ever rewritten in a later task, the safest improvement would be to separate two statements that are currently collapsed: **initial correction** (`*walăz` was wrong for an OE `hw-` outcome) and **comparative-source divergence** (Orel `*xwalaz` versus Kroonen `*hwali-`) [Germanic/data/germanic-aligned-final.tsv:2284-2284; docs/references/orel_handbook_germanic_etymology.vision.txt:22839-22841; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:14445-14446].
- Any future final lexeme report should keep singular `hwæl` and plural `hwalas` visibly distinct, because that contrast is the clearest in-repo support for the present row framing [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:92628-92631; Germanic/docs/analysis/arestoration_r_l_research.md:377-377].
- For `index.tsv`, this row presently has **no strong DEV_NOTES line anchor**. It looks documentable from support files, but not indexable by a genuine DEV_NOTES citation unless new DEV_NOTES material is later added.
