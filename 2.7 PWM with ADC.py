from machine import PWM, Pin, ADC
import time

pot_pin = ADC(Pin(26))
pwm_pin = PWM(Pin(16))

pwm_pin.freq(1000)

while True:
	pot_value = pot_pin.read_u16()
	
	pwm_pin.duty_u16(pot_value)
	
	pot_value_v = pot_value * 3.3 / 65535
	
	print(f"Pot Value = {pot_value}, V value = {pot_value_v}")
	
	time.sleep(0.05)