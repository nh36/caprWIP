import tempfile
import unittest
from pathlib import Path

from components import ComponentBuild


class First:
    RULES = ("Zeta", "Alpha")

    @staticmethod
    def definitions():
        return "define Alpha a; define Zeta z;"


class Second:
    RULES = ("Beta",)

    @staticmethod
    def definitions():
        return "define Beta b;"


class ComponentIsolationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.source = self.root / "source"
        self.source.write_text("source")
        (self.root / "defined.bin").write_bytes(b"definition image")

    @staticmethod
    def compile(source, cache, directory, recipe):
        mapping = {}
        for index, name in enumerate(recipe.RULES):
            output = directory / f"af_component_{index:02d}.bin"
            output.write_text(name)
            mapping[f"component:{name}"] = output
        return mapping

    def build(self, family, compiler=None):
        return ComponentBuild(compiler or self.compile, self.source, self.root,
                              self.root, family, "test runtime")

    def test_second_family_cannot_overwrite_first_numbered_export(self):
        first = self.build(First)
        second = self.build(Second)
        alpha = first.verify()["component:Alpha"]
        beta = second.verify()["component:Beta"]
        self.assertEqual(alpha.name, beta.name)
        self.assertNotEqual(alpha.parent, beta.parent)
        self.assertEqual((alpha.read_text(), beta.read_text()), ("Alpha", "Beta"))
        self.assertNotEqual(first.identity, second.identity)
        self.assertEqual(first.receipt(), self.build(First).receipt())

    def test_swapped_mapping_is_rejected(self):
        def redirected(*args):
            mapping = self.compile(*args)
            mapping["component:Alpha"], mapping["component:Zeta"] = (
                mapping["component:Zeta"], mapping["component:Alpha"])
            return mapping

        with self.assertRaisesRegex(ValueError, "unexpected component mapping"):
            self.build(First, redirected)

    def test_binary_overwrite_is_rejected(self):
        first = self.build(First)
        first.verify()["component:Alpha"].write_bytes(b"wrong binary")
        with self.assertRaisesRegex(ValueError, "compiled component changed: component:Alpha"):
            first.verify()


if __name__ == "__main__":
    unittest.main()
