if response == "no":
				setRGB(0,255,0)
				setText("then replace it and go away")
				time.sleep(5)
				story = 0
			if response =="yes":
				setRGB(0,0,255)
				setText("then you must answer my trivia")
				
				client.publish("alyssasrpi/trivia_request", "ready")
				time.sleep(10)
				choice = 0
				while choice ==0:
					pot = grovepi.analogRead(potentiometer)
					#print(pot)
					pressed = digitalRead(button)
					if pressed:
						if pot>500:
							response = "True"
						else:
							response = "False"
					choice = 1
				if response == answer:
					setRGB(0,255,0)
					setText("You are worthy! Keep the treasure and guard it with your life!")
					time.sleep(3)
					setText("Password is: ")
					#dont forget to enter password here

					story = 400
				else: 
					setText("Fail! Return the treasure at once!!")
					time.sleep(5)
					dist = ultrasonicRead(ranger)
					print(dist)
					if dist <10:
						setText("better luck next time!")
					else:
						setText("I hereby curse you with eternal syntax errors!!!")
						story = 400




try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    #p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    #p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()