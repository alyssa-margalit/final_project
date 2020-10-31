import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
#GPIO.setwarnings(False)

p.ChangeDutyCycle(10)
time.sleep(1)
p.ChangeDutyCycle(2.5)
				


def trivia_question_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	setText(str(message.payload, "utf-8"))


def trivia_answer_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	global answer
	answer = str(message.payload, "utf-8")
	



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
#subscribe tp all the different topics
    client.subscribe("alyssasrpi/trivia_question")
    client.message_callback_add("alyssasrpi/trivia_question", trivia_question_callback)
    client.subscribe("alyssasrpi/trivia_answer")
    client.message_callback_add("alyssasrpi/trivia_answer", trivia_answer_callback)
    #global story
    #story = 5
    #client.subscribe("alyssasrpi/button")
    #client.message_callback_add("alyssasrpi/button", button_callback)


#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))



if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()


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
		#print(story)
		#begin the sequence
		distance = ultrasonicRead(ranger)
		distance = int(distance)
		#if story != 400:
		story = 0
		if story == 0:
			if distance>10:
				story = 1

		if story ==1:
			setRGB(255,0,0)
			setText("who dares disturb my slumber")
			time.sleep(5)
			setText("have you come for my precious treasure?")
			time.sleep(5)
			while True:
				pot = grovepi.analogRead(potentiometer)
				#print(pot)
				pressed = digitalRead(button)
				if pressed:
					if pot>500:
						response = "yes"
						break
					else:
						response = "no"
						break
			print(response)
			if response == "no":
				setRGB(0,255,0)
				setText("then replace the key and go away")
				time.sleep(5)
				story = 0
			if response =="yes":
				setRGB(0,0,255)
				setText("then you must answer my trivia")
				
				client.publish("alyssasrpi/trivia_request", "ready")
				time.sleep(10)

				while True:
					pot = grovepi.analogRead(potentiometer)
					#print(pot)
					pressed = digitalRead(button)
					if pressed:
						if pot>500:
							response1 = "True"
							break
						else:
							response1 = "False"
							break
				print(response1)
				print(answer)
				if response1 == answer:
					setRGB(0,255,0)
					setText("You are worthy!")
					time.sleep(3)
					setText("Enter password 123 to unlock ")
					time.sleep(3)
					state = 0

					while True:

						if state ==0:
							pressed = digitalRead(button)
							if pressed:
								state = 1
								print("one press")
						elif state==1:
							pressed = digitalRead(button)
							if pressed:
								state = 2
								print("two press")
						elif state==2:
							pot = grovepi.analogRead(potentiometer)
							if pot>500:
								print("three press")
								time.sleep(2)
								break
						time.sleep(.3)

					#dont forget to enter password here

					story = 400
				else: 
					setText("Fail! Return the treasure at once!!")
					time.sleep(5)
					dist = ultrasonicRead(ranger)
					print(dist)
					if dist <10:
						setText("better luck next time!")
						time.sleep(5)
					else:
						setText("I hereby curse you with eternal syntax errors!!!")
						time.sleep(5)
						story = 400

			

				
			



