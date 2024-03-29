#!/usr/bin/env python

# Running the pixel top down like a faling snow

import colorsys
import math
import time
from random import randint

import unicornhat as unicorn

def clean():
    unicorn.clear()

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

try:
    while True:
        x = randint(0, (u_width-1))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        for y in range(0,u_height,1):
            unicorn.set_pixel(x, u_height-y-1, r, g, b)
            #print("y = " + str(u_height-y-1))
            unicorn.show()
            time.sleep(0.15)
            clean()
        
except KeyboardInterrupt:
    pass
