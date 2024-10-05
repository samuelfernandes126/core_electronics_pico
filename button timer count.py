from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(16, Pin.OUT)

timer = 0

while True:
	
	if button.value() == 1:
		timer = timer + 1
		led.value(1)
		
	else:
		led.value(0)
		
	time.sleep(1)
		
	print(timer)
	