from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QScrollArea, QTextEdit
from PyQt5.QtGui import QPixmap
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

        # Iterate over the items in the ebook
        for item in book.get_items():
            # Check if the item is an image
            if item.get_type() == ebooklib.ITEM_IMAGE:
                # Create a QLabel for the image
                label = QLabel(self)
                pixmap = QPixmap()
                pixmap.loadFromData(item.get_content())
                label.setPixmap(pixmap)
                self.layout.addWidget(label)
            # Check if the item is a document
            elif item.get_type() == ebooklib.ITEM_DOCUMENT:
                # Create a QTextEdit for the document text
                text_edit = QTextEdit(self)
                text_edit.setReadOnly(True)
                text_edit.setHtml(item.get_content().decode("utf-8"))
                self.layout.addWidget(text_edit)

        # Create a widget to hold the layout
        widget = QWidget(self)
        widget.setLayout(self.layout)

        # Create a scroll area and set the widget as its child
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)

        # Set the scroll area as the central widget
        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
