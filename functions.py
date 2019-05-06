#!/usr/bin/env python
from samplebase import SampleBase
from time import sleep

height = 32 # really 16
width = 32
mid_height = 7 # y-axis
mid_width = 15 # x-axis
#matrix[][] = two-Dim array

_red = 0x0
_green = 0x0
_blue = 0x0

'''
    Will turn of LEDs for cool pattern
    Aiming for hypnotic pattern
    Starting by creating simple squares

    Using 16x32 matrices, mirrored facing
    
'''

def SinglePixel(self, R, G, B):
    #offset_canvas = self.matrix.CreateFrameCanvas()
    offset_canvas = self
    offset_canvas.SetPixel((17), 13, R, G, B)
    #offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

def DoublePixel(self, R, G, B):
    #offset_canvas = self.matrix.CreateFrameCanvas()
    offset_canvas = self
    offset_canvas.SetPixel((18), 14, R, G, B)
    #offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


def PurpleLines(self, R, G, B):
    offset_canvas = self.matrix.CreateFrameCanvas()

    # Square rim 1                     x, y
    offset_canvas.SetPixel((mid_width-1), 0, R, G, B)
    
    offset_canvas.SetPixel((mid_width-1), 1, R, G, B)
    offset_canvas.SetPixel( ( mid_width), 1, R, G, B) ##
    offset_canvas.SetPixel((mid_width+1), 1, R, G, B) ##
    offset_canvas.SetPixel((mid_width+2), 1, R, G, B)
    
    offset_canvas.SetPixel((mid_width+2), 0, R, G, B)
    
    # Square rim 2                     x, y
    offset_canvas.SetPixel((mid_width-4), 0, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 1, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 2, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 3, R, G, B)
    
    offset_canvas.SetPixel((mid_width-4), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-3), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-2), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-1), 4, R, G, B)
    offset_canvas.SetPixel( ( mid_width), 4, R, G, B) ##blue
    offset_canvas.SetPixel((mid_width+1), 4, R, G, B) ##red
    offset_canvas.SetPixel((mid_width+2), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+3), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+4), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 4, R, G, B)
    
    offset_canvas.SetPixel((mid_width+5), 3, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 2, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 1, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 0, R, G, B)

    # Square rim 3                     x, y
    offset_canvas.SetPixel((mid_width-7), 0, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 1, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 2, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width-7), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 5, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 6, R, G, B)

    offset_canvas.SetPixel((mid_width-7), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-6), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-5), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 7, R, G, B)##
    offset_canvas.SetPixel((mid_width-3), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-2), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-1), 7, R, G, B)
    offset_canvas.SetPixel( ( mid_width), 7, R, G, B) ##blue
    offset_canvas.SetPixel((mid_width+1), 7, R, G, B) ##red
    offset_canvas.SetPixel((mid_width+2), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+3), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+4), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 7, R, G, B)##
    offset_canvas.SetPixel((mid_width+6), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+7), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 7, R, G, B)

    offset_canvas.SetPixel((mid_width+8), 6, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 5, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width+8), 2, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 1, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 0, R, G, B)

    # Square rim 4                    x  , y
    offset_canvas.SetPixel((mid_width-10), 0, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 1, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 2, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width-10), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 5, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 6, R, G, B)#
    offset_canvas.SetPixel((mid_width-10), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 8, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 9, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-9), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-8), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 10, R, G, B)#
    offset_canvas.SetPixel((mid_width-6), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-5), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 10, R, G, B)##
    offset_canvas.SetPixel((mid_width-3), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-2), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-1), 10, R, G, B)
    offset_canvas.SetPixel( ( mid_width), 10, R, G, B) ##blue
    offset_canvas.SetPixel((mid_width+1), 10, R, G, B) ##red
    offset_canvas.SetPixel((mid_width+2), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+3), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+4), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 10, R, G, B)##
    offset_canvas.SetPixel((mid_width+6), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+7), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 10, R, G, B)#
    offset_canvas.SetPixel((mid_width+9), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+10), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 10, R, G, B)

    offset_canvas.SetPixel((mid_width+11), 9, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 8, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 6, R, G, B)#
    offset_canvas.SetPixel((mid_width+11), 5, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width+11), 2, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 1, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 0, R, G, B)

    # Square rim 5                     x , y
    offset_canvas.SetPixel((mid_width-13), 0, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 1, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 2, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width-13), 4, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 5, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 6, R, G, B)#
    offset_canvas.SetPixel((mid_width-13), 7, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 8, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 9, R, G, B)####
    offset_canvas.SetPixel((mid_width-13), 10, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 11, R, G, B)
    offset_canvas.SetPixel((mid_width-13), 12, R, G, B)

    offset_canvas.SetPixel((mid_width-13), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-12), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-11), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-10), 13, R, G, B)#### 4's end
    offset_canvas.SetPixel((mid_width-9), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-8), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-7), 13, R, G, B)###
    offset_canvas.SetPixel((mid_width-6), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-5), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-4), 13, R, G, B)##
    offset_canvas.SetPixel((mid_width-3), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-2), 13, R, G, B)
    offset_canvas.SetPixel((mid_width-1), 13, R, G, B)
    offset_canvas.SetPixel( ( mid_width), 13, R, G, B) # blue
    offset_canvas.SetPixel((mid_width+1), 13, R, G, B) # red
    offset_canvas.SetPixel((mid_width+2), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+3), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+4), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+5), 13, R, G, B)##
    offset_canvas.SetPixel((mid_width+6), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+7), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+8), 13, R, G, B)###
    offset_canvas.SetPixel((mid_width+9), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+10), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+11), 13, R, G, B)#### 4's end
    offset_canvas.SetPixel((mid_width+12), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+13), 13, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 13, R, G, B)

    offset_canvas.SetPixel((mid_width+14), 12, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 11, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 10, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 9, R, G, B)####
    offset_canvas.SetPixel((mid_width+14), 8, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 7, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 6, R, G, B)#
    offset_canvas.SetPixel((mid_width+14), 5, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 4, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 3, R, G, B)#
    offset_canvas.SetPixel((mid_width+14), 2, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 1, R, G, B)
    offset_canvas.SetPixel((mid_width+14), 0, R, G, B)

        
    # sends out newly made frame
    #offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
    return offset_canvas

'''
    set pixels on a tmp frame
    this from will swap into current matrix display

    lulz! ~self.matrix.Fill(0, 0, 0)
'''
def FillMe(self, red, green, blue):
    offset_canvas = self.matrix.CreateFrameCanvas()

    offset_canvas.Fill( 0x0, 0x0, 0x0)
    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
    
# Using for PyTest
def setColors( R, G, B):
    _red = R
    _green = G
    _blue = B
    return _red

#def RGBLines( R, G, B):
    

