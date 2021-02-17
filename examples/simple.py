#!/usr/bin/env python

import colorsys
import math
import time
from random import randint

import unicornhat as unicorn

def clean():
    unicorn.clear()


print("""Unicorn HAT: Rainbow
Press Ctrl+C to exit!
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180) # 180 is correct when powercord is at top of RPi
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

i = 0.0
offset = 30
r = 128.0
g = 255.0
b = 60.0

try:
    while True:
       for x in range(width):
            for y in range(height):
               unicorn.set_pixel(x, y, int(r),int(g),int(b))

       unicorn.show()
       time.sleep(0.8)

except KeyboardInterrupt:
    unicorn.off()
