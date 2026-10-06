from PySide6.QtWidgets import QDialog, QDialogButtonBox
from provozni_denik.core.version import VERSION
from provozni_denik.ui.generated.settings_dialog import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, config, actor, settings, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.settings = settings
        self.ui.infoLabel.setText(f"Provozní deník {VERSION}\nOperátor (účet OS): {actor}\n"
                                  f"Databáze: {config.database_path}\n"
                                  "Časy se zobrazují v časovém pásmu tohoto počítače.\n"
                                  "Lokální verze nemá samostatné přihlašování ani správu rolí.")
        self.ui.roomEdit.setText(settings.value("default_room", "", type=str))
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).setText("Uložit")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setText("Zrušit")
        self.ui.buttonBox.accepted.connect(self.save)
        self.ui.buttonBox.rejected.connect(self.reject)

    def save(self):
        self.settings.setValue("default_room", self.ui.roomEdit.text().strip())
        self.accept()
