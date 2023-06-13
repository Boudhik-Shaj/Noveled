from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QWidget, QShortcut, QSpacerItem, QSizePolicy

from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QEvent, pyqtSignal

import ebooklib
from ebooklib import epub
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        # self.showFullScreen() 
        # self.setGeometry(0, 0, 1920, 1080)
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #101117;")

        self.layout = QVBoxLayout()

        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(12)

        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
        self.all_list = []

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                item = item.get_content().decode("utf-8")
                self.all_list.append(item)
            elif item.get_type() == ebooklib.ITEM_IMAGE:
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                self.all_list.append(pixmap)

            
        self.current_index = 0
        self.counter(0)

    def counter(self,value):
        self.clearMainLayout()
        if value == 0 :
            self.create_main(self.all_list[self.current_index])
        elif value==1 and self.current_index!=0:
            self.current_index = self.current_index - 1
            self.create_main(self.all_list[self.current_index])
        elif value==2 and self.current_index!=(len(self.all_list)-1):
            self.current_index = self.current_index + 1
            self.create_main(self.all_list[self.current_index])

    def scroller(self, to_print):
        self.epub_page = QWidget()
        self.epub_page.setLayout(to_print)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.epub_page)
        self.setCentralWidget(scroll_area)

    def create_main(self, item):
        self.main_layout = QHBoxLayout()

        if isinstance(item, QPixmap):
            label = QLabel(self)
            label.setPixmap(item)
            self.main_layout.addWidget(label)
        elif isinstance(item, str):
            text_layout = QLabel(self)
            text_layout.setWordWrap(True)
            text_layout.setText(item)
            text_layout.setFont(self.font)
            text_layout.setStyleSheet("color: white;")
            self.main_layout.addWidget(text_layout)

        button_layout = QHBoxLayout()

        button_forward = QPushButton('->', self)
        button_forward.setStyleSheet("color: white;")
        button_forward.setStyleSheet("background-color: grey;")

        QShortcut(QKeySequence('Right'), self).activated.connect(self.button_forward_clicked)
        button_forward.clicked.connect(self.button_forward_clicked)

        
        button_random = QPushButton('  ', self)
        button_random.setStyleSheet("color: white;")
        button_random.setFixedSize(1400, 30)
        button_random.setStyleSheet("background-color: #101117;")
        button_random.clicked.connect(button_random.click)

        button_backward = QPushButton('<-', self)
        button_backward.setStyleSheet("color: white;")
        button_backward.setStyleSheet("background-color: grey;")

        QShortcut(QKeySequence('Left'), self).activated.connect(self.button_backward_clicked)
        button_backward.clicked.connect(self.button_backward_clicked)

        button_layout.addWidget(button_backward)
        button_layout.addWidget(button_random)
        button_layout.addWidget(button_forward)

        self.layout.addLayout(self.main_layout)
        self.layout.addLayout(button_layout)

        self.scroller(self.layout)

    def button_forward_clicked(self):
        print("Button Forward Clicked")
        self.counter(2)

    def button_backward_clicked(self):
        print("Button Backwards Clicked")
        self.counter(1)
    
    def clearMainLayout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.layout():
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    if sub_item.widget():
                        sub_item.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())