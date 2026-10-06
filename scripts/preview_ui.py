"""Vykreslí okna s dočasnými ukázkovými daty, bez buildu a bez provozní databáze."""
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


def main():
    from PySide6.QtCore import QSettings
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QFontDatabase
    from provozni_denik.ui.theme import apply_theme
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
    from provozni_denik.ui.windows.startup_window import StartupWindow

    class Identity:
        def current_actor(self):
            return "Ukázkový operátor"

    app = QApplication([])
    # Windows offscreen plugin neposkytuje systémovou databázi fontů.
    if sys.platform == "win32":
        for filename in ("segoeui.ttf", "segoeuib.ttf"):
            font_path = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts" / filename
            if font_path.is_file():
                QFontDatabase.addApplicationFont(str(font_path))
    apply_theme(app)
    output = ROOT / "docs/images"
    output.mkdir(parents=True, exist_ok=True)
    splash = StartupWindow()
    splash.show()
    splash.set_status("Připravuji databázi…")
    app.processEvents()
    splash.grab().save(str(output / "startup.png"))
    splash.finish()
    with tempfile.TemporaryDirectory() as directory:
        config = Config(Path(directory))
        connection = connect(config.database_path)
        try:
            repository = SqliteVisitRepository(connection)
            identity = Identity()
            access = AccessService(repository, identity)
            first = access.arrive("Jan Novák", "Serverovna A", "Pravidelná kontrola infrastruktury")
            access.arrive("Petra Svobodová", "Serverovna A", "Výměna síťového prvku", "Jan Novák")
            access.arrive("Tomáš Dvořák", "Serverovna B", "Kontrola záložního napájení")
            access.depart(first)
            access.correct(first, "Jan Novák", "Serverovna A", "Pravidelná kontrola serverů", "", "Upřesnění účelu návštěvy")
            settings = QSettings(str(Path(directory) / "preview.ini"), QSettings.Format.IniFormat)
            window = MainWindow(access, AuditService(repository), ExportService(access),
                                BackupService(connection, config.database_path), identity, config)
            window.settings = settings
            dialogs = [AccessDialog(access, default_room="Serverovna A"),
                       HistoryDialog(repository.audit(first)),
                       SettingsDialog(config, identity.current_actor(), settings), AboutDialog()]
            for widget, name in zip([window, *dialogs], ["main", "arrival", "history", "settings", "about"]):
                widget.show()
                app.processEvents()
                if widget is window:
                    window.ui.visitsTable.selectRow(0)
                    app.processEvents()
                widget.grab().save(str(output / f"{name}.png"))
                widget.hide()
            window.resize(window.minimumSize())
            window.show()
            app.processEvents()
            window.grab().save(str(output / "main-small.png"))
            window.close()
            for dialog in dialogs:
                dialog.close()
        finally:
            connection.close()
    print(f"Náhledy oken: {output}")


if __name__ == "__main__":
    main()
