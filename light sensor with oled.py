import ssd1306
from machine import Pin, I2C, ADC
import time

# Define OLED parameters
OLED_WIDTH = 128
OLED_HEIGHT = 64

# Define I2C pins (example: ESP32)
i2c = I2C(-0, scl=Pin(1), sda=Pin(0))
# If using ESP8266, you might need to specify the I2C pins differently, e.g.:
# i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

# Create OLED object
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Define the ADC pin connected to the light sensor
light_pin = ADC(0)

# Display some text
def display_text(text):
    oled.fill(0)  # Clear the display
    oled.text(text, 0, 30)  # Write text at top-left corner
    oled.show()  # Update the display

# Main program loop
while True:
    # Read the analog value from the light sensor
    light_value = light_pin.read_u16()

    # Print the light sensor value
    print("Light Sensor Value:", light_value)

    # Display the light sensor value on the OLED
    display_text("Light: {}".format(light_value))

    # Add a delay before the next reading
    time.sleep(1)
