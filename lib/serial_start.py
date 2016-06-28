import time
import serial

#Start the seial communication with the microcontroller
serialFeed1 = serial.Serial('/dev/ttyACM0', 9600)
