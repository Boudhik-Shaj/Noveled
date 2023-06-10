from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtGui import QPixmap
import ebooklib
from ebooklib import epub
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setGeometry(100, 100, 1920, 1080)

        # Create a layout to hold the image labels
        self.image_layout = QVBoxLayout()

        # Read the EPUB file
        book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')

        # Iterate over the images in the EPUB file
        for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
            # Create a QLabel for each image
            label = QLabel(self)
            # Load the image data from the EPUB item
            pixmap = QPixmap()
            pixmap.loadFromData(image.get_content())
            # Set the image pixmap to the label
            label.setPixmap(pixmap)
            # Add the label to the layout
            self.image_layout.addWidget(label)

        # Create a widget to hold the image layout
        image_widget = QWidget(self)
        image_widget.setLayout(self.image_layout)

        # Create a scroll area and set the image widget as its child
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(image_widget)

        # Set the scroll area as the central widget
        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
