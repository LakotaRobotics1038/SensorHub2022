import board
import neopixel
import time
import sys

cycle = 0
rotateCheck = 0
qty = 10
firstRun = True
primary = True
leds = neopixel.NeoPixel(board.D18, qty, auto_write=False)

def rotate(colorA, colorB, length):
    global rotateCheck
    global primary
    if rotateCheck is length:
        rotateCheck = 0
    for i in range(qty):
        if i % length == 0:
            primary = not primary
        if primary:
            leds[i - rotateCheck] = colorA
        else:
            leds[i - rotateCheck] = colorB
    
    rotateCheck += 1
    leds.show()

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(led_count):
            pixel_index = (i * 256 // led_count) + j
            leds[i] = wheel(pixel_index & 255)
        leds.show()
        leds.sleep(wait)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)