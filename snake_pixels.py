#!/usr/bin/env python

import time
from random import randint

import unicornhat as unicorn


print("""Snake pixels
You should see randomly coloured dots crossing paths with each other.
If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()

points = []

class LightPoint:

    def __init__(self):
        self.x = randint(0, width - 1)
        self.y = randint(0, height - 1)
        self.kx = 1
        self.ky = 0
        self.colour = []
        for i in range(0, 3):
            self.colour.append(randint(100, 255))


try:
    while True:
        
except KeyboardInterrupt:
    pass