# SC059 clause separation: current-source follow-up

Base: `c7497b7de23c8e9c43d568454be317b3f918ffde`, PR19. This is a new,
immutable experiment, not a rewrite or a fresh certification of the earlier
29-configuration SC047/048 archive. The original
`sc047-sc048-evidence/unadopted-strict-ws.patch` is preserved byte-for-byte;
its five separately composed clauses are the candidate implemented here.

## Literature and falsification

Ringe and Taylor2014, pp.319--327, especially p.325, distinguish West Saxon
e/u mutation from non-West-Saxon e/a mutation: Mercian weofan contrasts with
West Saxon wefan. Hogg, *A Grammar of Old English*, volume1, pp.149--157,
§§5.103--106, distinguishes the dialectal conditions; pp.156--157,
§5.106(2), n.6, supplies West Saxon ealu through earlier ælu, with æ due
to i-mutation in the inflected paradigm. These passages were consulted in
the held originals. Neither reference independently dates nasalization
from the old steal/weave displacement.

Before execution the pinned plan predicted unchanged394 selected output
sets, an e/u positive and e/a negative in each eligible stress encoding,
an eligible æ/u and æ/a positive, no medial unmarked-target mutation,
staged ealu, and preservation of the adopted rainbow trace. Failure of
any of those observations would refute this minimal implementation.
The old versus separated SC059-after-SC078 comparison was explicitly
exploratory: its result was not presumed to equal the baseline.

## Executed matrix

Every configuration uses identical selected inputs, contexts and targets.
The archive records all394 complete output sets, not just match counts.

| Configuration | Matches | Changed output sets | Rejected / ambiguous |
|---|---:|---:|---:|
| Current parallel-clause control |386|0|0 /0|
| Separate clauses, same order |386|0|0 /0|
| Old clauses, SC048 after SC059 |384|2|0 /0|
| Separate clauses, SC048 after SC059 |386|0|0 /0|
| Old SC059 after SC078 |384|2|0 /0|
| Separate SC059 after SC078 |382|4|0 /0|

Both old displacements give steal2215 steolan and weave2281 weofan.
Those are artifacts of the earlier parallel relation's shared a context.
The separated delayed-nasalization run gives stelan and wefan.
The separated delayed-back-mutation run instead changes heaven2068
heofon→hefon, milk2126 meoloc→meloc, seven2174 seofon→sefon and world2302
weorold→werold. At that later checkpoint their original medial u triggers
have become o; spear2206 retains its final u and still mutates. This
assay crosses multiple operations and does not establish SC078 itself
as the first failing boundary or independently date historical mutation.

The compiled local relation gives initial stelun→steolun but retains
stelan, with parallel acute and secondary-grave controls. Ælu→ealu and
æla→eala are positive; dental and unstressed-medial controls remain
unchanged. Staged ælu, supplied immediately before SC059 rather than as
a fabricated Proto-Germanic lexical input, reaches ealu.

Rainbow2148 still has secondary u→o at SC017, short unstressed æ through
SC046 and corrected SC059, deletion at SC114, and stop b after n. Its
endpoint remains reġnboga; simplex boga and earthly eorþcunde remain.
The constructed secondary-root control still gives reġnbecan, displaying
the already known later weak-fronting limitation. The wholly unaccented
constructed second-member control gives reġnhbon; it is a transducer
probe, not a claimed lexical derivation.

## Reproducibility and cost

`manifest.json` binds the original source, corpus, archived starting patch,
candidate source and every `experiment.zip` member. The snapshot contains
the exact worker, preregistered plan, helper copies, source/context inputs,
execution logs and completion receipt. To reproduce, extract it, use the
recorded source and helpers in a fresh backend environment, establish
canonical bin freshness, and run `python3 worker.py --worker SNAPSHOT`.
Do not point its assertions at a changed production source.

This opt-in assay used six configurations and27 finite-domain networks:
one common-definition preparation and one private compilation, with no
production-bin writes. Measured preparation305.91s, private compilation
3.61s, total310.40s; peak Foma child RSS2,210,116KiB (Linux `wait4`).
Routine regressions authenticate the record without recompiling it.
The existing single-network staged runtime test is extended with paired
e/u and e/a inputs, not another compiler or a wider fixture scope.
Full strict certification is reserved for the final coherent follow-up,
not repeated for this intermediate discrete commit.
