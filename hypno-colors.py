#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep
from functions import *

class HypnoColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(HypnoColors, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas() # creates frame
        #self.matrix.Fill(0xFF, 0xFF, 0) # Fills all LEDs
        #sleep(1)
        WhiteLines(self)
        #SinglePixel(self)        
        #sleep(1)
        #ArtsyCanvas(self, 0, 0, 255)
        
        while(True):
            NOP=0
            
if __name__ == "__main__":
    hypno_colors = HypnoColors()
    if (not hypno_colors.process()):
        hypno_colors.print_help()
