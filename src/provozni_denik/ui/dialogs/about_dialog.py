from datetime import datetime
from html import escape
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
            "dateValue": datetime.fromisoformat(date).astimezone().strftime("%d.%m.%Y %H:%M:%S %z") if date else "Nesestaveno — spuštěno ze zdrojů",
            "tagValue": info.get("git_tag", info.get("version")) or "Není dostupný",
            "commitValue": info["git_commit"][:7] if info.get("git_commit") else "Není dostupný",
            "pythonValue": info.get("python_version") or "Není dostupná",
        }
        for name, value in values.items():
            label = getattr(self.ui, name)
            label.setTextFormat(Qt.TextFormat.PlainText)
            label.setText(value)
        author = escape(info.get("author") or "Miroslav Pospíšil")
        self.ui.authorValue.setTextFormat(Qt.TextFormat.RichText)
        self.ui.authorValue.setText(f'<a href="https://mp00077.github.io" style="color: #087f83;">{author}</a>')
        self.ui.authorValue.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.ui.authorValue.setOpenExternalLinks(True)
        self.ui.authorValue.setToolTip("https://mp00077.github.io")
        self.ui.commitValue.setToolTip(info.get("git_commit") or "Není dostupný")
        if not date:
            self.ui.noteLabel.setText("Vývojové spuštění • Git údaje a Python odpovídají aktuálnímu prostředí.")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Close).setText("Zavřít")
        self.ui.buttonBox.rejected.connect(self.reject)
