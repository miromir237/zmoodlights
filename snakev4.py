#!/usr/bin/env python

import time
from random import randint

import unicornhat as unicorn


print("""Snake pixels
You should see snake moving around the screen and bouncing off the edges.
If you're using a Unicorn HAT and only half the screen lights up,
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()

print(f"Width: {width}, Height: {height}")

class SnakePixels:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = [[x - i, y] for i in range(1, 3)]
        self.direction = [1,1]  # horizontal direction
        self.head_colour = [0, 0, 255]  # blue color
        self.body_colour = [0, 255, 0]  # blue color

    # This method is used to move the snake around the screen on horizontal lines and bounce it
    # off the edges. When it bounces it also moves one pixel down or up depending on the direction.
    def move_bounce_vertical(self):
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

snake = SnakePixels(width // 2, height // 2)

try:
    while True:
        unicorn.clear()
        print(f"Head: {snake.head} and direction: {snake.direction}")
        snake.move_bounce_vertical()
        unicorn.set_pixel(snake.head[0], snake.head[1], *snake.head_colour)
        for pixel in snake.body:
            unicorn.set_pixel(pixel[0], pixel[1], *snake.body_colour)
        unicorn.show()
        time.sleep(0.5)
except KeyboardInterrupt:
    unicorn.clear()
    unicorn.show()
