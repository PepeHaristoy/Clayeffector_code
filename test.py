from lib.end_effector import end_effector
from machine import Pin
import time
# we define the values to use in the code


a=(Pin(18, Pin.IN, Pin.PULL_UP))
b=(Pin(19, Pin.IN, Pin.PULL_UP))
c=(Pin(20, Pin.IN, Pin.PULL_UP))
d=(Pin(21, Pin.IN, Pin.PULL_UP))

enable=(Pin(22, Pin.IN, Pin.PULL_UP))
action_ended=(Pin(26, Pin.OUT, value=0))


while True:
    print("loop enabled"+"a.value()", a.value(), "b.value()", b.value(), "c.value()", c.value(), "d.value()", d.value(),"enable.value()", enable.value())
    time.sleep(1)