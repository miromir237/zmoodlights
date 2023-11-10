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

#print(f"Width: {width}, Height: {height}")

class SnakePixels:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 4)]
        self.direction = [randint(-1, 1), randint(-1, 1)]  # random direction
        self.head_colour = [0, 0, 255]  # blue color
        self.body_colour = [0, 255, 0]  # blue color

    def move_through_edges(self):
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

    # This method is used to move the snake around the screen and bounce it
    # off the edges.
    def move_bounce_edges(self):
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

# Randomize starting position

snake = SnakePixels(randint(0, width - 1), randint(0, height - 1))

try:
    while True:
        unicorn.clear()
        # If direction is [0, 0], generate a new random direction
        if snake.direction == [0, 0]:
            snake.direction = [randint(-1, 1), randint(-1, 1)]
        # If direction is [0,1] or [1,0], move the snake through the edges
        if snake.direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            snake.move_through_edges()
        else:
            snake.move_bounce_edges()

        #snake.move_through_edges()
        #snake.move_bounce_edges()
        unicorn.set_pixel(snake.head[0], snake.head[1], *snake.head_colour)
        for pixel in snake.body:
            unicorn.set_pixel(pixel[0], pixel[1], *snake.body_colour)
        unicorn.show()
        time.sleep(0.1)
except KeyboardInterrupt:
    unicorn.clear()
    unicorn.show()
