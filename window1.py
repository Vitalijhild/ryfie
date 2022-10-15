from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from window2 import *

class Win1(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lb_hello = QLabel(txt_hello)
        self.lb_instution = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.lb_hello, alignment=Qt.AlignCenter)
        self.vline.addWidget(self.lb_instution, alignment=Qt.AlignCenter)
        self.vline.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.vline)

    def connects(self):
        self.btn_next.clicked.connect(self.next_page)
    
    def next_page(self):
        self.hide()
        self.win2 = Win2()

app = QApplication([])
win1 = Win1()


app.exec_()