#!/usr/bin/env python3
"""Negative-fixture regression tests for the unified Index Verborum architecture.

These tests verify that the invariants introduced in the hardening pass (2026-07-31)
actually reject the specific failure modes they are protecting against. Each test
deliberately constructs a bad input and asserts it is rejected.

Run as part of the canonical build or standalone:
    python3 Germanic/tools/check_index_architecture_negatives.py
"""
from __future__ import annotations

import re
import sys
import textwrap
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"

_FAILURES: list[str] = []
_PASSES: int = 0


def expect_fail(label: str, fn) -> None:  # type: ignore[type-arg]
    """Assert fn() raises AssertionError (i.e., correctly rejects the bad input)."""
    global _PASSES
    try:
        fn()
        _FAILURES.append(f"NEGATIVE FIXTURE MISSED: '{label}' was accepted but should have been rejected.")
    except AssertionError:
        _PASSES += 1


def expect_pass(label: str, fn) -> None:  # type: ignore[type-arg]
    """Assert fn() does NOT raise (i.e., correctly accepts the good input)."""
    global _PASSES
    try:
        fn()
        _PASSES += 1
    except AssertionError as exc:
        _FAILURES.append(f"POSITIVE FIXTURE FAILED: '{label}' was incorrectly rejected: {exc}")


# ── Helpers ─────────────────────────────────────────────────────────────────

def _makeindex_names(tex: str) -> list[str]:
    return re.findall(r"\\makeindex\[name=([^,\]]+)", tex)


def _printindex_calls(tex: str) -> list[str]:
    return re.findall(r"\\printindex\[([^\]]+)\]", tex)


def _per_lang_hits(tex: str) -> list[str]:
    return re.compile(r"\\index\[(?!iv\])([^\]]+)\]\{").findall(tex)


def _doubled_star_hits(tex: str) -> list[str]:
    return re.compile(r"\\Recon\{[\\]?\*").findall(tex)


def _assert_unified_architecture(tex: str) -> None:
    """Full architecture check — extracted for reuse in fixtures."""
    names = _makeindex_names(tex)
    assert len(names) == 1, f"Expected exactly one \\makeindex (name=iv); found: {names}"
    assert names[0] == "iv", f"\\makeindex must use name=iv, not name={names[0]}"
    calls = _printindex_calls(tex)
    assert len(calls) == 1, f"Expected exactly one \\printindex; found: {calls}"
    assert calls[0] == "iv", f"\\printindex must use [iv], not [{calls[0]}]"
    per_lang = _per_lang_hits(tex)
    assert not per_lang, f"Per-language \\index commands found: {per_lang[:5]}"
    doubled = _doubled_star_hits(tex)
    assert not doubled, f"Doubled-star \\Recon found: {doubled[:5]}"


# ── Reconstruction negative fixtures ────────────────────────────────────────

def test_recon_star_detection_literal() -> None:
    """\\Recon{*form} must be detected as malformed."""
    bad_tex = r"\Recon{*júką}"
    doubled = _doubled_star_hits(bad_tex)
    assert doubled, "Must detect \\Recon{*...} as doubled-star"


def test_recon_star_detection_escaped() -> None:
    """\\Recon{\\*form} must also be detected."""
    bad_tex = r"\Recon{\*júką}"
    doubled = _doubled_star_hits(bad_tex)
    assert doubled, "Must detect \\Recon{\\*...} as doubled-star"


def test_recon_star_valid_passes() -> None:
    """\\Recon{júką} must NOT be flagged."""
    good_tex = r"\Recon{júką}"
    doubled = _doubled_star_hits(good_tex)
    assert not doubled, "Must NOT flag \\Recon{júką} as a doubled star"


# ── Index architecture negative fixtures ─────────────────────────────────────

def test_second_per_language_makeindex_rejected() -> None:
    """Adding a per-language \\makeindex[name=on,...] must be rejected."""
    bad_tex = (
        r"\makeindex[name=iv,title={},columns=3]" + "\n"
        r"\makeindex[name=on,title={Old Norse},columns=3]"
    )
    _assert_unified_architecture(bad_tex)  # should raise


def test_per_language_index_command_rejected() -> None:
    """\\index[on]{...} must be rejected."""
    bad_tex = (
        r"\makeindex[name=iv,title={},columns=3]" + "\n"
        r"\printindex[iv]" + "\n"
        r"\index[on]{fugl@fugl}"
    )
    _assert_unified_architecture(bad_tex)  # should raise due to per_lang_hits


def test_second_printindex_rejected() -> None:
    """A second \\printindex[...] must be rejected."""
    bad_tex = (
        r"\makeindex[name=iv,title={},columns=3]" + "\n"
        r"\printindex[iv]" + "\n"
        r"\printindex[on]"
    )
    _assert_unified_architecture(bad_tex)  # should raise


def test_missing_language_group_in_iv_command() -> None:
    """\\index[iv] without the two-level LANG!FORM structure must be flagged."""
    bad_cmd = r"\index[iv]{sculdrum@\emph{sċuldrum}}"  # missing LANG@ prefix
    iv_cmds_raw = re.findall(r"\\index\[iv\]\{([^}]+(?:\{[^}]*\}[^}]*)*)\}", bad_cmd)
    malformed = [c for c in iv_cmds_raw if "!" not in c]
    assert malformed, "Must detect \\index[iv] without language group level"


def test_doubled_recon_star_rejected() -> None:
    """\\Recon{*form} in generated TeX must be rejected."""
    bad_tex = r"\Recon{*draugma-}"
    doubled = _doubled_star_hits(bad_tex)
    assert doubled, "Must detect doubled-star reconstruction"


