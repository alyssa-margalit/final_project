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

while True: 
	digitalWrite(green_led,1)
	setText("hello")