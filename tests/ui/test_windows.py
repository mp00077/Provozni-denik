import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import tempfile
import unittest
from pathlib import Path
from PySide6.QtCore import QSettings
from PySide6.QtCore import QEventLoop, QTimer
from unittest.mock import patch
from PySide6.QtWidgets import QApplication
from provozni_denik.core.config import Config
from provozni_denik.infrastructure.database.connection import connect
from provozni_denik.infrastructure.database.repositories import SqliteVisitRepository
from provozni_denik.services.access_service import AccessService
from provozni_denik.services.audit_service import AuditService
from provozni_denik.services.export_service import ExportService
from provozni_denik.services.backup_service import BackupService
from provozni_denik.ui.windows.main_window import MainWindow
from provozni_denik.ui.dialogs.access_dialog import AccessDialog
from provozni_denik.ui.dialogs.history_dialog import HistoryDialog
from provozni_denik.ui.dialogs.settings_dialog import SettingsDialog
from provozni_denik.ui.dialogs.about_dialog import AboutDialog


class Identity:
    def current_actor(self):
        return "ui-test"


class WindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        from provozni_denik.ui.theme import apply_theme
        apply_theme(cls.app)

    def test_forms_save_filter_and_show_history(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Config(Path(directory))
            connection = connect(config.database_path)
            try:
                repository = SqliteVisitRepository(connection)
                identity = Identity()
                service = AccessService(repository, identity)
                window = MainWindow(service, AuditService(repository), ExportService(service),
                                    BackupService(connection, config.database_path), identity, config)
                with patch.object(window, "about_dialog") as about:
                    window.ui.aboutAction.trigger()
                    about.assert_called_once()
                dialog = AccessDialog(service, default_room="S1")
                dialog.ui.personEdit.setText("Testovací osoba")
                dialog.ui.purposeEdit.setText("Kontrola")
                dialog.save()
                self.assertEqual(dialog.result(), dialog.DialogCode.Accepted)
                window.refresh()
                self.assertEqual(window.proxy.rowCount(), 1)
                window.ui.visitsTable.selectRow(0)
                self.assertTrue(window.ui.departureButton.isEnabled())
                window.ui.searchEdit.setText("nenalezeno")
                self.assertEqual(window.proxy.rowCount(), 0)
                window.ui.searchEdit.clear()
                visit = service.list_visits()[0]
                correction = AccessDialog(service, visit=visit)
                correction.ui.purposeEdit.setText("Oprava")
                correction.ui.reasonEdit.setText("Upřesnění")
                correction.save()
                history = HistoryDialog(repository.audit(visit.id))
                self.assertEqual(history.ui.eventsTable.rowCount(), 2)
                self.assertIn("Kontrola", history.ui.detailsEdit.toPlainText())
                settings = QSettings(str(Path(directory) / "settings.ini"), QSettings.Format.IniFormat)
                settings_dialog = SettingsDialog(config, identity.current_actor(), settings)
                settings_dialog.ui.roomEdit.setText("S2")
                settings_dialog.save()
                self.assertEqual(settings.value("default_room"), "S2")
                service.depart(visit.id)
                window.refresh()
                window.ui.openOnlyCheck.setChecked(True)
                self.assertEqual(window.proxy.rowCount(), 0)
                for widget in (dialog, correction, history, settings_dialog, window):
                    widget.close()
            finally:
                connection.close()

    def test_about_shows_build_metadata_and_arbitrary_tag_as_plain_text(self):
        info = {"author": "Miroslav Pospíšil", "built_at": "2026-10-06T10:00:00+00:00",
                "git_tag": "release_<b>test</b>", "git_commit": "a" * 40, "python_version": "3.14.0"}
        with patch("provozni_denik.ui.dialogs.about_dialog.load_build_info", return_value=info):
            dialog = AboutDialog()
        self.assertIn("Miroslav Pospíšil", dialog.ui.authorValue.text())
        self.assertIn('href="https://mp00077.github.io"', dialog.ui.authorValue.text())
        self.assertTrue(dialog.ui.authorValue.openExternalLinks())
        self.assertIn("06.10.2026", dialog.ui.dateValue.text())
        self.assertEqual(dialog.ui.tagValue.text(), info["git_tag"])
        self.assertEqual(dialog.ui.commitValue.text(), info["git_commit"][:7])
        self.assertEqual(dialog.ui.commitValue.toolTip(), info["git_commit"])
        self.assertEqual(dialog.ui.pythonValue.text(), "3.14.0")
        dialog.close()

    def test_about_handles_development_without_git(self):
        with patch("provozni_denik.ui.dialogs.about_dialog.load_build_info", return_value={"built_at": None}):
            dialog = AboutDialog()
        self.assertIn("Nesestaveno", dialog.ui.dateValue.text())
        self.assertEqual(dialog.ui.tagValue.text(), "Není dostupný")
        self.assertEqual(dialog.ui.commitValue.text(), "Není dostupný")
        dialog.close()

    def test_background_export_and_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Config(Path(directory))
            connection = connect(config.database_path)
            try:
                repository = SqliteVisitRepository(connection)
                identity = Identity()
                service = AccessService(repository, identity)
                service.arrive("Osoba", "S1", "Kontrola")
                window = MainWindow(service, AuditService(repository), ExportService(service),
                                    BackupService(connection, config.database_path), identity, config)
                for method, filename in ((window.export, "data.csv"), (window.backup, "backup.sqlite3")):
                    destination = Path(directory) / filename
                    loop = QEventLoop()
                    timer = QTimer()
                    timer.setSingleShot(True)
                    timer.timeout.connect(loop.quit)
                    with patch("provozni_denik.ui.windows.main_window.QFileDialog.getSaveFileName",
                               return_value=(str(destination), "")), \
                         patch("provozni_denik.ui.windows.main_window.QMessageBox.information",
                               side_effect=lambda *args: loop.quit()) as success, \
                         patch("provozni_denik.ui.windows.main_window.QMessageBox.critical",
                               side_effect=lambda *args: loop.quit()) as failure:
                        method()
                        self.assertFalse(window.ui.backupButton.isEnabled())
                        timer.start(5000)
                        loop.exec()
                        timer.stop()
                        self.assertEqual(failure.call_count, 0)
                        self.assertEqual(success.call_count, 1)
                        self.assertTrue(destination.is_file())
                        self.assertTrue(window.ui.backupButton.isEnabled())
                other = connect(Path(directory) / "backup.sqlite3")
                try:
                    self.assertEqual(other.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0], 1)
                finally:
                    other.close()
                window.close()
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
