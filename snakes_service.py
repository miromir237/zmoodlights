#!/usr/bin/env python

# Snakes service
# Author:  Miroslav Pilat
# Description: This service will display a snake on the Unicorn HAT.
#              There are couple movements that the snake can do:
#                   - The snake will move around the screen and go through the edges.
#                   - The snake will move around the screen and bounce off the edges.
#                   - The snake will move veriticaly and bounce off the edges.
#                   - The snake will move horizontaly and bounce off the edges.
#              The snake will be made of pixels of two different colors.
#              

import signal
import time
from random import randint

import unicornhat as unicorn

# Class that will be used to gracefully exit the service
class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

# Class that will be used to represent the snake and its move around the screen and go through the edges
class SnakePixelsThrough_edges:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 3)]
        self.direction = [randint(-1, 1), randint(-1, 1)]  # random direction
        self.head_colour = [0, 0, 255]  # blue color
        self.body_colour = [0, 255, 0]  # blue color

    def move(self):
        # Save current head position as next position for first body pixel
        next_pos = list(self.head)
        # Update head position
        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]        
        # Here we are not changing the direction of the snake, but instead
        # we are changing the position of the head to the opposite side of the
        # screen. This way the snake will appear to go through the edge of the
        # screen and come out on the other side.
        if self.head[0] < 0:
            self.head[0] = width - 1
        elif self.head[0] >= width:
            self.head[0] = 0

        if self.head[1] < 0:
            self.head[1] = height - 1
        elif self.head[1] >= height:
            self.head[1] = 0

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()

# Class that will be used to represent the snake and its move around the screen and go bounce of the edges
class SnakePixelsBounce_edges:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 3)]
        self.direction = [randint(-1, 1), randint(-1, 1)]  # random direction
        self.head_colour = [0, 0, 255]  # blue color
        self.body_colour = [0, 255, 0]  # blue color    
    # This method is used to move the snake around the screen and bounce it
    # off the edges.
    def move(self):
        # Save current head position as next position for first body pixel
        next_pos = list(self.head)
        # Update head position
        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]

        # Check for collision with edge and change direction if necessary
        if self.head[0] <= 0 or self.head[0] >= width - 1:
            self.direction[0] *= -1
        if self.head[1] <= 0 or self.head[1] >= height - 1:
            self.direction[1] *= -1

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()

# Class that will be used to represent the snake and its horizontal movement
class SnakePixelsHorizontal:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 3)]
        self.direction = [1,1]  # horizontal direction
        self.head_colour = [255, 0, 255]  # blue color
        self.body_colour = [255, 255, 0]  # blue color

    # This method is used to move the snake around the screen on horizontal lines and bounce it
    # off the edges. When it bounces it also moves one pixel down or up depending on the direction.
    def move(self):
        # Save current head position as next position for first body pixel
        next_pos = list(self.head)
        # Update head position
        self.head[0] += self.direction[0]

        # If the head of the snake reaches the edge of the screen, change the direction
        # of the snake and move it one pixel down or up depending on the direction.
        if self.head[0] < 0:
            self.head[0] = 0
            self.direction[0] = 1
            self.head[1] += self.direction[1]
        elif self.head[0] >= width:
            self.head[0] = width - 1
            self.direction[0] = -1
            self.head[1] += self.direction[1]
            
        # If the head of the snake reaches the bottom of the screen, change the direction
        # of the snake and move it one pixel up.
        if self.head[1] > height - 1:
            self.direction[1] = -1 
            self.head[1] += self.direction[1] - 1
        # If the head of the snake reaches the top of the screen, change the direction
        # of the snake and move it one pixel down.
        elif self.head[1] < 0:
            self.direction[1] = 1 
            self.head[1] += self.direction[1] + 1
        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()

# Class that will be used to represent the snake and its vertical movement
class SnakePixelsVertical:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 3)]
        self.direction = [1,1]  # horizontal direction
        self.head_colour = [255, 0, 0]  # blue color
        self.body_colour = [0, 255, 255]  # blue color

    # This method is used to move the snake around the screen on horizontal lines and bounce it
    # off the edges. When it bounces it also moves one pixel down or up depending on the direction.
    def move(self):
        # Save current head position as next position for first body pixel
        next_pos = list(self.head)
        # Update head position
        self.head[1] += self.direction[1]

        # If the head of the snake reaches the edge of the screen, change the direction
        # of the snake and move it one pixel down or up depending on the direction.
        if self.head[1] < 0:
            self.head[1] = 0
            self.direction[1] = 1
            self.head[0] += self.direction[0]
        elif self.head[1] >= height:
            self.head[1] = height - 1
            self.direction[1] = -1
            self.head[0] += self.direction[0]

        # If the head of the snake reaches the bottom of the screen, change the direction
        # of the snake and move it one pixel left/right.
        if self.head[0] > width - 1:
            self.direction[0] = -1 
            self.head[0] += self.direction[0] - 1
        # If the head of the snake reaches the top of the screen, change the direction
        # of the snake and move it one pixel right/left.
        elif self.head[0] < 0:
            self.direction[0] = 1 
            self.head[0] += self.direction[0] + 1

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()        

# This function is used to update brightnes according to daytime
def setBrightness(currenttime):
  currenthour = currenttime.tm_hour
  # if it's between 10 am and 8 pm,
  # use dimmer brightness
  if(currenthour < 7 or currenthour > 21):
    unicorn.brightness(0.2)
  elif (currenthour > 7 and currenthour < 16):
    unicorn.brightness(0.5)
  else:
    unicorn.brightness(0.5)

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()

# Create a snake objects
snake_through = SnakePixelsThrough_edges(randint(0, width - 1), randint(0, height - 1))
snake_bounce = SnakePixelsBounce_edges(randint(0, width - 1), randint(0, height - 1))
snake_horizontal = SnakePixelsHorizontal(0, 0)
snake_vertical = SnakePixelsVertical(7, 3)  

# Put snake objects into a list
snakes = [snake_through, snake_bounce, snake_horizontal, snake_vertical]

def main():
    setBrightness(time.localtime())
    unicorn.clear()

    # Set timer to 90 seconds
    timer = 90
    
    # Randomly pick a snake from the list of snakes
    active_snake = snakes[randint(0, len(snakes) - 1)]
        
    # While timer is not 0, move the snake around the screen
    while timer > 0:
        unicorn.clear()
        # Move the snake around the screen
        active_snake.move()
        # Plot the snake on the Unicorn HAT
        unicorn.set_pixel(active_snake.head[0], active_snake.head[1], *active_snake.head_colour)
        for pixel in active_snake.body:
            unicorn.set_pixel(pixel[0], pixel[1], *active_snake.body_colour)
        # Show the snake on the Unicorn HAT
        unicorn.show()
        # Sleep for 0.1 seconds
        time.sleep(0.1)
        # Decrease timer by 1
        timer -= 1


if __name__ == '__main__':
  killer = GracefulKiller()
  while not killer.kill_now:
      main()

  print("End of the program. I was killed gracefully :)")