#!/usr/bin/env python
# "sudo ./HypnoColors.py --led-rows=16 --led-cols=32 --led-brightness=20"
from samplebase import SampleBase
from time import sleep
from functions import *
from layer2 import *

##_red = 0x0
##_green = 0x0
##_blue = 0x0

class HypnoColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(HypnoColors, self).__init__(*args, **kwargs)

    def run(self):
        global offset_canvas
        offset_canvas = self.matrix.CreateFrameCanvas() # creates frame
        SinglePixel(offset_canvas, 0, 255, 255)
        DoublePixel(offset_canvas, 255, 0x0, 0x0)
        offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
        dimmer = 0
        while(True):
            e = 0
##            dimmer += 1
##            offset_canvas = PurpleLines(self, 255, 0x0, 255)
##            sleep(.25)
##            GreenThickLines(self, 0x0, (255-dimmer), 0x0)
##            sleep(.5)
##            dimmer%=255
            
            
if __name__ == "__main__":
    hypno_colors = HypnoColors()
    #setColors( 0x0, 0x0, 0x0)
    if (not hypno_colors.process()):
        hypno_colors.print_help()

