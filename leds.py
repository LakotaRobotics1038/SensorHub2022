import neopixel
import board

global blue
rotateCheck = 0

def setup(pin, count):
    global led_count
    led_count = count
    global leds
    leds = neopixel.NeoPixel(pin, count)
    leds.fill((0,0,0))


def normal_Rotation(length):
    global rotateCheck
    if rotateCheck is length:
        rotateCheck = 0
    for i in range(led_count):
        if i % length == 0:
            blue = not blue
        if blue:
            leds[i - rotateCheck] = (0, 0, 255)
        else:
            leds[i - rotateCheck] = (255, 0, 255)
    
    rotateCheck += 1

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