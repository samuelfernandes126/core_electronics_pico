import time, Pin
from servo import Servo
my_servo = Servo(pin_id=0)


while True:
	my_input = int(input("Enter Number: "))
	my_servo.write(my_input)
	time.sleep(0.5)
	