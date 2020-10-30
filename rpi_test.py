import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt

def trivia_question_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	setText(str(message.payload, "utf-8"))
				#if response ==str(message.payload, "utf-8"):
					#setRGB(255,0,0)
					#setText("You are worthy!!")
				#else:
					#setText("fail! return the treasure or face my wrath")


def trivia_answer_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	choice = 0
	while choice ==0:
		pot = grovepi.analogRead(potentiometer)
				#print(pot)
		pressed = digitalRead(button)
		if pressed:
			if pot>500:
				response = "True"
				print("choice: "+response)

			else:
				response = "False"
				print("choice: "+response)
			choice = 1
	if response == str(message.payload, "utf-8"):
		setText("You are worthy!!")
	else:
		setText("Fail!! Return the treasure at once or face my wrath!!")



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
#subscribe tp all the different topics
    client.subscribe("alyssasrpi/trivia_question")
    client.message_callback_add("alyssasrpi/trivia_question", trivia_question_callback)
    client.subscribe("alyssasrpi/trivia_answer")
    client.message_callback_add("alyssasrpi/trivia_answer", trivia_answer_callback)
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
				#print(pot)
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
				
				client.publish("alyssasrpi/trivia_request", "ready")
				time.sleep(10)
				#publish request for trivia


