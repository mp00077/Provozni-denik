# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QHeaderView, QPlainTextEdit, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        if not HistoryDialog.objectName():
            HistoryDialog.setObjectName(u"HistoryDialog")
        HistoryDialog.resize(850, 550)
        self.layout = QVBoxLayout(HistoryDialog)
        self.layout.setObjectName(u"layout")
        self.eventsTable = QTableWidget(HistoryDialog)
        self.eventsTable.setObjectName(u"eventsTable")
        self.eventsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.eventsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.eventsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.layout.addWidget(self.eventsTable)

        self.detailsEdit = QPlainTextEdit(HistoryDialog)
        self.detailsEdit.setObjectName(u"detailsEdit")
        self.detailsEdit.setReadOnly(True)

        self.layout.addWidget(self.detailsEdit)

        self.buttonBox = QDialogButtonBox(HistoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.layout.addWidget(self.buttonBox)


        self.retranslateUi(HistoryDialog)

        QMetaObject.connectSlotsByName(HistoryDialog)
    # setupUi

    def retranslateUi(self, HistoryDialog):
        HistoryDialog.setWindowTitle(QCoreApplication.translate("HistoryDialog", u"Auditn\u00ed historie", None))
    # retranslateUi

