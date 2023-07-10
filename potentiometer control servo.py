import machine
import time
import utime
from servo import Servo

# Create an ADC object with ADC0 channel
adc = machine.ADC(machine.Pin(26))

# Create a servo object
servo = Servo(0)  # Servo pin is connected to GP0

def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Main loop
while True:
    # Read the ADC value from the potentiometer
    pot_value = adc.read_u16()

    # Map the potentiometer value to the servo angle range
    angle = int(servo_Map(pot_value, 0, 65535, 0, 360))

    # Set the servo angle
    servo.goto(angle)

    # Print the potentiometer value and corresponding servo angle
    print("Potentiometer value: {}, Servo angle: {}".format(pot_value, angle))

    # Delay for a short period of time
    utime.sleep(0.1)  # Adjust the delay time as needed
