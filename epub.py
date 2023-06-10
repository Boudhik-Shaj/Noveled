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
        self.text_list = []
        self.image_text = QtWidgets.QVBoxLayout()

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_IMAGE:
                label = QLabel(self)
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                label.setPixmap(pixmap)
                self.image_text.addWidget(label)

            elif item.get_type() == ebooklib.ITEM_DOCUMENT:
                text = item.get_content().decode("utf-8")
                self.text_list.append(text)
        self.current_index = 0
        self.counter(0)

    def counter(self,value):
        if value == 0 :
            self.create_word(self.text_list[self.current_index])
        elif value==1 and self.current_index!=0:
            self.current_index = self.current_index - 1
            self.create_word(self.text_list[self.current_index])
        elif value==2 and self.current_index!=(len(self.text_list)-1):
            self.current_index = self.current_index + 1
            self.create_word(self.text_list[self.current_index])

    def scroller(self, to_print):
        self.epub_page = QWidget()
        self.epub_page.setLayout(to_print)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.epub_page)
        self.setCentralWidget(scroll_area)

    def create_word(self, text):
        self.text_print = QVBoxLayout()
        text_layout = QLabel(self)
        text_layout.setWordWrap(True)
        text_layout.setText(text)
        self.text_print.addWidget(text_layout)

        # Add the button as a widget in the text_print layout
        button_forward = QPushButton('->', self)
        button_forward.clicked.connect(self.button_forward_clicked)
        self.text_print.addWidget(button_forward)

        button_backward = QPushButton('<-', self)
        button_backward.clicked.connect(self.button_backward_clicked)
        self.text_print.addWidget(button_backward)

        self.scroller(self.text_print)

    def button_forward_clicked(self):
        self.counter(2)

    def button_backward_clicked(self):
        self.counter(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
