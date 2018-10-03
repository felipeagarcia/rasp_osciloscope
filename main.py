import numpy as np
#from gpiozero import InputDevice
import matplotlib.pyplot as plt
from channel import Channel
from math import pi

if __name__ == '__main__':
	sample_rate = 44.1 * 1000 # 44.1 kHz
	duration = 2 # 2 seconds
	x = np.linspace(0, duration, num=duration*sample_rate)
	y = np.sin(8*pi*x)
	ch1 = Channel(1, 'r-', y, sample_rate, duration)
	ch1.show()
	print(ch1.get_max(), ch1.get_min(), ch1.get_peak_to_peak(), ch1.get_period())
	ch1.plot_fft()
	print('rise_time', ch1.compute_rise_time())
