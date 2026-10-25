# SC035 focused evidence and domain assay

This is follow-up research SOURCE, not another lexical corpus, stage registry
or publication-order authority. The current decision is owned by the registry's
adjudication pointer. The earlier three adjudications and all frozen experiments
remain unchanged.

## Attestation population and verification

`attestations.tsv` records 51 observations. Join `witness` to `witnesses.tsv`
for manuscript/object date, exemplar, dialect qualification and dating authority.
No missing date is silently equated with a linguistic stage. These are edition
page-image checks, not a new collation of the manuscripts themselves.

The nine aligned entries on Sweet p.48 give four gi/gi pairs, one ge/ge,
two gi/ge and two ge/gi. Their Corpus counterparts all have ge. They are
27 records of nine related glossary entries, all belonging to the same inherited
prefix family, not 27 independent tests of the law's lexical generality.
The rest is a deliberately focused comparison, not a census or a frequency
sample. Repeated forms, words and witnesses do not acquire independent votes.

Sweet's own marginal Corpus references for EE189 and EE191 are misleading:
the actual Corpus entries are 503 and 505, not the printed margins 500 and 502.
The Corpus pages, Latin lemmata and back-references resolve them. The corrected
locators do not alter either spelling. EE207 explicitly reports the first
Epinal e corrected from i; this is a scribal observation, not a dated sound
change. Square brackets and Sweet's anomalous-form warnings are retained in
the spelling/status fields; no editorial asterisk is treated as reconstruction.

Toller1921 p.284 (held PDF sheet296), entry ge-, was checked against its page
image and https://bosworthtoller.com/46976. Its nine-way counts agree. Its
dictionary ga-eádun, Erf75 corresponds to Sweet's gaeadun, EE76. Do not silently
identify the locator systems or reproduce OCR's ga-eddun. Ep228 gybyrdid is
verified against Sweet p.50; Corpus2152 gibrec against p.107. The additional
Toller gi-mynd, Wright Vocabularies II53,73, remains secondary reporting:
CAPR's Wright holding is volume I, not a verification of volume II.

Primary pages checked: Sweet1885 pp.39-40,43-44,48-53,107,125-127,148-149,
188-189; Stevenson1840 p.7; Sweet1871 p.3. The Durham scan repeats some
printed pages: duplicate scan sheets are not duplicate attestations.
Navigation extraction is imperfect; significant spellings were read on images.

The manuscript dating is not copied from Berg's compressed tables. Lucas and
Lucas2012 p.67 places Epinal around or just before700; Lucas2016 p.11 places
Corpus in the first half of the ninth century. Hogg's earlier dates and Sweet's
absolute dating are therefore not silently retained as current certainty.
Erfurt's date remains explicitly disputed in the directly consulted accounts:
Hogg pp.5-6 assigns an early eighth-century manuscript, whereas Sweet pp.3-4
reports a late ninth-century continental hand. Neither date is used to date the
English vowel. A modern catalogue/facsimile assessment of this hand remains
unverified. Pheifer's 1974 critical edition and 1987 glossary study were not
obtained in full; the Toronto digital project required human verification.
These access gaps affect renewed manuscript collation/dating and the exceptional
ga reading, not the directly verified presence of mixed gi/ge in both copies.

## Comparative and negative evidence

RingeTaylor2014 p.206 supplies normalized comparative prefix citations:
Gothic ga-, Old Saxon gi-, Old High German gi-, and reconstructed PGmc/PWGmc
ga-. These are handbook comparisons, not newly located diplomatic manuscript
tokens. They establish inherited a and continental reduced reflexes, not a
shared English palatal-fricative sound change. The Pforzen database's externally
dated585-610 object supplies a separate ga comparison; its complete reading
and segmentation are not settled by the database's deliberately partial
translation. The earlier570-600 search summary is not adopted.

RingeTaylor pp.334-335 and Campbell pp.31,140-141,153-155 distinguish ordinary
weakness/fronting from stressed forms. Normalized geatwe/gear and guest/give/
sheep are source-backed stress or root-development contrasts, not additional
early same-environment raising witnesses. Vespasian bibod and independently
reported ni > ne support a wider history of weak vowels; resemblance or
parallel lowering does not establish bi substitution.

No independently established non-ga positive sharing the entire early
environment was found. No securely weak, short, unraised ae immediately after
the already-palatal fricative was verified either. Erfurt gaeadun is a real
candidate difficulty, but its related forms, vowel-initial root, transmission,
quantity and consonant value do not establish those premises. Gybyrdid does
not establish a separate y pathway. Internal modgidanc is genuine orthographic
evidence, not proof that the current single-word annotation covers compounds.

## Computational evidence

Run inside the verified backend:

```sh
python3 docs/sound_changes/audits/sc035-generality/verify.py
```

It reuses the existing isolated compiler and checked lookup. The 345 controls
test 300 annotation cases, 28 raising cases, four headed-foot diphthongization
cases, five ae-merger cases and eight later-lowering cases. Artificial onset,
bridge, head, length and palatal contrasts are explicitly not attestations.
The normalized post-raising gidyrstig/gibeaten shapes test only subsequent
lowering, not invented complete PGmc histories.

Annotation is a bounded citation-word recognizer: one initial short vowel,
a nonempty consonantal bridge and a following positively acute-marked head.
It accepts onsetless and clustered onsets but not hiatus, two pretonic vowels,
a long weak vowel, a grave-only head or an internal weak syllable following a
root head. These limits are reported, not promoted into historical prohibitions.
The raising consumer trusts the annotation; it does not re-infer lost stress.
It recognizes the immediately preceding phonetic fricative, not g-origin or
prefix membership. Other palatals, velars, labials and long/stressed vowels
do not satisfy it. No historical example in this investigation requires a
general stress-system refactor.

`evidence.json` is the new generated observation at the accepted base; it does
not replace frozen earlier comparisons. Normal runtime tests rerun the domain
predictions. The pre-existing live prosody verifier separately compares all
389 selected forms at every one of109 current stages, composed and incremental
outputs, complete believe/climb derivations and shaft/prefixed-shaft controls.
Its frozen two-model comparison already establishes that skipping raising can
preserve final e while failing to generate the early i. Repeating that entire
historical experiment under a new filename would add no independent evidence.
