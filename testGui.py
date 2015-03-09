#!/usr/bin/python
# -*- coding: utf-8 -*-
        	
import speech_recognition as sr
import os
import platform
import wx
import voiceCMD
import transcribePodcast


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):
    	self.button1 = wx.Button(self, id=-1, label='Record Memo',pos=(22, 8), size=(175, 28))
    	self.button2 = wx.Button(self, id=-1, label='Play Memo',pos=(22, 36), size=(175, 28))
        self.button3 = wx.Button(self, id=-1, label='Voice Control',pos=(22, 64), size=(175, 28))
        self.button4 = wx.Button(self, id=-1, label='Transcribe Podcast', pos=(22, 80), size=(175,28))
    	self.button4 = wx.Button(self, id=-1, label= 'Close' ,pos=(22, 100), size=(175,28))
    	self.button1.Bind(wx.EVT_BUTTON, self.recordMemo)
    	self.button2.Bind(wx.EVT_BUTTON, self.playMemo)
        self.button3.Bind(wx.EVT_BUTTON, self.listenBtn)
        self.button3.Bing(wx.EVT_BUTTON, self.transcribePodcast)
    	self.button4.Bind(wx.EVT_BUTTON, self.OnQuitApp)
    	
    	self.SetSize((220, 180))
        self.SetTitle("Speech Recognition")
        self.Center()
        self.Show(True)
        
    def listenBtn(self, event):
		voiceCMD.getVoiceCommand()
		
    def recordMemo(self, event):
        voiceCMD.record_memo("params")

    def playMemo(self, event):
        voiceCMD.play_memo("params")

    def OnQuitApp(self, event):        
        self.Close()
    def transcribePodcast(self, event):
		transcribePodcast.openfile()
		
	

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main() 
 