#!/usr/bin/env python

import signal
import time
from random import randint

import unicornhat as unicorn


print("""Bouncing pixel
You should see randomly coloured dots crossing paths with each other.
If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()

points = []

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

class LightPoint:
    def __init__(self):
        self.x = randint(0, width - 1)
        self.y = randint(0, height - 1)
        self.kx = 1
        self.ky = 1
        self.colour = []
        for i in range(0, 3):
            self.colour.append(randint(100, 255))

def update_positions():
    for point in points:
        if ((point.y + point.ky) > height - 1) or ((point.y + point.ky) < 0):
            point.ky = -point.ky

        if ((point.x + point.kx) > width - 1) or ((point.x + point.kx) < 0):
            point.kx = -point.kx
        
        point.x += point.kx
        point.y += point.ky
                
def plot_points():
    unicorn.clear()
    for point in points:
        unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
    unicorn.show()

def setBrightness(currenttime):
  currenthour = currenttime.tm_hour
  # if it's between 10 am and 8 pm,
  # use dimmer brightness
  if(currenthour < 7 or currenthour > 22):
    unicorn.brightness(0.2)
  elif (currenthour > 7 and currenthour < 16):
    unicorn.brightness(0.8)
  else:
    unicorn.brightness(0.4)

def main():
    setBrightness(time.localtime())
    if len(points) < 5 and randint(0, 5) > 1:
        points.append(LightPoint())
    plot_points()
    update_positions()
    time.sleep(0.3)

if __name__ == '__main__':
  killer = GracefulKiller()
  while not killer.kill_now:
      main()

  print("End of the program. I was killed gracefully :)")

     
