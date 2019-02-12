#!/usr/bin/env python
from samplebase import SampleBase


class PulsingColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(PulsingColors, self).__init__(*args, **kwargs)

    def run(self):
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        continuum = 0

        while True:
            #self.usleep(5 * 1000)

            #song_1
            self.usleep(600000 / (114/2))


            #song_2
            #self.usleep(600000 / (116/2))
            
            continuum += 1
            continuum %= 3 * 255

            red = 0
            green = 0
            blue = 0

            if continuum <= 255:
                c = continuum
                blue = 255 - c
                ##blue = c
                red = c
            elif continuum > 255 and continuum <= 511:
                c = continuum - 256
                red = 255 - c
                ##red = c
                green = c
            else:
                c = continuum - 512
                #c = continuum - 256 #green would become neg
                green = 255 - c
                blue = c

            #RGB [ORDER]
            self.offscreen_canvas.Fill(red, green, blue) #b
            #self.offscreen_canvas.Fill(blue, red, green) #r
            # sets to all white!!!
            ##self.offscreen_canvas.Fill(red, red, red)
            # must mean each LED has RGB..?..
            #self.offscreen_canvas.Fill(red, 0, red) 
            self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)

# Main function
if __name__ == "__main__":
    pulsing_colors = PulsingColors()
    if (not pulsing_colors.process()):
        pulsing_colors.print_help()
