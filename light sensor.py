from machine import ADC
import time

# Define the ADC pin connected to the light sensor
light_pin = ADC(0)

while True:
    # Read the analog value from the light sensor
    light_value = light_pin.read_u16()

    # Print the light sensor value
    print("Light Sensor Value:", light_value)

    # Add a delay before the next reading
    time.sleep(1)
