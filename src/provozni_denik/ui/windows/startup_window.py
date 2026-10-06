from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from provozni_denik.ui.generated.startup_window import Ui_StartupWindow


class StartupWindow(QWidget):
    def __init__(self):
        super().__init__(None, Qt.WindowType.SplashScreen)
        self.ui = Ui_StartupWindow()
        self.ui.setupUi(self)
        self.setFixedSize(500, 290)
        self.finished = False
        icon = Path(__file__).resolve().parents[1] / "resources/icons/app.png"
        self.ui.iconLabel.setPixmap(QPixmap(str(icon)).scaled(
            56, 56, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def set_status(self, text):
        self.ui.statusLabel.setText(text)

    def finish(self):
        self.finished = True
        self.close()

    def closeEvent(self, event):
        if self.finished:
            event.accept()
        else:
            event.ignore()
