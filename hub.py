#from Laser import laser_base
#from digitalio import DigitalInOut

# SAMS CODE =================

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

# ^^^^^^^^^^^^^^^^^^^^^^^^^^

#import board
#import rio_coms
#import leds

# SAMS CODE ==================

app = Flask(__name__)

@app.route('/')
def main_response():
	currentTime = datetime.datetime.now()
	currentTimeString = currentTime.strftime('%Y-%m-%d %H:%M:%S')
	templateData = {
		'title' :  'SummerSensorSensation',
		'sensor1' : currentTimeString,
		'sensor2' : currentTimeString
	}
	return render_template('index.html', **templateData)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^

#xshut = laser_base.xshut
#lasers = laser_base.vl53
#enabled = True

#xshut.append(DigitalInOut(board.D21))
#xshut.append(DigitalInOut(board.D20))

#laser_base.set_addresses()
#leds.setup(board.D0, 30)

#while enabled:
    #if rio_coms.disabled():
        #enabled = False
    #else:
        #leds.normal_Rotation(4)
        #for i in range(len(lasers)):
            #rio_coms.send_value(int(laser_base.distance(i)), i)


#leds.rainbow_cycle(0.01)
#print("Que rainbow leds")
#laser_base.reset_addresses()

# SAMS CODE ===============

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

# ^^^^^^^^^^^^^^^^^^^^^^^^
