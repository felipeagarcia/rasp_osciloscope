import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QVBoxLayout,
    QPushButton, QApplication, QDesktopWidget, QLabel)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot
from controller import controller


class GUI():
    def __init__(self, window_height, window_width):
        self.height = window_height
        self.width = window_width
        self.ctrl = controller()
        self.init_ui()
        self.add_buttons()
        self.add_text("Medições", 300, 50)
        self.add_text("Gráficos", 100, 50)    

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def center(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

    def create_button(self, name, event, pos_x, pos_y):
        button = QPushButton(name, self.window)
        button.clicked.connect(event)
        button.resize(button.sizeHint())
        button.move(pos_x, pos_y)

    def add_text(self, text, align):
        self.window.label = QLabel(text)
        self.window.setAlignment(align)
        self.window.layout.addWidget(self.window.label)
        self.window.setLayout(self.window.layout)

    def init_ui(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(self.height, self.width)
        self.window.setWindowTitle('Rasp Osciloscope')
        self.window.setWindowIcon(QIcon('waves.png'))
        self.window.layout = QVBoxLayout() 
        self.center()

    def add_buttons(self):
        self.create_button("Exibir sinal no tempo", self.ctrl.show_signal, 300, 100)
        self.create_button("Exibir sinal na frequência", self.ctrl.show_fft, 300, 150)
        self.create_button("Tensão Máxima", self.ctrl.print_max, 300, 200)
        self.create_button("Tensão Mínima", self.ctrl.print_min, 300, 250)

    def on_click(self):
        print('PyQt5 button click')
