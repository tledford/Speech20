# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
#     audio = r.record(source)                        # extract audio data from the file

# try:
#     list = r.recognize(audio,True)                  # generate a list of possible transcriptions
#     print("Possible transcriptions:")
#     for prediction in list:
#         print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
# except LookupError:                                 # speech is unintelligible
#     print("Could not understand audio")

 
import speech_recognition as sr
import os
import platform

system = platform.system()

def browse_site(data):

	if(system == "Darwin"):
		#os.system("open /Applications/Google\ Chrome.app http://www." + data)
		os.system("open http://" + data)

	elif(system == "Linux"):
		os.system("xdg-open http://" + data)

	elif(system == "Windows"):
		os.system("start " + data)

	return "opening app"

def close_site(data):
	import subprocess

	#adapted from: https://discussions.apple.com/thread/4479819
	script = """
	tell application "Google Chrome"
	    set windowList to every tab of every window whose URL contains \"""" + data + """\"
	    repeat with tabList in windowList
	        repeat with thisTab in tabList
	            close thisTab
	        end repeat
	    end repeat
	end tell
	"""

	#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
	subprocess.call(['osascript', '-e', script])
	return "closing app"

def what_time(data):
	from datetime import datetime

	hour = (datetime.now().time().hour)%12
	minute = datetime.now().time().minute

	if minute < 10:
		minute = str(0) + str(minute)

	output = "Current time is " + str(hour) + ":" + str(minute)

	if(system == "Darwin"):
		os.system("say " + output)

	elif(system == "Linux"):
		#CHANGE THIS
		os.system()

	elif(system == "Windows"):
		#CHANGE THIS
		os.system()
	
	return(output)


def what_day(data):
	from datetime import datetime

	weekdays_dict = {0: "Monday",
					 1: "Tuesday",
					 2: "Wednesday",
					 3: "Thursday",
					 4: "Friday",
					 5: "Saturday",
					 6: "Sunday"}

	month_dict = {1: "January",
				  2: "February",
				  3: "March",
				  4: "April",
				  5: "May",
				  6: "June",
				  7: "July",
				  8: "August",
				  9: "September",
				  10: "October",
				  11: "November",
				  12: "December"}

	month = datetime.today().month
	day = datetime.today().day
	year = datetime.today().year
	weekday = datetime.today().weekday()

	#weekday = weekdays_dict[weekday]
	#print(weekday)
	output = "Today is " + weekdays_dict[weekday] + " " + month_dict[month] + " " + str(day) + " " + str(year)

	if(system == "Darwin"):
		os.system("say " + output)

	elif(system == "Linux"):
		#CHANGE THIS
		os.system()

	elif(system == "Windows"):
		#CHANGE THIS
		os.system()

	return(output)


def joke(data):
	from random import randrange

	randNum = randrange(1,11)

	joke_dict = {1: "I never wanted to believe that my Dad was stealing from his job as a road worker. But when I got home, all the signs were there.",
			  	 2: "I was wondering why the ball kept getting bigger and bigger, and then it hit me.",
			  	 3: "Two fish are in a tank. One turns to the other and says, Hey, do you know how to drive this thing?",
			  	 4: "Why did the tomato turn red? Because he saw the salad dressing!",
			  	 5: "What do cars eat on their toast? Traffic jam.",
			  	 6: "What do you call an alligator wearing a vest? An investigator.",
			  	 7: "What did the blanket say when it fell off the bed? Aww sheet!",
			   	 8: "What did the pony say when he had a sore throat? Sorry, I'm a little horse.",
			  	 9: "An SQL statement walks into a bar and sees two tables. It approaches and asks, may I join you?",
			  	 10: "How many programmers does it take to change a light bulb? None. Its a hardware problem."}

	if(system == "Darwin"):
		os.system("say " + joke_dict[randNum])

	elif(system == "Linux"):
		#CHANGE THIS
		os.system()

	elif(system == "Windows"):
		#CHANGE THIS
		os.system()

	return joke_dict[randNum]

def sleep(data):

	if(system == "Darwin"):
		os.system("pmset sleepnow")

	elif(system == "Linux"):
		#CHANGE THIS
		os.system()

	elif(system == "Windows"):
		#CHANGE THIS
		os.system()


def reboot(data):

	if(system == "Darwin"):
		osascript = "tell app \"System Event\" to restart"
		#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
		subprocess.call(['osascript', '-e', script])

	elif(system == "Linux"):
		#CHANGE THIS
		os.system("start " + data)

	elif(system == "Windows"):
		#CHANGE THIS
		os.system("start " + data)


def shutdown(data):

	if(system == "Darwin"):
		osascript = "tell app \"System Events\" to shut down"
		#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
		subprocess.call(['osascript', '-e', script])

	elif(system == "Linux"):
		#CHANGE THIS
		os.system()

	elif(system == "Windows"):
		#CHANGE THIS
		os.system()


def record_memo(data):
	import pyaudio
	import wave
	import sys

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 48000
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	return "Done."

def play_memo(data):
	import pyaudio
	import wave
	import sys

	# length of data to read.
	chunk = 1024

	# open the file for reading.
	wf = wave.open("output.wav", 'rb')

	# create an audio object
	p = pyaudio.PyAudio()

	# open stream based on the wave object which has been input.
	stream = p.open(format =
	                p.get_format_from_width(wf.getsampwidth()),
	                channels = wf.getnchannels(),
	                rate = wf.getframerate(),
	                output = True)

	# read data (based on the chunk size)
	data = wf.readframes(chunk)

	# play stream (looping from beginning of file to the end)
	while data != '':
	    # writing to the stream is what *actually* plays the sound.
	    stream.write(data)
	    data = wf.readframes(chunk)

	# cleanup stuff.
	stream.close()    
	p.terminate()

	return "Done."


def getVoiceCommand():

	command_list = ["browse", "close", 
					"time", "day",
					"joke", "playback",
					"sleep", "reboot", 
					"shutdown", "record"];

	command_list_dict = {"browse": browse_site, "close": close_site, 
						 "time": what_time, "day": what_day, 
						 "playback": play_memo, "joke": joke,
						 "sleep": sleep, "reboot": reboot, 
						 "shutdown": shutdown, "record": record_memo};

	flag = False;
	input = 'null'
	while flag == False:
		try:
			r = sr.Recognizer()
			with sr.Microphone() as source:                # use the default microphone as the audio source
			    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
			# with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
			# 	audio = r.record(source)                        # extract audio data from the file

			input = r.recognize(audio)
		except Exception, e:
			flag = False;
			print ("Couldn't quite understand that, try again.")
		else:
			flag = True
			
	
	try:
	    print("You said " + input)    # recognize speech using Google Speech Recognition
	except LookupError:                            # speech is unintelligible
	    print("Could not understand audio")
	    
	#os.system("open /Applications/Google\ Chrome.app http://www." + input + ".com/")

	#input = "tell me a joke please"

	input = input.lower()
	input = input.split()

	found = "null"
	for cmd in command_list:
		for i, term in enumerate(input):
			if cmd == term:
				found = cmd;
				try:
					data = input[i+1]
				except IndexError, e:
					data = 'NULL';

	if(found != "null"):
		#print(data)
		print(command_list_dict[found](data))
	else:
		print("not found")



##########################
# ANITA!!!!!!!!!!
# Call this function with
# your GUI button!
##########################
getVoiceCommand();






