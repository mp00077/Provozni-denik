# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName(u"heading")

        self.layout.addWidget(self.heading)

        self.toolbar = QHBoxLayout()
        self.toolbar.setObjectName(u"toolbar")
        self.arrivalButton = QPushButton(self.centralwidget)
        self.arrivalButton.setObjectName(u"arrivalButton")

        self.toolbar.addWidget(self.arrivalButton)

        self.departureButton = QPushButton(self.centralwidget)
        self.departureButton.setObjectName(u"departureButton")

        self.toolbar.addWidget(self.departureButton)

        self.correctButton = QPushButton(self.centralwidget)
        self.correctButton.setObjectName(u"correctButton")

        self.toolbar.addWidget(self.correctButton)

        self.historyButton = QPushButton(self.centralwidget)
        self.historyButton.setObjectName(u"historyButton")

        self.toolbar.addWidget(self.historyButton)

        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.toolbar.addWidget(self.refreshButton)


        self.layout.addLayout(self.toolbar)

        self.filters = QHBoxLayout()
        self.filters.setObjectName(u"filters")
        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setClearButtonEnabled(True)

        self.filters.addWidget(self.searchEdit)

        self.openOnlyCheck = QCheckBox(self.centralwidget)
        self.openOnlyCheck.setObjectName(u"openOnlyCheck")

        self.filters.addWidget(self.openOnlyCheck)


        self.layout.addLayout(self.filters)

        self.visitsTable = QTableView(self.centralwidget)
        self.visitsTable.setObjectName(u"visitsTable")
        self.visitsTable.setAlternatingRowColors(True)
        self.visitsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.visitsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.visitsTable.setSortingEnabled(True)

        self.layout.addWidget(self.visitsTable)

        self.footer = QHBoxLayout()
        self.footer.setObjectName(u"footer")
        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")

        self.footer.addWidget(self.exportButton)

        self.backupButton = QPushButton(self.centralwidget)
        self.backupButton.setObjectName(u"backupButton")

        self.footer.addWidget(self.backupButton)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")

        self.footer.addWidget(self.settingsButton)


        self.layout.addLayout(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Provozn\u00ed den\u00edk \u2014 serverovna", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Evidence p\u0159\u00edstup\u016f do serverovny", None))
        self.arrivalButton.setText(QCoreApplication.translate("MainWindow", u"Zapsat p\u0159\u00edchod", None))
        self.departureButton.setText(QCoreApplication.translate("MainWindow", u"Zapsat odchod", None))
        self.correctButton.setText(QCoreApplication.translate("MainWindow", u"Opravit z\u00e1znam", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"Historie z\u00e1znamu", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Obnovit", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hledat osobu, serverovnu nebo \u00fa\u010del\u2026", None))
        self.openOnlyCheck.setText(QCoreApplication.translate("MainWindow", u"Pouze p\u0159\u00edtomn\u00e9 osoby", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.backupButton.setText(QCoreApplication.translate("MainWindow", u"Z\u00e1loha datab\u00e1ze", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Informace a nastaven\u00ed", None))
    # retranslateUi

