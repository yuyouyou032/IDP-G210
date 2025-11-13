from machine import Pin , PWM
from utime import sleep


ina1 = Pin(4,Pin.OUT)
ina2 = Pin(7, Pin.OUT)

pwma = PWM(Pin(5))
pwmb = PWM(Pin(6))


pwma.freq(1000)
pwmb.freq(1000)

def forward(duty):
    ina1.value(1)
    ina2.value(0)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
    pwmb.duty_u16(duty_16)
    
def backward(duty):
    ina1.value(1)
    ina2.value(1)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
    pwmb.duty_u16(duty_16)


def RotateCW(duty):
    ina1.value(1)
    ina2.value(0)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
    pwmb.duty_u16(duty_16)


def RotateCCW(duty):
    ina1.value(0)
    ina2.value(1)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
    pwmb.duty_u16(duty_16)
    
def StopMotor():
    ina1.value(0)
    ina2.value(0)
    pwma.duty_u16(0)
    pwmb.duty_u16(0)
    

while True:
#     duty_cycle=float(input("Enter pwm duty cycle"))
    duty_cycle=float(30)
    print (duty_cycle)
    print('forward')
    forward(duty_cycle)
    
    sleep(5)
#     backward(duty_cycle)
#     sleep(5)
    print('CW')
    RotateCW(duty_cycle)
    sleep(5)
    print('CCW')
    RotateCCW(duty_cycle)
    sleep(5)
    StopMotor()