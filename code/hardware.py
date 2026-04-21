#library for run sequences for buzzer, servo and neopixel

from machine import Pin, PWM
from neopixel import NeoPixel
import time
from config import *


class Buzzer:
    def __init__(self):
        #had to remove a buzzer since the esp32 couldnt handle all the PWM counters of the other components as well
        self.pwm = PWM(Pin(PIN_BUZZER_1), freq=1000, duty=0)
    
    def _beep(self, freq, ms):
        self.pwm.freq(freq)
        self.pwm.duty(512)
        time.sleep_ms(ms)
        self.pwm.duty(0)
    
    def _pause(self, ms):
        time.sleep_ms(ms)
    

    def druid_chosen(self):
        self._beep(440, 80)
        self._pause(40)
        self._beep(550, 100)
    
    def tank_chosen(self):
        self._beep(150, 150)
        self._pause(30)
        self._beep(120, 200)
    
    def wraith_chosen(self):
        self._beep(600, 50)
        self._pause(30)
        self._beep(590, 150)
    
    def oracle_chosen(self):
        self._beep(660, 100)
        self._pause(50)
        self._beep(880, 150)
    
    def giver_chosen(self):
        self._beep(500, 30)
    
    def target_chosen(self):
        self._beep(600, 30)
        self._pause(20)
        self._beep(700, 50)
    
    def split_sound(self):
        self._beep(450, 40)
        self._pause(20)
        self._beep(500, 40)
    
    def ai_move(self):
        self._beep(350, 60)
    
    def kill_sound(self):
        self._beep(300, 100)
        self._pause(30)
        self._beep(200, 200)
    
    def revive_sound(self):
        self._beep(300, 80)
        self._beep(400, 80)
        self._beep(600, 150)
    
    def win_sound(self):
        self._beep(523, 100)
        self._pause(30)
        self._beep(659, 100)
        self._pause(30)
        self._beep(784, 300)
    
    def lose_sound(self):
        self._beep(400, 150)
        self._pause(50)
        self._beep(300, 150)
        self._pause(50)
        self._beep(200, 300)




