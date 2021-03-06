import requests
import socket
import json
import random 
import paho.mqtt.client as mqtt
import time
import sys
import math
# Reddit API: https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("alyssasrpi/trivia_request")
    client.message_callback_add("alyssasrpi/trivia_request", trivia_request_callback)
    

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
def trivia_request_callback(client,userdata,message):
    print(str(message.payload, "utf-8"))
    trivia = trivia_init()
    print(trivia[0])
    print(trivia[1])
    client.publish("alyssasrpi/trivia_question",trivia[0])
    client.publish("alyssasrpi/trivia_answer",trivia[1])
    #client.publish("alyssasrpi/trivia",trivia[1])



def button_callback(client,userdata,message):
    #print("on_message: " + message.topic + " " + str(message.payload, "utf-8"))
    print(str(message.payload, "utf-8"))#when button is pressed, print out the message "button pressed"

def trivia_init():

    response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')

    if response.status_code == 200: # Status: OK
        data = response.json()
        index = random.randint(0,9)
        question = data["results"][index]["question"]
        answer = data["results"][index]["correct_answer"]
        
        #print(json.dumps(question,sort_keys=True, indent = 4))
        #print(json.dumps(answer,sort_keys=True, indent = 4))

        #publish question and answer
       
        return question, answer

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


TRIVIA_APP = {
    'name': 'Trivia',
    'init': trivia_init
}


if __name__ == '__main__':
    
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    trivia_init()
    trivia = trivia_init()
    print(trivia[0])
    print(trivia[1])
    #print(answer)
    client.publish("alyssasrpi/trivia",trivia[1])
    while True:
        time.sleep(1)
