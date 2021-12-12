# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subscribe_pageBexyNq.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"*{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.858, y2:0.847, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"*{\n"
"	background: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"*{\n"
"	background: none;\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-family: Noto Sans;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setStyleSheet(u"*{\n"
"	background: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(15, 15))
        self.pushButton_3.setStyleSheet(u"*{\n"
"	background: rgb(84, 255, 117);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(15, 15))
        self.pushButton_4.setStyleSheet(u"*{\n"
"	background: rgb(255, 152, 55);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(15, 15))
        self.pushButton_2.setStyleSheet(u"*{\n"
"	background: rgb(255, 55, 55);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 25, -1, 25)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(350, 0))
        self.frame_5.setMaximumSize(QSize(375, 16777215))
        self.frame_5.setStyleSheet(u"*{\n"
"	background: rgba(255, 255, 255, 0.8);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, -1, 60, -1)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"*{\n"
"	background: none;\n"
"	font-family: Noto Sans;\n"
"	font-size: 16px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"*{\n"
"	background: rgba(0, 0, 0, 0.0);\n"
"	border: 1px solid;\n"
"	border-radius: 1px;\n"
"	border-top-color: rgba(0, 0, 0, 0.0);\n"
"	border-right-color: rgba(0, 0, 0, 0.0);\n"
"	border-left-color: rgba(0, 0, 0, 0.0);\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet(u"*{\n"
"	background: rgba(0, 0, 0, 0.0);\n"
"	border: 1px solid;\n"
"	border-radius: 1px;\n"
"	border-top-color: rgba(0, 0, 0, 0.0);\n"
"	border-right-color: rgba(0, 0, 0, 0.0);\n"
"	border-left-color: rgba(0, 0, 0, 0.0);\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_3.setStyleSheet(u"*{\n"
"	background: rgba(0, 0, 0, 0.0);\n"
"	border: 1px solid;\n"
"	border-radius: 1px;\n"
"	border-top-color: rgba(0, 0, 0, 0.0);\n"
"	border-right-color: rgba(0, 0, 0, 0.0);\n"
"	border-left-color: rgba(0, 0, 0, 0.0);\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_4.setStyleSheet(u"*{\n"
"	background: rgba(0, 0, 0, 0.0);\n"
"	border: 1px solid;\n"
"	border-radius: 1px;\n"
"	border-top-color: rgba(0, 0, 0, 0.0);\n"
"	border-right-color: rgba(0, 0, 0, 0.0);\n"
"	border-left-color: rgba(0, 0, 0, 0.0);\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setStyleSheet(u"*{\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 35))
        self.frame_4.setStyleSheet(u"*{\n"
"	background: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(150, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 6, 6, 6)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"*{\n"
"	color: white;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inscription \u00e0 Yokobot", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inscrivez-vous pour chatter avec YK", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre pseudo", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre mot de passe", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmez votre mot de passe", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Auteur: jesuisroot123", None))
    # retranslateUi

