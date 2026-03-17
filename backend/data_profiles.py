"""Detection and helpers for CAPR dataset profiles."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence, Tuple, List

from syllable_parser import build_syllable_parsed_entries, _STRESS_MARKERS


@dataclass(frozen=True)
class DataProfile:
    """Represents one dataset family and how syllables should be parsed."""

    key: str
    description: str
    allow_syllable_fallback: bool

    def segment_ipa(self, row: Mapping[str, str]) -> Sequence[str]:
        """Return a sequence of orthographic syllables.

        The default implementation leaves segmentation to the generic
        syllabizer; profiles override when the dataset provides better cues.
        """

        return []

    def build_syllables_parsed(
        self,
        row: Mapping[str, str],
        ipa_syllables: Sequence[str],
    ) -> List[Tuple[str, str]]:
        return build_syllable_parsed_entries(
            row.get("STRUCTURE", ""),
            row.get("TOKENS", ""),
            row.get("IPA", ""),
            ipa_syllables,
            allow_fallback=self.allow_syllable_fallback,
        )


class BurmishProfile(DataProfile):
    """Burmish retains the original IMRT-aware parsing."""

    # Base implementations are sufficient.


class GermanicProfile(DataProfile):
    """Germanic data carries C/V schemas; convert to IMRT on ingest."""

    def segment_ipa(self, row: Mapping[str, str]) -> Sequence[str]:
        groups = self._structured_groups(row)
        if groups:
            return ["".join(tok.replace(" ", "") for tok in tokens) for _, tokens in groups]
        ipa = (row.get("IPA") or "").replace(" ", "")
        return [ipa] if ipa else []

    def build_syllables_parsed(
        self,
        row: Mapping[str, str],
        ipa_syllables: Sequence[str],
    ) -> List[Tuple[str, str]]:
        groups = self._structured_groups(row)
        if groups and len(groups) == len(ipa_syllables):
            parsed: List[Tuple[str, str]] = []
            for (struct_tokens, symbol_tokens), ipa in zip(groups, ipa_syllables):
                entry = self._structured_imrt(struct_tokens, symbol_tokens, ipa)
                if entry is None:
                    return build_syllable_parsed_entries(
                        row.get("STRUCTURE", ""),
                        row.get("TOKENS", ""),
                        row.get("IPA", ""),
                        ipa_syllables,
                        allow_fallback=True,
                    )
                parsed.append(entry)
            return parsed

        return build_syllable_parsed_entries(
            row.get("STRUCTURE", ""),
            row.get("TOKENS", ""),
            row.get("IPA", ""),
            ipa_syllables,
            allow_fallback=True,
        )

    @staticmethod
    def _structured_groups(row: Mapping[str, str]) -> List[Tuple[List[str], List[str]]]:
        struct_tokens = [part for part in (row.get("STRUCTURE") or "").split() if part]
        token_tokens = [part for part in (row.get("TOKENS") or "").split() if part]
        if not struct_tokens or len(struct_tokens) != len(token_tokens):
            return []

        groups: List[Tuple[List[str], List[str]]] = []
        current_struct: List[str] = []
        current_tokens: List[str] = []
        last_case = struct_tokens[0].isupper()

        for struct_symbol, token_symbol in zip(struct_tokens, token_tokens):
            current_case = struct_symbol.isupper()
            if current_struct and current_case != last_case:
                groups.append((current_struct, current_tokens))
                current_struct = []
                current_tokens = []
            current_struct.append(struct_symbol)
            current_tokens.append(token_symbol)
            last_case = current_case

        if current_struct:
            groups.append((current_struct, current_tokens))

        return groups

    @staticmethod
    def _structured_imrt(
        struct_tokens: Sequence[str],
        symbol_tokens: Sequence[str],
        ipa_syllable: str,
    ) -> Tuple[str, str] | None:
        initial: List[str] = []
        medial: List[str] = []
        rhyme: List[str] = []
        tone: List[str] = []
        seen_vowel = False

        for struct_symbol, token_symbol in zip(struct_tokens, symbol_tokens):
            symbol = struct_symbol.upper()
            if symbol == "V":
                seen_vowel = True
                rhyme.append(token_symbol)
            elif symbol == "T":
                tone.append(token_symbol)
            elif symbol == "M":
                medial.append(token_symbol)
            elif seen_vowel:
                rhyme.append(token_symbol)
            else:
                initial.append(token_symbol)

        parts: List[Tuple[str, str]] = []
        if initial:
            parts.append(("i", " ".join(initial)))
        if medial:
            parts.append(("m", " ".join(medial)))
        if rhyme:
            parts.append(("r", " ".join(rhyme)))
        stress = "".join(ch for ch in ipa_syllable if ch in _STRESS_MARKERS)
        if stress:
            parts.append(("t", stress))
        if tone:
            parts.append(("t", " ".join(tone)))

        if not parts:
            return None

        positions = " ".join(position for position, _ in parts)
        tokens = " ".join(segment for _, segment in parts)
        return positions, tokens


# Canonical profiles currently supported by the pipeline.
BURMISH_PROFILE = BurmishProfile(
    key="burmish",
    description="Structured syllable tokens with tone markers",
    allow_syllable_fallback=False,
)
GERMANIC_PROFILE = GermanicProfile(
    key="germanic",
    description="Segmented IPA without explicit structure tokens",
    allow_syllable_fallback=True,
)

_PROFILE_ORDER = (BURMISH_PROFILE, GERMANIC_PROFILE)


def detect_profile(rows: Iterable[Mapping[str, str]]) -> DataProfile:
    """Infer the dataset profile based on TSV row contents.

    The current heuristics distinguish between datasets that retain explicit
    structure/token annotations (Burmish pipeline) and those that only provide
    plain IPA syllables (Germanic pipeline).
    """

    structured_hits = 0
    unstructured_hits = 0
    inspected = 0

    for inspected, row in enumerate(rows, start=1):
        tokens = (row.get("TOKENS") or "").strip()
        structure = (row.get("STRUCTURE") or "").strip()
        if tokens and " + " in tokens:
            structured_hits += 1
        elif structure and " + " in structure:
            structured_hits += 1
        elif tokens:
            unstructured_hits += 1
        elif structure:
            unstructured_hits += 1
        
        if inspected >= 100:
            break

    if structured_hits:
        return BURMISH_PROFILE
    if unstructured_hits:
        return GERMANIC_PROFILE

    # Fallback: default to Burmish profile so we keep strict checking, the
    # parser will simply return empty syllable slots if nothing is provided.
    return BURMISH_PROFILE


__all__ = [
    "DataProfile",
    "BURMISH_PROFILE",
    "GERMANIC_PROFILE",
    "detect_profile",
]
