import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QVBoxLayout,
    QPushButton, QApplication, QDesktopWidget, QLabel, QHBoxLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt


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
        button.resize(button.sizeHint())
        button.move(pos_x, pos_y)

    def add_text(self, text, pos_x, pos_y):
        self.window.label = QLabel(text)
        self.window.label.move(pos_x, pos_y)
        self.window.layout.addWidget(self.window.label)
        self.window.setLayout(self.window.layout)

    def init_ui(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(self.height, self.width)
        self.window.setWindowTitle('Rasp Osciloscope')
        self.window.setWindowIcon(QIcon('waves.png'))
        self.window.layout = QVBoxLayout() 
        self.label = QLabel(self.window)
        self.hbox = QHBoxLayout(self.window)
        text = QLabel("Comandos")
        text.setAlignment(Qt.AlignHCenter)
        text2 = QLabel("Medidas")
        text2.setAlignment(Qt.AlignVCenter)
        self.hbox.addWidget(self.label)
        self.hbox.addWidget(text)
        self.hbox.addWidget(text2)
        self.window.setLayout(self.hbox)
        self.set_image('imgs/time_plot.png')
        self.center()

    def add_buttons(self):
        self.create_button("Exibir sinal no tempo", self.ctrl.show_signal, 800, 50)
        self.create_button("Exibir sinal na frequência", self.ctrl.show_fft, 800, 100)
        self.create_button("Tensão Máxima", self.ctrl.print_max, 800, 150)
        self.create_button("Tensão Mínima", self.ctrl.print_min, 800, 200)

    def on_click(self):
        print('PyQt5 button click')

    def set_image(self, path):
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(700)
        self.label.setPixmap(pixmap)
        
        
