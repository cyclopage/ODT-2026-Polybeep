from machine import Pin
from time import sleep

butt = Pin(14, Pin.IN, Pin.PULL_UP)

while(1):
    if butt.value() == 0:
        print("click")
        break
