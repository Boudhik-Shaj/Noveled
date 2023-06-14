from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from test import create_layout

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Set the layout from layout_file.py
        layout_object = create_layout()
        widget = QWidget()
        widget.setLayout(layout_object)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
