#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep


class PulsingColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(PulsingColors, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        width = 32
        height = 32 
##        numBars = 8
##        barWidth = width/numBars #4
##        height_G = 8
##        height_Y = 4
##        height_O = 2
##        height_R = 2continuum = 0

        x=0
        y = 0
        t = 0
        while(True):
            x +=1
            x %= width
            y +=1
            y %= height
            t += 1
            t %= 256
            sleep(.5)
            for z in range(0, 32):
                offset_canvas.SetPixel( z, y, t, 255, t)
            



        #self.offscreen_canvas.Fill(red, green, blue)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

# Main function
if __name__ == "__main__":
    pulsing_colors = PulsingColors()
    if (not pulsing_colors.process()):
        pulsing_colors.print_help()
