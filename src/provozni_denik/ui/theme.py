"""Společný profesionální motiv všech oken."""
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import QDialogButtonBox

STYLE = """
QWidget { color: #182b43; font-size: 13px; }
QMainWindow, QDialog { background: #f3f6fa; }
QLabel { background: transparent; }
QLabel#heading, QLabel[role="title"] { font-size: 27px; font-weight: 700; color: #142b46; }
QLabel[role="subtitle"] { color: #64748b; }
QLabel[role="eyebrow"] { color: #127d80; font-size: 11px; font-weight: 700; }
QFrame[role="card"] { background: white; border: 1px solid #dfe6ef; border-radius: 12px; }
QLabel[role="metric"] { font-size: 29px; font-weight: 700; color: #173753; }
QLabel#presentValue { color: #087f78; }
QLabel[role="metricLabel"] { color: #64748b; font-size: 12px; }
QLabel[role="section"] { font-size: 15px; font-weight: 700; }
QPushButton { background: white; border: 1px solid #ccd7e4; border-radius: 7px; padding: 9px 16px; font-weight: 600; min-height: 18px; }
QPushButton:hover { background: #eef4fa; border-color: #95abc2; }
QPushButton:pressed { background: #e0eaf4; }
QPushButton:focus { border: 2px solid #258f96; padding: 8px 15px; }
QPushButton:disabled { color: #98a6b8; background: #f5f7fa; border-color: #e4e9f0; }
QPushButton[role="primary"] { background: #087f83; color: white; border-color: #087f83; }
QPushButton[role="primary"]:hover { background: #06696d; border-color: #06696d; }
QPushButton[role="primary"]:disabled { background: #aacacb; border-color: #aacacb; }
QLineEdit, QPlainTextEdit { background: white; border: 1px solid #ccd7e4; border-radius: 7px; padding: 10px; selection-background-color: #087f83; }
QLineEdit:focus, QPlainTextEdit:focus { border-color: #087f83; }
QCheckBox { spacing: 9px; color: #42566f; }
QCheckBox::indicator { width: 17px; height: 17px; }
QTableView { background: white; alternate-background-color: #f8fafc; border: none; gridline-color: #edf1f6; selection-background-color: #dceff0; selection-color: #124e52; }
QTableView::item { padding: 8px; border-bottom: 1px solid #edf1f6; }
QTableView::item:selected { background: #dceff0; color: #124e52; }
QHeaderView::section { background: #f4f7fb; color: #53667f; font-weight: 600; padding: 12px 8px; border: none; border-bottom: 1px solid #dfe6ef; }
QStatusBar { background: #eaf0f6; color: #52667f; border-top: 1px solid #dfe6ef; }
QStatusBar::item { border: none; }
QLabel#errorLabel { color: #a72c37; background: #fff0f1; border-radius: 6px; padding: 10px; }
QToolTip { background: #173753; color: white; border: none; padding: 8px; }
QMenuBar { background: white; padding: 4px 12px; border-bottom: 1px solid #dfe6ef; }
QMenuBar::item { padding: 6px 12px; background: transparent; }
QMenuBar::item:selected { background: #dceff0; border-radius: 4px; }
QMenu { background: white; border: 1px solid #dfe6ef; padding: 6px; }
QMenu::item { padding: 8px 24px; }
QMenu::item:selected { background: #dceff0; color: #124e52; }
QProgressBar { background: #dfe9ef; border: none; border-radius: 4px; max-height: 8px; min-height: 8px; }
QProgressBar::chunk { background: #087f83; border-radius: 4px; }
"""


def apply_theme(app):
    app.setStyle("Fusion")
    font = QFont()
    font.setFamilies(["Segoe UI", "SF Pro Text", "Noto Sans", "DejaVu Sans"])
    font.setPointSize(10)
    app.setFont(font)
    palette = QPalette()
    for role, color in ((QPalette.ColorRole.Window, "#f3f6fa"), (QPalette.ColorRole.WindowText, "#182b43"),
                        (QPalette.ColorRole.Base, "#ffffff"), (QPalette.ColorRole.Text, "#182b43"),
                        (QPalette.ColorRole.Button, "#ffffff"), (QPalette.ColorRole.ButtonText, "#182b43"),
                        (QPalette.ColorRole.Highlight, "#087f83"), (QPalette.ColorRole.HighlightedText, "#ffffff")):
        palette.setColor(role, QColor(color))
    app.setPalette(palette)
    app.setStyleSheet(STYLE)


def style_dialog(dialog):
    save = dialog.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save)
    if save:
        save.setProperty("role", "primary")
        save.style().unpolish(save)
        save.style().polish(save)
    dialog.setSizeGripEnabled(True)
