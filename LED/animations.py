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
    if rotateCheck is length:
        rotateCheck = 0
    for i in range(qty):
        if i % length == 0:
            blue = not blue
        if blue:
            leds[i - rotateCheck] = colorA
        else:
            leds[i - rotateCheck] = colorB
    
    rotateCheck += 1



def rotateDep(colorA, colorB, length):
    global firstRun
    global primary
    global cycle
    if firstRun:
        for i in range(qty):
            if primary:
                for j in range(length):
                    leds[i] = colorA
            else:
                for j in range(length):
                    leds[i] = colorB
            primary = not primary
        firstRun = False
    
    for i in range(10):
        if (i + cycle) % length == 0:
            print("lets see {}".format(i))
            if primary:
                leds[i] = colorA
            else:
                leds[i] = colorB
            primary = not primary
    if cycle == length:
        cycle = 0
    cycle += 1
    leds.show()
     