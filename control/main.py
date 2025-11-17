# from test_led import test_led
# from test_led_pwm import test_led_pwm
# from test_input import test_input_poll
from test_motor import wheels_forward, wheels_backward, CW, CCW, turn_off
from test_button_LED import sensor12, sensor34
# from test_linear_actuator import test_actuator1
from test_tcs3472 import test_tcs3472
# from test_vl53l0x import test_vl53l0x
# from test_mfrc522 import test_mfrc522
# from test_TMF8x01_get_distance import test_TMF8x01_get_distance
# from test_STU_22L_IO_Mode import test_STU_22L_IO_Mode
# from test_STU_22L_UART import test_STU_22L_UART
# from test_tiny_code_reader import test_tiny_code_reader

print("Welcome to main.py!")
pin_sensor1 = 12 #16
pin_sensor2 = 13 #17
pin_sensor3 = 2 # 4
pin_sensor4 = 15 # 20
#
last_readings=[1,1]
dev_sensors_readings = [1,1]
counters_dict = {'1111':0, '0111':0, '1110':0}



# assuming bot starts in the box
wheels_forward(40, 5)


while True:
    dev_sensors_readings = sensor12(12,13) #     pin 16, 17
    turn_sensors_readings = sensor34(pin_sensor3, pin_sensor4)
    
#     print(dev_sensors_readings)
    if dev_sensors_readings[0] == 0 and dev_sensors_readings[1] == 1:
        CCW(30, 0.2)
        last_readings=dev_sensors_readings
#         print("CW")
    if dev_sensors_readings[1] == 0 and dev_sensors_readings[0] == 1:
        CW(30, 0.2)
        last_readings=dev_sensors_readings
#         print("CCW")
    
    if dev_sensors_readings[1] == 1 and dev_sensors_readings[0] == 1:
        wheels_forward(30, 0.1)
#         print("forward")
    

        
    while dev_sensors_readings[0]== 0 and dev_sensors_readings[1]==0:
        if last_readings[0]==1:
            print("finding rounte - cw")
            CW(40,0.1)
        if last_readings[1]==1:
            print("finding rounte - ccw")
            CCW(40,0.1)
        dev_sensors_readings = sensor12(12,13)
        print(dev_sensors_readings)
        
    
    turn_sensors_readings = sensor34(pin_sensor3, pin_sensor4)
    
    
    
    if 1 in turn_sensors_readings: # for testing. change later.
        print(counters_dict)
        print()
        if turn_sensors_readings[1] == 1 and turn_sensors_readings[0] == 1:
            counters_dict['1111'] += 1
            while turn_sensors_readings[1] == 1 and turn_sensors_readings[0] == 1:
                wheels_forward(40, 0.1)
                turn_sensors_readings = sensor34(pin_sensor3, pin_sensor4)
            if counters_dict['1111'] == 1:
                print("turning left")
                wheels_forward(40, 1)
                CCW(40, 2)
            if counters_dict['1111'] == 2:
                print("turning right")
                wheels_forward(40, 1)
                CW(40, 2)
            print("1111", counters_dict)
        
        
        
#         0111
        if turn_sensors_readings[0] == 1 and turn_sensors_readings[1] == 0: # RHS detects line. turn right.
            counters_dict['0111'] += 1
            while turn_sensors_readings[0] == 1 and turn_sensors_readings[1] == 0:
                wheels_forward(40, 0.05)
                turn_sensors_readings = sensor34(pin_sensor3, pin_sensor4)
            if counters_dict['0111'] in [7, 9, 16]:
                print("turning right")
#                 wheels_forward(40, 0.5)
                CW(40, 1)
            print("0111", counters_dict)
            
            
#           1110  
        if turn_sensors_readings[0] == 0 and turn_sensors_readings[1] == 1:
            counters_dict['1110'] += 1
            while turn_sensors_readings[0] == 0 and turn_sensors_readings[1] == 1:
                wheels_forward(40, 0.05)
                turn_sensors_readings = sensor34(pin_sensor3, pin_sensor4)
#             print("turning left")
#             wheels_forward(40, 0.5)
#             CCW(40, 1)3
            print("1110", counters_dict)
            
        else:
            pass
    
            
    
    
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



