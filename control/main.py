# from test_led import test_led
# from test_led_pwm import test_led_pwm
# from test_input import test_input_poll
from test_motor import wheels_forward, wheels_backward, CW, CCW, turn_off
from test_button_LED import sensor12
# from test_linear_actuator import test_actuator1
from test_tcs3472 import test_tcs3472
# from test_vl53l0x import test_vl53l0x
# from test_mfrc522 import test_mfrc522
# from test_TMF8x01_get_distance import test_TMF8x01_get_distance
# from test_STU_22L_IO_Mode import test_STU_22L_IO_Mode
# from test_STU_22L_UART import test_STU_22L_UART
# from test_tiny_code_reader import test_tiny_code_reader

print("Welcome to main.py!")
pin_sensor1 = 12  # middle-right
pin_sensor2 = 13
# New additional sensors for turning left/right
pin_sensor3 = 7      # right-most
pin_sensor4 = 8
#
last_readings=sensor12(pin_sensor1, pin_sensor2)
dev_sensors_readings = [1,1]
while True:
    dev_sensors_readings = sensor12(pin_sensor1, pin_sensor2)
    print("2 front sensors:", dev_sensors_readings)

    MR, ML, FR, FL = sensor1234(pin_sensor1, pin_sensor2, pin_sensor3, pin_sensor4)
    # FL=far-left, ML=mid-left, MR=mid-right, FR=far-right
    print("4 sensors:", [FL, ML, MR, FR])

    if FL == 1:
        print("LEFT junction detected -> CCW turn")
        CCW(40, 0.25)
        continue

    if FR == 0:
        print("RIGHT junction detected -> CW turn")
        CW(40, 0.25)
        continue

    if dev_sensors_readings[0] == 0 and dev_sensors_readings[1] == 1:
        CCW(30, 0.2)
        last_readings = dev_sensors_readings
        print("CCW")

    if dev_sensors_readings[1] == 0 and dev_sensors_readings[0] == 1:
        CW(30, 0.2)
        last_readings = dev_sensors_readings
        print("CW")

    if dev_sensors_readings[1] == 1 and dev_sensors_readings[0] == 1:
        wheels_forward(30, 0.1)
        print("forward")

    counter = 0
    while dev_sensors_readings[0] == 0 and dev_sensors_readings[1] == 0:
        print(counter)
        counter += 1
        if last_readings[0] == 1:
            print("Left off - cw")
            CW(40, 0.1)
        if last_readings[1] == 1:
            print("Right off - ccw")
            CCW(40, 0.1)
        dev_sensors_readings = sensor12(pin_sensor1, pin_sensor2)
        print(dev_sensors_readings)
            
    
#     turn_sensor_readings = sensor12(14, 15)

# Uncomment the test to run
# test_led()
# test_led_pwm()
# test_input_poll()


# wheels_forward()
# wheels_backward( )
# CW()
# CCW()
turn_off()


# test_tcs3472()
# test_actuator1()
# test_vl53l0x()
# test_mfrc522()
# test_TMF8x01_get_distance()
# test_STU_22L_IO_Mode()
# test_STU_22L_UART()
# test_tiny_code_reader()

print("main.py Done!")



