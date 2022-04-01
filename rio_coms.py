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
    values = ","

    if rio.isOpen():
        pass
    else:
        rio.open()

    rio.write(values.join(lasers))

def read():
    rioOut = rio.read()
    # rioString = rioOut.decode('utf-8')
    print(rioOut)