#!/usr/bin/env python
from samplebase import SampleBase
import random
import time
import pyaudio
import time
import sys

FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1
RATE = 44100
CHUNK = 1024 # 1024bytes of data red from a buffer

def get_stream():
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
    return stream, audio

def stop_stream(stream):
    stream.stop_stream()
    stream.close()

class VisualMic(SampleBase):
    def __init__(self, *args, **kwargs):
        super(VisualMic, self).__init__(*args, **kwargs)
        # self.toroidal = False
        stream, audio = get_stream()
        self.stream = stream
        self.audio = audio


    def run(self):
        while True:

            # TODO: pull from self.stream
            # normalize data for -32k to 32k integers?
            # draw number of pixels?
            # draw lines based on length?

            self.canvas = self.matrix.SwapOnVSync(self.canvas)



# Main function
if __name__ == "__main__":
    gol = GameOfLifeAtom()
    if (not gol.process()):
        gol.print_help()
