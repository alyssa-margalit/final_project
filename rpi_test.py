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
	
	#begin the sequence
	distance = ultrasonicRead(ranger)
	distance = int(distance)
	if distance>10:
		story = 1
	if story ==1:
		setRGB(255,0,0)
		setText("who dares disturb my slumber")
		time.sleep(5)
		setText("have you come for my precious treasure?")
		choice = 0
		while choice ==0:
			pot = grovepi.analogRead(potentiometer)
			pressed = digitalRead(button)
			if pressed:
				if pot>500:
					response = "yes"
				else:
					response = "no"
				choice = 1
		if response == "no":
			setText("then replace it and go away")
			story = 0
			break
		if response =="yes":
			setText("then you must answer my trivia")
			#publish request for trivia


	#if distance>10:
	#	setRGB(255,0,0)
	#else:
	#	setRGB(0,255,0)
	#setText_norefresh("hi")
	#pot = grovepi.analogRead(potentiometer)
	#print(pot)