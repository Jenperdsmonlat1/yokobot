import os
import sys
import time
from subscribe_page import SubscribePage
from login_page import LoginPage
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QProgressBar, QWidget
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QPixmap


class SplashScreen(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(QSize(650, 450))
        self.setMaximumSize(QSize(650, 450))
        self.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(
            """
            *{
                background: rgb(38, 38, 38);
                border-radius: 10px;
            }
            """
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(125, 30, 500, 161))
        self.label.setPixmap(QPixmap(u"Yokobot-removebg-previewe.png"))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 182, 411, 31))
        self.label_2.setStyleSheet(
            """
            *{
                color: white;
                font-size: 20px;
                font-family: Noto Sans;
            }
            """
        )

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 290, 450, 23))
        self.progressBar.setStyleSheet(
            """
            *{
                background: rgb(75, 75, 75);
                border-radius: 10px;
            }
            
            *:chunk {
                background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.815, y2:1, stop:0 rgba(69, 104, 220, 255), stop:1 rgba(176, 106, 179, 255));
            }
            """
        )

        self.horizontalLayout.addWidget(self.frame)

        self.label.setText("")
        self.label_2.setText("A chatbot propulsed by artificial intelligence.")

        self.show()
        self.load_progress_bar(times=0.05)

    def load_progress_bar(self, times):

        QApplication.processEvents()
        for i in range(101):

            time.sleep(times)
            self.progressBar.setValue(i)

        self.close()

        self.user = os.getenv('USERPROFILE')
        self.rep = self.user.strip("\n\r") + "\\AppData\\Roaming\\" + "Temp.yk"

        if os.path.exists(self.rep):

            self.login = LoginPage()
            self.login.show()

        else:

            self.subscribe = SubscribePage()
            self.subscribe.show()

            with open(self.rep, "w") as file:

                file.write("")
                file.close()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    windows = SplashScreen()
    sys.exit(app.exec())
