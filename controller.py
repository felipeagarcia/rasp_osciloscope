from channel import Channel
import numpy as np
from math import pi

class controller():
	def __init__(self):
		self.sample_rate = 44.1 * 1000 # 44.1 kHz
		self.duration = 2 # 2 seconds
		x = np.linspace(0, self.duration, num=self.duration*self.sample_rate)
		y = np.sin(8*pi*x)
		self.ch = Channel(1, 'r-', y, self.sample_rate, self.duration)

	def show_signal(self):
		self.ch.show()

	def show_fft(self):
		self.ch.plot_fft()

	def print_max(self):
		max_val = self.ch.get_max()
		print("Max Value:", max_val)
		return max_val

	def print_min(self):
		min_val = self.ch.get_min()
		print("Min Value:", min_val)
		return min_val

