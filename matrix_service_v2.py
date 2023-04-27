#!/usr/bin/env python

import signal
import time
from random import randint
import logging
import unicornhat as unicorn

class TerminateProtected:
    """ Protect a piece of code from being killed by SIGINT or SIGTERM.
    It can still be killed by a force kill.

    Example:
        with TerminateProtected():
            run_func_1()
            run_func_2()

    Both functions will be executed even if a sigterm or sigkill has been received.
    """
    killed = False

    def _handler(self, signum, frame):
        logging.error("Received SIGINT or SIGTERM! Finishing this block, then exiting.")
        self.killed = True

    def __enter__(self):
        self.old_sigint = signal.signal(signal.SIGINT, self._handler)
        self.old_sigterm = signal.signal(signal.SIGTERM, self._handler)

    def __exit__(self, type, value, traceback):
        if self.killed:
            sys.exit(0)
        signal.signal(signal.SIGINT, self.old_sigint)
        signal.signal(signal.SIGTERM, self.old_sigterm)


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

 
    with TerminateProtected():
        while True:
            main(clock)
            clock += 1
            unicorn.clear()

    print("End of the program. I was killed gracefully :)")

 
