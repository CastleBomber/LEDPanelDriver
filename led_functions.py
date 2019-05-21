from struct import unpack
import numpy as np


sample_rate = 44100
chunk = 4000
device = 2


def red(y):
    if(y < 2): return 0
    if(y > 13): return 255
    return 255/16*y

def green(y):
    if(y > 13): return 0
    if(y < 2): return 255
    return 19*(19/y)

def piff(val):
    return int(2*chunk*val/sample_rate)
