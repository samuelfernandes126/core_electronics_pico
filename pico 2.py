from machine import Pin
import time

#setup pin 15 as an imput with pulldown resistor
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(16, Pin.OUT)

while True:
    #if button is pressed turn led on
    if button.value() == 1:
        led.value(1)

    else:
        led.value(0)

