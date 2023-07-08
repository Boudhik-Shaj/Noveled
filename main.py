from PyQt5.QtWidgets import  QMainWindow, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QWidget, QShortcut, QSplashScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QTimer, Qt
import sys
from random import randrange
import subprocess

import time



class loadingScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #101117;")
        self.setGeometry(
        (app.desktop().screenGeometry().width() - splash_pix.width()) // 2,
        (app.desktop().screenGeometry().height() - splash_pix.height()) // 2,
        splash_pix.width(),
        splash_pix.height(),
    )

        # self.loadngAnime = QLabel()
        self.loading_anim = ['loading.gif','loading1.gif']
        self.loadnggif = QMovie(self.loading_anim[randrange(0,2)])
        self.loadngAnime.setMovie(self.loadnggif)
        self.loadnggif.start()
        self.loadngAnime.setScaledContents(True)
        self.loadngAnime.setFixedSize(200,200)
        self.setPixmap(self.loadnggif)


        
        # self.loadngScreen = QWidget()
        # load = QVBoxLayout()
        # load.addWidget(self.loadngAnime)
        # load.setAlignment(self.loadngAnime, Qt.AlignCenter)
        # self.loadngScreen.setLayout(load)
        # self.setCentralWidget(self.loadngScreen)

    def delay(self):
        time.sleep(3)
        
class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Noveled")

        self.setWindowIcon(QIcon('icon-transparent.svg'))
        self.setStyleSheet("background-color: #101117;")
        # self.showMaximized()
        self.initUI()
        

    def initUI(self):
        
        # self.loadngAnime = QLabel()
        # self.loading_anim = ['loading.gif','loading1.gif']
        # loadnggif = QMovie(self.loading_anim[randrange(0,2)])
        # self.loadngAnime.setMovie(loadnggif)
        # loadnggif.start()
        # self.loadngAnime.setScaledContents(True)
        # self.loadngAnime.setFixedSize(200,200)
        # self.loadngAnime.setGeometry( 0, 0 ,300, 300)


        # self.loadngScreen = QWidget()
        # load = QVBoxLayout()
        # load.addWidget(self.loadngAnime)
        # load.setAlignment(self.loadngAnime, Qt.AlignCenter)
        # self.loadngScreen.setLayout(load)
        # self.setCentralWidget(self.loadngScreen)

        # self.timer = QTimer()
        # self.timer.setSingleShot(True)  # Trigger only once
        # self.timer.timeout.connect(self.closeLoadingScreen)
        # self.timer.start(3000) 

        self.homeScreen = QWidget()
        self.sampleTXT = QLabel()
        self.sampleTXT.setText("welcome")
        self.sampleTXT.setStyleSheet("color: white;")

        self.home_layout = QVBoxLayout()
        self.home_layout.addWidget(self.sampleTXT)
        self.homeScreen.setLayout(self.home_layout)
        self.setCentralWidget(self.homeScreen)


    # def closeLoadingScreen(self):
    #     subprocess.Popen(['python', 'epub.py'])
    #     self.loadingScreen.close()
        
        


        # self.showFullScreen() to make it full screen 
        # self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    load = loadingScreen()
    load.show()
    load.delay()

    win = window()
    win.showMaximized()

    load.finish(win)
    sys.exit(app.exec_())

