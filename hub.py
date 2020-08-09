from Laser import laser_base
from digitalio import DigitalInOut
import board
import rio_coms

xshut = laser_base.xshut
lasers = laser_base.vl53
enabled = True

xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))

laser_base.set_addresses()

print("setup over")
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        print("sending value")
        for i in range(len(lasers)):
            rio_coms.send_value(int(laser_base.distance(i)))


#it'd be cool to throw rainbow led code in here
print("ended")
laser_base.reset_addresses()