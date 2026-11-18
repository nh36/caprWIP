# SC047/SC048 follow-up on the corrected SC059 control

Control commit: `d83324ce433f135d6ea58d307555768efe5b4a36`.
The manifest pins its FST/corpus and every archive member. The separate
SC059 commit adopts the exact earlier `unadopted-strict-ws.patch`;
its six-configuration experiment is in `../sc059-clause-evidence/`.
No SC047/SC048 rule, position, selected input, target or baseline is
changed by this follow-up. PR19 remains for review, not merge.

## Sources and preregistration

Read before specifying the first new variants: Ringe and Taylor2014
§2.3.1(i),pp.27--29 and §§3.1.2--3.1.3,pp.44--47;
Fulk2018 §§4.2--4.3,pp.55--57 and §5.6,pp.91--92. Ringe--Taylor29
argues lowering before low-final loss from a-stems versus root nouns;
45 explicitly accommodates that order. Fulk's u-lowering discussion is
**§4.3**, not the requested §4.2 (closed-syllable shortening);
57n1 contains the relevant ordering argument. Neither early apocope
nor late selected endpoint fit licenses a new weight condition.

Ringe--Taylor46 has sarwą > saru, rīkiją > **rīkī**, gelwaz > gelu;
47 uses i-/ja-stem reanalysis, mettas beside mete, OHG beti and the
surviving genitive sagjas to argue pre-gemination vocalization and
later paradigm extension. The source's long final ī is preserved.
Ringe--Taylor153--154 supplies bindandī, competing guma cells and
concrete levelling evidence; Fulk169--171 supplies inherited accusative
un and Ruthwell galgu, not an independently regular accusative an.
Hogg Phonology156--157 checks the staged West Saxon ealu control and
its distinction from a Mercian implementation. Prior source holdings
and access limitations in `../sc047-sc048-evidence/source-assessment.md`
remain explicit; no missing original is newly claimed as read.

Each snapshot contains its plan with predictions/falsifiers **before**
execution. Controlled comes first. Staged follows its result; resolution
then addresses the observed saru endpoint and protected-carrier difference.
Their failure to deliver every predicted endpoint is preserved.

## Full selected-corpus results

`evidence.json` is a mechanical projection of each archived observed.json:
all22 executions have394 rows, complete output sets and row-level
changes. Every identity is386 matches with the same eight inherited
mismatches: buck,fire,fowl,rust,straw,tap,wolf,wool. No baseline is
refrozen. All configurations are unambiguous. Only the before-SC023
negative rejects an input (do1991).

| Configuration | Matches | Changed |
|---|---:|---:|
|Control|386|0|
|SC047 alone before gemination|373|14|
|SC017 alone before gemination|386|0|
|SC017 then SC047 before gemination|384|3|
|Joint early loss plus postconsonantal nuclearization|381|6|
|SC047 after ordinary final-z deletion|384|2|
|SC047 after rhotacism|386|0|
|SC047 after SC041|386|0|
|SC047 before SC023, diagnostic negative|372|15|
|Early final-n proxy|379|7|
|Early wider coda|378|8|
|Wider coda plus nasal i-consumer|379|7|
|Plus onset fronting|379|7|
|Plus explicit nasal restoration trigger|386|0|
|Direct coda blocking|386|0|

The original14 deltas are all reproduced on the corrected control.
The [SC047 memorandum](../sc047-adjudication.md) gives every row,
first representation change and subsequent mechanism. Loss alone
removes13 SC017 firings: twelve change root-vowel endpoints; yoke2307
is masked by OEWsPalatalGlide. Early SC017 alone and the joint trial
retain exactly the original40 firings, including Rainbow's secondary
target, without any condition change or added application.

Deer1988 loses exposed z at the separate monosyllabic-z rule rather
than rhotacizing it; door1992 gains length after r becomes final.
Thus recovered lowering still gives dōr, not dor. Straw2224 loses
the input of adopted SC111 stráwą > stráu > stráeu > strēa.
These are not new historical dates for loss; no z/r or SC111 rewrite
is attempted. In the glide candidate, hay2061,net2138,hue2332 add
three changes, respectively hēa,nete,hii. Their actual full prefixes,
not inferred explanations or accepted analogy repairs, are archived.

## Staged diagnostics and unsolved derivations

The plans label PG inputs separately from stage-fed starred forms.
Root accents are CAPR encodings, not source diacritics. Bindandī is
West Germanic and does not enter the PG gate. Synthetic nasal/stress/
length pairs test the transducer, not unattested lexical histories.

