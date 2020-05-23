import board
import serial


rio = serial.Serial('/dev/ttyAMA0', 115200, timeout = 0, write_timeout = 0)
#standin = rio.read()

def disabled():
    print(rio.read())
    if rio.read() is 'D':
        return True
    else:
        return False


#def disabled():
#    print((rio.read()).decode('utf-8'))
#    if rio.read() is 'D':                  #This block can be renamed and use a different byte for any command
#        return True
#    else:
#        return False


def send_value(value, laser):
    print("Value of Laser {}: {}".format(laser, value))
    rio.write([value])