#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep

height = 32 # really 16
width = 32
mid_height = 7 # y-axis
mid_width = 15 # x-axis
#matrix[][] = two-Dim array
'''
    Will turn of LEDs for cool pattern
    Aiming for hypnotic pattern
    Starting by creating simple squares

    Using 16x32 matrices, mirrored facing
'''
def SinglePixel(self):
    offset_canvas = self.matrix.CreateFrameCanvas()
    offset_canvas.SetPixel((17), 13, 255, 255, 255)
    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


def WhiteLines(self):
    offset_canvas = self.matrix.CreateFrameCanvas()

    # Square rim 1                     x, y
    offset_canvas.SetPixel((mid_width-1), 0, 255, 255, 255)
    
    offset_canvas.SetPixel((mid_width-1), 1, 255, 255, 255)
    offset_canvas.SetPixel( ( mid_width), 1, 255, 255, 255) ##
    offset_canvas.SetPixel((mid_width+1), 1, 255, 255, 255) ##
    offset_canvas.SetPixel((mid_width+2), 1, 255, 255, 255)
    
    offset_canvas.SetPixel((mid_width+2), 0, 255, 255, 255)

    # Square rim 2                     x, y
    offset_canvas.SetPixel((mid_width-4), 0, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 3, 255, 255, 255)
    
    offset_canvas.SetPixel((mid_width-4), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-3), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-2), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-1), 4, 255, 255, 255)
    offset_canvas.SetPixel( ( mid_width), 4, 0x0, 0x0, 255) ##blue
    offset_canvas.SetPixel((mid_width+1), 4, 255, 0x0, 0x0) ##red
    offset_canvas.SetPixel((mid_width+2), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+3), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+4), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 4, 255, 255, 255)
    
    offset_canvas.SetPixel((mid_width+5), 3, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 0, 255, 255, 255)

    # Square rim 3                     x, y
    offset_canvas.SetPixel((mid_width-7), 0, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-7), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 6, 255, 255, 255)

    offset_canvas.SetPixel((mid_width-7), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-6), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-5), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 7, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width-3), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-2), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-1), 7, 255, 255, 255)
    offset_canvas.SetPixel( ( mid_width), 7, 0x0, 0x0, 255) ##blue
    offset_canvas.SetPixel((mid_width+1), 7, 255, 0x0, 0x0) ##red
    offset_canvas.SetPixel((mid_width+2), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+3), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+4), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 7, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width+6), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+7), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 7, 255, 255, 255)

    offset_canvas.SetPixel((mid_width+8), 6, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+8), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 0, 255, 255, 255)

    # Square rim 4                    x  , y
    offset_canvas.SetPixel((mid_width-10), 0, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-10), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 6, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-10), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 8, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 9, 255, 255, 255)

    offset_canvas.SetPixel((mid_width-10), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-9), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-8), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 10, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-6), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-5), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 10, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width-3), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-2), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-1), 10, 255, 255, 255)
    offset_canvas.SetPixel( ( mid_width), 10, 0x0, 0x0, 255) ##blue
    offset_canvas.SetPixel((mid_width+1), 10, 255, 0x0, 0x0) ##red
    offset_canvas.SetPixel((mid_width+2), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+3), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+4), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 10, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width+6), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+7), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 10, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+9), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+10), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 10, 255, 255, 255)

    offset_canvas.SetPixel((mid_width+11), 9, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 8, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 6, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+11), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+11), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 0, 255, 255, 255)

    # Square rim 5                     x , y
    offset_canvas.SetPixel((mid_width-13), 0, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-13), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 6, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width-13), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 8, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 9, 255, 255, 255)####
    offset_canvas.SetPixel((mid_width-13), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 11, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-13), 12, 255, 255, 255)

    offset_canvas.SetPixel((mid_width-13), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-12), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-11), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-10), 13, 255, 255, 255)#### 4's end
    offset_canvas.SetPixel((mid_width-9), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-8), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-7), 13, 255, 255, 255)###
    offset_canvas.SetPixel((mid_width-6), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-5), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-4), 13, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width-3), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-2), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width-1), 13, 255, 255, 255)
    offset_canvas.SetPixel( ( mid_width), 13, 0x0, 0x0, 255) # blue
    offset_canvas.SetPixel((mid_width+1), 13, 255, 0x0, 0x0) # red
    offset_canvas.SetPixel((mid_width+2), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+3), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+4), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+5), 13, 255, 255, 255)##
    offset_canvas.SetPixel((mid_width+6), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+7), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+8), 13, 255, 255, 255)###
    offset_canvas.SetPixel((mid_width+9), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+10), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+11), 13, 255, 255, 255)#### 4's end
    offset_canvas.SetPixel((mid_width+12), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+13), 13, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 13, 255, 255, 255)

    offset_canvas.SetPixel((mid_width+14), 12, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 11, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 10, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 9, 255, 255, 255)####
    offset_canvas.SetPixel((mid_width+14), 8, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 7, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 6, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+14), 5, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 4, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 3, 255, 255, 255)#
    offset_canvas.SetPixel((mid_width+14), 2, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 1, 255, 255, 255)
    offset_canvas.SetPixel((mid_width+14), 0, 255, 255, 255)

        
    # sends out newly made frame
    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

'''
    set pixels on a tmp frame
    this from will swap into current matrix display
'''
def ArtsyCanvas(self, red, green, blue):
    offset_canvas = self.matrix.CreateFrameCanvas()
    for x in range(0, width):
        for y in range(0, height):
            offset_canvas.SetPixel(x, y, red, green, blue)
    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
    
