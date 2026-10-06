# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_StartupWindow(object):
    def setupUi(self, StartupWindow):
        if not StartupWindow.objectName():
            StartupWindow.setObjectName(u"StartupWindow")
        StartupWindow.setMinimumSize(QSize(500, 290))
        self.layout = QVBoxLayout(StartupWindow)
        self.layout.setSpacing(16)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(32, 28, 32, 28)
        self.iconLabel = QLabel(StartupWindow)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMinimumSize(QSize(56, 56))

        self.layout.addWidget(self.iconLabel)

        self.titleLabel = QLabel(StartupWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.layout.addWidget(self.titleLabel)

        self.loadingLabel = QLabel(StartupWindow)
        self.loadingLabel.setObjectName(u"loadingLabel")

        self.layout.addWidget(self.loadingLabel)

        self.progressBar = QProgressBar(StartupWindow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setTextVisible(False)

        self.layout.addWidget(self.progressBar)

        self.statusLabel = QLabel(StartupWindow)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setWordWrap(True)

        self.layout.addWidget(self.statusLabel)


        self.retranslateUi(StartupWindow)

        QMetaObject.connectSlotsByName(StartupWindow)
    # setupUi

    def retranslateUi(self, StartupWindow):
        StartupWindow.setWindowTitle(QCoreApplication.translate("StartupWindow", u"Provozn\u00ed den\u00edk \u2014 na\u010d\u00edt\u00e1n\u00ed", None))
        self.iconLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("StartupWindow", u"Provozn\u00ed den\u00edk", None))
        self.titleLabel.setProperty(u"role", QCoreApplication.translate("StartupWindow", u"title", None))
        self.loadingLabel.setText(QCoreApplication.translate("StartupWindow", u"Na\u010d\u00edt\u00e1 se aplikace\u2026", None))
        self.loadingLabel.setProperty(u"role", QCoreApplication.translate("StartupWindow", u"section", None))
        self.statusLabel.setText(QCoreApplication.translate("StartupWindow", u"P\u0159ipravuji prost\u0159ed\u00ed\u2026", None))
        self.statusLabel.setProperty(u"role", QCoreApplication.translate("StartupWindow", u"subtitle", None))
    # retranslateUi

