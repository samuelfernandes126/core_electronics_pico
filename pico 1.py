from machine import Pin
import time

led = Pin("LED", Pin.OUT) # 16 for GPIO 16, "LED" for using onboard LED

while True:  #Infinite Loop
	led.value(1) # Turn LED on
	time.sleep(2) # Wait for 2s
	
	led.value(0) # Turn LED off
	time.sleep(2) # Wait for 2s
	