class NeoAnimation:
    #colors based on hand value:
    #Player: Blue(1-3),Orange (4), Red (5)
    #AI:     Yellow(1-3), Orange (4), Red(5)
    
    BLUE   = (0, 0, BRIGHTNESS)
    YELLOW = (BRIGHTNESS, BRIGHTNESS, 0)
    ORANGE = (BRIGHTNESS, BRIGHTNESS//2, 0)
    RED    = (BRIGHTNESS, 0, 0)
    GREEN  = (0, BRIGHTNESS, 0)
    PURPLE = (BRIGHTNESS, 0, BRIGHTNESS)
    OFF    = (0, 0, 0)
    
    def __init__(self):

        self.strips = [
            NeoPixel(Pin(PIN_NEO_PLAYER_LEFT), PIXELS_PER_STRIP),
            NeoPixel(Pin(PIN_NEO_PLAYER_RIGHT), PIXELS_PER_STRIP),
            NeoPixel(Pin(PIN_NEO_AI_LEFT), PIXELS_PER_STRIP),
            NeoPixel(Pin(PIN_NEO_AI_RIGHT), PIXELS_PER_STRIP),
        ]
        self.clear_all()
    
    def clear_all(self):

        for strip in self.strips:
            strip.fill(self.OFF)
            strip.write()
    
    def _get_color(self, value, is_player):

        if value >= 5:
            return self.RED
        elif value == 4:
            return self.ORANGE
        else:
            return self.BLUE if is_player else self.YELLOW
    
    def _show_value(self, strip_idx, value, color):

        strip = self.strips[strip_idx]
        for i in range(PIXELS_PER_STRIP):
            strip[i] = color if i < value else self.OFF
        strip.write()
    
    def update_hands(self, player, ai):
        #refresh all 4 strips based on current hand states
        for i, hand in enumerate(player.hands):
            if hand.alive:
                color = self._get_color(hand.value, True)
                self._show_value(i, hand.value, color)
            else:
                self.strips[i].fill(self.OFF)
                self.strips[i].write()
        
        for i, hand in enumerate(ai.hands):
            if hand.alive:
                color = self._get_color(hand.value, False)
                self._show_value(i + 2, hand.value, color)
            else:
                self.strips[i + 2].fill(self.OFF)
                self.strips[i + 2].write()
    
    def blink_hand(self, strip_idx, times=3):
        #blink a strip on/off (for selection feedback)
        strip = self.strips[strip_idx]
        original = [strip[i] for i in range(PIXELS_PER_STRIP)]
        
        for _ in range(times):
            strip.fill(self.OFF)
            strip.write()
            time.sleep_ms(100)
            for i in range(PIXELS_PER_STRIP):
                strip[i] = original[i]
            strip.write()
            time.sleep_ms(100)
    

    def druid_anim(self):
        for s in self.strips:
            s.fill(self.GREEN)
            s.write()
        time.sleep_ms(200)
        self.clear_all()
    
    def tank_anim(self):
        for s in self.strips:
            s.fill(self.YELLOW)
            s.write()
        time.sleep_ms(200)
        self.clear_all()
    
    def wraith_anim(self):
        for _ in range(3):
            for s in self.strips:
                s.fill(self.PURPLE)
                s.write()
            time.sleep_ms(100)
            self.clear_all()
            time.sleep_ms(100)
    
    def oracle_anim(self):
        for s in self.strips:
            s.fill(self.BLUE)
            s.write()
        time.sleep_ms(200)
        self.clear_all()
    

    def kill_anim(self, strip_idx):
        #flash red when hand dies
        strip = self.strips[strip_idx]
        for _ in range(3):
            strip.fill(self.RED)
            strip.write()
            time.sleep_ms(100)
            strip.fill(self.OFF)
            strip.write()
            time.sleep_ms(100)
    
    def revive_anim(self, strip_idx):
        #purple fade in for revive
        strip = self.strips[strip_idx]
        for b in range(0, BRIGHTNESS, 10):
            strip.fill((b, 0, b))
            strip.write()
            time.sleep_ms(30)
        self._show_value(strip_idx, 1, self.YELLOW)
    
    def win_anim(self):
        #green flash for victory
        for _ in range(3):
            for s in self.strips:
                s.fill(self.GREEN)
                s.write()
            time.sleep_ms(200)
            self.clear_all()
            time.sleep_ms(200)
    
    def lose_anim(self):
        #red fade out for defeat
        for b in range(BRIGHTNESS, -1, -5):
            for s in self.strips:
                s.fill((b, 0, 0))
                s.write()
            time.sleep_ms(30)
        self.clear_all()



class GameServo:
    def __init__(self):
        self.pwm = PWM(Pin(PIN_SERVO), freq=50, duty=0)
        self._write(0)
    
    def _write(self, degrees):
        #convert degrees to PWM duty cycle
        #adding servo library as well was making the esp32 have too many
        #libraries and was causing problems loading HTML- decided to use this method
        us = 600 + (2400 - 600) * degrees // 180
        duty = us * 1024 * 50 // 1000000
        self.pwm.duty(duty)
    
    def set_character(self, name):
        #move servo to angle for chosen character
        angles = {
            'druid':  SERVO_ANGLE_DRUID,
            'tank':   SERVO_ANGLE_TANK,
            'wraith': SERVO_ANGLE_WRAITH,
            'oracle': SERVO_ANGLE_ORACLE,
        }
        self._write(angles.get(name, 0))



class Buttons:
    #button IDs
    PLAYER_LEFT  = 0
    PLAYER_RIGHT = 1
    AI_LEFT      = 2
    AI_RIGHT     = 3
    
    def __init__(self):
        #create pin objects with internal pull-up resistors
        self.pins = [
            Pin(PIN_PLAYER_LEFT, Pin.IN, Pin.PULL_UP),
            Pin(PIN_PLAYER_RIGHT, Pin.IN, Pin.PULL_UP),
            Pin(PIN_AI_LEFT, Pin.IN, Pin.PULL_UP),
            Pin(PIN_AI_RIGHT, Pin.IN, Pin.PULL_UP),
        ]
    
    def is_pressed(self, btn_id):
        #check if a button is currently pressed (active LOW)
        return self.pins[btn_id].value() == 0
    
    def wait_for_press(self, allowed=None, timeout_ms=None):
        """
        Wait until one of the allowed buttons is pressed.
        allowed: list of button IDs, or None for any
        timeout_ms: max wait time, or None for forever
        Returns: button ID, or None if timeout
        """
        start = time.ticks_ms()
        
        #wait for all buttons to be released first
        while any(p.value() == 0 for p in self.pins):
            time.sleep_ms(10)
        
        #now wait for a press
        while True:
            for i, pin in enumerate(self.pins):
                if pin.value() == 0:  #button pressed
                    if allowed is None or i in allowed:
                        time.sleep_ms(DEBOUNCE_MS)  #simple debounce
                        return i
            

            if timeout_ms:
                if time.ticks_diff(time.ticks_ms(), start) > timeout_ms:
                    return None
            
            time.sleep_ms(10)
    
    def is_player_btn(self, btn_id):
        return btn_id in (self.PLAYER_LEFT, self.PLAYER_RIGHT)
    
    def is_ai_btn(self, btn_id):
        return btn_id in (self.AI_LEFT, self.AI_RIGHT)
    
    def to_hand(self, btn_id):
        return 0 if btn_id in (self.PLAYER_LEFT, self.AI_LEFT) else 1
