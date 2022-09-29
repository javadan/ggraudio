import numpy as np
import pyaudio
import time, sys, math
from collections import deque

from src.utils import *

class Stream_Reader:

    def __init__(self,
        device = None,
        rate = None):

        self.rate = rate
        self.pa = pyaudio.PyAudio()

        self.device = device
        self.rate = 44100
        self.update_window_n_frames = 44100

        self.new_data = False

        self.stream = self.pa.open(
            input_device_index=self.device,
            format = pyaudio.paInt16,
            channels = 1,
            rate = self.rate,
            input=True,
            frames_per_buffer = self.rate)


    def get_frame(self):
        data = stream.read(frame_len, exception_on_overflow=False)
        frame_data = librosa.util.buf_to_float(data, n_bytes=2, dtype=np.int16)
        return frame_data

    def terminate(self):
        print("  Sending stream termination command...")
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

