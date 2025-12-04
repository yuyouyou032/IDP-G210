from machine import Pin
from utime import sleep

yellow_led = Pin(21, Pin.OUT)  # GP21, pin27
power = Pin(16, Pin.OUT) # GP16, pin21

def enableYellowLED():
    yellow_led.value(1)  # Turn on the yellow LED
    power.value(1)
    
def disableYellowLED():
    yellow_led.value(0)
    power.value(0)
    # yellow_led.value(0)  # Turn off the yellow LED
 