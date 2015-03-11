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
        self.button2 = wx.Button(self, id=-1, label='Play Memo',pos=(22, 36), size=(175, 28))
        self.button3 = wx.Button(self, id=-1, label='Voice Control',pos=(22, 64), size=(175, 28))
        self.button4 = wx.Button(self, id=-1, label='Transcribe Podcast', pos=(22, 96), size=(175,28))
        self.button6 = wx.Button(self, id=-1, label='Visualizer', pos=(22, 128), size=(175,28))
        self.button7 = wx.Button(self, id=-1, label='Record Voice', pos=(22,168), size= (175,28))
        self.button8 = wx.Button(self, id=-1, label='Display Recorded Voice', pos=(22, 306), size= (175,28))
        self.button9 = wx.Button(self, id=-1, label='Close' ,pos=(22, 334), size=(175,28))
        self.button1.Bind(wx.EVT_BUTTON, self.recordMemo)
        self.button2.Bind(wx.EVT_BUTTON, self.playMemo)
        self.button3.Bind(wx.EVT_BUTTON, self.listenBtn)
        self.button4.Bind(wx.EVT_BUTTON, self.transcribePodcast)
        self.button6.Bind(wx.EVT_BUTTON, self.visualize)
        self.button9.Bind(wx.EVT_BUTTON, self.OnQuitApp)
        self.button7.Bind(wx.EVT_BUTTON, self.recordVoice)
        self.button8.Bind(wx.EVT_BUTTON, self.displayVoice)
        self.button8
        
        self.SetSize((220, 400))
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

