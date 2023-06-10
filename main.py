from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QTimer
import sys
import time


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Noveled")

        self.setWindowIcon(QIcon('icon-transparent.svg'))
        self.setStyleSheet("background-color: #101117;")
        # self.showMaximized()
        self.initUI()
        

    def initUI(self):
        
        self.loadngAnime = QtWidgets.QLabel()
        loadnggif = QMovie("loading.gif")
        self.loadngAnime.setMovie(loadnggif)
        loadnggif.start()
        self.loadngAnime.setScaledContents(True)
        # self.loadngAnime.setFixedSize(300,300)
        self.loadngAnime.setGeometry( 0, 0 ,300, 300)


        self.loadngScreen = QtWidgets.QWidget()
        load = QtWidgets.QVBoxLayout()
        load.addWidget(self.loadngAnime)
        self.loadngScreen.setLayout(load)
        self.setCentralWidget(self.loadngScreen)
        self.timer = QTimer()
        self.timer.setSingleShot(True)  # Trigger only once
        self.timer.timeout.connect(self.closeLoadingScreen)
        self.timer.start(3000) 

        self.homeScreen = QtWidgets.QWidget()
        self.sampleTXT = QtWidgets.QLabel()
        self.sampleTXT.setText("welcome")
        self.sampleTXT.setStyleSheet("color: white;")

        self.home_layout = QtWidgets.QVBoxLayout()
        self.home_layout.addWidget(self.sampleTXT)
        self.homeScreen.setLayout(self.home_layout)

    def closeLoadingScreen(self):
        self.setCentralWidget(self.homeScreen)
        # self.show()
        


        # self.setCentralWidget(self.homeScreen)
        # self.showFullScreen() to make it full screen 
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.showMaximized()
    sys.exit(app.exec_())