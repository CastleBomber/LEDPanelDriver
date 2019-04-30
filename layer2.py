#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep

height = 32 # really 16
width = 32
mid_height = 7 # y-axis
mid_width = 15 # x-axis
low_height = 0
#matrix[][] = two-Dim array
'''
    Next part!!
'''
def GreenThickLines(self, R, G, B):
    offset_canvas = self.matrix.CreateFrameCanvas()

    # Thick square border 1
    offset_canvas.SetPixel( ( mid_width), ( low_height), R, G, B)#
    offset_canvas.SetPixel((mid_width+1), ( low_height), R, G, B)#

    # Thick square border 2
    offset_canvas.SetPixel((mid_width-3), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width-2), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+1), R, G, B)
    
    offset_canvas.SetPixel((mid_width-3),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+2), R, G, B)
    offset_canvas.SetPixel( ( mid_width),(low_height+3), R, G, B)#
    offset_canvas.SetPixel( ( mid_width),(low_height+2), R, G, B)# left
    offset_canvas.SetPixel((mid_width+1),(low_height+2), R, G, B)# right
    offset_canvas.SetPixel((mid_width+1),(low_height+3), R, G, B)#
    offset_canvas.SetPixel((mid_width+2),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+2),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+3), R, G, B)

    offset_canvas.SetPixel((mid_width+3), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width+4), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+1), R, G, B)

    # Thick square border 3
    offset_canvas.SetPixel((mid_width-6),(low_height+4), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-6), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width-6),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width-5), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width-5),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+4), R, G, B)

    offset_canvas.SetPixel((mid_width-6),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+6), R, G, B)##
    offset_canvas.SetPixel((mid_width-3),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+5), R, G, B)
    offset_canvas.SetPixel( ( mid_width),(low_height+6), R, G, B)#
    offset_canvas.SetPixel( ( mid_width),(low_height+5), R, G, B)# left
    offset_canvas.SetPixel((mid_width+1),(low_height+5), R, G, B)# right
    offset_canvas.SetPixel((mid_width+1),(low_height+6), R, G, B)#
    offset_canvas.SetPixel((mid_width+2),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+2),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+6), R, G, B)##
    offset_canvas.SetPixel((mid_width+5),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+5),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+6), R, G, B)

    offset_canvas.SetPixel((mid_width+6),(low_height+4), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+3), R, G, B)##
    offset_canvas.SetPixel((mid_width+6),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+6), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width+6),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width+7), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width+7),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+4), R, G, B)

    # Thick square border 4
    offset_canvas.SetPixel((mid_width-9),(low_height+7), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-9),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-9), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width-9),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width-8), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width-8),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-8),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+7), R, G, B)

    offset_canvas.SetPixel((mid_width-9),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+9), R, G, B)###
    offset_canvas.SetPixel((mid_width-6),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+9), R, G, B)##
    offset_canvas.SetPixel((mid_width-3),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+8), R, G, B)
    offset_canvas.SetPixel( ( mid_width),(low_height+9), R, G, B)#
    offset_canvas.SetPixel( ( mid_width),(low_height+8), R, G, B)# left
    offset_canvas.SetPixel((mid_width+1),(low_height+8), R, G, B)# right
    offset_canvas.SetPixel((mid_width+1),(low_height+9), R, G, B)#
    offset_canvas.SetPixel((mid_width+2),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+2),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+9), R, G, B)##
    offset_canvas.SetPixel((mid_width+5),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+5),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+9), R, G, B)###
    offset_canvas.SetPixel((mid_width+8),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+8),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+9), R, G, B)

    offset_canvas.SetPixel((mid_width+9),(low_height+7), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+9),(low_height+3), R, G, B)##
    offset_canvas.SetPixel((mid_width+9),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+9), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width+9),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width+10), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width+10),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+10),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+7), R, G, B)

    # Thick square border 5
    offset_canvas.SetPixel((mid_width-12),(low_height+10), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width-12),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-12),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-12), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width-12),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width-11), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width-11),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-11),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width-11),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+10), R, G, B)

    offset_canvas.SetPixel((mid_width-12),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-10),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-10),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+12), R, G, B)####
    offset_canvas.SetPixel((mid_width-9),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+12), R, G, B)###
    offset_canvas.SetPixel((mid_width-6),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+12), R, G, B)##
    offset_canvas.SetPixel((mid_width-3),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+11), R, G, B)
    offset_canvas.SetPixel( ( mid_width),(low_height+12), R, G, B)#
    offset_canvas.SetPixel( ( mid_width),(low_height+11), R, G, B)# left
    offset_canvas.SetPixel((mid_width+1),(low_height+11), R, G, B)# right
    offset_canvas.SetPixel((mid_width+1),(low_height+12), R, G, B)#
    offset_canvas.SetPixel((mid_width+2),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+2),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+12), R, G, B)##
    offset_canvas.SetPixel((mid_width+5),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+5),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+12), R, G, B)###
    offset_canvas.SetPixel((mid_width+8),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+8),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+12), R, G, B)####
    offset_canvas.SetPixel((mid_width+11),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+11),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+12), R, G, B)

    offset_canvas.SetPixel((mid_width+12),(low_height+10), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width+12),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+12),(low_height+3), R, G, B)##
    offset_canvas.SetPixel((mid_width+12),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+12), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width+12),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width+13), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width+13),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+13),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width+13),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+10), R, G, B)

    # Thick square, outermost border
    offset_canvas.SetPixel((mid_width-15),(low_height+13), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+10), R, G, B)#####
    offset_canvas.SetPixel((mid_width-15),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width-15),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-15),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-15), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width-15),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width-14), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width-14),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width-14),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width-14),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+10), R, G, B)#####
    offset_canvas.SetPixel((mid_width-14),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+13), R, G, B)

    offset_canvas.SetPixel((mid_width-15),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-15),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-14),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-13),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-13),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-12),(low_height+15), R, G, B)#####
    offset_canvas.SetPixel((mid_width-12),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-11),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-10),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-10),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-9),(low_height+15), R, G, B)####
    offset_canvas.SetPixel((mid_width-9),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-8),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-7),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-6),(low_height+15), R, G, B)###
    offset_canvas.SetPixel((mid_width-6),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-5),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-4),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-3),(low_height+15), R, G, B)##
    offset_canvas.SetPixel((mid_width-3),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-2),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width-1),(low_height+14), R, G, B)
    offset_canvas.SetPixel( ( mid_width),(low_height+15), R, G, B)#
    offset_canvas.SetPixel( ( mid_width),(low_height+14), R, G, B)# left
    offset_canvas.SetPixel((mid_width+1),(low_height+14), R, G, B)# right
    offset_canvas.SetPixel((mid_width+1),(low_height+15), R, G, B)#
    offset_canvas.SetPixel((mid_width+2),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+2),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+3),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+4),(low_height+15), R, G, B)##
    offset_canvas.SetPixel((mid_width+5),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+5),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+6),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+7),(low_height+15), R, G, B)###
    offset_canvas.SetPixel((mid_width+8),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+8),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+9),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+10),(low_height+15), R, G, B)####
    offset_canvas.SetPixel((mid_width+11),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+11),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+12),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+13),(low_height+15), R, G, B)#####
    offset_canvas.SetPixel((mid_width+14),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+14),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+15), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+14), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+15), R, G, B)

    offset_canvas.SetPixel((mid_width+15),(low_height+13), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+10), R, G, B)#####
    offset_canvas.SetPixel((mid_width+15),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width+15),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+15),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+15),(low_height+3), R, G, B)##
    offset_canvas.SetPixel((mid_width+15),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+15), ( low_height), R, G, B)##
    offset_canvas.SetPixel((mid_width+15),(low_height+1), R, G, B)
    offset_canvas.SetPixel((mid_width+16), ( low_height), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+1), R, G, B)##
    offset_canvas.SetPixel((mid_width+16),(low_height+2), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+3), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+4), R, G, B)###
    offset_canvas.SetPixel((mid_width+16),(low_height+5), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+6), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+7), R, G, B)####
    offset_canvas.SetPixel((mid_width+16),(low_height+8), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+9), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+10), R, G, B)#####
    offset_canvas.SetPixel((mid_width+16),(low_height+11), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+12), R, G, B)
    offset_canvas.SetPixel((mid_width+16),(low_height+13), R, G, B)

    # sends out newly made frame
    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
