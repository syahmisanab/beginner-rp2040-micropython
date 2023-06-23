import machine
import utime

# Define pin numbers for the switch and buzzer
switch_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer_pin = machine.Pin(22, machine.Pin.OUT)

while True:
    if switch_pin.value() == 0:  # Check if the switch is pressed (LOW)
        buzzer_pin.on()  # Turn on the buzzer
        utime.sleep(0.1)  # Keep the buzzer on for 1 second
        buzzer_pin.off()  # Turn off the buzzer

    utime.sleep(0.1)  # Small delay to debounce the switch
