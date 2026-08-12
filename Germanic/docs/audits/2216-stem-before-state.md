# Audit: row 2216 stem before-state (2026-08-12)

**Branch:** `stem-row-2216-correction`
**HEAD:** `046b8f6bb76a7050c66e2a1efa0f00a54c1be7ca`
**Status:** pre-correction evidence gate; no TSV or FST edits.

## Live TSV row
```tsv
ID	TOKENS	PROTOFORM	ALIGNMENT	IPA	COUNTERPART	COGIDS	DOCULECT	NOTE	HISTORY	DERIVATION_CLASS	STRUCTURE	BORROWING	CONCEPT	PROTO	GLOSSID
2216	s t e f n	*stámnaz	s t e f n	stefn	stefn	446	Old_English	Stem/trunk lexeme: PGmc *stámnaz (stem/trunk/prow family, Orel 2003:371). The *stébnō PROTOFORM previously assigned belongs to the unrelated OE homonym stefn/stemn "voice/sound" and has been removed. The coda mn→fn development (yielding OE stefn/stefna for stem/prow) is attested comparatively (ON stafn, OS stamn) but not yet modeled in the FST; derivation pending. Classified known_unmodelled until the relevant FST rule is implemented.		known_unmodelled			stem	*stámnaz	254
```

## Current cascade state
- Normalized input: `stámnaz`; outputs: `stamn`; multiplicity: 1; counterpart matched: no.
- Compact trace: `Proto Input *stámnaz -> EAF Final Z Deletion *stámna -> PWGmc Final Bare A Loss *stámn -> Outcome stamn`.
- Live mismatch bucket: `fronting_missing__also_wrong_form`; baseline row: `stem	*stámnaz	stámnaz	stefn	1	1	0	stamn`.
- Global OE baseline: accepted 380; matched 372; mismatched 8; ambiguous 0; outputs_sha256 `aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e`.
- Current mismatch set: buck, fire, fowl, rust, stem, tap, wolf, wool.
- Row 2216 is absent from `data/oe_known_problems.tsv`.

## Supporting-material inventory
- Present: `docs/lexeme_reports/model_entries/2216-stem-stefn.model.md`, `packets/2216-stem-stefn.md`, `research_memos/2216-stem-stefn.md`, `research_memo_index.tsv:101`, `docs/book/index_semantic_fingerprint_allowlist.tsv:2`.
- Absent or stale: no `report_manifest.tsv` entry; no row-2216 `dev_notes_slices` file; `coverage_audit.md:136` still says `early_analogy`; assembled `with_lexeme_reports*.md` still carry the older `*stébnō -> stefn` model layer.

This audit records the live row and baseline only; it makes no authoritative lexical change.
