from machine import Pin, PWM
from utime import sleep
from motors import wheels_forward, wheels_backward, stop   

class Actuator:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
           
    def set(self, dir, speed):
        self.mDir.value(dir)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

actuator1 = Actuator(dirPin=0, PWMPin=1)  # Actuator 1 controlled from Motor Driv1 #1, which is on GP0/1

def toLowestPos():
#     wheels_forward(speed=30, t=1)
    print("Extending quickly")
    actuator1.set(dir = 0, speed=100)
    sleep(5)  # nb we don't know when this has finished without another means
#     wheels_backward(speed=30, t=1)

def upToRackPos():
#     wheels_forward(speed=30, t=1)
    print("Retracing")
    actuator1.set(dir = 1, speed=100)
    sleep(1.5)  # nb we don't know when this has finished without another means
    actuator1.set(dir = 0, speed=0)
#     wheels_backward(speed=30, t=1)

def pickBox():
    wheels_forward(speed=30, t=1)
    print("Retracing")
    actuator1.set(dir = 1, speed=100)
    sleep(1.5)  # nb we don't know when this has finished without another means
    actuator1.set(dir = 0, speed=0)
    wheels_backward(speed=30, t=1)

def liftUp():
    pass

def liftDown():
    pass

def dropBox():
    wheels_forward(speed=30, t=1)
    print("Extendng")
    actuator1.set(dir = 0, speed=100)
    sleep(2)  # nb we don't know when this has finished without another means
    actuator1.set(dir = 0, speed=0)
    wheels_backward(speed=30, t=1)
    print("Retracing")
    actuator1.set(dir = 1, speed=100)
    sleep(2)  # nb we don't know when this has finished without another means
    actuator1.set(dir = 0, speed=0)
