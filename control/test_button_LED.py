from machine import Pin
from utime import sleep



#Set the LED pin and configuration
# led_pin = 28
# led = Pin(led_pin, Pin.OUT)

def sensor12(sensor1_pin, sensor2_pin):
#     front sensors 
    sensor1 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor2 = Pin(sensor2_pin, Pin.IN, Pin.PULL_DOWN)
#     print(sensor1.value, sensor2.value)
    return sensor1.value(), sensor2.value()

#Continiously update the LED value and print said value
# while True:
#   print(sensor12(12, 13))
#   sleep(0.1)
