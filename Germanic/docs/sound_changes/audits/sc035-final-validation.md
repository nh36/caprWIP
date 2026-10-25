# SC035 final audit: validation and editorial closeout

Base: `976c1d07a9ba2703f19ef61e1fe89c2ebdf22cec`, branch `update`,
2026-10-25. Scientific authority remains the registered
`sc035-literature-adjudication.md`, explicitly amended by
`sc035-source-critical-audit.md` and `sc035-source-collation.md`.

## Scientific result versus documentary corrections

RETAIN/B stands after the historical A–D comparison, not because a final
output matches. The justified characterization is a qualified regular
working reconstruction of this prefix family, not a demonstrated
cross-lexical law or an obligatory independently proved phonemic i stage.
The current bounded phonological expression implements that hypothesis;
no concrete historical/formal defect justifies a grammar or chronology
change. SC036/SC037 were not adjudicated.

Editorial change log:

- Correct the false Sweet/Pheifer disagreement to *gihiodum*, Sweet p.40;
  identify Épinal f.1v/94v d line37 and distinguish h, possible hiatus,
  written final m, transmitted expansion and emendation.
- Correct Samuels's *gisihðe* and Corpus *gibrec* 'phlegm'.
- Preserve Pheifer's 'striped(?)' for *gybyrdid*; collate the nine paired
  entries and the other frozen observations without rewriting their ledger.
- Add the revised critical edition with full project editorial credit,
  manuscript/archetype separation, and the real Corpus *saegeseotu*
  difference. Reconcile Toller's *ga-eádun*, Erf75, by lemma and witness
  alignment, not an assumed universal numbering offset.
- Qualify the nominal-accent and equipment etymologies, Ringe/Taylor's
  modal proposal, lexical generality, source independence and competing
  explanations; keep detailed textual problems out of the main narrative.
- Add Seiler2017 only for its relevant source-layer caution. Record
  Seiler2019 as unread and Versloot's stressed-vowel scope as non-decisive;
  correct the latter's issue year while preserving its stable key.

## Fresh technical evidence

The running backend was checked before FST work: `/usr/app`,
`/usr/app/fsts`, `foma` and `flookup` were present. All compilation and
lookup ran inside that container, through the supported interface/tests.

1. `python3 Germanic/tools/adjudicate.py SC035 --evidence`:
   forced canonical stage-bin rebuild; production/sandbox equivalence
   on389 selected rows; one live firing, believe1944. The census's
   annotation-free presentation is
   `*ʝ*æ*l*ēa*β*j*ą*n` → `*ʝ*i*l*ēa*β*j*ą*n`.
   This is execution evidence, not another manuscript observation.
2. `python3 -m pytest -q
   Germanic/tests/test_sc035_prosody.py::test_fresh_adopted_cascade_and_phonological_components
   Germanic/tests/test_sc035_generality.py::test_fresh_phonological_domain_and_registered_original_holdings
   Germanic/tests/test_cascade_baseline.py`:
   **18 passed, six subtests passed**. The tests exercise the current
   full selected cascade, composed/incremental equivalence, climb and
   creation/shaft controls, the345-case domain assay, actual original
   holding hashes and protected population/output baselines.

Earlier compressed/fronting-merger/raising model-comparison and displacement
receipts were reread and preserved, not rerun or overwritten. Their
labels are distinct from the final historical A–D comparison.
Synthetic boundary controls establish formal behavior only. Portable
checks establish documentary coherence only. Neither establishes the
historical correctness of a reconstructed vowel or phonemic contrast.

## Documentary and publication closeout

`python3 Germanic/tools/adjudicate.py SC035 --finalize` completed with
CONTROL PLANE CLEAN and propagation checks passed.
`python3 Germanic/tools/artifact_graph.py --check --mode full` also
reported CONTROL PLANE CLEAN.

The final portable command was `python3 -m pytest -q -m 'not runtime'`
with `test_sc035_prefix_reduction.py`, `test_sc035_model_comparison.py`,
`test_sc035_prosody.py`, `test_sc035_generality.py`,
`test_cascade_baseline.py`, `test_chapter_citation_ranges.py`,
`test_adjudication_protocol_guardrails.py` and `test_reader_architecture.py`
under `Germanic/tests/`: **98 passed, five runtime tests deselected,
33 subtests passed**. The additional coverage test resolves each
apparatus coverage key against the actual frozen IDs and requires
exactly one current apparatus mapping per observation.

`INDEX_VERBORUM_STRICT=1 bash
Germanic/docs/assembly/build_capr_book_draft_docker.sh` completed
successfully for the revised reader, lexical volume and combined book.
It reported zero paragraph-gloss violations, zero unresolved internal
references, passing bibliography/index policy and heading-wrap checks,
zero residual sect/sects locators in the checked combined TeX/PDF, and
18 passing index-architecture negative fixtures. Repeated Pandoc
“Ticker: poll failed: Interrupted system call” messages were nonfatal;
the command exited0 and the explicit final gates passed.

