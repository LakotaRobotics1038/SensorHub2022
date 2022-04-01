# v Imports/variables v#
from digitalio import DigitalInOut
import board
import time
from Sensors import laser_base
from Sensors import digitalSensors
import rio_coms
import animations

lightCount = animations.qty
xshut = laser_base.xshut
lasers = laser_base.vl53
dio = digitalSensors.digitalList
enabled = True


# v Between these are the only things you should change v#

# Possible GPIO Pins: 17, 27, 22, 5, 6, 26
# Add list of Laser XSHUT pins
listedShutoffs = [
  DigitalInOut(board.D11),
  DigitalInOut(board.D17)
]

xshut.extend(listedShutoffs)                    #Keep commented unless using lasers

# LED Signal Pin is set in animations, D21 to start
lightCount = 104  # Number of leds
mode = "Fade"  # "Rotate", "Fade", "Tower", or "Message" (or none for rainbow testing) right now
message = "Something mean about Sean"  # If running message code, message to convert
cycleDelay = 0.01 #0.01 for fade, 0.1 for rotate or message
hex1 = (200, 0, 200)
hex2 = (0, 0, 200)

# ^ Between these are the only things you should change ^#


# code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()
animations.setup(lightCount, mode, hex1, hex2, message)

while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        # input()                #only use when debugging, comment out otherwise

        # Runs the chosen LED program
        animations.run(mode, hex1, hex2)
        laser_values = list(map((lambda index: int(laser_base.distance(index))), range(len(lasers))))
        rio_coms.send_values(laser_values)
         # you may need a delay for the lights depending on the number of sensors, comment it out if you don't
        time.sleep(cycleDelay)


# This runs after the robot is disabled
laser_base.reset_addresses()
animations.rainbow_cycle(cycleDelay)
