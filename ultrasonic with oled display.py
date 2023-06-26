import ssd1306
from machine import Pin, I2C
import time
import utime

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = I2C(-0, scl=Pin(4), sda=Pin(4))
# If using raspi rp2040, you might need to specify the I2C pins differently, e.g.:
# i2c = I2C(0, scl=Pin(1), sda=Pin(0))

oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def display_text(text):
    oled.fill(0)
    oled.text(text, 0, 0)
    oled.show()

def ultrasound():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

while True:
    distance = ultrasound()
    display_text("Distance: {} cm".format(distance))
    time.sleep(2)