Actual rendered SC035 pages were opened and inspected: standalone reader
pp.77–80, combined book printed pp.77–80 (PDF sheets79–82). The count
table, h/gy/þ/æ letters, macrons, accents, reconstructed asterisks,
superscript context marker, rule box, section symbols in the combined
citations and SC cross-references render legibly without clipped content.
The chapter is continuous and proportionate; no source-file paths or
internal evidence-row IDs appear in its prose. The new critical-edition
and Seiler bibliography entries were also inspected (reader sheets104–105,
combined sheets289/291); edition credit and title accents are intact.
Bibliographic page breaks do not lose entry text. Text extraction from
both published projections independently confirms *gihiodum*,
*saegeseotu*, Herren2026 and Seiler2017, and no *gibiodun* in SC035.

| Published PDF | SHA256 |
|---|---|
| Standalone reader | `c063e7b8a2175b9994e7aac4a0547a90c9f23fe048a7668f5936cd97cd5018ab` |
| Lexical volume | `0fb3b61370fbdf27b793953ac528e8b3fa9e6ca93c1f80517b66b1bb3693432c` |
| Combined book | `1371c708791ba0b796eec54d4650dd34c682d0e8801abaa84117df4bcf54f969` |

## Frozen and scientific invariants

The final comparison is against the base commit, not a newly adopted
baseline. No selected vocabulary, reconstruction, stress input, stage,
scope, confidence, FST definition, chronology edge or protected receipt
changed. A byte comparison verified72 scientific SOURCE/frozen files,
including the FST, corpus, registries, chronology, baseline directory and
all four earlier experiment directories, identical to the base.
SC036/SC037 reader sources are unchanged. The live totals remain389
selected,381 matches, eight mismatches,167 assembled lexical entries.

| Invariant | SHA256 |
|---|---|
| FST source | `421e7ae9c0a705f910e081e20242f8f7b3a42731b9dc908124217d32826a9d77` |
| Corpus source | `d40b6e65280d4cbe8acb08271803ef8acc64b3ff8e6b2656d416951aebdfa0a0` |
| Frozen51 ledger | `2a40862514f052edc7ffeb0b039d09205bddd304473d83c6f8a59975f1e998cf` |
| Selected389 output identity | `53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e` |
| Legacy380 identity | `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce` |
| Lexical projection | `c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da` |
| Immutable archive | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

## Unresolved-issue classification

| Classification | Finding and publication consequence |
|---|---|
| Resolved | The supposed Sweet/Pheifer h/b disagreement, wrong Sweet page, Samuels's dropped h, Corpus gloss and Versloot issue year are corrected traceably. No identified OCR error remains as active phonological evidence. |
| Genuine scholarly disagreement, accurately represented | Dental/accent reconstruction, equipment etymology, discrete versus allophonic raising, bi influence and the precise early phonetic pathway remain open. A working regular account is preferred without representing alternatives as disproved. |
| Unverified but non-decisive, excluded or qualified | Original Erfurt/Rushworth and most other manuscript readings, the underlying EE207 correction, Pheifer's conversion-lost diacritics, unread Seiler2019 and uncollated older facsimiles. Campbell/Ringe–Taylor were checked through local text, not newly acquired original page images. No decisive phonetic or accent distinction is inferred from those unverified details. |
| Publication-blocking defect | None remains identified after source criticism, historical/formal review, supported regeneration and actual output inspection. |

The material citations have been checked at the level explicitly stated
in A01–A35: image, original, published text, or qualified local searchable
text. That is not a claim that every original manuscript or every lost
diacritic has been independently verified. The chapter represents the
scholars' positions with their modal qualifications, and its regularity
claim no longer exceeds the available independent evidence.

## Final judgment: PASS

| Required question | Explicit conclusion |
|---|---|
| OCR/print-conversion errors still treated as linguistic evidence? | No identified error remains active. C01/C02 correct transcription errors; the unchanged frozen ledger is expressly overridden, not silently trusted. |
| Important letters/diacritics still unverified? | Yes at the expressly qualified levels above, but none supplies a decisive vowel, accent, counterexample or chronology premise. The key h, gy and Corpus gi were checked on original images. |
| All material citations checked against actual sources? | Yes to the documented level in A01–A35, including explicitly text-only holdings; not a claim of complete manuscript collation or restoration of conversion-lost typography. |
| Positions fairly represented? | The nominal/dental premises, competing equipment etymologies, Ringe/Taylor's modal language and the strongest historical A–D alternatives are distinguished from CAPR's preference. |
| Asserted regularity stronger than independent evidence? | Not in the revised claim: qualified regular prefix-family reconstruction, no demonstrated unrelated-family generality or obligatory phonemic stage. |
| Implementation faithful? | Yes for one marked initial short weak syllable after ʝ, with positive headed-domain evidence. Wider internal/hiatus/stacked structures are not claimed as parsed. Fresh controls and corpus checks pass. |
| Published chapter coherent, proportionate and documented? | Yes on the inspected output; detailed textual collation is in the apparatus and the reader explains the phenomenon, disagreement, preference and bounded implementation. |

This is a publication-readiness judgment with bounded uncertainty, not
scholarly unanimity or a new scientific baseline. Stop at SC035.
