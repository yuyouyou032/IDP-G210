from machine import Pin, PWM
from utime import sleep

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)       # direction pin
        self.pwm = PWM(Pin(PWMPin))            # PWM pin
        self.pwm.freq(1000)                     # PWM frequency 1 kHz
        self.pwm.duty_u16(0)                    # start stopped

    def off(self):
        self.pwm.duty_u16(0)                    # stop motor

    def Forward(self, speed=30):
        self.mDir.value(0)                      # forward direction
        self.pwm.duty_u16(int(65535 * speed / 100))  # set speed (0-100%)

    def Reverse(self, speed=30):
        self.mDir.value(1)                      # reverse direction
        self.pwm.duty_u16(int(65535 * speed / 100))  # set speed

motor_left = Motor(dirPin=4, PWMPin=5)    # MotorLeft is controlled from Motor Driv2 #1, which is on GP4/5
motor_right = Motor(dirPin=7, PWMPin=6)   # MotorRight is controlled from Motor Driv2 #2, which is on GP7/6

def wheels_forward(speed=70, t=3):
    motor_left.Forward(speed)
    motor_right.Forward(speed)
    sleep(t)

def wheels_backward(speed=70, t=3):
    motor_left.Reverse(speed)
    motor_right.Reverse(speed)
    sleep(t)

def CW(speed=70, t=3):
    motor_left.Forward(speed)
    motor_right.Reverse(speed)
    sleep(t)

def CCW(speed=70, t=3):
    motor_left.Reverse(speed)
    motor_right.Forward(speed)
    sleep(t)

def turn_off():
    motor_left.off()
    motor_right.off()

# def test_motor_left():
#     while True:
#         print("Forward")
#         motor_left.Forward()
#         sleep(1)
#         print("Reverse")
#         motor_left.Reverse()
#         sleep(1)

# def test_motor_right():
#     while True:
#         print("Forward")
#         motor_right.Forward()
#         sleep(1)
#         print("Reverse")
#         motor_right.Reverse()
#         sleep(1)