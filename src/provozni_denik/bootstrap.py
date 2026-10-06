import logging
import sys


def main() -> int:
    from PySide6.QtWidgets import QApplication, QMessageBox
    from PySide6.QtGui import QIcon
    from pathlib import Path
    from provozni_denik.core.config import Config
    from provozni_denik.core.paths import data_directory
    from provozni_denik.core.logging_setup import configure_logging

    app = QApplication(sys.argv)
    app.setApplicationName("Provozní deník")
    app.setOrganizationName("ProvozniDenik")
    from provozni_denik.ui.theme import apply_theme
    apply_theme(app)
    app.setWindowIcon(QIcon(str(Path(__file__).parent / "ui/resources/icons/app.png")))
    try:
        config = Config(data_directory())
        configure_logging(config.data_dir / "logs")
        from provozni_denik.application import run
        return run(app, config)
    except Exception:
        logging.exception("Inicializace aplikace selhala")
        QMessageBox.critical(None, "Provozní deník", "Aplikaci nelze spustit. Zkontrolujte diagnostický log a dostupnost datového adresáře.")
        return 1
