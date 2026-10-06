# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
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
    QFormLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.setMinimumSize(QSize(650, 400))
        self.layout = QVBoxLayout(AboutDialog)
        self.layout.setSpacing(20)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(28, 28, 28, 28)
        self.titleLabel = QLabel(AboutDialog)
        self.titleLabel.setObjectName(u"titleLabel")

        self.layout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(AboutDialog)
        self.subtitleLabel.setObjectName(u"subtitleLabel")

        self.layout.addWidget(self.subtitleLabel)

        self.form = QFormLayout()
        self.form.setObjectName(u"form")
        self.form.setVerticalSpacing(16)
        self.form.setHorizontalSpacing(24)
        self.authorCaption = QLabel(AboutDialog)
        self.authorCaption.setObjectName(u"authorCaption")

        self.form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.authorCaption)

        self.authorValue = QLabel(AboutDialog)
        self.authorValue.setObjectName(u"authorValue")
        self.authorValue.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        self.form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.authorValue)

        self.dateCaption = QLabel(AboutDialog)
        self.dateCaption.setObjectName(u"dateCaption")

        self.form.setWidget(1, QFormLayout.ItemRole.LabelRole, self.dateCaption)

        self.dateValue = QLabel(AboutDialog)
        self.dateValue.setObjectName(u"dateValue")
        self.dateValue.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        self.form.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateValue)

        self.tagCaption = QLabel(AboutDialog)
        self.tagCaption.setObjectName(u"tagCaption")

        self.form.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tagCaption)

        self.tagValue = QLabel(AboutDialog)
        self.tagValue.setObjectName(u"tagValue")
        self.tagValue.setWordWrap(True)
        self.tagValue.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        self.form.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tagValue)

        self.commitCaption = QLabel(AboutDialog)
        self.commitCaption.setObjectName(u"commitCaption")

        self.form.setWidget(3, QFormLayout.ItemRole.LabelRole, self.commitCaption)

        self.commitValue = QLabel(AboutDialog)
        self.commitValue.setObjectName(u"commitValue")
        self.commitValue.setWordWrap(True)
        self.commitValue.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        self.form.setWidget(3, QFormLayout.ItemRole.FieldRole, self.commitValue)

        self.pythonCaption = QLabel(AboutDialog)
        self.pythonCaption.setObjectName(u"pythonCaption")

        self.form.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pythonCaption)

        self.pythonValue = QLabel(AboutDialog)
        self.pythonValue.setObjectName(u"pythonValue")
        self.pythonValue.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        self.form.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pythonValue)


        self.layout.addLayout(self.form)

        self.noteLabel = QLabel(AboutDialog)
        self.noteLabel.setObjectName(u"noteLabel")
        self.noteLabel.setWordWrap(True)

        self.layout.addWidget(self.noteLabel)

        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.layout.addWidget(self.buttonBox)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"O aplikaci", None))
        self.titleLabel.setText(QCoreApplication.translate("AboutDialog", u"Provozn\u00ed den\u00edk", None))
        self.titleLabel.setProperty(u"role", QCoreApplication.translate("AboutDialog", u"title", None))
        self.subtitleLabel.setText(QCoreApplication.translate("AboutDialog", u"Evidence p\u0159\u00edstup\u016f do serverovny", None))
        self.subtitleLabel.setProperty(u"role", QCoreApplication.translate("AboutDialog", u"subtitle", None))
        self.authorCaption.setText(QCoreApplication.translate("AboutDialog", u"Autor", None))
        self.authorValue.setText("")
        self.dateCaption.setText(QCoreApplication.translate("AboutDialog", u"Datum sestaven\u00ed", None))
        self.dateValue.setText("")
        self.tagCaption.setText(QCoreApplication.translate("AboutDialog", u"Git tag", None))
        self.tagValue.setText("")
        self.commitCaption.setText(QCoreApplication.translate("AboutDialog", u"Git commit", None))
        self.commitValue.setText("")
        self.pythonCaption.setText(QCoreApplication.translate("AboutDialog", u"Verze Pythonu", None))
        self.pythonValue.setText("")
        self.noteLabel.setProperty(u"role", QCoreApplication.translate("AboutDialog", u"subtitle", None))
        self.noteLabel.setText(QCoreApplication.translate("AboutDialog", u"\u00dadaje identifikuj\u00ed sestaven\u00ed aplikace.", None))
    # retranslateUi

