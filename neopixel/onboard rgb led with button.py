import machine
import utime
from neopixel import NeoPixel

# Define the pin numbers for the button and the Neopixel data pin
button_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
neopixel_pin = machine.Pin(11, machine.Pin.OUT)

# Define the number of Neopixels in the strip
num_pixels = 10

# Initialize the Neopixel strip
neopixels = NeoPixel(neopixel_pin, num_pixels)

# Function to set the color of the Neopixels
def set_neopixel_color(red, green, blue):
    for i in range(num_pixels):
        neopixels[i] = (red, green, blue)
    neopixels.write()

while True:
    if button_pin.value() == 0:  # Check if the button is pressed (LOW)
        set_neopixel_color(255, 0, 0)  # Set Neopixel color to red
    else:
        set_neopixel_color(0, 0, 0)  # Turn off the Neopixels

    # Add additional code logic or delays here if needed
    utime.sleep(0.1)  # Small delay to debounce the button
