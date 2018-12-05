from channel import Channel
import numpy as np
from math import pi
import pyaudio
import struct
import sounddevice as sd
import queue
import argparse
import test as live


class controller():
    def __init__(self):
        self.RATE = 44100
        self.duration = 0.5 #sec
        sd.default.samplerate = self.RATE
        sd.default.channels = 2
        myrecording = sd.rec(int(self.duration * self.RATE), dtype='float64')
        print('Recording...')
        sd.wait()
        myrecording = np.array(myrecording)
        ch1 = myrecording[:,0]
        ch2 = myrecording[:,1]
        self.signal = ch1
        print(len(ch1))
        print(myrecording)
        self.ch = Channel(1, 'b-', self.signal, self.RATE, self.duration)

    def audio_callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        # Fancy indexing with mapping creates a (necessary!) copy:
        self.signal = indata[::self.args.downsample, self.mapping]
        self.signal = np.reshape(self.signal, len(self.signal)*len(self.signal[0]))
        

    def show_signal(self):
        self.ch.show()

    def show_all(self):
        self.ch.show_entire_signal()

    def show_fft(self):
        self.ch.plot_fft()

    def auto_scale(self):
        self.ch.show_scaled()

    def live_plot(self):
        live.live()

    def show_hist(self):
        self.ch.compute_histogram()

    def eye_diagram(self):
        self.ch.eye_diagram()

    def print_max(self):
        max_val = self.ch.get_max()
        print("Max Value:", max_val)
        return max_val

    def print_min(self):
        min_val = self.ch.get_min()
        print("Min Value:", min_val)
        return min_val

    def update(self):                               #reading input  
        myrecording = sd.rec(int(self.duration * self.RATE))
        print('Recording...')
        sd.wait()
        ch1 = myrecording[:,0]
        ch2 = myrecording[:,1]
        self.signal = ch1
        self.ch = Channel(1, 'b-', self.signal, self.RATE, self.duration)
