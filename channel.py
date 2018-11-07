import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi
import math

# TODO:
# fix compute_fall_time -> done
# fix frequency and period calc -> use FFT !!!!!! ->fixed
# build UI
# acquire real signals

class Channel():
    def __init__(self, identifier, color, signal, sample_rate, duration):
        self.id = identifier
        self.color = color
        self.signal = signal
        self.sample_rate = sample_rate
        self.duration = duration
        self.frequency = self.get_frequency()
        if self.frequency == 0:
            print("Critical error, frequency = 0!")
            self.frequency = 1

    def show(self, step=0.1, save_fig=True):
        auto_correlation = np.correlate(self.signal, self.signal, mode='full')
        # limiting signal by its period
        y = self.signal[:math.ceil(max(auto_correlation)/self.frequency)].copy()
        x = np.linspace(0, self.get_period(), num=len(y))
        plt.plot(x, y, self.color)
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.title("Signal in time")
        plt.grid()
        if(save_fig):
            plt.savefig('imgs/time_plot.png')
            plt.clf()
        else:
            plt.show()

    def get_signal(self):
        return self.signal

    def get_max(self):
        return max(self.signal)

    def get_min(self):
        return min(self.signal)

    def get_peak_to_peak(self):
        return (self.get_max() - self.get_min())

    def get_frequency(self):
        signal_fft = np.fft.fft(self.signal)
        signal_fft = abs(signal_fft)
        frequency = np.argmax(signal_fft)/self.duration
        if frequency == 0:
            signal_fft = signal_fft[1:]
            frequency = np.argmax(signal_fft)/self.duration
        print('freq:', frequency)
        return frequency

    def get_period(self):
        return 1/self.frequency

    def compute_histogram(self, plot=True):
        histogram, bins = np.histogram(self.signal, bins=range(len(self.signal)), density=True)
        x = np.linspace(0, len(histogram), num=len(histogram))
        if plot:
            plt.plot(x, histogram, self.color)
            plt.title("Signal histogram")
            plt.grid()
            plt.show()
        return histogram.min(), histogram.max()

    def compute_rise_time(self):
        base_val, top_val = self.compute_histogram()
        print(base_val)
        print(top_val)
        base_time = 'invalid'
        top_time = 'invalid'
        for i in range(len(self.signal)):
            if(top_val*0.08 <= self.signal[i] <= top_val*0.12):
                base_time = i
            if(top_val*0.88 <= self.signal[i] <= top_val*0.92):
                top_time = i
                break
        if(base_time == 'invalid' or top_time == 'invalid'):
            print("Error, rise time cannot be measured")
        else:
            print('expected', np.arcsin(0.8)/(pi*self.frequency))
            return abs(top_time - base_time)*self.duration/self.sample_rate

    def compute_fall_time(self):
        top_val, base_val = self.compute_histogram(plot=False)
        base_time = 'invalid'
        top_time = 'invalid'
        for i in range(len(self.signal)):
            if(top_val*0.86 <= self.signal[i] <= base_val*0.94):
                top_time = i
            if(base_val*1.06 <= self.signal[i] <= base_val*1.14):
                base_time = i
        if(base_time == 'invalid' or top_time == 'invalid'):
            print("Error, fall time cannot be measured")
        else:
            return abs(base_time - top_time)*self.duration/self.sample_rate

    def plot_fft(self, step=0.1, save_fig=True):
        y = np.fft.fft(self.signal)
        x = np.linspace(-self.frequency, self.frequency, num=len(y))
        plt.plot(x, y, self.color)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Signal FFT")
        plt.grid()
        if(save_fig):
            plt.savefig('imgs/freq_plot.png')
            plt.clf()
        else:
            plt.show()