#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep

height = 32 # really 16
width = 32
mid_height = 7 # y-axis
mid_width = 15 # x-axis
#matrix[][] = two-Dim array
'''
    Next part!!
'''
def GreenThickLines(self):
    offset_canvas = self.matrix.CreateFrameCanvas()

    # Thick square border 1
    offset_canvas.SetPixel( ( mid_width), 1, 0x0, 255, 0x0)
    offset_canvas.SetPixel((mid_width+1), 1, 0x0, 255, 0x0)
