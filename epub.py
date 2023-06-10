from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QScrollArea, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import ebooklib
from ebooklib import epub
import sys

class Window(QMainWindow):
    image_text= QtWidgets.QVBoxLayout()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setGeometry(0, 0, 1920, 1080)

        # Create a layout to hold the widgets
        self.layout = QVBoxLayout()

        # Read the EPUB file
        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
        text_list = []
     

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
            # Check if the item is a document
            elif item.get_type() == ebooklib.ITEM_DOCUMENT:
                text = "yes"
            # Create a QTextEdit for the document text

        text_edit = QtWidgets.QWidget()
        text_edit.setLayout(self.image_text)

        # Create a scroll area and set the widget as its child
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(text_edit)

        # Set the scroll area as the central widget
        self.setCentralWidget(scroll_area)

    def create_word_print(self,text):
        self.text_print = QtWidgets.QVBoxLayout()
        text_layout = QLabel(self)
        text_layout.setWordWrap(True)
        text_layout.setText(text)
        self.image_text.addWidget(text_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
