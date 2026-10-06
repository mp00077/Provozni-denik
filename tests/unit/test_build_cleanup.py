import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("build_script", SCRIPTS / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class CleanupTests(unittest.TestCase):
    def test_removes_only_project_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("build", "dist/provozní deník", "dist/other-app", "src"):
                nested = root / name / "nested"
                nested.mkdir(parents=True)
                (nested / "file.txt").write_text("test")
            (root / "dist/notes.txt").write_text("keep")
            build.clean_outputs(root)
            self.assertFalse((root / "build").exists())
            self.assertFalse((root / "dist/provozní deník").exists())
            self.assertTrue((root / "dist/other-app/nested/file.txt").is_file())
            self.assertEqual((root / "dist/notes.txt").read_text(), "keep")
            self.assertTrue((root / "src/nested/file.txt").is_file())
            build.clean_outputs(root)  # Neexistující adresáře nejsou chyba.

    def test_validates_both_paths_before_removing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "build").mkdir()
            (root / "dist").write_text("not a directory")
            with self.assertRaises(RuntimeError):
                build.clean_outputs(root)
            self.assertTrue((root / "build").is_dir())

    def test_rejects_link_without_deleting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(Path, "is_symlink", return_value=True), \
                 patch.object(build.shutil, "rmtree") as remove:
                with self.assertRaises(RuntimeError):
                    build.clean_outputs(root)
                remove.assert_not_called()

    def test_rejects_linked_dist_parent_before_deleting_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "build").mkdir()
            with patch.object(Path, "is_symlink", autospec=True,
                              side_effect=lambda path: path == root / "dist"), \
                 patch.object(build.shutil, "rmtree") as remove:
                with self.assertRaises(RuntimeError):
                    build.clean_outputs(root)
                remove.assert_not_called()
