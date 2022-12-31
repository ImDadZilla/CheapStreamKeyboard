# CheapStreamKeyboard
A macro keyboard using a Raspberry Pi Pico board.

    Cheap Stream Keybaord - Macro Keyboard
    Author: DadZilla
    Version: 0.1

## How It Works:
The keyboard works by emulating extended function keys F13 - F20.  By themselves the keys do nothing until bound within an application.  For example, if you wanted to use the keys to control functions while on a Zoom call, you can set Keyboard Shortcuts in Zoom.
![Zoom Keyboard Shortcuts Screenshot](README_ASSETS/ZoomKeyboardShortcuts-ScreenShot-1.png)

## Hardware:
1. Raspberry Pi Pico board.
2. desired number of switches/buttons.  i used cherry mx switches.

## Library Requirements:
1. adafruit circuitpython (NOT INCLUDED)
2. adafruit_hid (included)
3. adafruit_debouncer (included)
4. adafruit_ticks (included)
5. dadzilla_button (included)

## Setup:
1. configure the pins used on the Raspberry Pi Pico in the array  labeled "pins"  This should be
	setup using the board class which can use the pin labels.  If you have a switch on GP0, that would
	be setup as "board.GP0".  Continue to list all pins comma seperated between the [].
	More info here: https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules
2. configure the keycodes that each button should represent on a keyboard when pressed.  this uses the
	adafruit_hid.keycode.Keycode class. You should setup the same number of pins in the last step as you
	setup in this step.  Make sure that the keycode you want to correspond to the button on the pin defined
	above are in the same position in the array. you can find all the keycodes in the documentation here:
	https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
