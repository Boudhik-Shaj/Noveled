from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QScrollArea, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import ebooklib
from ebooklib import epub
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setGeometry(0, 0, 1920, 1080)

        self.layout = QVBoxLayout()

        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
        self.all_list = []
        self.image_text = QtWidgets.QVBoxLayout()

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_IMAGE:
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                self.all_list.append(pixmap)

            elif item.get_type() == ebooklib.ITEM_DOCUMENT:
                item = item.get_content().decode("utf-8")
                self.all_list.append(item)
        self.current_index = 0
        self.counter(0)

    def counter(self,value):
        if value == 0 :
            self.create_wid(self.all_list[self.current_index])
        elif value==1 and self.current_index!=0:
            self.current_index = self.current_index - 1
            self.create_wid(self.all_list[self.current_index])
        elif value==2 and self.current_index!=(len(self.all_list)-1):
            self.current_index = self.current_index + 1
            self.create_wid(self.all_list[self.current_index])

    def scroller(self, to_print):
        self.epub_page = QWidget()
        self.epub_page.setLayout(to_print)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.epub_page)
        self.setCentralWidget(scroll_area)

    def create_wid(self, item):
        self.wid_print = QVBoxLayout()

        if isinstance(item, QPixmap):
            label = QLabel(self)
            label.setPixmap(item)
            self.wid_print.addWidget(label)
        elif isinstance(item, str):
            text_layout = QLabel(self)
            text_layout.setWordWrap(True)
            text_layout.setText(item)
            self.wid_print.addWidget(text_layout)

        button_forward = QPushButton('->', self)
        button_forward.clicked.connect(self.button_forward_clicked)
        self.wid_print.addWidget(button_forward)

        button_backward = QPushButton('<-', self)
        button_backward.clicked.connect(self.button_backward_clicked)
        self.wid_print.addWidget(button_backward)

        self.scroller(self.wid_print)

    def button_forward_clicked(self):
        self.counter(2)

    def button_backward_clicked(self):
        self.counter(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
