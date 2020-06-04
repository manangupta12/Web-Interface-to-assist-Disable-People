import speech_recognition as sr
import time
from subprocess import call
r = sr.Recognizer()

config = {}
temp = {}
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
					config['light']=1
					config['fan']=1
					temp = config.copy()
					config.clear()
					return temp
				if 'off' in text:
					config['light']=0
					config['fan']=0		
					temp = config.copy()
					config.clear()
					return temp	
			
			elif 'fan' in text:
				if 'on' in text:
					config['fan']=1
					temp = config.copy()
					config.clear()
					return temp
				if 'off' in text:
					config['fan']=0
					temp = config.copy()
					config.clear()
					return temp	

			elif 'light' in text:
				if 'on' in text:
					config['light']=1
					temp = config.copy()
					config.clear()
					return temp
				if 'off' in text:
					config['light']=0
					temp = config.copy()
					config.clear()
					return temp

			elif 'door' in text:
				if 'open' in text:
					config["door"] = 1
					temp = config.copy()
					config.clear()
					return temp
				if 'close' in text:
					config["door"] = 0
					temp = config.copy()
					config.clear()
					return temp
			else:
				return(config)
		except:
			print("Sorry could not recognize what you said")	
