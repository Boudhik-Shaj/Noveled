from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

def create_layout():
    layout = QVBoxLayout()

    label1 = QLabel("Layout 1")
    layout.addWidget(label1)

    return layout
