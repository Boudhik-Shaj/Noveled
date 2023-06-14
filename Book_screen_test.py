from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QWidget, QShortcut, QSpacerItem, QSizePolicy

from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QEvent, pyqtSignal, QMutexLocker

import ebooklib
from ebooklib import epub
import sys

current_index = 0
all_list = []
value = 0

window = QMainWindow()

def fonter():
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(12)
    return font

def epub_reader(epub_layout):
    global current_index
    global all_list
    global value
    book = epub.read_epub('Spellslinger_-_Sebastien_de_Castell.epub')
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            item = item.get_content().decode("utf-8")
            all_list.append(item)
        elif item.get_type() == ebooklib.ITEM_IMAGE:
            pixmap = QPixmap()
            pixmap.loadFromData(item.get_content())
            all_list.append(pixmap)
        return counter(epub_layout)


def counter(epub_layout):
    global current_index
    global all_list
    global value
    clearMainLayout(epub_layout)
    if value == 0 :
        return create_main(epub_layout,all_list[current_index])
    elif value==1 and current_index!=0:
        current_index = current_index - 1
        return create_main(epub_layout,all_list[current_index])
    elif value==2 and current_index!=(len(all_list)-1):
        current_index = current_index + 1
        return create_main(epub_layout,all_list[current_index])

def create_main(epub_layout,item):
    global current_index
    global all_list
    content_layout = QHBoxLayout()

    if isinstance(item, QPixmap):
        label = QLabel()
        label.setPixmap(item)
        content_layout.addWidget(label)
    elif isinstance(item, str):
        text_layout = QLabel()
        text_layout.setWordWrap(True)
        text_layout.setText(item)
        text_layout.setFont(fonter())
        text_layout.setStyleSheet("color: white;")
        content_layout.addWidget(text_layout)

    button_layout = QHBoxLayout()

    button_forward = QPushButton('->')
    button_forward.setStyleSheet("color: white;")
    button_forward.setStyleSheet("background-color: grey;")

    # QShortcut(QKeySequence('Right'), window).activated.connect(button_forward_clicked)
    button_forward.clicked.connect(button_forward_clicked)

    
    button_random = QPushButton('  ')
    button_random.setStyleSheet("color: white;")
    button_random.setFixedSize(1400, 30)
    button_random.setStyleSheet("background-color: #101117;")
    button_random.clicked.connect(button_random.click)

    button_backward = QPushButton('<-') 
    button_backward.setStyleSheet("color: white;")
    button_backward.setStyleSheet("background-color: grey;")

    # QShortcut(QKeySequence('Left'), window).activated.connect(button_backward_clicked)
    button_backward.clicked.connect(button_backward_clicked)

    button_layout.addWidget(button_backward)
    button_layout.addWidget(button_random)
    button_layout.addWidget(button_forward)

    epub_layout.addLayout(content_layout)
    epub_layout.addLayout(button_layout)

    return epub_layout

def button_forward_clicked():
    global value
    global current_index
    global all_list
    print("Button Forward Clicked")
    value = 2
    button_activate()

def button_backward_clicked():
    global value
    global current_index
    global all_list
    print("Button Backwards Clicked")
    value = 1
    button_activate()

def button_activate():
    from main_test import home
    my_instance = home()
    my_instance.scroller(epub_reader(my_instance.main_layout))

def stop_functions():
    global current_index
    global all_list
    print ("function done")

def clearMainLayout(epub_layout):
    global current_index
    global all_list
    while epub_layout.count():
        item = epub_layout.takeAt(0)
        if item.layout():
            while item.layout().count():
                sub_item = item.layout().takeAt(0)
                if sub_item.widget():
                    sub_item.widget().deleteLater()

