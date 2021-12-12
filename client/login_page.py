import sys
import json
import hashlib
from main_windows import MainWindows
from PyQt5.QtWidgets import qApp, QApplication, QFrame, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMainWindow, QProgressBar, QSizePolicy, QWidget
from PyQt5.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform


class LoginPage(QWidget):

    def __init__(self):

        super().__init__()
        self.resize(800, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(QSize(800, 600))
        self.setStyleSheet("")
        self.horizontalLayout = QHBoxLayout()

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(
            """
            *{
                background: qlineargradient(spread:pad, x1:0, y1:0.301, x2:0.825, y2:0.733136, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
                border-radius: 10px;
            }
            """
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleBar = QFrame(self.frame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 35))
        self.titleBar.setStyleSheet(
            """
            *{
                background: none;
            }"""
        )
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)

        self.titleFrame = QFrame(self.titleBar)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.title = QLabel(self.titleFrame)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(
            """
            *{
                color: whitesmoke;
                font-size: 18px;
                font-family: Noto Sans;
                background: none;
            }
            """
        )

        self.horizontalLayout_4.addWidget(self.title)

        self.horizontalLayout_2.addWidget(self.titleFrame)

        self.frameButton = QFrame(self.titleBar)
        self.frameButton.setObjectName(u"frameButton")
        self.frameButton.setMaximumSize(QSize(90, 16777215))
        self.frameButton.setFrameShape(QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameButton)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.minimiseButton = QPushButton(self.frameButton)
        self.minimiseButton.setObjectName(u"minimiseButton")
        self.minimiseButton.setMinimumSize(QSize(15, 15))
        self.minimiseButton.setMaximumSize(QSize(15, 15))
        self.minimiseButton.setStyleSheet(
            """
            *{
                background: rgb(84, 255, 117);
                border: none;
                border-radius: 7px;
            }
            """
        )

        self.minimiseButton.clicked.connect(self.showMinimized)

        self.horizontalLayout_3.addWidget(self.minimiseButton)

        self.maximiseButton = QPushButton(self.frameButton)
        self.maximiseButton.setObjectName(u"maximiseButton")
        self.maximiseButton.setMinimumSize(QSize(15, 15))
        self.maximiseButton.setMaximumSize(QSize(15, 15))
        self.maximiseButton.setStyleSheet(
            """
            *{
                background: rgb(255, 152, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )

        self.maximiseButton.clicked.connect(self.showFullScreen)

        self.horizontalLayout_3.addWidget(self.maximiseButton)

        self.exitButton = QPushButton(self.frameButton)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(15, 15))
        self.exitButton.setMaximumSize(QSize(15, 15))
        self.exitButton.setStyleSheet(
            """
            *{
                background: rgb(255, 55, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )
        self.exitButton.clicked.connect(self.quit_app)

        self.horizontalLayout_3.addWidget(self.exitButton)

        self.horizontalLayout_2.addWidget(self.frameButton)

        self.verticalLayout.addWidget(self.titleBar)

        self.contenu = QFrame(self.frame)
        self.contenu.setObjectName(u"contenu")
        self.contenu.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )

        self.contenu.setFrameShape(QFrame.StyledPanel)
        self.contenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.contenu)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(200, 20, 200, 20)
        self.formulaire = QFrame(self.contenu)
        self.formulaire.setObjectName(u"formulaire")
        self.formulaire.setMinimumSize(QSize(375, 460))
        self.formulaire.setMaximumSize(QSize(375, 440))
        self.formulaire.setStyleSheet(
            """
            *{
                background: rgba(0, 0, 0, 0.8);
                border-radius: 20px;
            }
            """
        )
        self.formulaire.setFrameShape(QFrame.StyledPanel)
        self.formulaire.setFrameShadow(QFrame.Raised)
        self.password = QLineEdit(self.formulaire)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(62, 266, 250, 31))
        self.password.setStyleSheet(
            """
            *{
                background: rgba(255, 255, 255, 0.0);
                color: white;
                border-radius: 1px;
                border: 2px solid;
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.801, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
                border-top-color: rgba(255, 255, 255, 0.0);
                border-right-color: rgba(255, 255, 255, 0.0);
                border-left-color: rgba(255, 255, 255, 0.0);
            }
            """
        )
        self.username = QLineEdit(self.formulaire)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(62, 175, 250, 31))
        self.username.setStyleSheet(
            """
            *{
                background: rgba(255, 255, 255, 0.0);
                color: white;
                border-radius: 1px;
                border: 2px solid;
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.801, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
                border-top-color: rgba(255, 255, 255, 0.0);
                border-right-color: rgba(255, 255, 255, 0.0);
                border-left-color: rgba(255, 255, 255, 0.0);
            }
            """
        )
        self.validerButton = QPushButton(self.formulaire)
        self.validerButton.setObjectName(u"validerButton")
        self.validerButton.setGeometry(QRect(87, 350, 200, 40))
        self.validerButton.setStyleSheet(
            """
            *{
                background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.801, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
                border-radius: 20px;
                color: white;
                font-family: Noto Sans;
            }
            """
        )
        self.validerButton.clicked.connect(self.check_users)

        self.title_formulaire = QLabel(self.formulaire)
        self.title_formulaire.setObjectName(u"title_formulaire")
        self.title_formulaire.setGeometry(QRect(105, 74, 165, 32))
        self.title_formulaire.setMaximumSize(QSize(175, 50))
        self.title_formulaire.setStyleSheet(
            """
            *{
                color: white;
                font-size: 23px;
                font-family: Noto Sans;
                background: none;
            }
            """
        )

        self.pushButton = QPushButton(self.formulaire)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(87, 420, 200, 24))
        self.pushButton.setStyleSheet(
            """
            *{
                background: none;
                font-family: Noto Sans;
                font-size: 10px;
            }
            """
        )
        self.pushButton.setText("Vous n'avez pas de compte créez-en un.")
        self.pushButton.setStyleSheet(
            """
            *{
                color: white;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.horizontalLayout_6.addWidget(self.formulaire)

        self.verticalLayout.addWidget(self.contenu)

        self.footer = QFrame(self.frame)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 35))
        self.footer.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Frame = QFrame(self.footer)
        self.Frame.setObjectName(u"Frame")
        self.Frame.setFrameShape(QFrame.StyledPanel)
        self.Frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Frame)

        self.credit = QLabel(self.footer)
        self.credit.setObjectName(u"credit")
        self.credit.setMaximumSize(QSize(120, 16777215))
        self.credit.setStyleSheet(
            """
            *{
                color: whitesmoke;
                font-size: 12px;
                font-family: Noto Sans;
            }
            """
        )

        self.horizontalLayout_5.addWidget(self.credit)

        self.verticalLayout.addWidget(self.footer)

        self.footer.raise_()
        self.titleBar.raise_()
        self.contenu.raise_()

        self.horizontalLayout.addWidget(self.frame)

        self.title.setText("Connexion à votre compte.")
        self.minimiseButton.setText("")
        self.exitButton.setText("")
        self.maximiseButton.setText("")
        self.username.setPlaceholderText("Votre nom d'utilisateur")
        self.password.setPlaceholderText("Votre mot de passe")
        self.validerButton.setText("Valider")
        self.title_formulaire.setText("Ah te revoilà !!!!")
        self.credit.setText("Auteur: jesuisroot123")

    def quit_app(self):

        qApp.quit()

    def check_users(self):

        self.user = self.username.text()
        self.passwd = self.password.text()

        self.passwd_hashed = hashlib.sha256(self.passwd.encode()).hexdigest()

        with open("users.json", "r") as file:

            data = json.load(file)

            if data['pseudo'] == self.user:
                if data['motdepasse'] == self.passwd_hashed:

                    self.windows = MainWindows()
                    self.windows.show()

            else:

                self.close()
