import speech_recognition as sr
import wave
import platform
import os
import wx
import matplotlib.pyplot as plt
import pylab

system = platform.system()
#used to determine which operating system the program is beign runned on
def open_file():
    if system == "Darwin":
        os.system("open newfile.txt")
    elif system == "Linux":
        os.system("gedit newfile.txt")

def transcribe():
	origAudio = wave.open('fourscore.wav','r') #this is the podcast we are transcribing
	numFrames = origAudio.getnframes()         #This gets the framerates in other words how fast the audio is.
	sampWidth = origAudio.getsampwidth()#All of this has to do with the audio file
	frameRate = origAudio.getframerate()#How fast it goes through all the frames
	length = numFrames / float(frameRate) #I grabed the amount of frames divided by the framerate to get the length of the file.
	nChannels = origAudio.getnchannels()#Checks if the original is mono audio or multi channel.
	file = open("newfile.txt", "w")#opens the file to output the text.


	start_pos = float(0) #this is how we handle the loops with a start position and end position.
	end_pos = float(6)

	while end_pos <= length: #only 7 to test short clip, real version should be 'length'

		origAudio.setpos(start_pos * frameRate) #We grab the start position multiplied by the framerate to know where to start.
		chunkData = origAudio.readframes(int((end_pos - start_pos) * frameRate))#we do the same for the end position to know where is the last frame.


		chunkAudio = wave.open('new_file.wav', 'w') #We create a new wavfile to pass in a 5 second wave file
		chunkAudio.setsampwidth(sampWidth)          #The api can only handle a 6 second wav file
		chunkAudio.setnchannels(1)                  #we make the channels and framerates and frames the same as the original.
		chunkAudio.setframerate(frameRate)          #this way each time it passes in 6 seconds of audio.
		chunkAudio.writeframes(chunkData)
		chunkAudio.close()


	
		r = sr.Recognizer()
		with sr.WavFile('new_file.wav') as source:              # use "test.wav" as the audio source
			audio = r.record(source)                        # extract audio data from the file

		try:
			print(r.recognize(audio))   # recognize speech using Google Speech Recognition
			file.write(r.recognize(audio))
			file.write("\n")
		
		except LookupError:                                 # speech is unintelligible
			start_pos -= 6.25
			end_pos -= 6.25                             #it will try the same points with a little bit less audio.
		
	
		end_pos += 6                #if it was succesful in transcribing the audio then it will increase the start position for the next part of the audio file.
		start_pos += 6              #we also increase the endposition to a new time.
	file.close()
	open_file()


def visualizer():

	characters = [];
	for x in range(0,26):
		characters.append(0)

	with open('newfile.txt') as f:
		while True:
			char = f.read(1)
			if not char:
				break
			char = char.lower()
			if (ord(char) != 32 and ord(char) != 10):
				characters[ord(char) - 97]+=1
	#for x in range(0,26):
		#print chr((x + 97)) + ": " + str(characters[x])
		

	x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
	plt.plot(x, characters)
	plt.xlabel('Alphabet')
	plt.ylabel('Quantity of Character Repeated')
	plt.title('Transcribed Podcast')
	pylab.xticks([1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	plt.show()
	     
