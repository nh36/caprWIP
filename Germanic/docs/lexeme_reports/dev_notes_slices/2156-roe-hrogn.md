---
row_id: 2156
concept: roe
counterpart: -
proto: *ráixōn
protoform: *ráixōn
derivation_class:
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 2156 roe / -

## Current row state

- The live OE row currently reads `CONCEPT = roe`, `COUNTERPART = -`, `PROTO = *ráixōn`, `PROTOFORM = *ráixōn`, and blank `DERIVATION_CLASS`. The row note is explicit: `Unattested OE; reconstructed *hrogn.` [Germanic/data/germanic-aligned-final.tsv:877-877]
- The live table already distinguishes the three levels that later reporting must keep separate: the comparative Germanic input is `*ráixōn`, the OE `COUNTERPART` field is still blank/dashed, and the only OE-form proposal surviving in-row is the note-level reconstruction `*hrogn` rather than an attested lemma in the counterpart column [Germanic/data/germanic-aligned-final.tsv:877-877].
- Immediate row context confirms that this is a cognate-set placeholder rather than an isolated typo. The same concept block has English `roe`, Dutch `ree`, and German `Reh` aligned to the same proto item, while the Old English row alone keeps `COUNTERPART = -` and pushes `*hrogn` into the note instead [Germanic/data/germanic-aligned-final.tsv:875-878].
- `Germanic/data/old_english_wiktionary.tsv` preserves the same distinction: for English `roe` it gives OE `-` and glosses the inheritance entry as `template:inh (unattested; reconstructed *hrogn)`, so the reconstruction is duplicated in repo-local row context but still not promoted to an attested OE headword field [Germanic/data/old_english_wiktionary.tsv:217-217].
- `Germanic/data/oe_known_problems.tsv` currently has no entry for row `2156`, for `*ráixōn`, for `roe`, or for `*hrogn`; the file's present contents are limited to unrelated `u`-lowering and analogy items, so this row is not presently tracked there as a known phonological exception bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

A direct review of `Germanic/docs/DEV_NOTES.md` finds no securely attachable row-specific note for row `2156`, no lexeme-specific section for `roe`, and no surviving discussion keyed to `*hrogn`, `*ráixōn`, or the current dashed OE counterpart. That negative result is the most important DEV_NOTES fact to preserve for this row. Unlike many other slices, there is no current project memorandum in `DEV_NOTES.md` that upgrades the OE side from provisional placeholder status into a literature-backed target.

Because no relevant DEV_NOTES authority survives, the safest replacement working note has to stay very close to the live row's own distinctions. The dataset does **not** currently present an attested Old English lemma for this concept. Instead, it presents a comparative proto label `*ráixōn`, leaves the OE `COUNTERPART` field blank as `-`, and records only a note-level reconstruction `*hrogn` [Germanic/data/germanic-aligned-final.tsv:877-877]. The matching `old_english_wiktionary.tsv` entry confirms the same state of play: unattested OE, reconstructed `*hrogn`, no OE headword installed in the counterpart column [Germanic/data/old_english_wiktionary.tsv:217-217].

That distinction matters operationally. Since `PROTO` and `PROTOFORM` are still identical `*ráixōn`, the row is **not** using an OE-facing substitute protoform of the sort seen in some other reconstructed rows; the table has not yet been given a special derivational input chosen to force a specific OE output. Equally, because `COUNTERPART` remains `-`, the reconstruction `*hrogn` should not be cited as though the live table had already adopted it as a settled OE target. At present it is best understood as a repository placeholder proposal attached to an unattested lexeme slot, not as a reviewed attested lemma and not as a DEV_NOTES-ratified project policy [Germanic/data/germanic-aligned-final.tsv:877-877; Germanic/data/old_english_wiktionary.tsv:217-217].

The absence of an `oe_known_problems.tsv` entry should also be read conservatively. It does **not** mean the row is documentation-secure; it only means the lexeme is not currently tracked in that file as a known FST exception or analogical outlier [Germanic/data/oe_known_problems.tsv:1-8]. Combined with the lack of any relevant `DEV_NOTES.md` section, the current state is therefore best described as a documentation gap around an unattested/reconstructed OE placeholder. Later work should begin from that plain fact rather than from any assumption that `*hrogn` has already been philologically validated inside the repo.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-exact-hit-for-2156-roe-hrogn

- Source heading: no exact row `2156` / `roe` / `*hrogn` / `*ráixōn` heading survives in `Germanic/docs/DEV_NOTES.md`
- Source line or section hint: direct review found no securely relevant hit to attach to this row
- Fragment type: `unclear_needs_human_review`
- Status: `uncertain`
- Issue tags: `missing_row_specific_authority`; `unattested_target`; `reconstructed_placeholder`; `negative_result`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This negative result is the only securely current DEV_NOTES fragment for the row. There is no surviving section in `Germanic/docs/DEV_NOTES.md` that explains why `*hrogn` was chosen, no attestation audit for an OE roe-word, and no row-policy note converting the dashed OE counterpart into a settled reconstructed target. For replacement-note purposes, that absence has to be stated directly, because otherwise a later reader could misread the live row note `Unattested OE; reconstructed *hrogn` as though it already rested on an identified DEV_NOTES dossier [Germanic/data/germanic-aligned-final.tsv:877-877].

What this fragment establishes is therefore procedural rather than phonological. The row currently has comparative alignment and a repo-local reconstruction placeholder, but it lacks a securely attachable in-repo discussion justifying that placeholder. Any later report, packet, or index entry should treat the OE side as unresolved documentation territory unless and until a new memo or literature-backed note is added.

## Superseded or diagnostic material

- No row-specific superseded DEV_NOTES analysis currently survives for `2156`; the problem is not that an older DEV_NOTES solution was later replaced, but that no securely relevant DEV_NOTES solution is presently attachable at all.
- The potentially misleading move would be to treat note-level `*hrogn` as though it were already the live OE counterpart. The current row does the opposite: it keeps `COUNTERPART = -` and stores `*hrogn` only in the unattested/reconstructed note, a distinction reinforced by `Germanic/data/old_english_wiktionary.tsv` [Germanic/data/germanic-aligned-final.tsv:877-877; Germanic/data/old_english_wiktionary.tsv:217-217].
- Because there is no packet, memo, or `oe_known_problems.tsv` entry attached to this row in the current repo state, there is also no secure present authority for indexing `*hrogn` as more than a diagnostic placeholder [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- Check whether a literature-backed OE reconstruction for the roe lexeme can be attached securely enough to justify promoting `*hrogn` from note-level placeholder to an explicit project target.
- If later work does confirm or revise the reconstruction, keep the three layers separate near the top of any report: comparative `PROTO/PROTOFORM *ráixōn`, live OE `COUNTERPART = -`, and reconstructed placeholder `*hrogn` [Germanic/data/germanic-aligned-final.tsv:877-877].
- Unless a new authority is attached, this slice should likely remain **no-index** or at most diagnostic-only in central indexing, because there is no securely current DEV_NOTES fragment to cite for a positive row-policy claim.
