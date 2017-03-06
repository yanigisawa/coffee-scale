import argparse
import time
import sys
import os
import threading
import logging

from rgbmatrix import RGBMatrix, RGBMatrixOptions

log = logging.getLogger()

class SampleBase(threading.Thread):
    def __init__(self, *args, **kwargs):
        log.debug('init base class')
        self._halt = threading.Event()
        options = RGBMatrixOptions()

        options.rows = 16
        options.disable_hardware_pulsing = True

        log.debug('constructing RGBMatrix')
        self.matrix = RGBMatrix(options = options)
        log.debug('exit base init')

    def run(self):
        log.debug('run from base class')

    def set_halt(self):
        log.debug('base, setting halt')
        self._halt.set()
