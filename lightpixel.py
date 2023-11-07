#!/usr/bin/env python

import time
from random import randint

import unicornhat as unicorn

# A Python code that will light up a point on Unicornhat matrix 8x4

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

while True:
    x = randint(0, 7)
    y = randint(0, 3)
    unicorn.set_pixel(x, y, 255, 255, 255)
    unicorn.show()
    time.sleep(0.1)
    unicorn.set_pixel(x, y, 0, 0, 0)
    unicorn.show()
    time.sleep(0.1)

    