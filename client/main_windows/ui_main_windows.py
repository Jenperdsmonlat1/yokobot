# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowsNVchRE.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import icon_butotn_rc

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
"	background: rgb(38, 38, 38);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.titleBar = QFrame(self.frame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 35))
        self.titleBar.setStyleSheet(u"")
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QFrame(self.titleBar)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setFrameShape(QFrame.StyledPanel)
        self.titleLabel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleLabel)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.titleLabel)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"*{\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-family: Noto Sans;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.buttonsFrame = QFrame(self.titleBar)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setMaximumSize(QSize(90, 16777215))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 2, 4, 2)
        self.minimizeButton = QPushButton(self.buttonsFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(15, 15))
        self.minimizeButton.setStyleSheet(u"*{\n"
"	background: rgb(84, 255, 117);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.buttonsFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMaximumSize(QSize(15, 15))
        self.maximizeButton.setStyleSheet(u"*{\n"
"	background: rgb(255, 152, 55);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.maximizeButton)

        self.exitButton = QPushButton(self.buttonsFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMaximumSize(QSize(15, 15))
        self.exitButton.setStyleSheet(u"*{\n"
"	background: rgb(255, 55, 55);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.exitButton)


        self.horizontalLayout_2.addWidget(self.buttonsFrame)


        self.verticalLayout.addWidget(self.titleBar)

        self.contenu = QFrame(self.frame)
        self.contenu.setObjectName(u"contenu")
        self.contenu.setStyleSheet(u"")
        self.contenu.setFrameShape(QFrame.StyledPanel)
        self.contenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.contenu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical{\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	margin: 15px 0 15px 0;\n"
"	background: rgb(63, 63, 63);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	background: rgb(228, 112, 176);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"	background: rgb(162, 79, 126);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	background: rgb(228, 112, 176);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"	background: rgb(162, 79, 126);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	background: rgb(228, 112, 176);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"	background: rgb(162, 79, 126);\n"
"}\n"
""
                        "\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background: none;\n"
"}\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 770, 478))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_2 = QFrame(self.contenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 45))
        self.frame_2.setMaximumSize(QSize(16777215, 45))
        self.frame_2.setStyleSheet(u"*{\n"
"	border-radius: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(52, 148, 230, 255), stop:1 rgba(236, 110, 173, 255));\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(7, 2, 7, 2)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"*{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"*{\n"
"	background-color: white;\n"
"	padding: 20px;\n"
"	border-radius: 14px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/send-solid-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.contenu)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Yokobot - Accueil - version 0.2", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.exitButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Votre message \u00e0 Yokobot", None))
        self.pushButton.setText("")
    # retranslateUi

