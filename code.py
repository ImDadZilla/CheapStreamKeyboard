"""
    Cheap Stream Keybaord - Macro Keyboard
    Author: DadZilla
    Version: 0.1
    
    Hardware:
        1. Raspberry Pi Pico board.
        2. desired number of switches/buttons.  i used cherry mx switches.
    
    Library Requirements:
        1. adafruit circuitpython
        2. adafruit_hid (specifically keyboard, keyboard_layout, keyboard_layout_us and keycode)
        3. adafruit_debouncer
            a. adafruit_ticks
        4. dadzilla_button - helper class for handling the button setup with debouncer and keycode objects.
    
    Setup:
        1. configure the pins used on the Raspberry Pi Pico in the array  labeled "pins"  This should be
            setup using the board class which can use the pin labels.  If you have a switch on GP0, that would
            be setup as "board.GP0".  Continue to list all pins comma seperated between the [].
            More info here: https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules
        2. configure the keycodes that each button should represent on a keyboard when pressed.  this uses the
            adafruit_hid.keycode.Keycode class. You should setup the same number of pins in the last step as you
            setup in this step.  Make sure that the keycode you want to correspond to the button on the pin defined
            above are in the same position in the array. you can find all the keycodes in the documentation here:
            https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode

"""

import time
import board
import digitalio
import usb_hid
import pwmio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer
from dadzilla_button import Button

# define the pins to keycode mappings.
# the pins should be in the same array position as the desired keycodes for that respective position
pins = [board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7]
leds = [board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP26,
        board.GP22,
        board.GP21,
        board.GP20]
keycodes = [Keycode.F13,
            Keycode.F14,
            Keycode.F15,
            Keycode.F16,
            Keycode.F17,
            Keycode.F18,
            Keycode.F19,
            Keycode.F20]

# Check if there are enough pins defined for desired keys
if len(pins) < len(keycodes):
    raise Exception("Not enough pins to cover all the keycodes")
elif len(pins) > len(keycodes):
    print("WARNING! More pins than keycodes. Continueing but only for those keycodes defined")
    numOfKeys = len(keycodes)
else:
    numOfKeys = len(pins)

# Set debounce interval (its in seconds so 0.1 = 1 milisecond. thus 0.02 is 20 milliseconds)
interval = 0.02

# buttons array will hold the instances of class Button
buttons = []

# setup button objects for all pin/keycode combinations defined and store in buttons array
for x in range(numOfKeys):
        tmp_pin = digitalio.DigitalInOut(pins[x])
        tmp_pin.direction = digitalio.Direction.INPUT
        tmp_pin.pull = digitalio.Pull.UP
        tmp_debouncer = Debouncer(tmp_pin,interval)
        tmp_led = pwmio.PWMOut(leds[x], frequency=5000, duty_cycle=10000)
        buttons.append(Button(tmp_debouncer,keycodes[x],pins[x],tmp_led))

# Used for debugging to show button press, hold and release.
# set useDebugLed True to have the onboard LED light, False to turn off
useDebugLed = True
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
def ledOn():
    if useDebugLed:
        led.value = True
def ledOff():
    if useDebugLed:
        led.value = False

dutyCycle=10000

# instantiate the keyboard object for sending keyboard keycodes when pressed or released
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# *******************
#    MAIN LOOP
# *******************
while True:
    # loop all buttons
    for button in buttons:
        # update button state from Debouncer
        button.buttonUpdate()
        # Check if a button was just pressed since the last update
        if button.buttonFell():
            print(button.getPin())
            ledOn()
            button.ledValue(65025)
            button.buttonPressKeyboard(keyboard)
        # check if button was just released since the last update
        elif button.buttonRose():
            print('Just Released')
            ledOff()
            button.ledValue(10000)
        # Check if the button value indicates its still being held down since it was pressed
        elif not button.buttonValue():
            ledOn()          
