"""Isolate numbered Foma builds and bind each mapping to its inputs and bytes."""

import hashlib
import json
from pathlib import Path
from tempfile import mkdtemp
from types import MappingProxyType


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ComponentBuild:
    def __init__(self, compiler, source, cache, workspace, family, runtime):
        names = sorted(family.RULES)
        if len(set(names)) != len(names):
            raise ValueError("Duplicate component names")
        self.directory = Path(mkdtemp(prefix="components-", dir=workspace)).resolve()
        definitions = family.definitions()

        class Recipe:
            RULES = tuple(names)

            @staticmethod
            def definitions():
                return definitions

        self.configuration = MappingProxyType({
            "source_sha256": digest(source),
            "definition_image_sha256": digest(cache / "defined.bin"),
            "definitions_sha256": hashlib.sha256(definitions.encode()).hexdigest(),
            "runtime": runtime,
            "ordered_exports": tuple(names),
        })
        configured = json.dumps(dict(self.configuration), sort_keys=True).encode()
        self.identity = hashlib.sha256(configured).hexdigest()
        actual = compiler(source, cache, self.directory, Recipe)
        expected = {f"component:{name}": self.directory / f"af_component_{index:02d}.bin"
                    for index, name in enumerate(names)}
        if actual != expected:
            raise ValueError("Compiler returned an unexpected component mapping")
        self.paths = MappingProxyType(expected)
        self.hashes = MappingProxyType({key: digest(path) for key, path in expected.items()})

    def verify(self):
        for key, path in self.paths.items():
            if path.resolve() != path or digest(path) != self.hashes[key]:
                raise ValueError(f"{self.identity}: compiled component changed: {key}")
        return dict(self.paths)

    def receipt(self):
        self.verify()
        return {
            "identity": self.identity, "configuration": dict(self.configuration),
            "exports": {key: {"file": path.name, "sha256": self.hashes[key]}
                        for key, path in self.paths.items()},
        }
