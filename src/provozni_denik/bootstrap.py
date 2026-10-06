import logging
import sys


def main() -> int:
    from PySide6.QtWidgets import QApplication, QMessageBox
    from provozni_denik.core.config import Config
    from provozni_denik.core.paths import data_directory
    from provozni_denik.core.logging_setup import configure_logging

    app = QApplication(sys.argv)
    app.setApplicationName("Provozní deník")
    app.setOrganizationName("ProvozniDenik")
    try:
        config = Config(data_directory())
        configure_logging(config.data_dir / "logs")
        from provozni_denik.application import run
        return run(app, config)
    except Exception:
        logging.exception("Inicializace aplikace selhala")
        QMessageBox.critical(None, "Provozní deník", "Aplikaci nelze spustit. Zkontrolujte diagnostický log a dostupnost datového adresáře.")
        return 1
