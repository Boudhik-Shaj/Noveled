from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QTimer, Qt
import sys
from random import randrange

class home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setWindowIcon(QIcon('icon-transparent.svg'))
        self.setStyleSheet("background-color: #101117;")
        self.initUI()

    def initUI(self):
        self.loadngAnime = QLabel()
        self.loading_anim = ['loading.gif','loading1.gif']
        loadnggif = QMovie(self.loading_anim[randrange(0,2)])
        self.loadngAnime.setMovie(loadnggif)
        loadnggif.start()
        self.loadngAnime.setScaledContents(True)
        self.loadngAnime.setFixedSize(200,200)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.loadngAnime)
        self.main_layout.setAlignment(self.loadngAnime, Qt.AlignCenter)
        self.scroller(self.main_layout)

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.closeLoadingScreen)
        self.timer.start(3000)

    def closeLoadingScreen(self):
        from Book_screen_test import epub_reader 
        self.scroller(epub_reader(self.main_layout))

    def scroller(self, to_print):
        if to_print:
            self.main_widget = QWidget()
            self.main_widget.setLayout(to_print)
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(self.main_widget)
            self.setCentralWidget(scroll_area)
        else:
            print("Invalid layout passed to scroller method.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = home()
    win.showMaximized()
    sys.exit(app.exec_())
