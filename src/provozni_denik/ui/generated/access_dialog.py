# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'access_dialog.ui'
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

class Ui_AccessDialog(object):
    def setupUi(self, AccessDialog):
        if not AccessDialog.objectName():
            AccessDialog.setObjectName(u"AccessDialog")
        AccessDialog.setMinimumSize(QSize(480, 300))
        self.layout = QVBoxLayout(AccessDialog)
        self.layout.setObjectName(u"layout")
        self.form = QFormLayout()
        self.form.setObjectName(u"form")
        self.personLabel = QLabel(AccessDialog)
        self.personLabel.setObjectName(u"personLabel")

        self.form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.personLabel)

        self.personEdit = QLineEdit(AccessDialog)
        self.personEdit.setObjectName(u"personEdit")
        self.personEdit.setMaxLength(150)

        self.form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.personEdit)

        self.roomLabel = QLabel(AccessDialog)
        self.roomLabel.setObjectName(u"roomLabel")

        self.form.setWidget(1, QFormLayout.ItemRole.LabelRole, self.roomLabel)

        self.roomEdit = QLineEdit(AccessDialog)
        self.roomEdit.setObjectName(u"roomEdit")
        self.roomEdit.setMaxLength(150)

        self.form.setWidget(1, QFormLayout.ItemRole.FieldRole, self.roomEdit)

        self.purposeLabel = QLabel(AccessDialog)
        self.purposeLabel.setObjectName(u"purposeLabel")

        self.form.setWidget(2, QFormLayout.ItemRole.LabelRole, self.purposeLabel)

        self.purposeEdit = QLineEdit(AccessDialog)
        self.purposeEdit.setObjectName(u"purposeEdit")
        self.purposeEdit.setMaxLength(1000)

        self.form.setWidget(2, QFormLayout.ItemRole.FieldRole, self.purposeEdit)

        self.escortLabel = QLabel(AccessDialog)
        self.escortLabel.setObjectName(u"escortLabel")

        self.form.setWidget(3, QFormLayout.ItemRole.LabelRole, self.escortLabel)

        self.escortEdit = QLineEdit(AccessDialog)
        self.escortEdit.setObjectName(u"escortEdit")
        self.escortEdit.setMaxLength(150)

        self.form.setWidget(3, QFormLayout.ItemRole.FieldRole, self.escortEdit)

        self.reasonLabel = QLabel(AccessDialog)
        self.reasonLabel.setObjectName(u"reasonLabel")

        self.form.setWidget(4, QFormLayout.ItemRole.LabelRole, self.reasonLabel)

        self.reasonEdit = QLineEdit(AccessDialog)
        self.reasonEdit.setObjectName(u"reasonEdit")
        self.reasonEdit.setMaxLength(1000)

        self.form.setWidget(4, QFormLayout.ItemRole.FieldRole, self.reasonEdit)


        self.layout.addLayout(self.form)

        self.errorLabel = QLabel(AccessDialog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setWordWrap(True)

        self.layout.addWidget(self.errorLabel)

        self.buttonBox = QDialogButtonBox(AccessDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.layout.addWidget(self.buttonBox)


        self.retranslateUi(AccessDialog)

        QMetaObject.connectSlotsByName(AccessDialog)
    # setupUi

    def retranslateUi(self, AccessDialog):
        AccessDialog.setWindowTitle(QCoreApplication.translate("AccessDialog", u"Zapsat p\u0159\u00edchod", None))
        self.personLabel.setText(QCoreApplication.translate("AccessDialog", u"Osoba *", None))
        self.roomLabel.setText(QCoreApplication.translate("AccessDialog", u"Serverovna *", None))
        self.purposeLabel.setText(QCoreApplication.translate("AccessDialog", u"\u00da\u010del vstupu *", None))
        self.escortLabel.setText(QCoreApplication.translate("AccessDialog", u"Doprovod", None))
        self.reasonLabel.setText(QCoreApplication.translate("AccessDialog", u"D\u016fvod opravy *", None))
        self.errorLabel.setText("")
    # retranslateUi

