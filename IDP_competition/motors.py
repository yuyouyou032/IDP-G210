from machine import Pin, PWM
from utime import sleep

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=100):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=30):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))

def test_motor3():
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5

    while True:
        print("Forward")
        motor3.Forward()
        sleep(1)
        print("Reverse")
        motor3.Reverse()
        sleep(1)

def test_motor4():
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #1, which is on GP4/5

    while True:
        print("Forward")
        motor4.Forward()
        sleep(1)
        print("Reverse")
        motor4.Reverse()
        sleep(1)
        
def wheels_forward(speed=40, t=2):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
#     print('forward')
    motor3.Forward(speed)
    motor4.Forward(speed)
    sleep(t)
    
def wheels_backward(speed=40, t=3):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
#     print('backward')
    motor3.Reverse(speed)
    motor4.Reverse(speed)
    sleep(t)
    
def CCW(speed=50, t=3):
    motor3 = Motor(dirPin=4, PWMPin=5)  
    motor4 = Motor(dirPin=7, PWMPin=6)
#     print('CW')
    motor3.Forward(speed)
    motor4.Reverse(speed)
    sleep(t)
    
def CW(speed=50, t=3):
    motor3 = Motor(dirPin=4, PWMPin=5)  
    motor4 = Motor(dirPin=7, PWMPin=6)
#     print('CCW')
    motor3.Reverse(speed)
    motor4.Forward(speed)
    sleep(t)

def right_pivot(speed=60, t=2.5):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
    motor4.Forward(speed)
    sleep(t)
    print('off')
    motor3.off()
    motor4.off()
    
def left_pivot(speed=60, t=2.5):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
    motor3.Forward(speed)
    sleep(t)
    print('off')
    motor3.off()
    motor4.off()

def half_turn_L(speed=60, t=2.5):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
    motor3.Forward(speed)
    motor4.Reverse(speed)
    sleep(t)
    print('off')
    motor3.off()
    motor4.off()

def half_turn_R(speed=60, t=2.5):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
    motor4.Forward(speed)
    motor3.Reverse(speed)
    sleep(t)
    print('off')
    motor3.off()
    motor4.off()

def stop():
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)
    motor3.off()
    motor4.off()