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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 800)
        MainWindow.setMinimumSize(QSize(980, 680))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setSpacing(20)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(28, 28, 28, 28)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(6)
        self.titleLayout.setObjectName(u"titleLayout")
        self.eyebrow = QLabel(self.centralwidget)
        self.eyebrow.setObjectName(u"eyebrow")

        self.titleLayout.addWidget(self.eyebrow)

        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName(u"heading")

        self.titleLayout.addWidget(self.heading)

        self.subtitle = QLabel(self.centralwidget)
        self.subtitle.setObjectName(u"subtitle")

        self.titleLayout.addWidget(self.subtitle)


        self.headerLayout.addLayout(self.titleLayout)

        self.headerSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.arrivalButton = QPushButton(self.centralwidget)
        self.arrivalButton.setObjectName(u"arrivalButton")

        self.headerLayout.addWidget(self.arrivalButton)


        self.layout.addLayout(self.headerLayout)

        self.metricsLayout = QHBoxLayout()
        self.metricsLayout.setSpacing(16)
        self.metricsLayout.setObjectName(u"metricsLayout")
        self.presentCard = QFrame(self.centralwidget)
        self.presentCard.setObjectName(u"presentCard")
        self.presentLayout = QVBoxLayout(self.presentCard)
        self.presentLayout.setSpacing(5)
        self.presentLayout.setObjectName(u"presentLayout")
        self.presentLayout.setContentsMargins(18, 18, 18, 18)
        self.presentValue = QLabel(self.presentCard)
        self.presentValue.setObjectName(u"presentValue")

        self.presentLayout.addWidget(self.presentValue)

        self.presentCaption = QLabel(self.presentCard)
        self.presentCaption.setObjectName(u"presentCaption")

        self.presentLayout.addWidget(self.presentCaption)


        self.metricsLayout.addWidget(self.presentCard)

        self.totalCard = QFrame(self.centralwidget)
        self.totalCard.setObjectName(u"totalCard")
        self.totalLayout = QVBoxLayout(self.totalCard)
        self.totalLayout.setSpacing(5)
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalLayout.setContentsMargins(18, 18, 18, 18)
        self.totalValue = QLabel(self.totalCard)
        self.totalValue.setObjectName(u"totalValue")

        self.totalLayout.addWidget(self.totalValue)

        self.totalCaption = QLabel(self.totalCard)
        self.totalCaption.setObjectName(u"totalCaption")

        self.totalLayout.addWidget(self.totalCaption)


        self.metricsLayout.addWidget(self.totalCard)

        self.closedCard = QFrame(self.centralwidget)
        self.closedCard.setObjectName(u"closedCard")
        self.closedLayout = QVBoxLayout(self.closedCard)
        self.closedLayout.setSpacing(5)
        self.closedLayout.setObjectName(u"closedLayout")
        self.closedLayout.setContentsMargins(18, 18, 18, 18)
        self.closedValue = QLabel(self.closedCard)
        self.closedValue.setObjectName(u"closedValue")

        self.closedLayout.addWidget(self.closedValue)

        self.closedCaption = QLabel(self.closedCard)
        self.closedCaption.setObjectName(u"closedCaption")

        self.closedLayout.addWidget(self.closedCaption)


        self.metricsLayout.addWidget(self.closedCard)


        self.layout.addLayout(self.metricsLayout)

        self.recordsCard = QFrame(self.centralwidget)
        self.recordsCard.setObjectName(u"recordsCard")
        self.recordsLayout = QVBoxLayout(self.recordsCard)
        self.recordsLayout.setSpacing(16)
        self.recordsLayout.setObjectName(u"recordsLayout")
        self.recordsLayout.setContentsMargins(18, 18, 18, 18)
        self.recordsHeader = QHBoxLayout()
        self.recordsHeader.setObjectName(u"recordsHeader")
        self.recordsTitle = QLabel(self.recordsCard)
        self.recordsTitle.setObjectName(u"recordsTitle")

        self.recordsHeader.addWidget(self.recordsTitle)

        self.recordsSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.recordsHeader.addItem(self.recordsSpacer)

        self.refreshButton = QPushButton(self.recordsCard)
        self.refreshButton.setObjectName(u"refreshButton")

        self.recordsHeader.addWidget(self.refreshButton)


        self.recordsLayout.addLayout(self.recordsHeader)

        self.filters = QHBoxLayout()
        self.filters.setObjectName(u"filters")
        self.searchEdit = QLineEdit(self.recordsCard)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setClearButtonEnabled(True)

        self.filters.addWidget(self.searchEdit)

        self.openOnlyCheck = QCheckBox(self.recordsCard)
        self.openOnlyCheck.setObjectName(u"openOnlyCheck")

        self.filters.addWidget(self.openOnlyCheck)


        self.recordsLayout.addLayout(self.filters)

        self.visitsTable = QTableView(self.recordsCard)
        self.visitsTable.setObjectName(u"visitsTable")
        self.visitsTable.setAlternatingRowColors(True)
        self.visitsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.visitsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.visitsTable.setSortingEnabled(True)
        self.visitsTable.setShowGrid(False)

        self.recordsLayout.addWidget(self.visitsTable)

        self.emptyLabel = QLabel(self.recordsCard)
        self.emptyLabel.setObjectName(u"emptyLabel")
        self.emptyLabel.setWordWrap(True)
        self.emptyLabel.setAlignment(Qt.AlignCenter)

        self.recordsLayout.addWidget(self.emptyLabel)

        self.toolbar = QHBoxLayout()
        self.toolbar.setObjectName(u"toolbar")
        self.departureButton = QPushButton(self.recordsCard)
        self.departureButton.setObjectName(u"departureButton")

        self.toolbar.addWidget(self.departureButton)

        self.correctButton = QPushButton(self.recordsCard)
        self.correctButton.setObjectName(u"correctButton")

        self.toolbar.addWidget(self.correctButton)

        self.historyButton = QPushButton(self.recordsCard)
        self.historyButton.setObjectName(u"historyButton")

        self.toolbar.addWidget(self.historyButton)

        self.selectionSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbar.addItem(self.selectionSpacer)

        self.resultLabel = QLabel(self.recordsCard)
        self.resultLabel.setObjectName(u"resultLabel")

        self.toolbar.addWidget(self.resultLabel)


        self.recordsLayout.addLayout(self.toolbar)


        self.layout.addWidget(self.recordsCard)

        self.footer = QHBoxLayout()
        self.footer.setObjectName(u"footer")
        self.footerSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer.addItem(self.footerSpacer)

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
        self.eyebrow.setText(QCoreApplication.translate("MainWindow", u"SPR\u00c1VA SERVEROVNY", None))
        self.eyebrow.setProperty(u"role", QCoreApplication.translate("MainWindow", u"eyebrow", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Provozn\u00ed den\u00edk", None))
        self.subtitle.setText(QCoreApplication.translate("MainWindow", u"P\u0159\u00edstupy, p\u0159\u00edtomn\u00e9 osoby a historie n\u00e1v\u0161t\u011bv na jednom m\u00edst\u011b.", None))
        self.subtitle.setProperty(u"role", QCoreApplication.translate("MainWindow", u"subtitle", None))
        self.arrivalButton.setProperty(u"role", QCoreApplication.translate("MainWindow", u"primary", None))
        self.arrivalButton.setText(QCoreApplication.translate("MainWindow", u"+  Zapsat p\u0159\u00edchod", None))
        self.presentCard.setProperty(u"role", QCoreApplication.translate("MainWindow", u"card", None))
        self.presentValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.presentValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metric", None))
        self.presentCaption.setText(QCoreApplication.translate("MainWindow", u"Aktu\u00e1ln\u011b p\u0159\u00edtomn\u00e9 osoby", None))
        self.presentCaption.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metricLabel", None))
        self.totalCard.setProperty(u"role", QCoreApplication.translate("MainWindow", u"card", None))
        self.totalValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metric", None))
        self.totalCaption.setText(QCoreApplication.translate("MainWindow", u"Celkem evidovan\u00fdch n\u00e1v\u0161t\u011bv", None))
        self.totalCaption.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metricLabel", None))
        self.closedCard.setProperty(u"role", QCoreApplication.translate("MainWindow", u"card", None))
        self.closedValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.closedValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metric", None))
        self.closedCaption.setText(QCoreApplication.translate("MainWindow", u"Uzav\u0159en\u00e9 n\u00e1v\u0161t\u011bvy", None))
        self.closedCaption.setProperty(u"role", QCoreApplication.translate("MainWindow", u"metricLabel", None))
        self.recordsCard.setProperty(u"role", QCoreApplication.translate("MainWindow", u"card", None))
        self.recordsTitle.setText(QCoreApplication.translate("MainWindow", u"Evidence n\u00e1v\u0161t\u011bv", None))
        self.recordsTitle.setProperty(u"role", QCoreApplication.translate("MainWindow", u"section", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Obnovit", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hledat osobu, serverovnu nebo \u00fa\u010del\u2026", None))
        self.openOnlyCheck.setText(QCoreApplication.translate("MainWindow", u"Pouze p\u0159\u00edtomn\u00e9 osoby", None))
        self.emptyLabel.setText(QCoreApplication.translate("MainWindow", u"Zat\u00edm nejsou evidovan\u00e9 \u017e\u00e1dn\u00e9 n\u00e1v\u0161t\u011bvy.", None))
        self.emptyLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"subtitle", None))
        self.departureButton.setText(QCoreApplication.translate("MainWindow", u"Zapsat odchod", None))
        self.correctButton.setText(QCoreApplication.translate("MainWindow", u"Opravit z\u00e1znam", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"Historie z\u00e1znamu", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"0 z\u00e1znam\u016f", None))
        self.resultLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"subtitle", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.backupButton.setText(QCoreApplication.translate("MainWindow", u"Z\u00e1loha datab\u00e1ze", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed", None))
    # retranslateUi

