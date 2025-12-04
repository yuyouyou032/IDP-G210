from machine import Pin, SoftI2C, I2C
from libs.tcs3472_micropython.tcs3472 import tcs3472
# from color import tcs34725
from utime import sleep

button = Pin(10, Pin.OUT)  # GP10 / pin14 to control the LED on the color sensor
# Initialize I2C (Make sure pins 8 = SDA, 9 = SCL are correct for your board!)
# i2c_bus = I2C(id=0, sda=Pin(8), scl=Pin(9), freq = 100000) # GP8 pin11; GP9 pin12
# tcs = tcs3472(i2c_bus)
i2c_bus = I2C(id=1, sda=Pin(2), scl=Pin(3), freq = 100000) # GP8 pin4; GP9 pin5
print(i2c_bus.scan())
tcs = tcs3472(i2c_bus)
def colorDetector():
    button.value(1) # Turn on the LED to illuminate the color sensor
    while True:
        r, g, b = tcs.rgb()
        print("RGB:", (r, g, b))
        total = r + g + b
        if total == 0:
            continue
        rn, gn, bn = r/total, g/total, b/total

        # ========= RED: Use dominance, not absolute ranges =========
        # Red must have R clearly highest
        if rn > 0.25 and g < 83 and r > 75:
            button.value(0)  # Turn off the LED
            print("Detected: Red")
            return "Red"

        # ========= YELLOW: lowest B values in all samples =========
        if b <= 67:
            button.value(0)  # Turn off the LED
            print("Detected: Yellow")
            return "Yellow"

        # ========= GREEN: B = 70–72 AND G highest =========
        if 70 <= b <= 72 and g > r and g > b:
            button.value(0)  # Turn off the LED
            print("Detected: Green")
            return "Green"

        # ========= BLUE: high B values (≥ 73) =========
        if b >= 73 and g < 85:
            button.value(0)  # Turn off the LED
            print("Detected: Blue")
            return "Blue"

        sleep(0.2)