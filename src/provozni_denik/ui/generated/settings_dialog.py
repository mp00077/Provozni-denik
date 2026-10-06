# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
        SettingsDialog.setMinimumSize(QSize(550, 280))
        self.layout = QVBoxLayout(SettingsDialog)
        self.layout.setObjectName(u"layout")
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
        self.infoLabel.setText("")
        self.roomLabel.setText(QCoreApplication.translate("SettingsDialog", u"V\u00fdchoz\u00ed serverovna", None))
    # retranslateUi

