# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setMinimumSize(QSize(640, 380))
        self.layout = QVBoxLayout(SettingsDialog)
        self.layout.setSpacing(18)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(28, 28, 28, 28)
        self.dialogTitle = QLabel(SettingsDialog)
        self.dialogTitle.setObjectName(u"dialogTitle")
        self.dialogTitle.setWordWrap(True)

        self.layout.addWidget(self.dialogTitle)

        self.dialogSubtitle = QLabel(SettingsDialog)
        self.dialogSubtitle.setObjectName(u"dialogSubtitle")
        self.dialogSubtitle.setWordWrap(True)

        self.layout.addWidget(self.dialogSubtitle)

        self.infoLabel = QLabel(SettingsDialog)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.layout.addWidget(self.infoLabel)

        self.form = QFormLayout()
        self.form.setObjectName(u"form")
        self.roomLabel = QLabel(SettingsDialog)
        self.roomLabel.setObjectName(u"roomLabel")

        self.form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.roomLabel)

        self.roomEdit = QLineEdit(SettingsDialog)
        self.roomEdit.setObjectName(u"roomEdit")
        self.roomEdit.setMaxLength(150)

        self.form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.roomEdit)


        self.layout.addLayout(self.form)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.layout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Informace a nastaven\u00ed", None))
        self.dialogTitle.setText(QCoreApplication.translate("SettingsDialog", u"Nastaven\u00ed", None))
        self.dialogTitle.setProperty(u"role", QCoreApplication.translate("SettingsDialog", u"title", None))
        self.dialogSubtitle.setText(QCoreApplication.translate("SettingsDialog", u"Informace o aplikaci a v\u00fdchoz\u00ed hodnoty pro nov\u00e9 n\u00e1v\u0161t\u011bvy.", None))
        self.dialogSubtitle.setProperty(u"role", QCoreApplication.translate("SettingsDialog", u"subtitle", None))
        self.infoLabel.setText("")
        self.roomLabel.setText(QCoreApplication.translate("SettingsDialog", u"V\u00fdchoz\u00ed serverovna", None))
        self.roomEdit.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"Nap\u0159. Serverovna A", None))
    # retranslateUi

