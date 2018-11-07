from channel import Channel
import numpy as np
from math import pi
import pyaudio
import struct
import sounddevice as sd
import queue
import argparse
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


class controller():
    def __init__(self):
        # p = pyaudio.PyAudio()
        # self.CHUNK = 1024 * 4            # samples per frame
        # self.FORMAT = pyaudio.paInt16    # audio format (bytes per sample)
        # self.CHANNELS = 1                # single channel for microphone
        # self.RATE = 44100                # samples per second
        # self.stream = p.open(
        #     format=self.FORMAT,
        #     channels=self.CHANNELS,
        #     rate=self.RATE,
        #     input=True,
        #     output=False,
        #     frames_per_buffer=self.CHUNK
        # )
        # data = self.stream.read(self.CHUNK)                                   #reading input  
        # signal = struct.unpack(str(2 * self.CHUNK) + 'B', data) 
        # self.signal = np.array(signal)/255
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-w', '--window', type=float, default=200, metavar='DURATION',
            help='visible time slot (default: %(default)s ms)')
        parser.add_argument(
            '-i', '--interval', type=float, default=30,
            help='minimum time between plot updates (default: %(default)s ms)')
        parser.add_argument(
            '-b', '--blocksize', type=int, help='block size (in samples)')
        parser.add_argument(
            '-r', '--samplerate', type=float, help='sampling rate of audio device')
        parser.add_argument(
            '-n', '--downsample', type=int, default=10, metavar='N',
            help='display every Nth sample (default: %(default)s)')
        parser.add_argument(
            'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
            help='input channels to plot (default: the first)')
        self.args = parser.parse_args()
        if any(c < 1 for c in self.args.channels):
            parser.error('argument CHANNEL: must be >= 1')
        self.mapping = [c - 1 for c in self.args.channels]  # Channel numbers start with 1
        self.q = queue.Queue()
        self.RATE=44100
        self.duration = 1  # seconds
        #myrecording = sd.rec(self.duration * self.RATE, samplerate=self.RATE, channels=1,dtype='float64')

        print("**recording**")
        #sd.wait()
        #print(myrecording)
        #myrecording = np.reshape(myrecording, len(myrecording)*len(myrecording[0]))
        #print(myrecording.shape)
        device_info = sd.query_devices(self.args.device, 'input')
        self.args.samplerate = device_info['default_samplerate']
        self.stream = sd.InputStream(
                                device=self.args.device, channels=max(self.args.channels),
                                samplerate=self.RATE)
        self.signal = np.ones(100)
        with self.stream:
            self.signal, _ = self.stream.read(self.RATE)
            self.signal = np.reshape(self.signal, len(self.signal)*len(self.signal[0]))
            self.ch = Channel(1, 'r-', self.signal, self.RATE, len(self.signal)/self.RATE)
        print(self.signal)
        

    def audio_callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        # Fancy indexing with mapping creates a (necessary!) copy:
        self.signal = indata[::self.args.downsample, self.mapping]
        self.signal = np.reshape(self.signal, len(self.signal)*len(self.signal[0]))
        

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

    def update(self):                               #reading input  
        # myrecording = sd.rec(self.duration * self.RATE, samplerate=self.RATE, channels=1,dtype='float64')

        # print("**recording**")
        # sd.wait()
        # print(myrecording)
        # myrecording = np.reshape(myrecording, len(myrecording)*len(myrecording[0]))
        # print(myrecording.shape)
        # self.signal = myrecording*255
        self.stream = sd.InputStream(
                                device=self.args.device, channels=max(self.args.channels),
                                samplerate=self.RATE)
        with self.stream:
            self.signal, _ = self.stream.read(self.RATE)
            self.signal = np.reshape(self.signal, len(self.signal)*len(self.signal[0]))
            self.ch = Channel(1, 'r-', self.signal, self.RATE, len(self.signal)/self.RATE)
