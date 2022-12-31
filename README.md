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
2. Custom Printed Circuit Board Version 1.0 (Link to easyeda)
	![Circuit Board](/README_ASSETS/EasyEDA-CheapStreamKeyboard-V1.0.png)
3. 8 Cherry MX Style switches
4. 8 surface mount LEDs (1206) along with 8 appropriatly sized surface mount resistors (0603).
5. 3D printed case.

## Library Requirements:
1. adafruit circuitpython (included)
2. adafruit_hid (included)
3. adafruit_debouncer (included)
4. adafruit_ticks (included)
5. dadzilla_button (included)

## Setup:
1. Install Adafruit Circuitpython
	- while pressing the BOOTSEL button on the Raspberry PI Pico, plug in the USB cable connected to your PC, then release the button.
		- this should open the device as a removable storage device with a name like 'CIRCUITPY'.
	- delete existing files.
	- copy the 'adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2' file to the raspberry pi pico.  
		- this will flash it and should reboot.
2. now open the 'CheapStreamKeyboardCode' folder and copy all files and paste onto the raspberry pi pico.  it should look like this (ignore the files you didn't copy as those are system generated files): ![CIRCUITPY Files](/README_ASSETS/CheapStreamKeyboard-FilesScreenshot.png)
3. Unplug the USB cable from the keybaord, then plug it in again to reboot with the new code and all the LEDs on the keyboard should be on.	
