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

class SnakePixels:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 4)]
        #self.direction = [randint(-1, 1), randint(-1, 1)]  # random direction
        #self.direction = [1,0] # moves horizontal
        self.direction = [0,1] # moves vertical
        self.head_colour = [0, 0, 255]  # blue color
        self.body_colour = [0, 255, 0]  # blue color


    def move(self):
        # Save current head position as next position for first body pixel
        next_pos = list(self.head)
        # Update head position
        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]

        # Check for collision with edge and change direction if necessary
        if self.head[0] < 0 or self.head[0] >= width:
            self.direction[0] *= -1
        if self.head[1] < 0 or self.head[1] >= height:
            self.direction[1] *= -1

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()

    def move_through_edges_verticaly(self):
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
            self.head[0] += 1
        elif self.head[1] >= height:
            self.head[1] = 0
            self.head[0] += 1

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()


    def move_through_edges_horizontaly(self):
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
            self.head[0] = 0
            # Move to next vertical line (increment the column)
            self.head[1] += 1
            self.direction[0] = 1
        elif self.head[0] >= width:
            self.head[0] = width - 1
            # Move to next vertical line (increment the column)
            self.head[1] += 1
            self.direction[0] = -1

        if self.head[1] < 0:
            self.head[1] = height - 1
        elif self.head[1] >= height:
            self.head[1] = 0

        # Move body pixels
        self.body.insert(0, next_pos)
        self.body.pop()


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


snake = SnakePixels(width // 2, height // 2)

try:
    while True:
        unicorn.clear()
        # Detect direction of movement and move accordingly
        if snake.direction == [1,0]:
            snake.move_through_edges_horizontaly()
        elif snake.direction == [0,1]:
            snake.move_through_edges_verticaly()
        else:
            snake.move_through_edges()
        unicorn.set_pixel(snake.head[0], snake.head[1], *snake.head_colour)
        for pixel in snake.body:
            unicorn.set_pixel(pixel[0], pixel[1], *snake.body_colour)
        unicorn.show()
        time.sleep(0.5)
except KeyboardInterrupt:
    unicorn.clear()
    unicorn.show()
