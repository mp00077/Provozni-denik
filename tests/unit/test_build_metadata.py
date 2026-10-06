import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("build_metadata", ROOT / "scripts/build_metadata.py")
metadata = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = metadata
spec.loader.exec_module(metadata)


class MetadataTests(unittest.TestCase):
    def test_release_and_prerelease_tags(self):
        for tag, numeric in (("v1.2.3", (1, 2, 3, 0)), ("2.3.4.5", (2, 3, 4, 5)),
                             ("v1.2.3-rc.1", (1, 2, 3, 0))):
            version = metadata.parse_tag(tag)
            self.assertEqual(version.tag, tag)
            self.assertEqual(version.numbers, numeric)

    def test_arbitrary_tags_are_preserved_without_validation(self):
        for tag, numeric in (("release", (0, 0, 0, 0)), ("v1.2", (1, 2, 0, 0)),
                             ("1.2.65536", (0, 0, 0, 0)), ("1.2.3/extra", (1, 2, 3, 0)),
                             ("verze_2026_10", (2026, 10, 0, 0))):
            version = metadata.parse_tag(tag)
            self.assertEqual(version.tag, tag)
            self.assertEqual(version.numbers, numeric)
            self.assertIn(repr(tag), metadata.windows_version_text(version))

    def test_missing_git_tag_is_optional(self):
        with patch.object(metadata.subprocess, "run", side_effect=subprocess.CalledProcessError(128, "git")):
            self.assertIsNone(metadata.git_version(ROOT))
        with patch.object(metadata.subprocess, "run", side_effect=FileNotFoundError("git")):
            self.assertIsNone(metadata.git_version(ROOT))

    def test_untagged_metadata_keeps_author_without_version(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "packaging/icons").mkdir(parents=True)
            (root / "packaging/icons/app.ico").touch()
            with patch.object(metadata, "git_version", return_value=None):
                result = metadata.prepare_metadata(root, "win32")
            text = result["windows_version"].read_text(encoding="utf-8")
            self.assertIn("Miroslav Pospíšil", text)
            self.assertIn("provozní deník serverovny", text)
            self.assertNotIn("StringStruct('FileVersion'", text)
            self.assertNotIn("StringStruct('ProductVersion'", text)
            self.assertIn('"version": null', result["metadata"].read_text(encoding="utf-8"))

    def test_windows_resource_fields_without_building(self):
        # Na Windows zkontroluje skutečný parser version resources PyInstalleru.
        if sys.platform != "win32":
            self.skipTest("Parser Windows resources je dostupný na Windows.")
        try:
            from PyInstaller.utils.win32.versioninfo import load_version_info_from_text_file
        except ImportError:
            self.skipTest("Volitelná build závislost PyInstaller není nainstalovaná.")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "version.txt"
            path.write_text(metadata.windows_version_text(metadata.parse_tag("v2.4.6")), encoding="utf-8")
            info = load_version_info_from_text_file(str(path))
            self.assertEqual(info.ffi.fileVersionMS, (2 << 16) | 4)
            self.assertEqual(info.ffi.fileVersionLS, 6 << 16)
            fields = {item.name: item.val for item in info.kids[0].kids[0].kids}
            self.assertEqual(fields["CompanyName"], "Miroslav Pospíšil")
            self.assertEqual(fields["Author"], "Miroslav Pospíšil")
            self.assertEqual(fields["FileDescription"], "provozní deník serverovny")
            self.assertEqual(fields["FileVersion"], "v2.4.6")
            self.assertTrue(info.toRaw())

    def test_platform_metadata_and_icon_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "packaging/icons").mkdir(parents=True)
            for name in ("app.ico", "app.icns", "app.png"):
                (root / "packaging/icons" / name).touch()
            with patch.object(metadata, "git_version", return_value=metadata.parse_tag("v3.2.1")):
                for platform, name in (("win32", "app.ico"), ("darwin", "app.icns"), ("linux", "app.png")):
                    result = metadata.prepare_metadata(root, platform)
                    self.assertEqual(result["icon"].name, name)
                    self.assertIn("Miroslav Pospíšil", result["windows_version"].read_text(encoding="utf-8"))
                    self.assertIn('"version": "v3.2.1"', result["metadata"].read_text(encoding="utf-8"))
