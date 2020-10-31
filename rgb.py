import sys, time
import RPi.GPIO as GPIO
redPin   = 11
greenPin = 13
bluePin  = 15
GPIO.setwarnings(False)
def blink(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
def redOn():
	blink(redPin)
def greenOn():
	blink(greenPin)

def blueOn():
	blink(bluePin)
def magentaOn():
	blink(redPin)
	blink(bluePin)
def main():
	while True:
		redOn()
		time.sleep(2)
		greenOn()
		time.sleep(2)
		blueOn()
		time.sleep(2)

main()
