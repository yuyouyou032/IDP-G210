from utime import sleep
from machine import Pin, SoftI2C, I2C, ADC
from libs.DFRobot_TMF8x01.DFRobot_TMF8x01 import DFRobot_TMF8801, DFRobot_TMF8701

adc = ADC(26)   # GP26 / ADC0, pin31
def getDistFromUltrasonic():
    raw = adc.read_u16()
    distance_cm = (raw / 65535) * 500
    return round(distance_cm, 1)
 
class Distance:
    def __init__(self):
        # 0-90mm 0/..
        self.i2c_bus = I2C(id=0, sda=Pin(20), scl=Pin(21), freq=100000) # I2C1 greendata GP20pin26 GP21pin27
        # print(self.i2c_bus.scan())
        self.tof = DFRobot_TMF8701(i2c_bus=self.i2c_bus)
        while(self.tof.begin() != 0):
            print("   Initialisation failed")
            sleep(0.5)
        print("   Initialisation done.")
        self.tof.start_measurement(calib_m = self.tof.eMODE_NO_CALIB, mode = self.tof.eCOMBINE) #mode = self.tof.eCOMBINE)

    def getDistFromTMF8x01(self): 
        if self.tof.is_data_ready():
            print(f"Distance = {self.tof.get_distance_mm()} mm")
            return self.tof.get_distance_mm()
        else:
            print("Not ready")

  