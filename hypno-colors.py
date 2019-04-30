#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep
from functions import *
from layer2 import *

class HypnoColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(HypnoColors, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas() # creates frame
        #self.matrix.Fill(0xFF, 0xFF, 0) # Fills all LEDs
        #sleep(1)
        WhiteLines(self)
        sleep(.25)
        #FillMe(self, 0x0, 0x0, 0x0)
        GreenThickLines(self, 0x0, 255, 0x0)
        #offset_canvas.Fill( 0x0, 0x0, 0x0)
        #offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
        #SinglePixel(self)        
        dimmer = 0
        while(True):
            dimmer += 1
            WhiteLines(self)
            sleep(.25)
            GreenThickLines(self, 0x0, (255-dimmer), 0x0)
            sleep(.5)
            dimmer%=255
            
            
if __name__ == "__main__":
    hypno_colors = HypnoColors()
    if (not hypno_colors.process()):
        hypno_colors.print_help()
