# testDataViz.py
# Author: Team 20
# Created: March 2015
# Summary: This file deals with visualizing the data
# from the podcast transcription. This will open up
# a graph that will plot the amount of characters found 
# in 'newfile.txt' 

import matplotlib.pyplot as plt
import pylab


def visualizer():

#Initializes the characters array to hold 0
	characters = [];
	for x in range(0,26):
		characters.append(0)
		
# Takes in the text file statistics and place them into an array. 
	with open('newfile.txt') as f:
		while True:
			char = f.read(1)
			if not char:
				break
			char = char.lower() #changes all characters to lower case
			if (ord(char) != 32 and ord(char) != 10):
				#print (ord(char) - 97) 
				characters[ord(char) - 97]+=1
	
	#for x in range(0,26):
		#print chr((x + 97)) + ": " + str(characters[x])
		
	# Plots elements in characters 
	x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
	plt.plot(x, characters)
	plt.xlabel('Alphabet')
	plt.ylabel('Quantity of Character Repeated')
	plt.title('Transcribed Podcast')
	pylab.xticks([1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	plt.show()
	
visualizer()