#######################################################
# Library to handle voice commands from our GUI application.
# Since different OSes execute processes in different ways,
# each function has an if/else to determine the OS of the
# machine calling the function. Darwin is MAC OSX and Linux is Linux.
# Winodws OS is only currently supported for browsing a webpage.
#
# Last Edited: 23 March 2015
#######################################################


import speech_recognition as sr
import os
import platform
import subprocess

system = platform.system()

#function to open a webpage to the input URL
def browse_site(data):

	if(system == "Darwin"):
		#os.system("open /Applications/Google\ Chrome.app http://www." + data)
		os.system("say opening " + data)
		os.system("open http://" + data)

	elif(system == "Linux"):
		os.system("espeak \'Opening new tab for " + data + "\'")
		os.system("xdg-open http://" + data + "&")

	elif(system == "Windows"):
		os.system("start " + data)

	return "opening app"

#function to close a running app
def close(data):
	if (system == "Darwin"):
		script = "quit app \"" + data + "\""
		subprocess.call(['osascript', '-e', script])
		os.system("say Closing " + data)
	elif (system == "Linux"):
		os.system("espeak \'Closing " + data + "\'")
		os.system("ps x | grep "+ data +" | kill -1 `awk '{print $1}'`")

#function to start an app on the computer
def start(data):
	if (system == "Darwin"):
		script = "open app \"" + data + "\""
		subprocess.call(['osascript', '-e', script])
		os.system("say Opening " + data)
		#go tommy go
	elif (system == "Linux"):
		os.system("espeak \'Opening " + data + "\'")
		os.system(data + "&")

#	import subprocess
#
#	#adapted from: https://discussions.apple.com/thread/4479819
#	script = """
#	tell application "Google Chrome"
#	    set windowList to every tab of every window whose URL contains \"""" + data + """\"
#	    repeat with tabList in windowList
#	        repeat with thisTab in tabList
#	            close thisTab
#	        end repeat
#	    end repeat
#	end tell
#	"""
#
#	#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
#	subprocess.call(['osascript', '-e', script])
#	return "closing app"

#function to handle currently unknown commands.
def dev():
	if(system == "Darwin"):
		os.system("say This command is currently under development")

	elif(system == "Linux"):
		os.system("espeak \'This command is currently under development\'")
	
#function to dictate the current time
def what_time(data):
	from datetime import datetime

	from random import randrange
	randNum = randrange(1,100)

	if(randNum == 58):
		if(system == "Darwin"):
			os.system("say hammer time!")
			return("Hammer time")

		elif(system == "Linux"):
			os.system("espeak \'Hammer time\'")
			return("Hammer time")

	apm = datetime.now().time().strftime('%p')
	hour = (datetime.now().time().hour)%12
	minute = datetime.now().time().minute

	output = "Current time is " + str(hour) + ":" + str(minute)

	if(system == "Darwin"):
		os.system("say " + output)

	elif(system == "Linux"):
		if minute < 10:
			minute = 'o' + str(minute)

		if hour == 0:
			hour = 12
		os.system("espeak \'The current time is" + str(hour) + " " + str(minute) + apm + "\'")
	
	return(output)

#function to dictate the current day, month, and year
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

	output = "Today is " + weekdays_dict[weekday] + " " + month_dict[month] + " " + str(day) + " " + str(year)

	if(system == "Darwin"):
		os.system("say " + output)

	elif(system == "Linux"):
		os.system("espeak \'Today is " + weekdays_dict[weekday] + " " + month_dict[month] + " " + str(day) + " " + str(year) + "\'")

	return(output)

#function to dictate a random joke, pulled from a list of 10 predefined jokes.
def joke(data):
	from random import randrange

	randNum = randrange(1,10)

	joke_dict = {1: "I never wanted to believe that my Dad was stealing from his job as a road worker. But when I got home, all the signs were there.",
			  	 2: "I was wondering why the ball kept getting bigger and bigger, and then it hit me.",
			  	 3: "Two fish are in a tank. One turns to the other and says, Hey, do you know how to drive this thing?",
			  	 4: "Why did the tomato turn red? Because he saw the salad dressing!",
			  	 5: "What do cars eat on their toast? Traffic jam.",
			  	 6: "What do you call an alligator wearing a vest? An investigator.",
			  	 7: "What did the blanket say when it fell off the bed? Aww sheet!",
			   	 8: "What did the pony say when he had a sore throat? Sorry, Im a little horse.",
			  	 9: "An SQL statement walks into a bar and sees two tables. It approaches and asks, may I join you?",
			  	 10: "How many programmers does it take to change a light bulb? None. Its a hardware problem."}

	if(system == "Darwin"):
		os.system("say " + joke_dict[randNum])

	elif(system == "Linux"):
		os.system("espeak \'" + joke_dict[randNum] + "\'")

	return joke_dict[randNum]

#function to sleep a computer.
#Currently only supported on Mac OSX
def sleep(data):

	if(system == "Darwin"):
		os.system("pmset sleepnow")

	elif(system == "Linux"):
		#CHANGE THIS
		#os.system("espeak \'Sleeping\'")
		#os.system("pm-hibernate &")
		dev()

#function to restart a computer
def reboot(data):

	if(system == "Darwin"):
		osascript = "tell app \"System Event\" to restart"
		#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
		subprocess.call(['osascript', '-e', script])

	elif(system == "Linux"):
		os.system("espeak Rebooting")
		os.system("reboot")

#function to shutdown a computer.
def shutdown(data):

	if(system == "Darwin"):
		osascript = "tell app \"System Events\" to shut down"
		#adapted from: http://stackoverflow.com/questions/14942709/closing-a-program-using-terminal-from-python
		subprocess.call(['osascript', '-e', script])

	elif(system == "Linux"):
		os.system("poweroff")
		os.system()


def cmds(data):
	if(system == "Darwin"):
		os.system("say Current commands are: browse, open, close, time, day, joke, sleep, reboot, shutdown, reecord, playback, and help")

	if(system == "Linux"):
		os.system("espeak \'Current commands are: browse, open, close, time, day, joke, sleep, reboot, shutdown, reecord, playback, and help\'")


def notFound():
	if(system == "Darwin"):
		os.system("say Command not found")
	if(system == "Linux"):
		os.system("espeak \'Command not found\'")


def egg(data):
	if(system == "Darwin"):
		os.system("say Bacon is love, bacon is life")
	if(system == "Linux"):
		os.system("espeak \'Bacon is love, bacon is life\'")


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
					"shutdown", "record",
					"open", "bacon",
					"help"];

	command_list_dict = {"browse": browse_site, "close": close, 
						 "time": what_time, "day": what_day, 
						 "playback": play_memo, "joke": joke,
						 "sleep": sleep, "reboot": reboot, 
						 "shutdown": shutdown, "record": record_memo,
						 "open": start, "bacon": egg,
						 "help": cmds};

	flag = False;
	input = 'null'
	while flag == False:
		try:
			r = sr.Recognizer()
			r.energy_threshold = 2000
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
