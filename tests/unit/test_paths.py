import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from provozni_denik.core.paths import application_directory, data_directory


class PathTests(unittest.TestCase):
    def test_source_database_is_in_project_root(self):
        root = Path(__file__).resolve().parents[2]
        with patch.object(sys, "frozen", False, create=True):
            self.assertEqual(application_directory(), root)
            self.assertEqual(data_directory(), root / "db")

    def test_frozen_database_is_next_to_executable(self):
        executable = Path(__file__).resolve().parent / "ProvozniDenik.exe"
        with patch.object(sys, "frozen", True, create=True), \
             patch.object(sys, "platform", "win32"), patch.object(sys, "executable", str(executable)):
            self.assertEqual(data_directory(), executable.parent / "db")

    def test_mac_database_is_next_to_app_bundle(self):
        root = Path(__file__).resolve().parent
        executable = root / "provozní deník.app/Contents/MacOS/ProvozniDenik"
        with patch.object(sys, "frozen", True, create=True), \
             patch.object(sys, "platform", "darwin"), patch.object(sys, "executable", str(executable)):
            self.assertEqual(data_directory(), root / "db")
