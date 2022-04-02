# v Imports/variables v#
from digitalio import DigitalInOut
import board
from Sensors import laser_base
from Sensors import digitalSensors
import rio_coms

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

# ^ Between these are the only things you should change ^#


# code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()

while enabled:
    else:
        # input()                #only use when debugging, comment out otherwise

        laser_values = list(map((lambda index: int(laser_base.distance(index))), range(len(lasers))))
        rio_coms.send_values(laser_values)
