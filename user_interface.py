import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QVBoxLayout,
    QPushButton, QApplication, QDesktopWidget, QLabel, QHBoxLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore

class GUI():
    def __init__(self, window_height, window_width):
        self.height = window_height
        self.width = window_width
        self.init_ui()
        #self.add_buttons()
          

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
        button.setGeometry(QtCore.QRect(pos_x, pos_y, 125, 25))
        button.move(pos_x, pos_y)

    def add_text(self, text, x, y):
        text = QLabel(text, self.window)
        text.setGeometry(QtCore.QRect(x, y, 300, 20))
        return text

    def init_ui(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(self.height, self.width)
        self.window.setWindowTitle('Rasp Osciloscope')
        self.window.setWindowIcon(QIcon('waves.png'))
        self.window.layout = QVBoxLayout() 
        self.label = QLabel(self.window)
        self.hbox = QHBoxLayout(self.window)
        self.add_text("Comandos", 825, 10)
        self.add_text("Medidas", 800, 375)
        self.hbox.addWidget(self.label)
        self.window.setLayout(self.hbox)
        self.set_image('imgs/time_plot.png')
        self.txt_freq = self.add_text("Frequência:", 720, 400)
        self.txt_per = self.add_text("Período:", 720, 420)
        self.txt_rise = self.add_text("Subida:", 720, 440)
        self.txt_vmax = self.add_text("Tensão Máxima:", 720, 460)
        self.txt_vmin = self.add_text("Tensão Mínima:", 720, 480)
        self.txt_vpic = self.add_text("Tensão Pico a Pico:", 720, 500)
        self.center()

    def add_buttons(self):
        self.create_button("Exibir sinal períodico", self.ctrl.show_signal, 800, 50)
        self.create_button("Exibir sinal completo", self.ctrl.show_all, 800, 100)
        self.create_button("Exibir sinal na frequência", self.ctrl.show_fft, 800, 150)
        self.create_button("Tensão Máxima", self.ctrl.print_max, 800, 200)
        self.create_button("Tensão Mínima", self.ctrl.print_min, 800, 250)

    def set_image(self, path):
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(700)
        self.label.setPixmap(pixmap)
        
        
