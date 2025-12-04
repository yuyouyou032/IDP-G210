from machine import Pin

button_pin = 22   # GP22 / pin29
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)

def isButtonPressed():
    return button.value()   # 1 = pressed, 0 = not pressed
