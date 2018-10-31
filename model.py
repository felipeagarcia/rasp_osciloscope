from user_interface import GUI
from controller import controller


class model():
    def __init__(self):
        self.ctrl = controller()
        self.ctrl.show_signal()
        self.gui = GUI(1000, 600)
        self.add_buttons()
        self.gui.show()

    def show_signal(self):
        self.ctrl.show_signal()
        self.gui.set_image('imgs/time_plot.png')

    def show_fft(self):
        self.ctrl.show_fft()
        self.gui.set_image('imgs/freq_plot.png')

    def print_max(self):
        self.ctrl.print_max()

    def print_min(self):
        self.ctrl.print_min()

    def update(self):
        self.ctrl.update()
        self.ctrl.show_signal()
        self.gui.set_image('imgs/time_plot.png')

    def add_buttons(self):
        self.gui.create_button("Exibir sinal no tempo", self.show_signal, 800, 50)
        self.gui.create_button("Exibir sinal na frequência", self.show_fft, 800, 100)
        self.gui.create_button("Tensão Máxima", self.print_max, 800, 150)
        self.gui.create_button("Tensão Mínima", self.print_min, 800, 200)
        self.gui.create_button("Medir Sinal", self.update, 800, 250)
