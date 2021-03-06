#!/usr/bin/env python
from samplebase import SampleBase
from kit import SimpleSquare
from mario import Mario
import time


class WrapAnimation(SampleBase):
    def __init__(self, *args, **kwargs):
        super(WrapAnimation, self).__init__(*args, **kwargs)
        self.mario = Mario()
        self.kit = SimpleSquare()

    def run(self):
        max_seconds = 20
        time_running = 0
        while True:
            self.run_animation()



# Main function
if __name__ == "__main__":
    wrap_animation = WrapAnimation()
    if (not wrap_animation.process()):
        wrap_animation.print_help()
