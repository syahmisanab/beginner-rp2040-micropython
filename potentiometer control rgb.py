import machine
import time
import ninawifi

ninawifi.initialize_leds()

# Create an ADC object with ADC0 channel
adc = machine.ADC(machine.Pin(26))

while True:
    # Read the ADC value
    adc_value = adc.read_u16()

    # Map the ADC value to the range 0-255 for the LED brightness
    led_brightness = int((adc_value / 65535) * 255)

    # Set the RGB LED color based on the ADC value
    ninawifi.ninapin_analog_write(ninawifi.LEDR, led_brightness)
    ninawifi.ninapin_analog_write(ninawifi.LEDG, 255 - led_brightness)
    ninawifi.ninapin_analog_write(ninawifi.LEDB, led_brightness)

    # Print the ADC value and LED brightness
    print("ADC value: {}, LED brightness: {}".format(adc_value, led_brightness))

    # Delay for a short period of time
    time.sleep(0.5)

