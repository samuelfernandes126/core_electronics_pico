from machine import PWM, Pin

pwm_pin = PWM(Pin(16))

max = 65535

pwm_pin.freq(1000)

while True:
	PWM_value = int(1 * max)
	
	pwm_pin.duty_u16(PWM_value)