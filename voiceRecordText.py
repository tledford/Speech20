import speech_recognition as sr
import platform
import os

system = platform.system()

def recordVoice():
	newfile = open('newrecordfile.txt', 'w')
	
	r = sr.Recognizer()
	r.energy_threshold = 2000
	with sr.Microphone() as source:
		audio = r.listen(source)  
    	               # listen for the first phrase and extract it into audio data

	try:
		text = r.recognize(audio)
		newfile.write(text)  
	except LookupError:
		newfile.write("Could not understand audio")
		
	newfile.close()
	
def openNewFile():
	if system == "Darwin":
		os.system("open newrecordfile.txt")
		
	elif system == "Linux":
		os.system("gedit newrecordfile.txt")

	
