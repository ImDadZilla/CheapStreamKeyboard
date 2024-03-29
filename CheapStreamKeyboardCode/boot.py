import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", switch.value)