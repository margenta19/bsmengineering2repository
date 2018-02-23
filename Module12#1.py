# if sensor reads 1- turn the motor off
# if sensor reads 0- continue

# looking in python the hard way at ex 33 to figure out
#if there is enough information there to make a while loop

#script to make i the sensor must come before

import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 8
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()

if RPL.digitalRead(sensor_pin) == 1:
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(0, 1000)
    print "on correct"
if RPL.digitalRead(sensor_pin) == 0:
    import RoboPiLib
    import setup
    RPL.servoWrite(0, 0)
    print "off correct"
