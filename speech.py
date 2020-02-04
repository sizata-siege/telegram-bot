import pyttsx3

def Say(p):
	#e = engine
	e = pyttsx3.init()
	e.setProperty('rate' , 100)
	voices = e.getProperty('voices')
	e.setProperty('voice' , voices[1].id)
	e.setProperty('volume',1.0)
	e.say(p)
	e.runAndWait()

import datetime
print(datetime.datetime.now())

while True:
	text = input("Saying : ")
	Say(text)

