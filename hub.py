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

laser_base.reset_addresses()
laser_base.set_addresses()
#leds.setup(board.D0, 30)

print("enabled")
while enabled:
    print(len(lasers))
        #leds.normal_Rotation(4)
    for i in range(len(lasers)):
        print("for")
        print(int(laser_base.distance(i)), i)
            #rio_coms.send_value(int(laser_base.distance(i)), i)


#leds.rainbow_cycle(0.01)
print("Queue rainbow leds")
laser_base.reset_addresses()