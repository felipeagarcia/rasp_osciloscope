import numpy as np
#from gpiozero import InputDevice
import matplotlib.pyplot as plt
from channel import Channel


from math import pi

if __name__ == '__main__':
	x = np.linspace(0, 2*pi)
	y = np.sin(x)
	ch1 = Channel(1, 'r-', y)
	ch1.show()
	print(ch1.get_max(), ch1.get_min(), ch1.get_peak_to_peak())
	ch1.plot_fft()
