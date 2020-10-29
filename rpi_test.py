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
	story = 0
	if distance>10:
		story = 1
	if story ==1:
		setRGB(255,0,0)
		setText("who dares disturb my slumber")
		time.sleep(5)
		setText("have you come for my precious treasure?")
		time.sleep(5)
		choice = 0
		while choice ==0:
			pot = grovepi.analogRead(potentiometer)
			print(pot)
			pressed = digitalRead(button)
			if pressed:
				if pot>500:
					response = "yes"
				else:
					response = "no"
				choice = 1
		if response == "no":
			setRGB(0,255,0)
			setText("then replace it and go away")
			time.sleep(5)
			story = 0
			break
		if response =="yes":
			setRGB(0,0,255)
			setText("then you must answer my trivia")
			time.sleep(5)

			#publish request for trivia


	#if distance>10:
	#	setRGB(255,0,0)
	#else:
	#	setRGB(0,255,0)
	#setText_norefresh("hi")
	#pot = grovepi.analogRead(potentiometer)
	#print(pot)