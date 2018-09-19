import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

	def animated_plot(self):
		fig, ax = plt.subplots()
		auto_correlation = np.correlate(self.signal, self.signal, mode='full')
		# limiting signal by its period
		y = self.signal[:math.ceil(max(auto_correlation))].copy()
		x = np.linspace(0, len(y), num=len(y))
		line, = ax.plot(x, y, self.color)


		def animate(i):
		    line.set_ydata(np.sin(x + i/10.0))  # update the data
		    return line,


		# Init only required for blitting to give a clean slate.
		def init():
		    line.set_ydata(np.ma.array(x, mask=True))
		    return line,
		ani = animation.FuncAnimation(fig, animate, np.arange(0, len(y)), init_func=init,
		                              interval=25, blit=True)
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
		return max(auto_correlation)

	def get_frequency(self):
		return 1/self.get_period()

	def compute_histogram(self, plot=True):
		histogram, bins = np.histogram(self.signal, density=True)
		x = np.linspace(0, len(histogram), len(histogram))
		maximum_val = max(histogram, key=abs)
		histogram = np.divide(histogram, maximum_val)
		maximum_val = max(histogram, key=abs)
		minimum_val = min(histogram, key=abs)
		base_val, top_val = minimum_val, maximum_val
		if plot:
			plt.plot(x, histogram, self.color)
			plt.title("Signal histogram")
			plt.grid()
			plt.show()
		return base_val, top_val

	def compute_rise_time(self):
		base_val, top_val = self.compute_histogram(plot=False)
		print('base', base_val)
		print('top', top_val)
		base_time = 'invalid'
		top_time = 'invalid'
		for i in range(len(self.signal)):
			if(self.signal[i] == base_val):
				base_time = i
			if(self.signal[i] == top_val*0.90):
				top_time = i
		if(base_time == 'invalid' or top_time == 'invalid'):
			print("Error, rise time cannot be measured")
		else:
			return 0.9*top_time - (0.1*top_time + base_time)

	def plot_fft(self, step=0.1):
		y = np.fft.fft(self.signal)
		x = np.linspace(-int(len(y)/2), int(len(y)/2), num=len(y))
		plt.plot(x, y, self.color)
		plt.xlabel("Frequency (Hz)")
		plt.ylabel("Amplitude")
		plt.title("Signal FFT")
		plt.grid()
		plt.show()