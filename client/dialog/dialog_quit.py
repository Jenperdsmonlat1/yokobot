import sys
from PyQt5.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PyQt5.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, qApp


class DialogQuit(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(400, 168)
        self.setMinimumSize(QSize(400, 168))
        self.setMaximumSize(QSize(400, 168))

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 150))
        self.frame.setMaximumSize(QSize(500, 250))
        self.frame.setStyleSheet(
            """
            *{
                background: rgb(77, 104, 217);
                border-radius: 10px;
            }
            """
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )

        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(
            """
            *{
                color: white;
            }
            """
        )

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(35, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(15, 15))
        self.pushButton.setStyleSheet(
            """
            *{
                background: rgb(255, 55, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )

        self.pushButton.clicked.connect(self.ne_rien_faire)

        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(
            """
            *{
                background: none;
            }
            """
        )

        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(67, 30, 270, 16))
        self.label.setStyleSheet(
            """
            *{
                color: white;
                font-size: 16px;
                font-family: Noto Sans;
            }
            """
        )

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 36, 36))
        self.label_3.setPixmap(QPixmap(u"../icon/info-circle-solid-36.png"))
        self.buttonBox = QDialogButtonBox(self.frame_3)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(210, 60, 141, 31))
        self.buttonBox.setStyleSheet(
            """
            *{
                background: rgb(50, 69, 143);
                color: white;
                width: 65px;
                height: 20px;
            }
            """
        )

        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)

        self.buttonBox.accepted.connect(self.quitter)
        self.buttonBox.rejected.connect(self.ne_rien_faire)

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Quitter ?", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Etes-vous s\u00fbr(e) de vouloir quitter ?", None))

    def quitter(self):

        self.close()
        qApp.quit()

    def ne_rien_faire(self):

        self.close()
