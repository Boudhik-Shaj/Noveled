from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QTextEdit, QWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Split Text Example")
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QHBoxLayout()

        self.widget1 = QWidget()
        self.widget2 = QWidget()

        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()

        self.main_layout.addWidget(self.widget1)
        self.main_layout.addWidget(self.widget2)

        self.widget1.setLayout(QHBoxLayout())
        self.widget2.setLayout(QHBoxLayout())

        self.widget1.layout().addWidget(self.text_edit1)
        self.widget2.layout().addWidget(self.text_edit2)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.main_layout)

        self.loadTextFile()

    def loadTextFile(self):
        with open("large_text.txt", "r") as file:
            lines = file.readlines()

        total_lines = len(lines)
        half_lines = total_lines // 2

        text_widget1 = "".join(lines[:half_lines])
        text_widget2 = "".join(lines[half_lines:])

        self.text_edit1.setPlainText(text_widget1)
        self.text_edit2.setPlainText(text_widget2)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
