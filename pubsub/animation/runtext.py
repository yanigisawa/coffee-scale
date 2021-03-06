#!/usr/bin/env python
# Display a runtext with double-buffering.
import os
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import random
import redis


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.joke = False
        self.load_text()
        self.line = random.randint(0, len(self.all_lines) - 1)
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.animation_queue = os.environ.get("REDIS_ANIMATION_QUEUE")
        num = random.randint(0, 100)
        self.title = {
                "song": "Something Something Dark Side",
                "composer": "Something Something Complete",
                "extra": None
                }

    def load_text(self):
        with open("/home/pi/src/coffee-scale/pubsub/animation/marquee_text.txt", "r") as f:
            self.all_lines = f.readlines()

    def getColor(self):
        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))

        return tuple(rgb)

    def get_line(self):
        if not self.joke:
            line = """## {0} - {1} """.format(self.title['song'], self.title['composer'])
            if self.title["extra"] is not None:
                line += "- {0}".format(self.title["extra"])
            line += " ##"
            return line
        return self.all_lines[self.line].strip()

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        self.load_text()
        font = graphics.Font()
        font_base_path = "/home/pi/src/coffee-scale/pubsub/animation/"
        font.LoadFont(font_base_path + "fonts/7x13.bdf")
        # font.LoadFont("fonts/10x20.bdf")
        color = graphics.Color(*self.getColor())
        title_color = graphics.Color(*self.getColor())
        pos = offscreen_canvas.width
        my_text = self.args.text
        y_coords = [0, 10, 30]
        y_opt, y_other = 1, -1
        count = 0

        while True:
            offscreen_canvas.Clear()
            text = graphics.DrawText(offscreen_canvas, font, pos, y_coords[y_opt], color, self.get_line())

            pos -= 1
            if pos + text < 0:
                count += 1
                if count > 1:
                    self.redis.publish(self.animation_queue, "STOP")
                title_only = False
                pos = offscreen_canvas.width
                y_opt *= -1
                if self.joke:
                    self.line = random.randint(0, 22)
                self.joke = not self.joke
                color = graphics.Color(*self.getColor())
                if self.line >= len(self.all_lines):
                    self.line = 0

            time.sleep(0.03)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
