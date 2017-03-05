import argparse
import time
import sys
import os
import threading
import logging

# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
# from rgbmatrix import RGBMatrix, RGBMatrixOptions

log = logging.getLogger()

class SampleBase(threading.Thread):
    def __init__(self, *args, **kwargs):
        log.debug('init base class')
        self._halt = threading.Event()

    def run(self):
        log.debug('run from base class')

    def set_halt(self):
        log.debug('base, setting halt')
        self._halt.set()
