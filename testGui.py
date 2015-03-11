#!/usr/bin/python
# -*- coding: utf-8 -*-
            
import speech_recognition as sr
import os
import platform
import wx
import voiceCMD
import transcribePodcast
import voiceRecordText


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):
        self.button1 = wx.Button(self, id=-1, label='Record Memo',pos=(22, 8), size=(175, 28))
        self.button2 = wx.Button(self, id=-1, label='Play Memo',pos=(22, 38), size=(175, 28))
        self.button3 = wx.Button(self, id=-1, label='Voice Control',pos=(22, 68), size=(175, 28))
        self.button4 = wx.Button(self, id=-1, label='Transcribe Podcast', pos=(22, 98), size=(175,28))
        self.button6 = wx.Button(self, id=-1, label='Visualizer', pos=(22, 128), size=(175,28))
        self.button7 = wx.Button(self, id=-1, label='Record Voice', pos=(22,158), size= (175,28))
        self.button8 = wx.Button(self, id=-1, label='Display Recorded Voice', pos=(22, 188), size= (175,28))
        self.button9 = wx.Button(self, id=-1, label='Close' ,pos=(22, 228), size=(175,28))
        self.button1.Bind(wx.EVT_BUTTON, self.recordMemo)
        self.button2.Bind(wx.EVT_BUTTON, self.playMemo)
        self.button3.Bind(wx.EVT_BUTTON, self.listenBtn)
        self.button4.Bind(wx.EVT_BUTTON, self.transcribePodcast)
        self.button6.Bind(wx.EVT_BUTTON, self.visualize)
        self.button7.Bind(wx.EVT_BUTTON, self.recordVoice)
        self.button8.Bind(wx.EVT_BUTTON, self.displayVoice)
    	self.button9.Bind(wx.EVT_BUTTON, self.OnQuitApp)

        
        self.SetSize((220, 265))
        self.SetBackgroundColour("blue")
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
        transcribePodcast.transcribe()

    def visualize(self, event):
        transcribePodcast.visualizer()
        
    def recordVoice(self, event):
    	voiceRecordText.recordVoice()
    
    def displayVoice(self, event):
    	voiceRecordText.openNewFile()
    

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main() 

