# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pagesqkjak.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 900, 600))
        self.frame.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0.142, x2:1, y2:0.880682, stop:0 rgba(254, 172, 94, 255), stop:1 rgba(199, 121, 208, 255));\n"
"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameFormulaire = QFrame(self.frame)
        self.frameFormulaire.setObjectName(u"frameFormulaire")
        self.frameFormulaire.setGeometry(QRect(275, 100, 350, 450))
        self.frameFormulaire.setStyleSheet(u"background: rgba(255, 255, 255, 0.8);\n"
"border-radius: 20px;\n"
"border: none;")
        self.frameFormulaire.setFrameShape(QFrame.StyledPanel)
        self.frameFormulaire.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.frameFormulaire)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(50, 140, 250, 35))
        self.username.setStyleSheet(u"background: rgba(0, 0, 0, 0.0);\n"
"border: 1px solid;\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(254, 172, 94, 255), stop:1 rgba(199, 121, 208, 255));\n"
"border-right-color: rgba(0, 0, 0, 0.0);\n"
"border-left-color: rgba(0, 0, 0, 0.0);\n"
"border-top-color: rgba(0, 0, 0, 0.0);\n"
"color: rgb(0, 0, 0);")
        self.password = QLineEdit(self.frameFormulaire)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(50, 230, 250, 35))
        self.password.setStyleSheet(u"background: rgba(0, 0, 0, 0.0);\n"
"border: 1px solid;\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(254, 172, 94, 255), stop:1 rgba(199, 121, 208, 255));\n"
"border-right-color: rgba(0, 0, 0, 0.0);\n"
"border-left-color: rgba(0, 0, 0, 0.0);\n"
"border-top-color: rgba(0, 0, 0, 0.0);\n"
"color: rgb(0, 0, 0);")
        self.ButtonValidation = QPushButton(self.frameFormulaire)
        self.ButtonValidation.setObjectName(u"ButtonValidation")
        self.ButtonValidation.setGeometry(QRect(80, 320, 190, 45))
        self.ButtonValidation.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(254, 172, 94, 255), stop:1 rgba(199, 121, 208, 255));\n"
"border-radius: 22px;")
        self.titre = QLabel(self.frameFormulaire)
        self.titre.setObjectName(u"titre")
        self.titre.setGeometry(QRect(80, 60, 190, 30))
        self.titre.setStyleSheet(u"background: rgba(0, 0, 0, 0.0);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 27px;\n"
"font-family: Noto Sans;")
        self.ButtonCreateAccount = QPushButton(self.frameFormulaire)
        self.ButtonCreateAccount.setObjectName(u"ButtonCreateAccount")
        self.ButtonCreateAccount.setGeometry(QRect(130, 410, 90, 20))
        self.ButtonCreateAccount.setStyleSheet(u"background: rgba(0, 0, 0, 0.0);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 12px;")
        self.titleBar = QFrame(self.frame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 900, 35))
        self.titleBar.setStyleSheet(u"background: rgba(39, 39, 39, 0.8);\n"
"border: none;")
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.minimizeButton = QPushButton(self.titleBar)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(825, 10, 15, 15))
        self.minimizeButton.setStyleSheet(u"background: rgb(84, 255, 117);\n"
"border: none;\n"
"border-radius: 7px;")
        self.bigscreenButton = QPushButton(self.titleBar)
        self.bigscreenButton.setObjectName(u"bigscreenButton")
        self.bigscreenButton.setGeometry(QRect(850, 10, 15, 15))
        self.bigscreenButton.setStyleSheet(u"background: rgba(255, 152, 55, 0.5);\n"
"border: none;\n"
"border-radius: 7px;")
        self.exitButton = QPushButton(self.titleBar)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(875, 10, 15, 15))
        self.exitButton.setStyleSheet(u"background: rgb(255, 55, 55);\n"
"border: none;\n"
"border-radius: 7px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre nom d'utilisateur.", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre mot de passe.", None))
        self.ButtonValidation.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.titre.setText(QCoreApplication.translate("MainWindow", u"Ah te revoil\u00e0 !!!!", None))
        self.ButtonCreateAccount.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un compte.", None))
        self.minimizeButton.setText("")
        self.bigscreenButton.setText("")
        self.exitButton.setText("")
    # retranslateUi

