from PyQt5.QtWidgets import  QMainWindow, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QWidget, QShortcut
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QTimer, Qt
import sys
from random import randrange
import subprocess


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Noveled")

        self.setWindowIcon(QIcon('icon-transparent.svg'))
        self.setStyleSheet("background-color: #101117;")
        # self.showMaximized()
        self.initUI()
        

    def initUI(self):
        
        self.loadngAnime = QLabel()
        self.loading_anim = ['loading.gif','loading1.gif']
        loadnggif = QMovie(self.loading_anim[randrange(0,2)])
        self.loadngAnime.setMovie(loadnggif)
        loadnggif.start()
        self.loadngAnime.setScaledContents(True)
        self.loadngAnime.setFixedSize(200,200)
        # self.loadngAnime.setGeometry( 0, 0 ,300, 300)


        self.loadngScreen = QWidget()
        load = QVBoxLayout()
        load.addWidget(self.loadngAnime)
        load.setAlignment(self.loadngAnime, Qt.AlignCenter)
        self.loadngScreen.setLayout(load)
        self.setCentralWidget(self.loadngScreen)

        self.timer = QTimer()
        self.timer.setSingleShot(True)  # Trigger only once
        self.timer.timeout.connect(self.closeLoadingScreen)
        self.timer.start(3000) 

        self.homeScreen = QWidget()
        self.sampleTXT = QLabel()
        self.sampleTXT.setText("welcome")
        self.sampleTXT.setStyleSheet("color: white;")

        self.home_layout = QVBoxLayout()
        self.home_layout.addWidget(self.sampleTXT)
        self.homeScreen.setLayout(self.home_layout)

    def closeLoadingScreen(self):
        subprocess.Popen(['python', 'epub.py'])
        self.loadingScreen.close()
        
        


        # self.setCentralWidget(self.homeScreen)
        # self.showFullScreen() to make it full screen 
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.showMaximized()
    sys.exit(app.exec_())

