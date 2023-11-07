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
        self.kx = 1 if randint(0, 1) == 0 else -1
        self.ky = 1 if randint(0, 1) == 0 else -1
        self.colour = []
        for i in range(0, 3):
            self.colour.append(randint(100, 255))

    def move(self):
        self.x += self.kx
        self.y += self.ky
        if self.x < 0 or self.x >= width:
            self.kx *= -1
        if self.y < 0 or self.y >= height:
            self.ky *= -1

points = [LightPoint() for _ in range(4)]

try:
    while True:
        unicorn.clear()
        for point in points:
            point.move()
            unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
        unicorn.show()
        time.sleep(0.01)
except KeyboardInterrupt:
    unicorn.clear()
    unicorn.show()