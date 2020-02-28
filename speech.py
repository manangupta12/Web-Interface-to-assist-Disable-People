import speech_recognition as sr
import time
from subprocess import call
r = sr.Recognizer()
control = {"light":0,"fan":0}
def call():
	with sr.Microphone() as source:
		print("Speak Anything :")
		audio = r.listen(source)
		print("Listened")
		try:
			text = r.recognize_google(audio)
			print("You said : {}".format(text))
			if 'light' and 'fan' in text:
				if 'on' in text:
					control['light']=1
					control['fan']=1
					return control
				if 'off' in text:
					control['light']=0
					control['fan']=0		
					return control		
			if 'light' in text:
				if 'on' in text:
					control['light']=1
					return control
				if 'off' in text:
					control['light']=0
					return (control)
			if 'fan' in text:
				if 'on' in text:
					control['fan']=1
					return control
				if 'off' in text:
					control['fan']=0
					return control
		except:
			print("Sorry could not recognize what you said")	