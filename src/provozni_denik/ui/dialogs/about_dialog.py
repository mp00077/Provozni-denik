from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from provozni_denik.core.build_info import load_build_info
from provozni_denik.ui.generated.about_dialog import Ui_AboutDialog
from provozni_denik.ui.theme import style_dialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        style_dialog(self)
        info = load_build_info()
        date = info.get("built_at")
        values = {
            "authorValue": info.get("author") or "Miroslav Pospíšil",
            "dateValue": datetime.fromisoformat(date).astimezone().strftime("%d.%m.%Y %H:%M:%S %z") if date else "Nesestaveno — spuštěno ze zdrojů",
            "tagValue": info.get("git_tag", info.get("version")) or "Není dostupný",
            "commitValue": info.get("git_commit") or "Není dostupný",
            "pythonValue": info.get("python_version") or "Není dostupná",
        }
        for name, value in values.items():
            label = getattr(self.ui, name)
            label.setTextFormat(Qt.TextFormat.PlainText)
            label.setText(value)
        if not date:
            self.ui.noteLabel.setText("Vývojové spuštění • Git údaje a Python odpovídají aktuálnímu prostředí.")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Close).setText("Zavřít")
        self.ui.buttonBox.rejected.connect(self.reject)
