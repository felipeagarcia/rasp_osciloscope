from channel import Channel
import numpy as np
from math import pi
import pyaudio
import struct


class controller():
    def __init__(self):
        p = pyaudio.PyAudio()
        self.CHUNK = 1024 * 4            # samples per frame
        self.FORMAT = pyaudio.paInt16    # audio format (bytes per sample)
        self.CHANNELS = 1                # single channel for microphone
        self.RATE = 44100                # samples per second
        self.stream = p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )
        data = self.stream.read(self.CHUNK)                                   #reading input  
        signal = struct.unpack(str(2 * self.CHUNK) + 'B', data) 
        self.signal = np.array(signal)/255
        self.ch = Channel(1, 'r-', self.signal, self.RATE, len(self.signal)/self.RATE)

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

    def update(self):
        data = self.stream.read(self.CHUNK)                                   #reading input  
        signal = struct.unpack(str(2 * self.CHUNK) + 'B', data) 
        self.signal = np.array(signal)/255
        self.ch = Channel(1, 'r-', self.signal, self.RATE, len(self.signal)/self.RATE)