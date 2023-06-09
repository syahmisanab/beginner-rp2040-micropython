import machine
import time

# Create an ADC object with ADC0 channel
adc = machine.ADC(machine.Pin(26))

# Main loop
while True:
    # Read the ADC value
    adc_value = adc.read_u16()

    # Print the ADC value
    print("ADC value: {}".format(adc_value))

    # Delay for a short period of time
    time.sleep(1)  # Adjust the delay time as needed
