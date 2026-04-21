from machine import Pin
from servo import Servo
from time import sleep

servo = Servo(Pin(27))

servo.write_angle(0)
sleep(1)
servo.write_angle(50)