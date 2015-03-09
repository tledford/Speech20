import speech_recognition as sr
import wave
import platform
import os

system = platform.system()

def open_file():
    if system == "Darwin":
        os.system("open newfile.txt")
    elif system == "Linux":
        os.system("gedit newfile.txt")

def transcribe():
	origAudio = wave.open('fourscore.wav','r')
	numFrames = origAudio.getnframes()
	sampWidth = origAudio.getsampwidth()
	frameRate = origAudio.getframerate()
	length = numFrames / float(frameRate)
	nChannels = origAudio.getnchannels()
	file = open("newfile.txt", "w")


	start_pos = float(0)
	end_pos = float(6)

	while end_pos <= length: #only 7 to test short clip, real version should be 'length'

		origAudio.setpos(start_pos * frameRate)
		chunkData = origAudio.readframes(int((end_pos - start_pos) * frameRate))


		chunkAudio = wave.open('new_file.wav', 'w')
		chunkAudio.setsampwidth(sampWidth)
		chunkAudio.setnchannels(1)
		chunkAudio.setframerate(frameRate)
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
			print("Could not understand audio")
			start_pos -= 6.25
			end_pos -= 6.25
		
	
		end_pos += 6
		start_pos += 6
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
				#print (ord(char) - 97)
				characters[ord(char) - 97]+=1
	for x in range(0,26):
		print chr((x + 97)) + ": " + str(characters[x])