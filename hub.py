from digitalio import DigitalInOut
import board

from Laser import laser_base
import rio_coms
from LED import animations

lightCount = animations.qty
xshut = laser_base.xshut
lasers = laser_base.vl53
enabled = True


#Between these are the only things you should change#
xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))
lightCount = 10
#Between these are the only things you should change#

laser_base.set_addresses()

animations.rainbow_cycle(1)
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        animations.rotate((255,0,255), (0,0,255), 4)
        print("sending value")
        for i in range(len(lasers)):
            rio_coms.send_value(i, int(laser_base.distance(i)))


#it'd be cool to throw rainbow led code in here
animations.rainbow_cycle(1)
print("ended")
laser_base.reset_addresses()