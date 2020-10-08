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

#xshut.append(DigitalInOut(board.D21))          #copy to add lasers, change board port to the xshut pin

#dio['limitSwitch'] = DigitalInOut(board.D18)    #copy to add digital sensors, board port is signal pin, change name

lightCount = 10                                 #number of leds
animations.messageSetup("message here")         #converts your message to binary
#^ Between these are the only things you should change ^#


#code that runs during the match
digitalSensors.pinSetup()
laser_base.set_addresses()
animations.rotateSetup((100,0,255), (0,0,255), lightCount, 4)
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        #animations.rotate((125,0,255), (0,0,255), 4)       #only have one LED program active
        animations.message((125,0,255), (0,0,255))          #only have one LED program active
        print(digitalSensors.sensorCheck(0))
        for i in range(len(lasers)):
            rio_coms.send_value(i, int(laser_base.distance(i)))
        #input()                #only use when debugging, comment out otherwise
        time.sleep(0.1)        #you may need a delay for the lights depending on the number of sensors, comment it out if you don't


#This runs after the robot is disabled
animations.rainbow_cycle(0)
laser_base.reset_addresses()