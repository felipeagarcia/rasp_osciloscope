import numpy as np
#from gpiozero import InputDevice
import matplotlib.pyplot as plt
from channel import Channel
from math import pi
import string, serial
from user_interface import GUI

if __name__ == '__main__':
	# sample_rate = 44.1 * 1000 # 44.1 kHz
	# duration = 2 # 2 seconds
	# x = np.linspace(0, duration, num=duration*sample_rate)
	# y = np.sin(8*pi*x)
	# ch1 = Channel(1, 'r-', y, sample_rate, duration)
	# ch1.show()
	# print(ch1.get_max(), ch1.get_min(), ch1.get_peak_to_peak(), ch1.get_period())
	# ch1.plot_fft()
	# print('rise_time', ch1.compute_rise_time())
	gui = GUI(800, 600)
	gui.show()

	# output = " "
	# ser = serial.Serial('/dev/bus/usb/001/001', 4800, 8, 'N', 1, timeout=1)
	# while True:
	#   print("----")
	#   while output != "":
	#     output = ser.readline()
	#     print (output)