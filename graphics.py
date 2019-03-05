#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/5x7.bdf")

        red = graphics.Color(255, 0, 0)
        green = graphics.Color(0, 250, 0)
        blue = graphics.Color(0, 0, 255)
        
        #graphics.DrawLine(canvas, 10, 10, 22, 13, green)
        #graphics.DrawCircle(canvas, 30, 15, 10, blue)
        graphics.DrawText(canvas, font, 1, 30, red, "cBombs")

        time.sleep(30)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