Early apocope plus separately composed postconsonantal ij > ī,
j > i,w > u reaches saru/rīkī before gemination. Rīkī reaches rīċe;
medial j in sagjas still geminates. Saru instead fronts to særu,
misses rw breaking and is restored by SC046 to saru: **searu is not
solved**. The oral comparison reaches gelu locally, but its tested
continuation is ġielu, not ġeolu. These partial successes do not
justify adopting the glide candidate or reopening settled SC046.
Straw's postvocalic w is outside the proposed nuclearization.

Wider early coda nasalization gives bindąndī; without a nasal
i-consumer it yields bindande, while adding one recovers bindende.
The first nasal-fronting step bindændī is separately observed.
Incumbent oral a and direct blocking already yield bindende, so
the final spelling does not choose the intermediate. Bacan/wadan
distinguish restoration from nasality; lung2114 separates the missing
i-consumer. Long ā and acute á are not nasalization targets; à is.
Protected flaskōn and short flascan remain distinct routes.

Both wider-complete and direct candidates preserve the selected corpus,
but **they are not identical transducers**. A protected artificial
gumanô carrier gives gumena versus gumana because ô is not in the
ordinary vocalic class. Local ordinary ō/ā onset controls do front;
source-shaped ordinary gumanō/gumanā full continuations both give
unresolved gumne, not gumena. Different fronting checkpoints are
preserved even where endpoints agree. The carrier is not a literal
source quantity and cannot decide historical nasality.

All stages of the parallel guma inputs are retained. Ringe--Taylor's
accusative gumanų loses medial a before late high-tail loss and gives
gumn. Fulk-adapted gúmonų lacks early o > u and gives guman through
late o-lowering, not verified inherited un. Nom.pl. gúmaniz supplies
guman; gen.sg. gúminiz/dat.sg. gúmini yield unrelevelled gymen.
Dat.pl. gúmammaz gives gumemm live and gumamm under wide/direct,
not source gumum. Staged gumum is a checkpoint, not a completed
PG-to-OE derivation. Ringe--Taylor's accusative/nominative donors
and Fulk's inherited-un/other-case donors are not conflated.

Ringe--Taylor154 cites early WS tungna and poetic syncope, followed
by -ana (including early Mercian fingirdoccana and WS witnesses) and
dissimilation to -ena. This is positive evidence for the additional
genitive-plural paradigm history, not a free repair of gumne.
No analogy, grammatical conditioning or lexical diffusion is coded.

## Reproduction and validation cost

The zip contains exact source, corpus, sentence contexts, worker,
helper copies/hashes, plans, complete observations, completion files
and authentic command logs/receipts. Canonical corrected-source
SC047 evidence is also archived; SC048's unchanged upstream census
is recoverable from that same rebuilt full trace. No hand-picked
generator is used. This is not a new nearest-boundary sweep.

For an opt-in historical replay, extract a snapshot and stage its
captured worker/plan/source under the backend container. The worker
requires exact current FST, corpus, helper hashes and fresh canonical
bins, then executes its explicit definitions and expanded stage lists.
Read its captured CLI (`--worker SNAPSHOT`) and receipt; do not run
a source-mismatched historical worker against arbitrary current bins.
Normal tests authenticate results rather than rerunning the matrices.

The three SC047 matrices use22 variant executions and1621 finite
networks, one definition image plus one batched compiler per matrix.
Measured preparation:304.931/295.991/301.215seconds; private
compilation:5.569/9.073/3.805seconds. Peak preparation RSS:
2,243,696/2,243,788/2,245,812KiB. Exact values and total times are
in evidence.json. SC059's separate six-variant/27-network cost is
reported in its own archive, not hidden in these figures.

Regression-cost entry: four new frozen-evidence tests and one contextual
gloss regression (seven short Pandoc invocations); **no** new Foma
runtime compiler, shared fixture, sweep, production rebuild or
concurrency. The gloss repair preserves the scholarly prose, requires
an earlier glossed rīce and the exact rīċe discussion, and rejects
missing/later anchors, other contexts, Part II and changed quantities.
The failed first book receipt and pre-repair journal remain preserved;
the complete manuscript passed the repaired gate before adoption.
SC059 extends the existing one-network runtime assay
from four to twelve probes without adding a compiler or fixture.
Canonical evidence, final regeneration, strict serial/exclusive and
book rendering remain their separate required checks; receipts on
the final source state do not inherit c749's exact-commit certificate.

Disposition: retain SC047/SC048, adopt only the separately committed
SC059 condition correction. Early ordering, stranded-glide and
wider/direct-coda candidates remain reviewable experimental evidence.
