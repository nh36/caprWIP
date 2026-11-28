# I1: Component identity and isolation

The [third-cycle correction](../hiatus-cycle3/CHRONOLOGY.md) found that two families could both export `af_component_00.bin` into one directory while the first mapping still referred to it. The prospective runner uses the existing CAPR compiler but allocates a fresh directory per component family. It accepts exactly the compiler's sorted name-to-file mapping, does not cache candidate binaries, and verifies path resolution and binary digests before returning a mapping and again on receipt creation. The receipt binds exports to the frozen source, definition image, overlay text digest, ordered exports and Foma version. A mapping redirect, rename or binary replacement fails closed. Frozen stage cache verification remains the separate source/order/binary check in `cached_stages`.

The real compiler test first queries `IdAlpha`, then compiles `IdBeta` to the same numbered filename in a different directory and rechecks `IdAlpha`'s mappings, hashes and output. `IdAlpha` resolves only the dental probe, `IdBeta` only the nasal probe; both preserve preexisting *j*. The host tests also attempt a redirected mapping and an intentional overwrite.

```sh
cycle=Germanic/articles/hay/research/hiatus-cycle4
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "$cycle" -p test_components.py
bash "$cycle/run-container.sh" component_check --stage-cache /tmp/capr-hay-stress.lVemXDSn
```

The test receipt is not a chronology experiment. It does not modify any historical input, production stage or certified output.
