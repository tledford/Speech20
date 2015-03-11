import speech_recognition as sr


def record():
	newfile = open('newrecordfile.txt', 'w')
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)  
    	               # listen for the first phrase and extract it into audio data

	try:
		text = r.recognize(audio)
		newfile.write(text)  
	except LookupError:
		newfile.write("Could not understand audio")
		
	newfile.close()
    
record()