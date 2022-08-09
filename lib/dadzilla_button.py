"""
    Button Helper Class
    
"""
import time
from adafruit_hid.keyboard import Keyboard

class Button:
    
    numberOfButtons = 0
    
    def __init__(self, debouncer, keycode):
        self.debouncer = debouncer
        self.keycode = keycode
        Button.numberOfButtons += 1
        
    def getDebouncer(self):
        return self.debouncer
        
    def getKeycode(self):
        return self.keycode
    
    def buttonUpdate(self):
        return self.debouncer.update()
    
    def buttonFell(self):
        return self.debouncer.fell
    
    def buttonRose(self):
        return self.debouncer.rose
    
    def buttonValue(self):
        return self.debouncer.value
    
    def buttonPressKeyboard(self, keyboard):
        keyboard.press(self.keycode)
        time.sleep(0.03)
        keyboard.release(self.keycode)
    
    @staticmethod
    def getNumberOfButtons():
        return Button.numberOfButtons
      