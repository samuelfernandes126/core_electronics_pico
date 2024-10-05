from machine import Pin, ADC
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
pot = ADC(Pin(26))

while True:
	print(pot.read_u16()/19860, button.value())
	time.sleep(0.1)