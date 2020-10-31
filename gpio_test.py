import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(27,GPIO.IN)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

p.ChangeDutyCycle(10)
