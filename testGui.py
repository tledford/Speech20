#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import speech_recognition as sr


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):

        self.pnl = wx.Panel(self)
        self.PlayButton = wx.Button(self.pnl, wx.ID_ANY, label = "RECORD", pos=(10, 10))
        self.Bind(wx.EVT_BUTTON, self.playVoice, self.PlayButton)
        
        
        self.exitButton = wx.Button(self.pnl, wx.ID_ANY, label = "CLOSE", pos=(20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, self.exitButton)
        

        self.SetSize((220, 180))
        self.SetTitle("Speech Recognition")
        self.Centre()
        self.Show(True)
    

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
    
    
        
'''
        grid = wx.GridSizer(3, 2)

        grid.AddMany([(wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_MENU_PLAY), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW))])

        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_EXIT)
        self.Bind(wx.EVT_BUTTON, self.OnDo, id=wx.ID_MENU_PLAY)

        pnl.SetSizer(grid)
'''
 