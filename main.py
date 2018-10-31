import numpy as np
#from gpiozero import InputDevice
import matplotlib.pyplot as plt
from channel import Channel
from math import pi
import string, serial
import pyaudio
import struct
from model import model

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
    model = model()



     
    # CHUNK = 1024 * 4            # samples per frame
    # FORMAT = pyaudio.paInt16    # audio format (bytes per sample)
    # CHANNELS = 1                # single channel for microphone
    # RATE = 44100                # samples per second

     
     
    # p = pyaudio.PyAudio()
     
    # stream = p.open(
    #     format=FORMAT,
    #     channels=CHANNELS,
    #     rate=RATE,
    #     input=True,
    #     output=True,
    #     frames_per_buffer=CHUNK
    # )

    # while True:
    #     data = stream.read(CHUNK)                                   #reading input  
    #     data_int = struct.unpack(str(2 * CHUNK) + 'B', data)    #converts bytes to integers

    #     sample_rate = 44.1 * 1000 # 44.1 kHz
    #     duration = 2 # 2 seconds
    #     data_int = np.array(data_int)/255
    #     ch1 = Channel(1, 'r-', data_int, RATE, len(data_int)/RATE)
    #     ch1.show()
    #     print(ch1.get_max(), ch1.get_min(), ch1.get_peak_to_peak(), ch1.get_period())
    #     ch1.plot_fft()
