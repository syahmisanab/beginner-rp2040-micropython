import machine
import utime
from neopixel import NeoPixel
import urandom

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

# Function to create a smooth transition between colors
def smooth_transition(current_color, target_color, duration):
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < duration:
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
        ratio = elapsed_time / duration
        r = int((1 - ratio) * current_color[0] + ratio * target_color[0])
        g = int((1 - ratio) * current_color[1] + ratio * target_color[1])
        b = int((1 - ratio) * current_color[2] + ratio * target_color[2])
        set_neopixel_color(r, g, b)
        utime.sleep(0.01)

# Function to create a random color effect with smooth transitions
def random_color_effect(duration):
    current_color = (0, 0, 0)
    target_color = (urandom.randint(0, 255), urandom.randint(0, 255), urandom.randint(0, 255))
    for _ in range(duration):
        smooth_transition(current_color, target_color, 1000)
        current_color = target_color
        target_color = (urandom.randint(0, 255), urandom.randint(0, 255), urandom.randint(0, 255))
        set_neopixel_color(*current_color)
        utime.sleep(0.5)

while True:
    if button_pin.value() == 0:  # Check if the button is pressed (LOW)
        random_color_effect(5)  # Random color effect for 5 iterations
    else:
        set_neopixel_color(0, 0, 0)  # Turn off the Neopixels

    # Add additional code logic or delays here if needed
    utime.sleep(0.1)  # Small delay to debounce the button
