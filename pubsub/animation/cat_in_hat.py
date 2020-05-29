#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep

class CatInTheHat(SampleBase):
    def __init__(self, *args, **kwargs):
        super(CatInTheHat, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix.CreateFrameCanvas()
        print("{0} / {1}".format(canvas.width, canvas.height))
        print("{0} / {1}".format(self.matrix.width, self.matrix.height))
        # x and y are top left of the hat - note: brim will be x - 3
        x, y = 8, 0
        min_x, max_x = 0, 16
        min_y, max_y = 0, 32
        width = 10

        for i in range(width):
            canvas.SetPixel(x + i, y, 255, 0, 0)
            canvas.SetPixel(x + i, y + 1, 255, 0, 0)
            canvas.SetPixel(x + i, y + 2, 255, 0, 0)

            canvas.SetPixel(x + i, y + 3, 255, 255, 255)
            canvas.SetPixel(x + i, y + 4, 255, 255, 255)
            canvas.SetPixel(x + i, y + 5, 255, 255, 255)

            canvas.SetPixel(x + i, y + 6, 255, 0, 0)
            canvas.SetPixel(x + i, y + 7, 255, 0, 0)
            canvas.SetPixel(x + i, y + 8, 255, 0, 0)

            canvas.SetPixel(x + i, y + 9, 255, 255, 255)
            canvas.SetPixel(x + i, y + 10, 255, 255, 255)
            canvas.SetPixel(x + i, y + 11, 255, 255, 255)


            canvas.SetPixel(x + i, y + 12, 255, 0, 0)
            canvas.SetPixel(x + i, y + 13, 255, 0, 0)
            canvas.SetPixel(x + i, y + 14, 255, 0, 0)


        for i in range(x - 2, x + width + 2):
            canvas.SetPixel(i, y + 15, 255, 255, 255)
            # canvas.SetPixel(i, y + 4, 255, 255, 255)
            # canvas.SetPixel(i, y + 5, 255, 255, 255)



        canvas = self.matrix.SwapOnVSync(canvas)

        while True:
            sleep(10)



# Main function
if __name__ == "__main__":
    cat_in_the_hat = CatInTheHat()
    if (not cat_in_the_hat.process()):
        cat_in_the_hat.print_help()
