#v Imports/variables v#
from collections import namedTuple
from digitalio import DigitalInOut
import board
from Sensors import laser_base
from Sensors import digitalSensors
import rio_coms
import animations

lightCount = animations.qty
xshut = laser_base.xshut
lasers = laser_base.vl53
dio = digitalSensors.digitalSensors
enabled = True


#v Between these are the only things you should change v#
xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))

dio['limitSwitch'] = DigitalInOut(board.D18)

lightCount = 10
#^ Between these are the only things you should change ^#


#code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        animations.rotate((125,0,255), (0,0,255), 4)
        digitalSensors.sensorCheckOne()
        for i in range(len(lasers)):
            rio_coms.send_value(i, int(laser_base.distance(i)))


#This runs after the robot is disabled
animations.rainbow_cycle(0)
laser_base.reset_addresses()