from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from instr import *
from PyQt5.QtGui import QFont

class Win2(QWidget):
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
        self.lb_name = QLabel(txt_name)
        self.le_name = QLineEdit(txt_hintname)

        self.lb_age = QLabel(txt_age)
        self.le_age = QLineEdit(txt_hintage)

        self.lb_test1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.le_test1 = QLineEdit(txt_hinttest1)

        self.lb_test2 = QLabel(txt_test2)
        self.dtn_test2 = QPushButton(txt_starttest1)
        
        self.lb_test3 = QLabel(txt_test3)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.le_test2 = QLineEdit(txt_hinttest2)
        self.le_test3 = QLineEdit(txt_hinttest3)

        self.btn_next = QPushButton(txt_sendresults)

        self.lb_timer = QLabel(txt_timer)
        self.lb_timer.setFont(QFont('Times', 36, QFont.Bold))

        #! розташування віджетів
        self.h_live = QHBoxLayout()
        self.v_live_l = QVBoxLayout()
        self.v_live_r = QVBoxLayout()

        self.v_live_l.addWidget(self.lb_name, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.le_name, alignment=Qt.AlignLeft)
        
        self.v_live_l.addWidget(self.lb_age, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.le_age, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.lb_test1, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.le_test1, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.lb_test2, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.le_test2, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.le_test3, alignment=Qt.AlignLeft)
        self.v_live_l.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        
        self.v_live_r.addWidget(self.lb_timer, alignment=Qt.AlignCenter)
        self.h_live.addLayout(self.v_live_l)
        self.h_live.addLayout(self.v_live_r)       
        self.setLayout(self.h_live)

    def connects(self):
        pass