import numpy as np
import matplotlib.pyplot as plt
from math import pi
import math

class Channel():
	def __init__(self, identifier, color, signal):
		self.id = identifier
		self.color = color
		self.signal = signal

	def show(self, step=0.1):
		auto_correlation = np.correlate(self.signal, self.signal, mode='full')
		# limiting signal by its period
		y = self.signal[:math.ceil(max(auto_correlation))].copy()
		x = np.linspace(0, len(y), num=len(y))
		plt.plot(x, y, self.color)
		plt.xlabel("Time (s)")
		plt.ylabel("Voltage (V)")
		plt.title("Signal in time")
		plt.grid()
		plt.show()

	def get_signal(self):
		return self.signal

	def get_max(self):
		return max(self.signal)

	def get_min(self):
		return min(self.signal)

	def get_peak_to_peak(self):
		return (self.get_max() - self.get_min())

	def get_period(self):
		auto_correlation = np.correlate(self.signal, self.signal, mode='full')
		return math.ceil(max(auto_correlation))

	def plot_fft(self, step=0.1):
		y = np.fft.fft(self.signal)
		x = np.linspace(-int(len(y)/2), int(len(y)/2))
		plt.plot(x, y, self.color)
		plt.xlabel("Frequency (Hz)")
		plt.ylabel("Amplitude")
		plt.title("Signal FFT")
		plt.grid()
		plt.show()