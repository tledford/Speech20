#!/usr/bin/python
# -*- coding: utf-8 -*-
        	
import speech_recognition as sr
import os
import platform



import wx

import speech_recognition as sr


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):
    	self.button1 = wx.Button(self, id=-1, label='Record Voice',pos=(8, 8), size=(175, 28))
    	self.button2 = wx.Button(self, id=-1, label='Voice Command',pos=(8, 36), size=(175, 28))
    	self.button3 = wx.Button(self, id=-1, label= 'Close' ,pos=(8,64), size=(175,28))
    	self.button1.Bind(wx.EVT_BUTTON, self.playVoice)
    	self.button2.Bind(wx.EVT_BUTTON, self.testMethod)
    	self.button3.Bind(wx.EVT_BUTTON, self.OnQuitApp)
    	
    	self.SetSize((220, 180))
        self.SetTitle("Speech Recognition")
        self.Center()
        self.Show(True)
        
    def testMethod(self, event):
		print "it works!"
		
    def playVoice(self, event):
        
   
    		r = sr.Recognizer()
		with sr.Microphone() as source:                
  	  		audio = r.listen(source)                   
		try:
   			print("You said " + r.recognize(audio))    
		except LookupError:                           
    			print("Could not understand audio")
    def OnQuitApp(self, event):
        
        self.Close()

	

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main() 
 