import machine
import utime
from neopixel import NeoPixel

# Define the pin number for the potentiometer
adc = machine.ADC(machine.Pin(26))

# Define the pin number for the Neopixel data pin
neopixel_pin = machine.Pin(11, machine.Pin.OUT)

# Define the number of Neopixels in the strip
num_pixels = 10

# Initialize the Neopixel strip
neopixels = NeoPixel(neopixel_pin, num_pixels)

# Function to set the color of the Neopixels based on the potentiometer value
def set_neopixel_color(pot_value):
    # Scale the potentiometer value to the range of 0-255
    pot_value_scaled = int(pot_value / 4095 * 255)

    # Set the color of the Neopixels
    for i in range(num_pixels):
        neopixels[i] = (pot_value_scaled, 255 - pot_value_scaled, 0)  # Red and Blue channels based on potentiometer value
    neopixels.write()

# Main loop
while True:
    # Read the potentiometer value
    pot_value = adc.read_u16()

    # Set the color of the Neopixels based on the potentiometer value
    set_neopixel_color(pot_value)

    # Add additional code logic or delays here if needed
    utime.sleep(0.1)  # Small delay
