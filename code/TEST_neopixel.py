#lets import the libraries
from machine import Pin
import time
from neopixel import NeoPixel

#define a pin on which i attach the neopixel data line
dataPin=18

#create a variable for number of pixels
pixels=5
2
#create the neopixel abstract variable
np=NeoPixel(Pin(dataPin, Pin.OUT),pixels)

#clear the strip first, so no leftover colors from previous runs
np.fill((0,0,0))
np.write()

#small brightness value, full 255 on all channels can draw a lot of current
#and is painfully bright to look at while testing
brightness=50

while(1):
    
    #Animation 1: walking single pixel in RED
    #light one led at a time, from first to last
    for i in range(pixels):
        np.fill((0,0,0))
        np[i]=(brightness,0,0)
        np.write()
        time.sleep(0.2)
    
    #Animation 2: walking single pixel in GREEN
    for i in range(pixels):
        np.fill((0,0,0))
        np[i]=(0,brightness,0)
        np.write()
        time.sleep(0.2)
    
    #Animation 3: walking single pixel in BLUE
    for i in range(pixels):
        np.fill((0,0,0))
        np[i]=(0,0,brightness)
        np.write()
        time.sleep(0.2)
    
    #Animation 4: fill the whole strip one by one in WHITE
    #this confirms every pixel in the strip is alive
    np.fill((0,0,0))
    np.write()
    for i in range(pixels):
        np[i]=(brightness,brightness,brightness)
        np.write()
        time.sleep(0.2)
    
    #hold the full white for a moment
    time.sleep(0.5)
    
    #Animation 5: fade out the whole strip from current brightness down to 0
    #this checks that colour mixing on each led works smoothly
    for b in range(brightness,-1,-2):
        np.fill((b,b,b))
        np.write()
        time.sleep(0.03)
      
    #small pause before the whole cycle repeats
    time.sleep(0.5)
# 6