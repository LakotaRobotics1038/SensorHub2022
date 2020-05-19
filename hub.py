from Laser import laser_base
from digitalio import DigitalInOut
import board
import rio_coms
import leds

xshut = laser_base.xshut
lasers = laser_base.vl53
enabled = True

xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))

laser_base.set_addresses()
leds.setup(4, 30)

print("setup over")
while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        leds.normal_Rotation(4)
        print("sending value")
        for i in range(len(lasers)):
            rio_coms.send_value(int(laser_base.distance(i)))


leds.rainbow_cycle(0.01)
print("ended")
laser_base.reset_addresses()