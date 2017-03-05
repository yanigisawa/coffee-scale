import argparse
import time
import sys
import os
import logging

from base import SampleBase 

# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
# from rgbmatrix import RGBMatrix, RGBMatrixOptions

log = logging.getLogger()

class Square(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Square, self).__init__()
        log.debug('init square class')

    def run(self):
        for i in range(10):
            if self._halt.isSet(): 
                log.debug('received halt')
                break
            log.debug('executing from square {0}'.format(i))
            time.sleep(1)
