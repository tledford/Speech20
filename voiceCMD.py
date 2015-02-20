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


def open_chrome(data):
	return "opening app"
	os.system("open /Applications/Google\ Chrome.app http://www." + data + ".com/")


def close_chrome(data):
	import subprocess
	return "closing app"

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


def what_time(data):
	from datetime import datetime

	hour = (datetime.now().time().hour)%12
	minute = datetime.now().time().minute

	if minute < 10:
		minute = str(0) + str(minute)
	return("Current time is " + str(hour) + ":" + str(minute))


def what_day(data):
	from datetime import datetime

	weekdays_dict = {0: "Monday",
					 1: "Tuesday",
					 2: "Wednesday",
					 3: "Thursday",
					 4: "Friday",
					 5: "Saturday",
					 6: "Sunday"}

	month_dict = {0: "January",
				  1: "February",
				  2: "March",
				  3: "April",
				  4: "May",
				  5: "June",
				  6: "July",
				  7: "August",
				  8: "September",
				  9: "October",
				  10: "November",
				  11: "December"}

	month = datetime.today().month
	day = datetime.today().day
	year = datetime.today().year
	weekday = datetime.today().weekday()

	#weekday = weekdays_dict[weekday]
	#print(weekday)
	return("Today is " + weekdays_dict[weekday] + " " + month_dict[month] + " " + str(day) + " " + str(year))


def play_music():
	return "5"

def joke(data):
	from random import randrange

	randNum = randrange(1,11)

	joke_dict = {1: "",
			  	 2: "",
			  	 3: "",
			  	 4: "",
			  	 5: "",
			  	 6: "",
			  	 7: "",
			   	 8: "",
			  	 9: "",
			  	 10: ""}

	#return joke_dict[r]

def sleep():
	return "7"


def wake():
	return "8"


def shutdown():
	return "9"


def record_memo():
	return "10"


def play_memo():
	return "11"


def getVoiceCommand():

	command_list = ["open", "close", 
					"time", "day", 
					"music", "joke",
					"sleep", "wake", 
					"shutdown", "record", 
					"playback"];

	command_list_dict = {"open": open_chrome, "close": close_chrome, 
						 "time": what_time, "day": what_day, 
						 "music": play_music, "joke": joke,
						 "sleep": sleep, "wake": wake, 
						 "shutdown": shutdown, "record": record_memo, 
						 "playback": play_memo};

	# r = sr.Recognizer()
	# with sr.Microphone() as source:                # use the default microphone as the audio source
	#     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
	# # with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
	# # 	audio = r.record(source)                        # extract audio data from the file

	# input = r.recognize(audio)
	# try:
	#     print("You said " + input)    # recognize speech using Google Speech Recognition
	# except LookupError:                            # speech is unintelligible
	#     print("Could not understand audio")
	    
	#os.system("open /Applications/Google\ Chrome.app http://www." + input + ".com/")

	input = "tell me a joke please"

	input = input.lower()
	input = input.split()

	found = "null"
	for cmd in command_list:
		for i, term in enumerate(input):
			if cmd == term:
				found = cmd;
				data = input[i+1]
				break;

	if(found != "null"):
		#print(data)
		print(command_list_dict[found](data))
	else:
		print("not found")



getVoiceCommand();






