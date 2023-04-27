#!/usr/bin/env python

# Pixel bars moving up and down according to system load

import os
import unicornhat as unicorn
import time

def clean():
    unicorn.clear()

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

points = []

# Screen matrix
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7


class LightPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cred = [255,0,0]
        self.cgreen = [0,255,0]
        self.cyellow = [255,255,0]
        self.colour = []
        if (self.x > 6):
            self.colour = self.cred
        elif (self.x > 4):
            self.colour = self.cyellow
        else:
            self.colour = self.cgreen
        
# Function to plot points
def plot_points():
    unicorn.clear()
    for point in points:
        unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
    unicorn.show()

try:
    while True:
        # Get system load
        load = os.getloadavg()

        # Get system memory
        mem = os.popen('free -t -m').readlines()[-3].split()[1:4]

        memusedprec = int( ((int(mem[1]) / int(mem[0])) * 100) / 8)
        
        # Prepare screen matrix (x represents load, y represents bar)
        for y in range(0, 3):
            rozsah_x = int((load[y] * 100) / 8)
            for x in range(0, rozsah_x):
                points.append(LightPoint(x,y))
                
        for x in range(0, memusedprec):
            points.append(LightPoint(x,4))
            
        plot_points()

        time.sleep(0.3)
        
except KeyboardInterrupt:
    pass        