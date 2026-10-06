import logging
import sys


def main() -> int:
    from PySide6.QtWidgets import QApplication, QMessageBox
    from PySide6.QtGui import QIcon
    from pathlib import Path
    from PySide6.QtCore import QTimer

    app = QApplication(sys.argv)
    app.setApplicationName("Provozní deník")
    app.setOrganizationName("ProvozniDenik")
    from provozni_denik.ui.theme import apply_theme
    apply_theme(app)
    app.setWindowIcon(QIcon(str(Path(__file__).parent / "ui/resources/icons/app.png")))
    from provozni_denik.ui.windows.startup_window import StartupWindow
    splash = StartupWindow()
    app.setQuitOnLastWindowClosed(False)
    splash.show()
    session = None
    steps = None

    def advance():
        nonlocal session, steps
        try:
            if session is None:
                from provozni_denik.core.config import Config
                from provozni_denik.core.paths import application_directory, data_directory
                from provozni_denik.core.logging_setup import configure_logging
                configure_logging(application_directory() / "logs")
                from provozni_denik.application import ApplicationSession
                session = ApplicationSession(Config(data_directory()))
                steps = session.initialize()
            try:
                splash.set_status(next(steps))
            except StopIteration:
                session.window.show()
                splash.finish()
                app.setQuitOnLastWindowClosed(True)
                return
            # Nechat Qt vykreslit stav před dalším krokem a lazy importy.
            QTimer.singleShot(0, advance)
        except Exception:
            logging.exception("Inicializace aplikace selhala")
            splash.finish()
            if session is not None:
                session.close()
            QMessageBox.critical(None, "Provozní deník", "Aplikaci nelze spustit. Zkontrolujte diagnostický log a dostupnost datového adresáře.")
            app.exit(1)

    QTimer.singleShot(0, advance)
    try:
        return app.exec()
    finally:
        if steps is not None:
            steps.close()
        if session is not None:
            session.close()
        splash.finish()
