from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noveled")
        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

