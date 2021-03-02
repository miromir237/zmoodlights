#!/usr/bin/env python

import signal
import time
from random import randint

import unicornhat as unicorn


class GracefulInterruptHandler(object):

    def __init__(self, sig=signal.SIGTERM):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True

        return True

def main(clock):
   for person in blue_pilled_population:
            y = person[1]
            for rgb in wrd_rgb:
                    if (y <= 7) and (y >= 0):
                            unicorn.set_pixel(person[0], y, rgb[0], rgb[1], rgb[2])
                    y += 1
            person[1] -= 1
   unicorn.show()
   time.sleep(0.1)
   unicorn.clear()
   #clock += 1
   if clock % 5 == 0:
           blue_pilled_population.append([randint(0,7), 7])
   if clock % 7 == 0:
           blue_pilled_population.append([randint(0,7), 7])
   while len(blue_pilled_population) > 100:
           blue_pilled_population.pop(0)

if __name__ == '__main__':
    # Global variables
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(0.8)

    wrd_rgb = [[154, 173, 154], [0, 255, 0], [0, 200, 0], [0, 162, 0], [0, 145, 0], [0, 96, 0], [0, 74, 0], [0, 0, 0,]]

    clock = 0

    blue_pilled_population = [[randint(0,7), 7]]
 
    print("""Matrix

    Follow the white rabbit...
    """)

 
    with GracefulInterruptHandler() as h1:
        while True:
            main(clock)
            clock += 1
            if h1.interrupted:
                print("End of the program. I was killed gracefully :)")
                unicorn.clear()
                break
    



 
