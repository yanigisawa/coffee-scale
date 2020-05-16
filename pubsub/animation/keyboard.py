#!/usr/bin/env python
import curses
import os
from samplebase import SampleBase
from threading import Thread, Lock

COLUMNS = ['123456qwertyuiopasdfghjklzxcvbnm!@#$%^QWERTYUIOPASDFGHJKLZXCVBNM']


class KeyboardInput(SampleBase):
    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        self.animate = False
        self.lock = Lock()
        self.configure_args()
        self.canvas = self.matrix.CreateFrameCanvas()
        self.animate_thread = None

    def stop(self):
        self.animate = False
        if self.animate_thread is not None:
            self.animate_thread.join()
        self.clear_screen()
    
    def clear_screen(self):
        self.win.addstr("\nClear: {0} - {1}".format(self.canvas.width, self.canvas.height))
        for i in range(self.canvas.width):
            for j in range(self.canvas.height):
                self.canvas.SetPixel(i, j, 0, 0, 0)

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def run(self, key="k"):
        self.win.addstr("{0} / {1} - {2}".format(self.canvas.width, self.canvas.height, key))
        x, y = 0, 7
        start, end, direction = 0, 32, 1
        while self.animate:
            self.usleep(50000)

            for j in range(0, self.canvas.width):
                if j == x + direction * 4:
                    self.canvas.SetPixel(j, y, 255, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 255, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 255, 0, 0)
                elif j == x + direction * 5:
                    self.canvas.SetPixel(j, y, 255, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 255, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 255, 0, 0)
                if j == x + direction * 2:
                    self.canvas.SetPixel(j, y, 175, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 175, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 175, 0, 0)
                elif j == x + direction * 3:
                    self.canvas.SetPixel(j, y, 155, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 155, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 155, 0, 0)
                elif j == x + direction:
                    self.canvas.SetPixel(j, y, 55, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 55, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 55, 0, 0)
                elif j == x: 
                    self.canvas.SetPixel(j, y, 25, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 25, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 25, 0, 0)
                else:
                    self.canvas.SetPixel(j, y, 0, 0, 0)
                    self.canvas.SetPixel(j, y - 1, 0, 0, 0)
                    self.canvas.SetPixel(j, y + 1, 0, 0, 0)

            x = x + direction
            if x > end or x < start:
                direction = -direction

            self.canvas = self.matrix.SwapOnVSync(self.canvas)


    def main(self, win):
        self.animate = True
        win.nodelay(True)
        self.win = win
        prev_key, key="", ""
        win.clear()
        win.addstr("Detected key:")
        while True:
            try:
                key = win.getkey()
                win.clear()
                win.addstr("Detected key:")
                win.addstr(str(key))
                win.addstr("\nTruthy: {0}".format(str(key) == True))
                if key == os.linesep:
                    win.addstr("Detected S - Stop Animate")
                    self.stop()
                    break
                win.addstr("\n{0}".format(key))
                key = str(key)
                win.addstr("\n{0}".format(key))
                if key:
                    win.addstr("\nbegin thread")
                    with self.lock:
                        if self.animate:
                            self.stop()
                        self.animate = True
                    win.addstr("\nbegin thread")
                    self.animate_thread = Thread(target=self.run, args=(key))
                    self.animate_thread.start()
                    prev_key = key
            except Exception as e:
                # No input
                pass


# Main function
if __name__ == "__main__":
    keyboard_input = KeyboardInput()
    curses.wrapper(keyboard_input.main)
