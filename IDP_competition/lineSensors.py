from machine import Pin
from utime import sleep
from motors import wheels_forward, CW, CCW

def sensor12(sensor1_pin=8, sensor2_pin=9):
#     middle sensors 
    sensor1 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor2 = Pin(sensor2_pin, Pin.IN, Pin.PULL_DOWN)
#     print(sensor1.value, sensor2.value)
    return [sensor1.value(), sensor2.value()]

def sensor1234(sensor1_pin=8, sensor2_pin=9, sensor3_pin=12, sensor4_pin=13):  # pin 11, 12, 16, 17
    sensor1 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor2 = Pin(sensor2_pin, Pin.IN, Pin.PULL_DOWN)
    sensor3 = Pin(sensor3_pin, Pin.IN, Pin.PULL_DOWN)
    sensor4 = Pin(sensor4_pin, Pin.IN, Pin.PULL_DOWN)
#     print(sensor1.value, sensor2.value, sensor3.value, sensor4.value)
    return [sensor1.value(), sensor2.value(), sensor3.value(), sensor4.value()]

# Persistent memory across calls
last_readings = [1, 1]     # assume starting on line

def lineFollowStep(pin_sensor1=8, pin_sensor2=9):
    global last_readings
    dev = sensor12(pin_sensor1, pin_sensor2)

    # --- Normal line follow ---
    if dev[0] == 0 and dev[1] == 1:
        CCW(30, 0.05)

    elif dev[1] == 0 and dev[0] == 1:
        CW(30, 0.05)

    elif dev == [1,1]:
        wheels_forward(60, 0.05)

    # --- Lost line case ---
    elif dev == [0,0]:

        # last left sensor saw line
        if last_readings[0] == 1:
            CW(40, 0.05)          # turn right to recover line

        # last right sensor saw line
        elif last_readings[1] == 1:
            CCW(40, 0.05)         # turn left to recover line

        # completely lost: default search
        else:
            CW(40, 0.05)

    # Save reading for next step
    last_readings = dev


# def lineFollow(pin_sensor1=2, pin_sensor2=3, forward_speed=50):
#     print("Line follow started…")
#     last_readings = [1, 1]
#     while True:
#         dev_sensors_readings = sensor12(pin_sensor1, pin_sensor2) #     
#         # dev_sensors_readings[0] = right sensor
#         # dev_sensors_readings[1] = left sensor
#         # print(dev_sensors_readings)
#         if dev_sensors_readings[0] == 0 and dev_sensors_readings[1] == 1:
#             # veering right → turn CCW
#             CCW(30, 0.2)
#             last_readings = dev_sensors_readings
#             print("CCW")
#         if dev_sensors_readings[1] == 0 and dev_sensors_readings[0] == 1:
#             # veering left → turn CW
#             CW(30, 0.2)
#             last_readings = dev_sensors_readings
#             print("CW")
#         if dev_sensors_readings[1] == 1 and dev_sensors_readings[0] == 1:
#             wheels_forward(60, 0.1)
#             print("forward")
#     
#         while dev_sensors_readings[0]== 0 and dev_sensors_readings[1]==0:
#             if last_readings[0] == 1:
# #             print("finding rounte - cw")
#                 CW(40,0.1)
#             if last_readings[1] == 1:
# #             print("finding rounte - ccw")
#                 CCW(40,0.1)
#             dev_sensors_readings = sensor12(pin_sensor1, pin_sensor2)
 