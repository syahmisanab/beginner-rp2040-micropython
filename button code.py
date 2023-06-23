# connect button with gpio 25 and gnd 
# onboard arduino nano rp2040 is on pin 6


import machine
import time

button = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(6, machine.Pin.OUT)

while True:
    if button.value() == 1:  # Button is pressed
        led.value(0)  # Turn on the LED
    else:
        led.value(1)  # Turn off the LED
    time.sleep(0.1)  # Add a small delay to avoid rapid toggling
