"""EE 250L Lab 05 Starter Code
https://github.com/usc-ee250-fall2020/lab05-lab5team.git
Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math

sonic = 4
led = 2
button = 3
pinMode(button,"INPUT")
pinMode(led,"OUTPUT")

def lcd_callback(client,userdata,message):
    #print("on_message: " + message.topic + " " + str(message.payload, "utf-8"))
    text = str(message.payload, "utf-8")
    setText(text)
def led_callback(client, userdata, message):#callback for when vm_publisher sends data about turning the led on and off
    #recieve either LED_OFF or LED_ON and convert it to string and turn the led on or off
    led_status = str(message.payload,"utf-8")
    if led_status == "LED_OFF":
        digitalWrite(led,0)
    else:
        digitalWrite(led,1)
   
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("alyssasrpi/led")
    client.message_callback_add("alyssasrpi/led", led_callback)
    client.subscribe("alyssasrpi/lcd")
    client.message_callback_add("alyssasrpi/lcd",lcd_callback)
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


    
    #digitalWrite(led,1)
    distance = grovepi.ultrasonicRead(sonic)
    button_status = digitalRead(button)
    while True:
        #have rpi read distance and button status, publish this data
        distance = grovepi.ultrasonicRead(sonic)
        dist = int(distance)
        #print(distance)
        client.publish("alyssasrpi/ultrasonicRanger", dist)
        button_status = digitalRead(button)
        if button_status:
            client.publish("alyssasrpi/button", "Button pressed!")
            print("button pressed...")
        time.sleep(1)
            

