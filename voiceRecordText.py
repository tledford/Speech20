# voiceRecordText.py
# Author: Team 20
# Created: March 2015
# Summary: This file will deal with the voice 
# record functionality of the project. It will 
# allow for the voice to be recorded while being written into
# a file. Also, it will open  the file it was written into. 

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

	
