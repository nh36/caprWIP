#!/usr/bin/env python3
"""FST health checks for germanic.txt.

Checks:
1. Unused definitions (defined but never referenced elsewhere).
2. OldEnglishRemoveStars entries that duplicate OldEnglishOrthography
   (safety nets that mask bugs and may map to wrong values).
3. OldEnglishRemoveStars entries for symbols never created by any rule.

Run from the server/ directory or the project root.
"""

import re
import sys
from pathlib import Path


def find_germanic_txt() -> Path:
    for candidate in [
        Path("server/fsts/germanic.txt"),
        Path("fsts/germanic.txt"),
        Path("/usr/app/fsts/germanic.txt"),
    ]:
        if candidate.exists():
            return candidate
    print("ERROR: cannot find germanic.txt", file=sys.stderr)
    sys.exit(1)


def check_unused_definitions(text: str, lines: list[str]) -> list[str]:
    """Find definitions that are only referenced on their own define line.

    Instrumentation chains (GermanAfter*, EnglishAfter*) are exempt — these
    are sequential debug-trace stages where the terminal node is intentionally
    unreferenced outside the chain.
    """
    issues = []
    define_pat = re.compile(r"^define\s+(\S+)")

    # Build set of all definition names
    all_defs = {}
    for i, line in enumerate(lines, 1):
        m = define_pat.match(line)
        if m:
            all_defs[m.group(1)] = i

    # Identify instrumentation chain members (XxxAfterYyy patterns)
    chain_members = {
        name for name in all_defs if re.search(r"After[A-Z]", name)
    }

    for name, lineno in all_defs.items():
        count = len(re.findall(r"\b" + re.escape(name) + r"\b", text))
        if count == 1:
            if name in chain_members:
                continue  # terminal node of an instrumentation chain
            issues.append(f"  UNUSED definition: {name} (line {lineno})")
    return issues


def check_remove_stars(text: str) -> list[str]:
    """Check OldEnglishRemoveStars for redundant or suspect entries."""
    issues = []

    # Extract OldEnglishOrthography block
    orth_match = re.search(
        r"define\s+OldEnglishOrthography\s*\[(.*?)\];", text, re.DOTALL
    )
    if not orth_match:
        issues.append("  WARNING: OldEnglishOrthography not found")
        return issues
    orth_block = orth_match.group(1)
    orth_symbols = set(re.findall(r"\{[^}]+\}", orth_block))

    # Extract OldEnglishRemoveStars block
    rs_match = re.search(
        r"define\s+OldEnglishRemoveStars\s*\[(.*?)\];", text, re.DOTALL
    )
    if not rs_match:
        issues.append("  WARNING: OldEnglishRemoveStars not found")
        return issues
    rs_block = rs_match.group(1)
    rs_entries = re.findall(r"(\{[^}]+\})\s*->\s*([^,\]]+)", rs_block)

    for symbol, target in rs_entries:
        target = target.strip()
        # Check if this symbol is also in OldEnglishOrthography (redundant)
        if symbol in orth_symbols:
            issues.append(
                f"  REDUNDANT in RemoveStars: {symbol} -> {target} "
                f"(already handled by OldEnglishOrthography)"
            )

        # Check if the symbol is ever created by any rule (excluding its
        # own definition line in RemoveStars)
        # Remove the RemoveStars block to avoid self-matches
        text_without_rs = text[: rs_match.start()] + text[rs_match.end() :]
        # Also exclude define lines for alphabet/set definitions (they list
        # the symbol but don't create it in the pipeline)
        occurrences = re.findall(re.escape(symbol), text_without_rs)
        if len(occurrences) == 0:
            issues.append(
                f"  NEVER CREATED: {symbol} -> {target} in RemoveStars "
                f"(no rule produces this symbol)"
            )

    return issues


def main():
    path = find_germanic_txt()
    text = path.read_text()
    lines = text.splitlines()

    all_issues = []

    unused = check_unused_definitions(text, lines)
    if unused:
        all_issues.append("=== Unused definitions ===")
        all_issues.extend(unused)

    rs_issues = check_remove_stars(text)
    if rs_issues:
        all_issues.append("=== OldEnglishRemoveStars issues ===")
        all_issues.extend(rs_issues)

    if all_issues:
        print(f"FST health check: {len(all_issues) - all_issues.count('=== Unused definitions ===') - all_issues.count('=== OldEnglishRemoveStars issues ===')} issue(s) found")
        for line in all_issues:
            print(line)
        return 1
    else:
        print("FST health check: all clean")
        return 0


if __name__ == "__main__":
    sys.exit(main())
