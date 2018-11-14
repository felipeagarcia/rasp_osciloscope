from user_interface import GUI
from controller import controller

class model():
    def __init__(self):
        self.ctrl = controller()
        self.ctrl.show_signal()
        self.gui = GUI(1000, 700)
        self.add_buttons()
        self.gui.txt_freq.setText("Frequência: " + str(self.ctrl.ch.frequency) + " Hz")
        self.gui.txt_per.setText("Período: " + str(1/self.ctrl.ch.frequency) + " s")
        self.gui.txt_rise.setText("Subida: " + str(self.ctrl.ch.compute_rise_time()) + " s")
        self.gui.txt_vmax.setText("Tensão Máxima: " + str(self.ctrl.ch.get_max()) + " V")
        self.gui.txt_vmin.setText("Tensão Mínima: " + str(self.ctrl.ch.get_min()) + " V")
        self.gui.txt_vpic.setText("Tensão Pico a Pico: " + str(self.ctrl.ch.get_peak_to_peak()) + " V")
        self.gui.show()

    def show_signal(self):
        self.ctrl.show_signal()
        self.gui.set_image('imgs/time_plot.png')

    def show_all(self):
        self.ctrl.show_all()
        self.gui.set_image('imgs/full_plot.png')

    def show_fft(self):
        self.ctrl.show_fft()
        self.gui.set_image('imgs/freq_plot.png')

    def auto_scale(self):
        self.ctrl.auto_scale()
        self.gui.set_image('imgs/scaled_plot.png')

    def print_max(self):
        self.ctrl.print_max()

    def print_min(self):
        self.ctrl.print_min()

    def live_plot(self):
        self.ctrl.live_plot()

    def show_hist(self):
        self.ctrl.show_hist()
        self.gui.set_image('imgs/histogram.png')        

    def update(self):
        self.ctrl.update()
        self.gui.txt_freq.setText("Frequência: " + str(self.ctrl.ch.frequency) + " Hz")
        self.gui.txt_per.setText("Período: " + str(1/self.ctrl.ch.frequency) + " s")
        self.gui.txt_rise.setText("Subida: " + str(self.ctrl.ch.compute_rise_time()) + " s")
        self.gui.txt_vmax.setText("Tensão Máxima: " + str(self.ctrl.ch.get_max()) + " V")
        self.gui.txt_vmin.setText("Tensão Mínima: " + str(self.ctrl.ch.get_min()) + " V")
        self.gui.txt_vpic.setText("Tensão Pico a Pico: " + str(self.ctrl.ch.get_peak_to_peak()) + " V")
        self.ctrl.show_signal()
        self.gui.set_image('imgs/time_plot.png')

    def add_buttons(self):
        self.gui.create_button("Sinal no tempo", self.show_signal, 715, 50)
        self.gui.create_button("Sinal completo", self.show_all, 715, 100)
        self.gui.create_button("FFT", self.show_fft, 715, 150)
        self.gui.create_button("Histograma", self.show_hist, 715, 200)
        self.gui.create_button("Auto Scale", self.auto_scale, 865, 50)
        self.gui.create_button("Tempo Real", self.live_plot, 865, 100)
        self.gui.create_button("Medir Sinal", self.update, 865, 150)
