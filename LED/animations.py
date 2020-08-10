import board
import neopixel
import time
import sys
qty = 10
pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False)

def dim(color):
    for j in range(0, max(color)+5, 5):
        r = color[0]-j
        if r <= 0:
            r = 0
        g = color[1]-j
        if g <= 0:
            g = 0
        b =  color[2]-j
        if b <= 0:
            b = 0
        pixels.fill((r, g, b))
        pixels.show()

def brighten(color):
    for j in range(0, max(color)-5, 5):
        r = j
        if r >= color[0]:
            r = color[0]
        g = j
        if g >= color[1]:
            g = color[1]
        b =  j
        if b >= color[2]:
            b = color[2]
        pixels.fill((r, g, b))
        pixels.show()

def spiral(color):
    for i in range(qty):
         pixels[i] = color
         pixels.show()
    dim(color)    

def spiralback(color):
    for i in reversed(range(qty)):
         pixels[i] = color
         pixels.show()
    dim(color)  

def blink(color):
    brighten(color)
    time.sleep(1)
    dim(color)

def tunnel(color):
    for i in range(0, qty-50, 50):
        for j in range(0, max(color), 5):
            r = j
            if r >= color[0]:
                r = color[0]
            g = j
            if g >= color[1]:
                g = color[1]
            b =  j
            if b >= color[2]:
                b = color[2]
            for x in range(50):
                pixels[i+x] = (r, g, b)
            pixels.show()
    dim(color)

    for i in range(0, 300, 25):
       for y in range(51):
          for x in range(i, i+25):
             pixels[x] = (0, y*4, 0)
          pixels.show()
    for u in range(51):
       pixels.fill((0, 200-u*4, 0))
       pixels.show()