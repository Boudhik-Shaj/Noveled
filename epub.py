from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QScrollArea, QTextEdit
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

        # Create a layout to hold the widgets
        self.layout = QVBoxLayout()

        # Read the EPUB file
        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
        self.text_list = []
        self.image_text= QtWidgets.QVBoxLayout()
     

        # Iterate over the items in the ebook
        for item in book.get_items():
            # Check if the item is an image
            if item.get_type() == ebooklib.ITEM_IMAGE:
                # Create a QLabel for the image
                label = QLabel(self)
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                label.setPixmap(pixmap)
                self.image_text.addWidget(label)

            elif item.get_type() == ebooklib.ITEM_DOCUMENT:
                text = item.get_content().decode("utf-8")
                self.text_list.append(text)

        # self.scroller(self.image_text)
        self.create_word(self.text_list[7])

    def scroller(self,to_print):
        self.epub_page = QtWidgets.QWidget()
        self.epub_page.setLayout(to_print)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.epub_page)
        self.setCentralWidget(scroll_area)

    def create_word(self,text):
        self.text_print = QtWidgets.QVBoxLayout()
        text_layout = QLabel(self)
        text_layout.setWordWrap(True)
        text_layout.setText(text)
        self.text_print.addWidget(text_layout)
        self.scroller(self.text_print)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
