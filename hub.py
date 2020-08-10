from digitalio import DigitalInOut
import board

from Laser import laser_base
import rio_coms
from LED import animations

lightCount = animations.qty
animations.firstRun = True
animations.primary = True 
xshut = laser_base.xshut
lasers = laser_base.vl53
enabled = True

xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))
lightCount = 10

laser_base.set_addresses()

while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        animations.rotate((255,0,255), (0,0,255), 4)
        print("sending value")
        for i in range(len(lasers)):
            rio_coms.send_value(i, int(laser_base.distance(i)))


#it'd be cool to throw rainbow led code in here
print("ended")
laser_base.reset_addresses()