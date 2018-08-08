import RPi.GPIO as GPIO
from time import sleep

SERVO_1_PIN = 3
SERVO_2_PIN = 5
SERVO_3_PIN = 7

#activate gpio pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_1_PIN, GPIO.OUT)
GPIO.setup(SERVO_2_PIN, GPIO.OUT)
GPIO.setup(SERVO_3_PIN, GPIO.OUT)

#setup pwm
pwm1 = GPIO.PWM(SERVO_1_PIN, 50)
pwm2 = GPIO.PWM(SERVO_2_PIN, 50)
pwm3 = GPIO.PWM(SERVO_3_PIN, 50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

def setServo1Angle(angle):
	duty = angle / 18 + 2
	GPIO.output(SERVO_1_PIN, True)
	pwm1.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(SERVO_1_PIN, False)
	pwm1.ChangeDutyCycle(0)

def setServo2Angle(angle):
	duty = angle / 18 + 2
	GPIO.output(SERVO_2_PIN, True)
	pwm2.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(SERVO_2_PIN, False)
	pwm2.ChangeDutyCycle(0)

def setServo3Angle(angle):
	duty = angle / 18 + 2
	GPIO.output(SERVO_3_PIN, True)
	pwm3.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(SERVO_3_PIN, False)
	pwm3.ChangeDutyCycle(0)

def cleanup():
    pwm1.stop()
	pwm2.stop()
	pwm3.stop()
	GPIO.cleanup()