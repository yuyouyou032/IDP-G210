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
pin_sensor1 = 12
pin_sensor2 = 13

while True:
    wheels_forward(30, 5)
    dev_sensors_readings = sensor12(12,13)
#     pin 15,16
    print(dev_sensors_readings)
    # 
    if dev_sensors_readings[0] == 0:
        CW(30, 3)
    if dev_sensors_readings[1] == 0:
        CCW(30, 3)
    
    turn_sensor_readings = sensor12(14, 15)

# Uncomment the test to run
# test_led()
# test_led_pwm()
# test_input_poll()
# wheels_forward()
# wheels_backward( )
# CW()
# CCW()
# turn_off()
# test_tcs3472()
# test_actuator1()
# test_vl53l0x()
# test_mfrc522()
# test_TMF8x01_get_distance()
# test_STU_22L_IO_Mode()
# test_STU_22L_UART()
# test_tiny_code_reader()

print("main.py Done!")
