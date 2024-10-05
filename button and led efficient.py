from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)     # set up pin 15 as an input with a pull-down resistor

led = Pin(16, Pin.OUT)   # set up pin 16 connected to the LED as an output

while True:
	b_state = button.value()
	
	if b_state == 1:
		led.value(1)    # if the button is pressed, then turn on the LED
	
	else:
		led.value(0)    # if its not pressed, then turn the LED off
		
	print (b_state)
    time.sleep(0.05)