# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenlHCEBg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QWidget)
import banner_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(650, 450))
        self.centralwidget.setMaximumSize(QSize(650, 450))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"*{\n"
"	background: rgb(38, 38, 38);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(75, 30, 500, 161))
        self.label.setPixmap(QPixmap(u":/label/Yokobot-removebg-previewe.png"))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 190, 411, 31))
        self.label_2.setStyleSheet(u"*{\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	font-family: Noto Sans;\n"
"}")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(75, 290, 500, 23))
        self.progressBar.setStyleSheet(u"*{\n"
"	background: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"*:chunk {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")
        self.progressBar.setValue(50)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A chatbot propulsed by artificial intelligence.", None))
    # retranslateUi

