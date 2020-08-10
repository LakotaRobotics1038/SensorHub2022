import board
import neopixel
import time
import sys

cycle = 0
qty = 10
firstRun = True
primary = True
pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False)

def rotate(colorA, colorB, length):
    global firstRun
    global primary
    global cycle
    if firstRun:
        for i in range(qty):
            if primary:
                for j in range(length):
                    pixels[i] = colorA
            else:
                for j in range(length):
                    pixels[i] = colorB
            primary = not primary
        firstRun = False
    
    for i in range(10):
        if i + cycle % 4 == 0:
            if primary:
                print(i)
                print(cycle)
                pixels[i] = colorA
            else:
                print(i)
                print(cycle)
                pixels[i] = colorB
            primary = not primary
    
    cycle += 1
    pixels.show()
     