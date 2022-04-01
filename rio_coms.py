#v Imports/variables v#
import serial
#usb is dev/serial1
rio = serial.Serial('/dev/serial0', 9600, timeout = 0, write_timeout = 0)

#checks if the robot has been disabled
def disabled():
    standin = rio.read().decode('utf-8')
    if standin == 'D':
        return True
    else:
        return False

#sends values to rio and prints them, add any new sensors to this
def send_values(lasers):
    laser_strings = [str(int) for int in lasers]
    values = ","

    if rio.isOpen():
        pass
    else:
        rio.open()

    string_to_write = values.join(laser_strings) + "\n"
    rio.write(string_to_write.encode('utf-8'))

def read():
    rioOut = rio.read()
    # rioString = rioOut.decode('utf-8')
    print(rioOut)