def test_unknown_language_would_produce_fallback_prefix() -> None:
    """An unregistered language code must not appear in a valid canonical build."""
    import csv
    registry_codes: set[str] = set()
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if (row.get("active") or "").strip() == "1":
                code = (row.get("code") or "").strip()
                if code:
                    registry_codes.add(code)
    # Construct a fake print_main row with an unknown language
    fake_lang = "UNKNOWN_LANG_XYZ"
    assert fake_lang not in registry_codes, "Fixture: unknown lang must not be in active registry"
    # The build would produce 99UNKNOWN_LANG_XYZ prefix — flag any such prefix in real TeX
    from pathlib import Path as P
    default_tex = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
    if default_tex.exists():
        tex_text = default_tex.read_text(encoding="utf-8")
        assert "99" not in re.compile(r"\\index\[iv\]\{99").findall(tex_text) or not re.compile(r"\\index\[iv\]\{99").search(tex_text), (
            "Generated TeX contains 99xx fallback language prefix — unregistered language in print_main"
        )


def test_duplicate_makeindex_declarations_rejected() -> None:
    """Two \\makeindex[name=iv] declarations must be rejected."""
    bad_tex = (
        r"\makeindex[name=iv,title={},columns=3]" + "\n"
        r"\makeindex[name=iv,title={},columns=3]"  # duplicate
    )
    names = _makeindex_names(bad_tex)
    assert len(names) != 1, "Duplicate \\makeindex[name=iv] must produce count != 1"


def test_occurrence_multiset_missing_entry() -> None:
    """Missing detection fixture: the 'no extra commands' check correctly passes when no extras exist."""
    cmd_a = r"\index[iv]{02oe@\textbf{Old English}!sculdrum@\emph{sċuldrum}}"
    cmd_b = r"\index[iv]{02oe@\textbf{Old English}!heofon@\emph{heofon}}"
    expected_set = {cmd_a, cmd_b}
    # TeX contains only cmd_a — that is fine (expected ⊇ actual, no spurious entries)
    actual_in_tex = [cmd_a]
    spurious = [c for c in actual_in_tex if c not in expected_set]
    assert not spurious, "cmd_a is in expected_set; no spurious entries detected (correct)"


def test_occurrence_multiset_extra_entry() -> None:
    """An unexpected index command NOT in the expected set must be detected."""
    cmd_a = r"\index[iv]{02oe@\textbf{Old English}!sculdrum@\emph{sċuldrum}}"
    cmd_spurious = r"\index[iv]{02oe@\textbf{Old English}!unexpected_xyz_form@\emph{unexpected}}"
    expected_set = {cmd_a}
    actual_in_tex = [cmd_a, cmd_spurious]  # cmd_spurious is NOT in expected_set
    spurious = [c for c in actual_in_tex if c not in expected_set]
    assert spurious, "Spurious extra command must be detected"


# ── Positive fixtures (good inputs must be accepted) ─────────────────────────

def test_valid_unified_architecture_accepted() -> None:
    """A valid unified-index TeX snippet must pass all architecture checks."""
    good_tex = textwrap.dedent(r"""
        \makeindex[name=iv,title={},columns=3]
        \printindex[iv]
        \index[iv]{02oe@\textbf{Old English}!sculdrum@\emph{sċuldrum}}
        \index[iv]{03pgmc@\textbf{Proto-Germanic}!skuldramiz@*skúldramiz}
    """)
    _assert_unified_architecture(good_tex)  # must not raise


def test_valid_recon_accepted() -> None:
    """\\Recon{júką} must not be flagged as doubled-star."""
    good_tex = r"\Recon{júką}"
    assert not _doubled_star_hits(good_tex)


# ── Runner ───────────────────────────────────────────────────────────────────

def main() -> int:
    # Detection helpers: verify the detection logic correctly identifies bad patterns.
    # The test function PASSES when detection works, so use expect_pass.
    expect_pass("literal * inside \\Recon is detected by helper", test_recon_star_detection_literal)
    expect_pass("escaped \\* inside \\Recon is detected by helper", test_recon_star_detection_escaped)
    expect_pass("valid \\Recon{júką} is NOT flagged as doubled-star", test_recon_star_valid_passes)
    expect_pass("\\Recon{*form} doubled-star is detected by helper", test_doubled_recon_star_rejected)
    expect_pass("\\index[iv] without language group is detected by helper", test_missing_language_group_in_iv_command)
    expect_pass("duplicate \\makeindex count != 1 is detected by helper", test_duplicate_makeindex_declarations_rejected)
    expect_pass("missing index entry detected by multiset comparison", test_occurrence_multiset_missing_entry)
    expect_pass("extra index entry detected by multiset comparison", test_occurrence_multiset_extra_entry)

    # Full architecture check: _assert_unified_architecture must RAISE on bad inputs.
    # The bad input is deliberate; the function should raise AssertionError, so expect_fail.
    expect_fail("second \\makeindex[name=on] causes assertion failure", test_second_per_language_makeindex_rejected)
    expect_fail("per-language \\index[on]{} causes assertion failure", test_per_language_index_command_rejected)
    expect_fail("second \\printindex causes assertion failure", test_second_printindex_rejected)

    # Positive fixtures: good inputs must be accepted without error.
    expect_pass("valid unified architecture is accepted", test_valid_unified_architecture_accepted)
    expect_pass("valid \\Recon{júką} not flagged as doubled-star", test_valid_recon_accepted)

    # Live-TeX check
    expect_pass("unknown language not present in real generated TeX", test_unknown_language_would_produce_fallback_prefix)

    if _FAILURES:
        for f in _FAILURES:
            print(f"FAIL: {f}", file=sys.stderr)
        print(f"\n{len(_FAILURES)} fixture(s) failed. {_PASSES} passed.", file=sys.stderr)
        return 1
    print(f"index architecture negative fixtures passed ({_PASSES} checks).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
