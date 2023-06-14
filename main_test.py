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
        self.target_layout = QVBoxLayout()
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
        self.scroller(self.main_layout, "start")

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.closeLoadingScreen)
        self.timer.start(3000)

    def closeLoadingScreen(self):
        from Book_screen_test import button_activate,myclass
        button_activate(self.main_layout)
        print("finish")
    
    # def button_activate(self):
    #     from Book_screen_test import epub_reader 
    #     hi, yo = epub_reader(self.main_layout)
    #     self.scroller(hi, yo)

    def scroller(self, to_print,value):
        if to_print:
            # if to_print is self.target_layout:
            #     print("layout1 and layout2 are the same")
            # else:
            #     print("laysout1 and layout2 are different")
            # self.copy(to_print)
            print(value)
            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(self.main_widget)
            self.setCentralWidget(scroll_area)
        else:
            print(value)
            print("Invalid layout passed to scroller method.")

    # def copy(self, source_layout):
    #     from Book_screen_test import clearMainLayout
    #     clearMainLayout(self.target_layout)
    #     while source_layout.count():
    #         item = source_layout.takeAt(0)
    #         if item.layout():
    #             self.target_layout.addLayout(item.layout())
    #         elif item.widget():
    #             self.target_layout.addWidget(item.widget())
    #     return 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = home()
    win.showMaximized()
    sys.exit(app.exec_())
