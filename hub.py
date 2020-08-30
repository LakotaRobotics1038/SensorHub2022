#v Imports/variables v#
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


#v Between these are the only things you should change v#

#xshut.append(DigitalInOut(board.D21))
#dio['limitSwitch'] = DigitalInOut(board.D18)
lightCount = 10

#^ Between these are the only things you should change ^#


#code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()
animations.rotateSetup((100,0,255), (0,0,255), lightCount, 4)
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        animations.rotate()
        #animations.rainbow_cycle(0)
        for i in range(len(dio)):
            print("{}: {}".format(dio[i]), digitalSensors.sensorCheck(i))
        for i in range(len(lasers)):
            rio_coms.send_value(i, int(laser_base.distance(i)))
        #input()                #only use when debugging, comment out otherwise
        time.sleep(0.1)        #you may need a delay for the lights depending on the number of sensors, comment it out if you don't


#This runs after the robot is disabled
animations.rainbow_cycle(0)
laser_base.reset_addresses()