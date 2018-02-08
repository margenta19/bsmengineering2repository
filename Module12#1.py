# if sensor reads 1- turn the motor off
# if sensor reads 0- continue

# looking in python the hard way at ex 33 to figure out
#if there is enough information there to make a while loop

#script to make i the sensor must come before

i = sensor_pin
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

while i < 0:
    RPL.servoWrite(0, 1000)
    print "on correct"

while i > 0:
    RPL.servoWrite(0, 0)
    print "off correct"

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
