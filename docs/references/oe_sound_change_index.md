# OE sound-change quick index

Purpose: keep frequently used citations and exact search commands in one place so we do not re-hunt the same passages.

## Ringe + Taylor (LH Vol. 2)

- File: `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- Topic: general retraction / restoration of a; retraction after breaking; conditioning by single/geminate or sC + back vowel.
- Quick commands:
  - `rg -n "6.3.1 General retraction" docs/references/ringe_taylor_linguistic_history_vol2.txt`
  - `sed -n '10990,11020p' docs/references/ringe_taylor_linguistic_history_vol2.txt`

## Hogg (Grammar of Old English, Vol. 1)

- File: `docs/references/hogg_vol1.txt`
- Topic: "Restoration of a" before back vowels; low-vowel system recap.
- Quick commands:
  - `rg -n "Restoration of a" docs/references/hogg_vol1.txt`
  - `sed -n '5175,5205p' docs/references/hogg_vol1.txt`

## Implementation pointers (local code)

- A-restoration rule context: `server/fsts/germanic.txt` (`OldEnglishARestoration*` definitions).
- Pipeline order: `server/fsts/old_english_sandbox.txt`.

If line numbers drift after edits, re-run `rg` and update the `sed` ranges above.
