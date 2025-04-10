from machine import Pin
from utime import sleep

led = Pin(2, Pin.OUT)
push_button = Pin(13, Pin.IN)

while True:
    logic_state = push_button.value()
    print(f"Estado del botón: {1 if logic_state else 0}")  
    led.value(1 if logic_state else 0)  
    sleep(0.1)