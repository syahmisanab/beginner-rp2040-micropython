import machine
import time
import ninawifi

ninawifi.initialize_leds()

while True:
    time.sleep(0.5)
    ninawifi.ninapin_analog_write(ninawifi.LEDR, 0)
    ninawifi.ninapin_analog_write(ninawifi.LEDG, 255)
    ninawifi.ninapin_analog_write(ninawifi.LEDB, 0)

