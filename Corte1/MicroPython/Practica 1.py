from machine import Pin
import time

leds = [Pin(i, Pin.OUT)for i in(22, 21, 19, 18, 5, 4, 2, 15,)]

while True:
    for led in leds:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
    for led in reversed (leds):
        led.value(1)
        time.sleep(0.5)
        led.value(0)