#!/usr/bin/env python

import colorsys
import math
import time
import signal

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)


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

def main(i):
    offset = 30
    for y in range(4):
            for x in range(8):
                    r = 0#x * 32
                    g = 0#y * 32
                    xy = x + y / 4
                    r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                    g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                    b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                    r = max(0, min(255, r + offset))
                    g = max(0, min(255, g + offset))
                    b = max(0, min(255, b + offset))
                    unicorn.set_pixel(x,y,int(r),int(g),int(b))
    unicorn.show()
    time.sleep(0.0666666)

if __name__ == '__main__':
 
    print("Reticulating splines")
    time.sleep(.5)
    print("Enabled unicorn poop module!")
    time.sleep(.5)
    print("Pooping rainbows...")

 
    i = 0.0
    
    with GracefulInterruptHandler() as h1:
        while True:
            i = i + 0.3
            main(i)
            if h1.interrupted:
                print("End of the program. I was killed gracefully :)")
                unicorn.clear()
                break
 
