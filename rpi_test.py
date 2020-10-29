import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math

red_led = 8
green_led = 7
button = 4
ranger = 3
buzzer = 2
potentiometer = 2

grovepi.pinMode(red_led, "OUTPUT")
grovepi.pinMode(green_led, "OUTPUT")
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.pinMode(button, "INPUT")


while True: 
	digitalWrite(green_led,1)
	#setRGB(0,0,255)
	distance = ultrasonicRead(ranger)
	distance = int(distance)
	if distance>10:
		setRGB(255,0,0)
	else:
		setRGB(0,255,0)
	setText_norefresh("hi")
	pot = grovepi.analogRead(potentiometer)
	print(pot)