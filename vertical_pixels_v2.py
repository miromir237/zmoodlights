#!/usr/bin/env python

# Running the pixels top down like a faling snow

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
width,height=unicorn.get_shape()

points = []

class LightPoint:

    def __init__(self,xpos):
        self.x = xpos
        self.y = randint(1,5)
        self.dx = 0
        self.dy = -1
        self.colour = []
        for i in range(0, 3):
            self.colour.append(randint(100, 255))

def update_positions():
    for point in points:
        if ((point.y + point.dy) < 0):
            point.y = height
        point.y += point.dy
                

def plot_points():
    unicorn.clear()
    for point in points:
        unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
    unicorn.show()

## Main

for i in range(0,8):
    points.append(LightPoint(i))

try:
    while True:
        plot_points()
        update_positions()
        time.sleep(0.3)        
except KeyboardInterrupt:
    pass
