import os
import hashlib
from main_windows import MainWindows
from client.modules.db_insert import DbWriter
from dialog.dialogError.DialogError import dialogError
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import qApp, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class SubscribePage(QWidget):

    def __init__(self):

        super().__init__()
        self.setMinimumSize(QSize(800, 600))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 10px;
                background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.858, y2:0.847, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )
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
        self.label_2.setStyleSheet(
            """
            *{
                background: none;
                color: white;
                font-size: 18px;
                font-family: Noto Sans;
            }
            """
        )

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(15, 15))
        self.pushButton_3.setStyleSheet(
            """
            *{
                background: rgb(84, 255, 117);
                border: none;
                border-radius: 7px;
            }
            """
        )
        self.pushButton_3.clicked.connect(self.showMinimized)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(15, 15))
        self.pushButton_4.setStyleSheet(
            """
            *{
                background: rgb(255, 152, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )
        self.pushButton_4.clicked.connect(self.showMaximized)

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(15, 15))
        self.pushButton_2.setStyleSheet(
            """
            *{
                background: rgb(255, 55, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )
        self.pushButton_2.clicked.connect(qApp.quit)

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
        self.frame_5.setStyleSheet(
            """
            *{
                background: rgba(0, 0, 0, 0.8);
            }
            """
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, -1, 60, -1)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(
            """
            *{
                background: none;
                font-family: Noto Sans;
                font-size: 15px;
                color: white;
            }
            """
        )

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(
            """
            *{
                background: rgba(0, 0, 0, 0.0);
                color: white;
                border: 1px solid;
                border-radius: 1px;
                border-top-color: rgba(0, 0, 0, 0.0);
                border-right-color: rgba(0, 0, 0, 0.0);
                border-left-color: rgba(0, 0, 0, 0.0);
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }""")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet(
            """*{
                background: rgba(0, 0, 0, 0.0);
                color: white;
                border: 1px solid;
                border-radius: 1px;
                border-top-color: rgba(0, 0, 0, 0.0);
                border-right-color: rgba(0, 0, 0, 0.0);
                border-left-color: rgba(0, 0, 0, 0.0);
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_3.setStyleSheet(
            """*{
                background: rgba(0, 0, 0, 0.0);
                color: white;
                border: 1px solid;
                border-radius: 1px;
                border-top-color: rgba(0, 0, 0, 0.0);
                border-right-color: rgba(0, 0, 0, 0.0);
                border-left-color: rgba(0, 0, 0, 0.0);
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_4.setStyleSheet(
            """
            *{
                background: rgba(0, 0, 0, 0.0);
                color: white;
                border: 1px solid;
                border-radius: 1px;
                border-top-color: rgba(0, 0, 0, 0.0);
                border-right-color: rgba(0, 0, 0, 0.0);
                border-left-color: rgba(0, 0, 0, 0.0);
                border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setStyleSheet(
            """
            *{
                color: white;
                border: none;
                border-radius: 20px;
                background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )

        self.verticalLayout_2.addWidget(self.pushButton)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 35))
        self.frame_4.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )
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
        self.label_3.setStyleSheet(
            """
            *{
                color: white;
            }
            """
        )

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalLayout_6.addWidget(self.frame_9)

        self.verticalLayout.addWidget(self.frame_4)

        self.horizontalLayout.addWidget(self.frame)

        self.label_2.setText("Inscription \u00e0 Yokobot")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.label.setText("Inscrivez-vous pour chatter avec YK")
        self.lineEdit.setPlaceholderText("Votre pseudo")
        self.lineEdit_2.setPlaceholderText("Votre email")
        self.lineEdit_3.setPlaceholderText("Votre mot de passe")
        self.lineEdit_4.setPlaceholderText("Confirmez votre mot de passe")
        self.pushButton.setText("Valider")
        self.label_3.setText("Auteur: jesuisroot123")

        self.pushButton.clicked.connect(self.write_infos)

    def write_infos(self):

        self.pseudo = self.lineEdit.text()
        self.email = self.lineEdit_2.text()
        self.motdepasse = self.lineEdit_3.text()
        self.confirmation_motdepasse = self.lineEdit_4.text()

        if (self.motdepasse == self.confirmation_motdepasse):

            self.passwd_hashed = hashlib.sha256(self.motdepasse.encode()).hexdigest()

            DbWriter(
                pseudo=self.pseudo,
                email=self.email,
                motdepasse=self.passwd_hashed
            )

            self.window = MainWindows()
            self.window.show()
            self.close()

        else:

            self.error = dialogError()
            self.error.show()