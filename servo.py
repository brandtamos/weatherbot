import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

pwm = GPIO.PWM(3, 50)
pwm.start(0)

def setAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)

setAngle(90)
sleep(1)
setAngle(45)
sleep(1)
setAngle(18)
sleep(1)
setAngle(180)
sleep(1)
pwm.stop()
GPIO.cleanup()