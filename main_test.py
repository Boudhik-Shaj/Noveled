from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QTimer, Qt
import sys
from random import randrange
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QWidget, QShortcut, QSpacerItem, QSizePolicy

from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QEvent, pyqtSignal, QMutexLocker

import ebooklib
from ebooklib import epub
import sys



class home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setWindowIcon(QIcon('icon-transparent.svg'))
        self.setStyleSheet("background-color: #101117;")
        self.current_index = 0
        self.all_list = []
        self.value = 0
        self.counters = []
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
        self.timer.start(5000)

    def closeLoadingScreen(self):
        from Book_screen_test import epub_reader 
        self.clearMainLayout(self.main_layout)
        hi, yo = epub_reader(self.main_layout)
        self.scroller(hi, yo)
    
    def button_activate(self):
        from Book_screen_test import epub_reader 
        self.clearMainLayout(self.main_layout)
        hi, yo = epub_reader(self.main_layout)
        self.scroller(hi, yo)

    def scroller(self, to_print,value):
        if to_print:
            # if to_print is self.target_layout:
            #     print("layout1 and layout2 are the same")
            # else:
            #     print("laysout1 and layout2 are different")
            # self.copy(to_print)
            print(self.value)
            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(self.main_widget)
            self.setCentralWidget(scroll_area)
        else:
            print(self.value)
            print("Invalid layout passed to scroller method.")

    def clearMainLayout(self, main_layout):
        while main_layout.count():
            item = main_layout.takeAt(0)
            if item.layout():
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    if sub_item.widget():
                        sub_item.widget().deleteLater()

    def fonter(self):
        self.counters.append("fonter")    
        self.counters.append(self.current_index)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        return font

    def epub_reader(self):
        self.counters.append("epub_reader")
        self.counters.append(self.current_index)

        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                item = item.get_content().decode("utf-8")
                self.all_list.append(item)
            elif item.get_type() == ebooklib.ITEM_IMAGE:
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                self.all_list.append(pixmap)
        return self.counter()


    def counter(self):
        self.counters.append("counter")
        self.counters.append(self.current_index)

        # clearMainLayout(epub_layout)
        if self.value == 0 :
            return self.create_main(self.main_layout,self.all_list[self.current_index])
        elif self.value==1 and self.current_index!=0:
            self.current_index = self.current_index - 1
            return self.create_main(self.main_layout,self.all_list[self.current_index])
        elif self.value==2 and self.current_index!=(len(self.all_list)-1):
            self.current_index = self.current_index + 1
            return self.create_main(self.main_layout,self.all_list[self.current_index])

    def create_main(self,item):
        self.counters.append("create_main")
        self.counters.append(self.current_index)

        content_layout = QHBoxLayout()

        if isinstance(item, QPixmap):
            label = QLabel()
            label.setPixmap(item)
            content_layout.addWidget(label)
        elif isinstance(item, str):
            text_layout = QLabel()
            text_layout.setWordWrap(True)
            text_layout.setText(item)
            text_layout.setFont(self.fonter())
            text_layout.setStyleSheet("color: white;")
            content_layout.addWidget(text_layout)

        button_layout = QHBoxLayout()

        button_forward = QPushButton('->')
        button_forward.setStyleSheet("color: white;")
        button_forward.setStyleSheet("background-color: grey;")

        # QShortcut(QKeySequence('Right'), window).activated.connect(button_forward_clicked)
        button_forward.clicked.connect(lambda: self.button_forward_clicked())

        
        button_random = QPushButton('  ')
        button_random.setStyleSheet("color: white;")
        button_random.setFixedSize(1400, 30)
        button_random.setStyleSheet("background-color: #101117;")
        button_random.clicked.connect(button_random.click)

        button_backward = QPushButton('<-') 
        button_backward.setStyleSheet("color: white;")
        button_backward.setStyleSheet("background-color: grey;")

        # QShortcut(QKeySequence('Left'), window).activated.connect(button_backward_clicked)
        button_backward.clicked.connect(lambda: self.button_backward_clicked())

        button_layout.addWidget(button_backward)
        button_layout.addWidget(button_random)
        button_layout.addWidget(button_forward)

        self.main_layout.addLayout(content_layout)
        self.main_layout.addLayout(button_layout)

        return (self.counters)

    def button_forward_clicked(self):
        self.counters.append("button_forward_clicked")
        self.counters.append(self.current_index)
        self.value = 2
        self.button_activate()
        # button_activate(main_layout)
        print("Button Forward Clicked")


    def button_backward_clicked(self):
        self.counters.append("button_backward_clicked")
        self.counters.append(self.current_index)
        self.value = 1
        self.button_activate()
        print("Button Backwards Clicked")
        # button_activate(main_layout)

    def stop_functions(self):
        self.counters.append("stop_functions")
        self.counters.append(self.current_index)
        print ("function done")

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
