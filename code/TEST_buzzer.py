from machine import Pin
from time import sleep

buzz = Pin(18, Pin.OUT)

buzz.on()
sleep(1)
buzz.off()